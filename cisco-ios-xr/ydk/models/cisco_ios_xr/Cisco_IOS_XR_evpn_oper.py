""" Cisco_IOS_XR_evpn_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR evpn package operational data.

This module contains definitions
for the following management objects\:
  evpn\: EVPN Operational Table

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpRouteTarget(Enum):
    """
    BgpRouteTarget (Enum Class)

    Bgp route target

    .. data:: no_stitching = 0

    	RT is default type

    .. data:: stitching = 1

    	RT is for stitching (Golf-L2)

    """

    no_stitching = Enum.YLeaf(0, "no-stitching")

    stitching = Enum.YLeaf(1, "stitching")


class BgpRouteTargetFormat(Enum):
    """
    BgpRouteTargetFormat (Enum Class)

    Bgp route target format

    .. data:: none = 0

    	No route target

    .. data:: two_byte_as = 1

    	2 Byte AS:nn format

    .. data:: four_byte_as = 2

    	4 byte AS:nn format

    .. data:: ipv4_address = 3

    	IP:nn format

    .. data:: es_import = 1538

    	a.a.i format

    """

    none = Enum.YLeaf(0, "none")

    two_byte_as = Enum.YLeaf(1, "two-byte-as")

    four_byte_as = Enum.YLeaf(2, "four-byte-as")

    ipv4_address = Enum.YLeaf(3, "ipv4-address")

    es_import = Enum.YLeaf(1538, "es-import")


class BgpRouteTargetRole(Enum):
    """
    BgpRouteTargetRole (Enum Class)

    Bgp route target role

    .. data:: both = 0

    	Both Import and export roles

    .. data:: import_ = 1

    	Import role

    .. data:: export = 2

    	Export role

    """

    both = Enum.YLeaf(0, "both")

    import_ = Enum.YLeaf(1, "import")

    export = Enum.YLeaf(2, "export")


class L2vpnAdRd(Enum):
    """
    L2vpnAdRd (Enum Class)

    L2vpn ad rd

    .. data:: l2vpn_ad_rd_none = 0

    	Route Distinguisher not set

    .. data:: l2vpn_ad_rd_auto = 1

    	Route Distinguisher auto-generated

    .. data:: l2vpn_ad_rd_as = 2

    	Route Distinguisher with 2 Byte AS number

    .. data:: l2vpn_ad_rd_4byte_as = 3

    	Route Distinguisher with 4 Byte AS number

    .. data:: l2vpn_ad_rd_v4_addr = 4

    	Route Distinguisher with IPv4 Address

    """

    l2vpn_ad_rd_none = Enum.YLeaf(0, "l2vpn-ad-rd-none")

    l2vpn_ad_rd_auto = Enum.YLeaf(1, "l2vpn-ad-rd-auto")

    l2vpn_ad_rd_as = Enum.YLeaf(2, "l2vpn-ad-rd-as")

    l2vpn_ad_rd_4byte_as = Enum.YLeaf(3, "l2vpn-ad-rd-4byte-as")

    l2vpn_ad_rd_v4_addr = Enum.YLeaf(4, "l2vpn-ad-rd-v4-addr")


class L2vpnAdRt(Enum):
    """
    L2vpnAdRt (Enum Class)

    L2vpn ad rt

    .. data:: l2vpn_ad_rt_none = 0

    	Route target not set

    .. data:: l2vpn_ad_rt_as = 1

    	Route Target with 2 Byte AS number

    .. data:: l2vpn_ad_rt_4byte_as = 2

    	Route Target with 4 Byte AS number

    .. data:: l2vpn_ad_rt_v4_addr = 3

    	Route Target with IPv4 Address

    .. data:: es_import = 1538

    	Ethernet Segment Route Target from BGP

    """

    l2vpn_ad_rt_none = Enum.YLeaf(0, "l2vpn-ad-rt-none")

    l2vpn_ad_rt_as = Enum.YLeaf(1, "l2vpn-ad-rt-as")

    l2vpn_ad_rt_4byte_as = Enum.YLeaf(2, "l2vpn-ad-rt-4byte-as")

    l2vpn_ad_rt_v4_addr = Enum.YLeaf(3, "l2vpn-ad-rt-v4-addr")

    es_import = Enum.YLeaf(1538, "es-import")


class L2vpnAdRtRole(Enum):
    """
    L2vpnAdRtRole (Enum Class)

    L2vpn ad rt role

    .. data:: both = 0

    	Both

    .. data:: import_ = 1

    	Import

    .. data:: export = 2

    	Export

    """

    both = Enum.YLeaf(0, "both")

    import_ = Enum.YLeaf(1, "import")

    export = Enum.YLeaf(2, "export")


class L2vpnEvpn(Enum):
    """
    L2vpnEvpn (Enum Class)

    L2vpn evpn

    .. data:: evpn_type_invalid = 0

    	Unspecify type for that EVI entry

    .. data:: evpn_type_evpn = 1

    	EVPN service type

    .. data:: evpn_type_pbb_evpn = 2

    	PBB EVPN service type

    .. data:: evpn_type_evpn_vpws_vlan_unaware = 3

    	EVPN VPWS vlan-unaware service type

    .. data:: evpn_type_evpn_vpws_vlan_aware = 4

    	EVPN VPWS vlan-aware service type

    .. data:: evpn_type_max = 5

    	Max EVPN type

    """

    evpn_type_invalid = Enum.YLeaf(0, "evpn-type-invalid")

    evpn_type_evpn = Enum.YLeaf(1, "evpn-type-evpn")

    evpn_type_pbb_evpn = Enum.YLeaf(2, "evpn-type-pbb-evpn")

    evpn_type_evpn_vpws_vlan_unaware = Enum.YLeaf(3, "evpn-type-evpn-vpws-vlan-unaware")

    evpn_type_evpn_vpws_vlan_aware = Enum.YLeaf(4, "evpn-type-evpn-vpws-vlan-aware")

    evpn_type_max = Enum.YLeaf(5, "evpn-type-max")


class L2vpnEvpnEsi(Enum):
    """
    L2vpnEvpnEsi (Enum Class)

    EVPN ESI types

    .. data:: esi_type0 = 0

    	ESI type zero

    .. data:: esi_type1 = 1

    	ESI type one

    .. data:: esi_type2 = 2

    	ESI type two

    .. data:: esi_type3 = 3

    	ESI type three

    .. data:: esi_type4 = 4

    	ESI type four

    .. data:: esi_type5 = 5

    	ESI type five

    .. data:: l2vpn_evpn_esi_type_legacy = 128

    	ESI type legacy

    .. data:: l2vpn_evpn_esi_type_override = 129

    	ESI type override (10-octet value)

    .. data:: esi_type_invalid = 255

    	ESI type invalid

    """

    esi_type0 = Enum.YLeaf(0, "esi-type0")

    esi_type1 = Enum.YLeaf(1, "esi-type1")

    esi_type2 = Enum.YLeaf(2, "esi-type2")

    esi_type3 = Enum.YLeaf(3, "esi-type3")

    esi_type4 = Enum.YLeaf(4, "esi-type4")

    esi_type5 = Enum.YLeaf(5, "esi-type5")

    l2vpn_evpn_esi_type_legacy = Enum.YLeaf(128, "l2vpn-evpn-esi-type-legacy")

    l2vpn_evpn_esi_type_override = Enum.YLeaf(129, "l2vpn-evpn-esi-type-override")

    esi_type_invalid = Enum.YLeaf(255, "esi-type-invalid")


class L2vpnEvpnLbMode(Enum):
    """
    L2vpnEvpnLbMode (Enum Class)

    L2VPN EVPN load balancing mode

    .. data:: invalid_load_balancing = 0

    	Invalid load balancing

    .. data:: single_homed = 1

    	Single-homed site or network

    .. data:: multi_homed_aa_per_flow = 2

    	Multi-homed access network active/active per

    	flow

    .. data:: multi_homed_aa_per_service = 3

    	Multi-homed access network active/active per

    	service

    """

    invalid_load_balancing = Enum.YLeaf(0, "invalid-load-balancing")

    single_homed = Enum.YLeaf(1, "single-homed")

    multi_homed_aa_per_flow = Enum.YLeaf(2, "multi-homed-aa-per-flow")

    multi_homed_aa_per_service = Enum.YLeaf(3, "multi-homed-aa-per-service")


class L2vpnEvpnMfMode(Enum):
    """
    L2vpnEvpnMfMode (Enum Class)

    L2VPN EVPN MAC flushing mode

    .. data:: invalid = 0

    	Invalid MAC Flushing mode

    .. data:: tcn_stp = 1

    	TCN STP MAC Flushing mode

    .. data:: mvrp = 2

    	MVRP MAC Flushing mode

    """

    invalid = Enum.YLeaf(0, "invalid")

    tcn_stp = Enum.YLeaf(1, "tcn-stp")

    mvrp = Enum.YLeaf(2, "mvrp")


class L2vpnEvpnRtOrigin(Enum):
    """
    L2vpnEvpnRtOrigin (Enum Class)

    L2vpn evpn rt origin

    .. data:: invalid = 0

    	Incomplete Configuration

    .. data:: extracted = 1

    	From ESI

    .. data:: configured = 2

    	Locally configured

    """

    invalid = Enum.YLeaf(0, "invalid")

    extracted = Enum.YLeaf(1, "extracted")

    configured = Enum.YLeaf(2, "configured")


class L2vpnEvpnScMode(Enum):
    """
    L2vpnEvpnScMode (Enum Class)

    EVPN Ethernet\-Segment service carving mode

    .. data:: invalid = 0

    	Invalid service carving mode

    .. data:: auto = 1

    	Auto service carving mode

    .. data:: manual = 2

    	Manual service carving

    """

    invalid = Enum.YLeaf(0, "invalid")

    auto = Enum.YLeaf(1, "auto")

    manual = Enum.YLeaf(2, "manual")


class L2vpnEvpnSmacSrc(Enum):
    """
    L2vpnEvpnSmacSrc (Enum Class)

    L2vpn evpn smac src

    .. data:: invalid = 0

    	Incomplete Configuration

    .. data:: not_applicable = 1

    	Source MAC Not Applicable (EVPN)

    .. data:: local = 2

    	Local

    .. data:: pbb_bsa = 3

    	PBB BSA

    .. data:: esi = 4

    	From ESI

    .. data:: esi_invalid = 5

    	From ESI, Error

    .. data:: pbb_bsa_overrride = 6

    	PBB BSA, no ESI

    """

    invalid = Enum.YLeaf(0, "invalid")

    not_applicable = Enum.YLeaf(1, "not-applicable")

    local = Enum.YLeaf(2, "local")

    pbb_bsa = Enum.YLeaf(3, "pbb-bsa")

    esi = Enum.YLeaf(4, "esi")

    esi_invalid = Enum.YLeaf(5, "esi-invalid")

    pbb_bsa_overrride = Enum.YLeaf(6, "pbb-bsa-overrride")


class L2vpnRgRole(Enum):
    """
    L2vpnRgRole (Enum Class)

    L2vpn rg role

    .. data:: l2vpn_rg_role_not_defined = 0

    	l2vpn rg role not defined

    .. data:: l2vpn_rg_role_active = 1

    	l2vpn rg role active

    .. data:: l2vpn_rg_role_standby = 2

    	l2vpn rg role standby

    .. data:: l2vpn_rg_role_max = 3

    	l2vpn rg role max

    """

    l2vpn_rg_role_not_defined = Enum.YLeaf(0, "l2vpn-rg-role-not-defined")

    l2vpn_rg_role_active = Enum.YLeaf(1, "l2vpn-rg-role-active")

    l2vpn_rg_role_standby = Enum.YLeaf(2, "l2vpn-rg-role-standby")

    l2vpn_rg_role_max = Enum.YLeaf(3, "l2vpn-rg-role-max")



class Evpn(Entity):
    """
    EVPN Operational Table
    
    .. attribute:: nodes
    
    	Table of EVPN operational data for a particular node
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes>`
    
    .. attribute:: active
    
    	Active EVPN operational data
    	**type**\:  :py:class:`Active <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active>`
    
    .. attribute:: standby
    
    	Standby EVPN operational data
    	**type**\:  :py:class:`Standby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby>`
    
    

    """

    _prefix = 'evpn-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(Evpn, self).__init__()
        self._top_entity = None

        self.yang_name = "evpn"
        self.yang_parent_name = "Cisco-IOS-XR-evpn-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Evpn.Nodes)), ("active", ("active", Evpn.Active)), ("standby", ("standby", Evpn.Standby))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Evpn.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")

        self.active = Evpn.Active()
        self.active.parent = self
        self._children_name_map["active"] = "active"
        self._children_yang_names.add("active")

        self.standby = Evpn.Standby()
        self.standby.parent = self
        self._children_name_map["standby"] = "standby"
        self._children_yang_names.add("standby")
        self._segment_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn"


    class Nodes(Entity):
        """
        Table of EVPN operational data for a particular
        node
        
        .. attribute:: node
        
        	EVPN operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node>`
        
        

        """

        _prefix = 'evpn-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Evpn.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "evpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Evpn.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Evpn.Nodes, [], name, value)


        class Node(Entity):
            """
            EVPN operational data for a particular node
            
            .. attribute:: node_id  (key)
            
            	Location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: evis
            
            	L2VPN EVPN EVI Table
            	**type**\:  :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.Evis>`
            
            .. attribute:: summary
            
            	L2VPN EVPN Summary
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.Summary>`
            
            .. attribute:: evi_detail
            
            	L2VPN EVI Detail Table
            	**type**\:  :py:class:`EviDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail>`
            
            .. attribute:: internal_labels
            
            	EVPN Internal Label Table
            	**type**\:  :py:class:`InternalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.InternalLabels>`
            
            .. attribute:: ethernet_segments
            
            	EVPN Ethernet\-Segment Table
            	**type**\:  :py:class:`EthernetSegments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments>`
            
            .. attribute:: ac_ids
            
            	EVPN AC ID table
            	**type**\:  :py:class:`AcIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.AcIds>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_id']
                self._child_container_classes = OrderedDict([("evis", ("evis", Evpn.Nodes.Node.Evis)), ("summary", ("summary", Evpn.Nodes.Node.Summary)), ("evi-detail", ("evi_detail", Evpn.Nodes.Node.EviDetail)), ("internal-labels", ("internal_labels", Evpn.Nodes.Node.InternalLabels)), ("ethernet-segments", ("ethernet_segments", Evpn.Nodes.Node.EthernetSegments)), ("ac-ids", ("ac_ids", Evpn.Nodes.Node.AcIds))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_id', YLeaf(YType.str, 'node-id')),
                ])
                self.node_id = None

                self.evis = Evpn.Nodes.Node.Evis()
                self.evis.parent = self
                self._children_name_map["evis"] = "evis"
                self._children_yang_names.add("evis")

                self.summary = Evpn.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
                self._children_yang_names.add("summary")

                self.evi_detail = Evpn.Nodes.Node.EviDetail()
                self.evi_detail.parent = self
                self._children_name_map["evi_detail"] = "evi-detail"
                self._children_yang_names.add("evi-detail")

                self.internal_labels = Evpn.Nodes.Node.InternalLabels()
                self.internal_labels.parent = self
                self._children_name_map["internal_labels"] = "internal-labels"
                self._children_yang_names.add("internal-labels")

                self.ethernet_segments = Evpn.Nodes.Node.EthernetSegments()
                self.ethernet_segments.parent = self
                self._children_name_map["ethernet_segments"] = "ethernet-segments"
                self._children_yang_names.add("ethernet-segments")

                self.ac_ids = Evpn.Nodes.Node.AcIds()
                self.ac_ids.parent = self
                self._children_name_map["ac_ids"] = "ac-ids"
                self._children_yang_names.add("ac-ids")
                self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Nodes.Node, ['node_id'], name, value)


            class Evis(Entity):
                """
                L2VPN EVPN EVI Table
                
                .. attribute:: evi
                
                	L2VPN EVPN EVI Entry
                	**type**\: list of  		 :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.Evis.Evi>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Nodes.Node.Evis, self).__init__()

                    self.yang_name = "evis"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("evi", ("evi", Evpn.Nodes.Node.Evis.Evi))])
                    self._leafs = OrderedDict()

                    self.evi = YList(self)
                    self._segment_path = lambda: "evis"

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Nodes.Node.Evis, [], name, value)


                class Evi(Entity):
                    """
                    L2VPN EVPN EVI Entry
                    
                    .. attribute:: evi  (key)
                    
                    	EVPN id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bd_name
                    
                    	Bridge domain name
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Nodes.Node.Evis.Evi, self).__init__()

                        self.yang_name = "evi"
                        self.yang_parent_name = "evis"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['evi']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evi', YLeaf(YType.int32, 'evi')),
                            ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                            ('bd_name', YLeaf(YType.str, 'bd-name')),
                            ('type', YLeaf(YType.enumeration, 'type')),
                        ])
                        self.evi = None
                        self.evi_xr = None
                        self.bd_name = None
                        self.type = None
                        self._segment_path = lambda: "evi" + "[evi='" + str(self.evi) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Nodes.Node.Evis.Evi, ['evi', 'evi_xr', 'bd_name', 'type'], name, value)


            class Summary(Entity):
                """
                L2VPN EVPN Summary
                
                .. attribute:: router_id
                
                	EVPN Router ID
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: as_
                
                	BGP AS number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ev_is
                
                	Number of EVI DB Entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_mac_routes
                
                	Number of Local MAC Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_ipv4_mac_routes
                
                	Number of Local IPv4 MAC\-IP Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_ipv6_mac_routes
                
                	Number of Local IPv6 MAC\-IP Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: es_global_mac_routes
                
                	Number of ES\:Global MAC Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_mac_routes
                
                	Number of Remote MAC Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_soo_mac_routes
                
                	Number of Remote Soo MAC Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_ipv4_mac_routes
                
                	Number of Remote IPv4 MAC\-IP Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_ipv6_mac_routes
                
                	Number of Remote IPv6 MAC\-IP Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_imcast_routes
                
                	Number of Local IMCAST Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_imcast_routes
                
                	Number of Remote IMCAST Routes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: labels
                
                	Number of Internal Labels
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: es_entries
                
                	Number of ES Entries in DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: neighbor_entries
                
                	Number of neighbor Entries in DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_ead_routes
                
                	Number of Local EAD Entries in DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: remote_ead_routes
                
                	Number of Remote EAD Entries in DB
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: global_source_mac
                
                	Global Source MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: peering_time
                
                	EVPN ES Peering Time (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: recovery_time
                
                	EVPN ES Recovery Time (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: carving_time
                
                	EVPN ES Carving Time (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: mac_secure_move_count
                
                	Number of moves within the move interval before locking the MAC
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mac_secure_move_interval
                
                	Interval to watch for subsequent mac moves before locking the MAC
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mac_secure_freeze_time
                
                	Length of time to lock the mac after a MAC security violation
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mac_secure_retry_count
                
                	Number of times to retry after a MAC un\-freezes
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: cost_out
                
                	EVPN Node Cost\-out
                	**type**\: bool
                
                .. attribute:: startup_cost_in_time
                
                	EVPN Node startup cost\-in Time (minutes)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minute
                
                .. attribute:: l2rib_throttle
                
                	Send to L2RIB Throttled
                	**type**\: bool
                
                .. attribute:: logging_df_election_enabled
                
                	Logging EVPN Designated Forwarder changes enabled
                	**type**\: bool
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('router_id', YLeaf(YType.str, 'router-id')),
                        ('as_', YLeaf(YType.uint32, 'as')),
                        ('ev_is', YLeaf(YType.uint32, 'ev-is')),
                        ('local_mac_routes', YLeaf(YType.uint32, 'local-mac-routes')),
                        ('local_ipv4_mac_routes', YLeaf(YType.uint32, 'local-ipv4-mac-routes')),
                        ('local_ipv6_mac_routes', YLeaf(YType.uint32, 'local-ipv6-mac-routes')),
                        ('es_global_mac_routes', YLeaf(YType.uint32, 'es-global-mac-routes')),
                        ('remote_mac_routes', YLeaf(YType.uint32, 'remote-mac-routes')),
                        ('remote_soo_mac_routes', YLeaf(YType.uint32, 'remote-soo-mac-routes')),
                        ('remote_ipv4_mac_routes', YLeaf(YType.uint32, 'remote-ipv4-mac-routes')),
                        ('remote_ipv6_mac_routes', YLeaf(YType.uint32, 'remote-ipv6-mac-routes')),
                        ('local_imcast_routes', YLeaf(YType.uint32, 'local-imcast-routes')),
                        ('remote_imcast_routes', YLeaf(YType.uint32, 'remote-imcast-routes')),
                        ('labels', YLeaf(YType.uint32, 'labels')),
                        ('es_entries', YLeaf(YType.uint32, 'es-entries')),
                        ('neighbor_entries', YLeaf(YType.uint32, 'neighbor-entries')),
                        ('local_ead_routes', YLeaf(YType.uint32, 'local-ead-routes')),
                        ('remote_ead_routes', YLeaf(YType.uint32, 'remote-ead-routes')),
                        ('global_source_mac', YLeaf(YType.str, 'global-source-mac')),
                        ('peering_time', YLeaf(YType.uint32, 'peering-time')),
                        ('recovery_time', YLeaf(YType.uint32, 'recovery-time')),
                        ('carving_time', YLeaf(YType.uint32, 'carving-time')),
                        ('mac_secure_move_count', YLeaf(YType.uint32, 'mac-secure-move-count')),
                        ('mac_secure_move_interval', YLeaf(YType.uint32, 'mac-secure-move-interval')),
                        ('mac_secure_freeze_time', YLeaf(YType.uint32, 'mac-secure-freeze-time')),
                        ('mac_secure_retry_count', YLeaf(YType.uint32, 'mac-secure-retry-count')),
                        ('cost_out', YLeaf(YType.boolean, 'cost-out')),
                        ('startup_cost_in_time', YLeaf(YType.uint32, 'startup-cost-in-time')),
                        ('l2rib_throttle', YLeaf(YType.boolean, 'l2rib-throttle')),
                        ('logging_df_election_enabled', YLeaf(YType.boolean, 'logging-df-election-enabled')),
                    ])
                    self.router_id = None
                    self.as_ = None
                    self.ev_is = None
                    self.local_mac_routes = None
                    self.local_ipv4_mac_routes = None
                    self.local_ipv6_mac_routes = None
                    self.es_global_mac_routes = None
                    self.remote_mac_routes = None
                    self.remote_soo_mac_routes = None
                    self.remote_ipv4_mac_routes = None
                    self.remote_ipv6_mac_routes = None
                    self.local_imcast_routes = None
                    self.remote_imcast_routes = None
                    self.labels = None
                    self.es_entries = None
                    self.neighbor_entries = None
                    self.local_ead_routes = None
                    self.remote_ead_routes = None
                    self.global_source_mac = None
                    self.peering_time = None
                    self.recovery_time = None
                    self.carving_time = None
                    self.mac_secure_move_count = None
                    self.mac_secure_move_interval = None
                    self.mac_secure_freeze_time = None
                    self.mac_secure_retry_count = None
                    self.cost_out = None
                    self.startup_cost_in_time = None
                    self.l2rib_throttle = None
                    self.logging_df_election_enabled = None
                    self._segment_path = lambda: "summary"

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Nodes.Node.Summary, ['router_id', 'as_', 'ev_is', 'local_mac_routes', 'local_ipv4_mac_routes', 'local_ipv6_mac_routes', 'es_global_mac_routes', 'remote_mac_routes', 'remote_soo_mac_routes', 'remote_ipv4_mac_routes', 'remote_ipv6_mac_routes', 'local_imcast_routes', 'remote_imcast_routes', 'labels', 'es_entries', 'neighbor_entries', 'local_ead_routes', 'remote_ead_routes', 'global_source_mac', 'peering_time', 'recovery_time', 'carving_time', 'mac_secure_move_count', 'mac_secure_move_interval', 'mac_secure_freeze_time', 'mac_secure_retry_count', 'cost_out', 'startup_cost_in_time', 'l2rib_throttle', 'logging_df_election_enabled'], name, value)


            class EviDetail(Entity):
                """
                L2VPN EVI Detail Table
                
                .. attribute:: elements
                
                	EVI BGP RT Detail Info Elements
                	**type**\:  :py:class:`Elements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements>`
                
                .. attribute:: evi_children
                
                	Container for all EVI detail info
                	**type**\:  :py:class:`EviChildren <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Nodes.Node.EviDetail, self).__init__()

                    self.yang_name = "evi-detail"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("elements", ("elements", Evpn.Nodes.Node.EviDetail.Elements)), ("evi-children", ("evi_children", Evpn.Nodes.Node.EviDetail.EviChildren))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.elements = Evpn.Nodes.Node.EviDetail.Elements()
                    self.elements.parent = self
                    self._children_name_map["elements"] = "elements"
                    self._children_yang_names.add("elements")

                    self.evi_children = Evpn.Nodes.Node.EviDetail.EviChildren()
                    self.evi_children.parent = self
                    self._children_name_map["evi_children"] = "evi-children"
                    self._children_yang_names.add("evi-children")
                    self._segment_path = lambda: "evi-detail"


                class Elements(Entity):
                    """
                    EVI BGP RT Detail Info Elements
                    
                    .. attribute:: element
                    
                    	EVI BGP RT Detail Info
                    	**type**\: list of  		 :py:class:`Element <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Nodes.Node.EviDetail.Elements, self).__init__()

                        self.yang_name = "elements"
                        self.yang_parent_name = "evi-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("element", ("element", Evpn.Nodes.Node.EviDetail.Elements.Element))])
                        self._leafs = OrderedDict()

                        self.element = YList(self)
                        self._segment_path = lambda: "elements"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements, [], name, value)


                    class Element(Entity):
                        """
                        EVI BGP RT Detail Info
                        
                        .. attribute:: evi  (key)
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: flow_label
                        
                        	Flow Label Information
                        	**type**\:  :py:class:`FlowLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel>`
                        
                        .. attribute:: rd_auto
                        
                        	Automatic Route Distingtuisher
                        	**type**\:  :py:class:`RdAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto>`
                        
                        .. attribute:: rd_configured
                        
                        	Configured Route Distinguisher
                        	**type**\:  :py:class:`RdConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured>`
                        
                        .. attribute:: rt_auto
                        
                        	Automatic Route Target
                        	**type**\:  :py:class:`RtAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto>`
                        
                        .. attribute:: rt_auto_stitching
                        
                        	Automatic Route Target Stitching
                        	**type**\:  :py:class:`RtAutoStitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching>`
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: description
                        
                        	EVI description
                        	**type**\: str
                        
                        .. attribute:: bd_name
                        
                        	Bridge domain name
                        	**type**\: str
                        
                        .. attribute:: type
                        
                        	Service Type
                        	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                        
                        .. attribute:: unicast_label
                        
                        	Unicast Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: multicast_label
                        
                        	Multicast Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: cw_disable
                        
                        	Control\-Word Disable
                        	**type**\: bool
                        
                        .. attribute:: table_policy_name
                        
                        	Table\-policy Name
                        	**type**\: str
                        
                        .. attribute:: forward_class
                        
                        	Forward Class attribute
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: rt_import_block_set
                        
                        	Is Import RT None set
                        	**type**\: bool
                        
                        .. attribute:: rt_export_block_set
                        
                        	Is Export RT None set
                        	**type**\: bool
                        
                        .. attribute:: advertise_mac
                        
                        	Advertise MAC\-only routes on this EVI
                        	**type**\: bool
                        
                        .. attribute:: advertise_bvi_mac
                        
                        	Advertise BVI MACs routes on this EVI
                        	**type**\: bool
                        
                        .. attribute:: aliasing_disabled
                        
                        	Route Aliasing is disabled
                        	**type**\: bool
                        
                        .. attribute:: unknown_unicast_flooding_disabled
                        
                        	Unknown\-unicast flooding is disabled
                        	**type**\: bool
                        
                        .. attribute:: reoriginate_disabled
                        
                        	Route Re\-origination is disabled
                        	**type**\: bool
                        
                        .. attribute:: stitching
                        
                        	EVPN Instance is Regular/Stitching side
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: encapsulation
                        
                        	EVPN Instance encapsulation
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EviDetail.Elements.Element, self).__init__()

                            self.yang_name = "element"
                            self.yang_parent_name = "elements"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['evi']
                            self._child_container_classes = OrderedDict([("flow-label", ("flow_label", Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel)), ("rd-auto", ("rd_auto", Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto)), ("rd-configured", ("rd_configured", Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured)), ("rt-auto", ("rt_auto", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto)), ("rt-auto-stitching", ("rt_auto_stitching", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('description', YLeaf(YType.str, 'description')),
                                ('bd_name', YLeaf(YType.str, 'bd-name')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('unicast_label', YLeaf(YType.uint32, 'unicast-label')),
                                ('multicast_label', YLeaf(YType.uint32, 'multicast-label')),
                                ('cw_disable', YLeaf(YType.boolean, 'cw-disable')),
                                ('table_policy_name', YLeaf(YType.str, 'table-policy-name')),
                                ('forward_class', YLeaf(YType.uint8, 'forward-class')),
                                ('rt_import_block_set', YLeaf(YType.boolean, 'rt-import-block-set')),
                                ('rt_export_block_set', YLeaf(YType.boolean, 'rt-export-block-set')),
                                ('advertise_mac', YLeaf(YType.boolean, 'advertise-mac')),
                                ('advertise_bvi_mac', YLeaf(YType.boolean, 'advertise-bvi-mac')),
                                ('aliasing_disabled', YLeaf(YType.boolean, 'aliasing-disabled')),
                                ('unknown_unicast_flooding_disabled', YLeaf(YType.boolean, 'unknown-unicast-flooding-disabled')),
                                ('reoriginate_disabled', YLeaf(YType.boolean, 'reoriginate-disabled')),
                                ('stitching', YLeaf(YType.uint8, 'stitching')),
                                ('encapsulation', YLeaf(YType.uint8, 'encapsulation')),
                            ])
                            self.evi = None
                            self.evi_xr = None
                            self.description = None
                            self.bd_name = None
                            self.type = None
                            self.unicast_label = None
                            self.multicast_label = None
                            self.cw_disable = None
                            self.table_policy_name = None
                            self.forward_class = None
                            self.rt_import_block_set = None
                            self.rt_export_block_set = None
                            self.advertise_mac = None
                            self.advertise_bvi_mac = None
                            self.aliasing_disabled = None
                            self.unknown_unicast_flooding_disabled = None
                            self.reoriginate_disabled = None
                            self.stitching = None
                            self.encapsulation = None

                            self.flow_label = Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel()
                            self.flow_label.parent = self
                            self._children_name_map["flow_label"] = "flow-label"
                            self._children_yang_names.add("flow-label")

                            self.rd_auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto()
                            self.rd_auto.parent = self
                            self._children_name_map["rd_auto"] = "rd-auto"
                            self._children_yang_names.add("rd-auto")

                            self.rd_configured = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured()
                            self.rd_configured.parent = self
                            self._children_name_map["rd_configured"] = "rd-configured"
                            self._children_yang_names.add("rd-configured")

                            self.rt_auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto()
                            self.rt_auto.parent = self
                            self._children_name_map["rt_auto"] = "rt-auto"
                            self._children_yang_names.add("rt-auto")

                            self.rt_auto_stitching = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching()
                            self.rt_auto_stitching.parent = self
                            self._children_name_map["rt_auto_stitching"] = "rt-auto-stitching"
                            self._children_yang_names.add("rt-auto-stitching")
                            self._segment_path = lambda: "element" + "[evi='" + str(self.evi) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element, ['evi', 'evi_xr', 'description', 'bd_name', 'type', 'unicast_label', 'multicast_label', 'cw_disable', 'table_policy_name', 'forward_class', 'rt_import_block_set', 'rt_export_block_set', 'advertise_mac', 'advertise_bvi_mac', 'aliasing_disabled', 'unknown_unicast_flooding_disabled', 'reoriginate_disabled', 'stitching', 'encapsulation'], name, value)


                        class FlowLabel(Entity):
                            """
                            Flow Label Information
                            
                            .. attribute:: static_flow_label
                            
                            	Static flow label
                            	**type**\: bool
                            
                            .. attribute:: global_flow_label
                            
                            	Globally configured flow label
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel, self).__init__()

                                self.yang_name = "flow-label"
                                self.yang_parent_name = "element"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('static_flow_label', YLeaf(YType.boolean, 'static-flow-label')),
                                    ('global_flow_label', YLeaf(YType.boolean, 'global-flow-label')),
                                ])
                                self.static_flow_label = None
                                self.global_flow_label = None
                                self._segment_path = lambda: "flow-label"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel, ['static_flow_label', 'global_flow_label'], name, value)


                        class RdAuto(Entity):
                            """
                            Automatic Route Distingtuisher
                            
                            .. attribute:: auto
                            
                            	auto
                            	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr>`
                            
                            .. attribute:: rd
                            
                            	RD
                            	**type**\:  :py:class:`L2vpnAdRd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRd>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto, self).__init__()

                                self.yang_name = "rd-auto"
                                self.yang_parent_name = "element"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("auto", ("auto", Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto)), ("two-byte-as", ("two_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rd', YLeaf(YType.enumeration, 'rd')),
                                ])
                                self.rd = None

                                self.auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto()
                                self.auto.parent = self
                                self._children_name_map["auto"] = "auto"
                                self._children_yang_names.add("auto")

                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs()
                                self.two_byte_as.parent = self
                                self._children_name_map["two_byte_as"] = "two-byte-as"
                                self._children_yang_names.add("two-byte-as")

                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs()
                                self.four_byte_as.parent = self
                                self._children_name_map["four_byte_as"] = "four-byte-as"
                                self._children_yang_names.add("four-byte-as")

                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr()
                                self.v4_addr.parent = self
                                self._children_name_map["v4_addr"] = "v4-addr"
                                self._children_yang_names.add("v4-addr")
                                self._segment_path = lambda: "rd-auto"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto, ['rd'], name, value)


                            class Auto(Entity):
                                """
                                auto
                                
                                .. attribute:: router_id
                                
                                	BGP Router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: auto_index
                                
                                	Auto\-generated Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto, self).__init__()

                                    self.yang_name = "auto"
                                    self.yang_parent_name = "rd-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', YLeaf(YType.str, 'router-id')),
                                        ('auto_index', YLeaf(YType.uint16, 'auto-index')),
                                    ])
                                    self.router_id = None
                                    self.auto_index = None
                                    self._segment_path = lambda: "auto"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto, ['router_id', 'auto_index'], name, value)


                            class TwoByteAs(Entity):
                                """
                                two byte as
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs, self).__init__()

                                    self.yang_name = "two-byte-as"
                                    self.yang_parent_name = "rd-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                        ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                    ])
                                    self.two_byte_as = None
                                    self.four_byte_index = None
                                    self._segment_path = lambda: "two-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                            class FourByteAs(Entity):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs, self).__init__()

                                    self.yang_name = "four-byte-as"
                                    self.yang_parent_name = "rd-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.four_byte_as = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "four-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                            class V4Addr(Entity):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr, self).__init__()

                                    self.yang_name = "v4-addr"
                                    self.yang_parent_name = "rd-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.ipv4_address = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "v4-addr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                        class RdConfigured(Entity):
                            """
                            Configured Route Distinguisher
                            
                            .. attribute:: auto
                            
                            	auto
                            	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto>`
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr>`
                            
                            .. attribute:: rd
                            
                            	RD
                            	**type**\:  :py:class:`L2vpnAdRd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRd>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured, self).__init__()

                                self.yang_name = "rd-configured"
                                self.yang_parent_name = "element"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("auto", ("auto", Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto)), ("two-byte-as", ("two_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rd', YLeaf(YType.enumeration, 'rd')),
                                ])
                                self.rd = None

                                self.auto = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto()
                                self.auto.parent = self
                                self._children_name_map["auto"] = "auto"
                                self._children_yang_names.add("auto")

                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs()
                                self.two_byte_as.parent = self
                                self._children_name_map["two_byte_as"] = "two-byte-as"
                                self._children_yang_names.add("two-byte-as")

                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs()
                                self.four_byte_as.parent = self
                                self._children_name_map["four_byte_as"] = "four-byte-as"
                                self._children_yang_names.add("four-byte-as")

                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr()
                                self.v4_addr.parent = self
                                self._children_name_map["v4_addr"] = "v4-addr"
                                self._children_yang_names.add("v4-addr")
                                self._segment_path = lambda: "rd-configured"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured, ['rd'], name, value)


                            class Auto(Entity):
                                """
                                auto
                                
                                .. attribute:: router_id
                                
                                	BGP Router ID
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: auto_index
                                
                                	Auto\-generated Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto, self).__init__()

                                    self.yang_name = "auto"
                                    self.yang_parent_name = "rd-configured"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('router_id', YLeaf(YType.str, 'router-id')),
                                        ('auto_index', YLeaf(YType.uint16, 'auto-index')),
                                    ])
                                    self.router_id = None
                                    self.auto_index = None
                                    self._segment_path = lambda: "auto"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto, ['router_id', 'auto_index'], name, value)


                            class TwoByteAs(Entity):
                                """
                                two byte as
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs, self).__init__()

                                    self.yang_name = "two-byte-as"
                                    self.yang_parent_name = "rd-configured"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                        ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                    ])
                                    self.two_byte_as = None
                                    self.four_byte_index = None
                                    self._segment_path = lambda: "two-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                            class FourByteAs(Entity):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs, self).__init__()

                                    self.yang_name = "four-byte-as"
                                    self.yang_parent_name = "rd-configured"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.four_byte_as = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "four-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                            class V4Addr(Entity):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr, self).__init__()

                                    self.yang_name = "v4-addr"
                                    self.yang_parent_name = "rd-configured"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.ipv4_address = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "v4-addr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                        class RtAuto(Entity):
                            """
                            Automatic Route Target
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr>`
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto, self).__init__()

                                self.yang_name = "rt-auto"
                                self.yang_parent_name = "element"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr)), ("es-import", ("es_import", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rt', YLeaf(YType.enumeration, 'rt')),
                                ])
                                self.rt = None

                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs()
                                self.two_byte_as.parent = self
                                self._children_name_map["two_byte_as"] = "two-byte-as"
                                self._children_yang_names.add("two-byte-as")

                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs()
                                self.four_byte_as.parent = self
                                self._children_name_map["four_byte_as"] = "four-byte-as"
                                self._children_yang_names.add("four-byte-as")

                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr()
                                self.v4_addr.parent = self
                                self._children_name_map["v4_addr"] = "v4-addr"
                                self._children_yang_names.add("v4-addr")

                                self.es_import = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport()
                                self.es_import.parent = self
                                self._children_name_map["es_import"] = "es-import"
                                self._children_yang_names.add("es-import")
                                self._segment_path = lambda: "rt-auto"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto, ['rt'], name, value)


                            class TwoByteAs(Entity):
                                """
                                two byte as
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs, self).__init__()

                                    self.yang_name = "two-byte-as"
                                    self.yang_parent_name = "rt-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                        ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                    ])
                                    self.two_byte_as = None
                                    self.four_byte_index = None
                                    self._segment_path = lambda: "two-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                            class FourByteAs(Entity):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs, self).__init__()

                                    self.yang_name = "four-byte-as"
                                    self.yang_parent_name = "rt-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.four_byte_as = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "four-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                            class V4Addr(Entity):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr, self).__init__()

                                    self.yang_name = "v4-addr"
                                    self.yang_parent_name = "rt-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.ipv4_address = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "v4-addr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                            class EsImport(Entity):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport, self).__init__()

                                    self.yang_name = "es-import"
                                    self.yang_parent_name = "rt-auto"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                        ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                    ])
                                    self.high_bytes = None
                                    self.low_bytes = None
                                    self._segment_path = lambda: "es-import"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport, ['high_bytes', 'low_bytes'], name, value)


                        class RtAutoStitching(Entity):
                            """
                            Automatic Route Target Stitching
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr>`
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching, self).__init__()

                                self.yang_name = "rt-auto-stitching"
                                self.yang_parent_name = "element"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr)), ("es-import", ("es_import", Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rt', YLeaf(YType.enumeration, 'rt')),
                                ])
                                self.rt = None

                                self.two_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs()
                                self.two_byte_as.parent = self
                                self._children_name_map["two_byte_as"] = "two-byte-as"
                                self._children_yang_names.add("two-byte-as")

                                self.four_byte_as = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs()
                                self.four_byte_as.parent = self
                                self._children_name_map["four_byte_as"] = "four-byte-as"
                                self._children_yang_names.add("four-byte-as")

                                self.v4_addr = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr()
                                self.v4_addr.parent = self
                                self._children_name_map["v4_addr"] = "v4-addr"
                                self._children_yang_names.add("v4-addr")

                                self.es_import = Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport()
                                self.es_import.parent = self
                                self._children_name_map["es_import"] = "es-import"
                                self._children_yang_names.add("es-import")
                                self._segment_path = lambda: "rt-auto-stitching"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching, ['rt'], name, value)


                            class TwoByteAs(Entity):
                                """
                                two byte as
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs, self).__init__()

                                    self.yang_name = "two-byte-as"
                                    self.yang_parent_name = "rt-auto-stitching"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                        ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                    ])
                                    self.two_byte_as = None
                                    self.four_byte_index = None
                                    self._segment_path = lambda: "two-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                            class FourByteAs(Entity):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs, self).__init__()

                                    self.yang_name = "four-byte-as"
                                    self.yang_parent_name = "rt-auto-stitching"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.four_byte_as = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "four-byte-as"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                            class V4Addr(Entity):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr, self).__init__()

                                    self.yang_name = "v4-addr"
                                    self.yang_parent_name = "rt-auto-stitching"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.ipv4_address = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "v4-addr"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                            class EsImport(Entity):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport, self).__init__()

                                    self.yang_name = "es-import"
                                    self.yang_parent_name = "rt-auto-stitching"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                        ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                    ])
                                    self.high_bytes = None
                                    self.low_bytes = None
                                    self._segment_path = lambda: "es-import"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport, ['high_bytes', 'low_bytes'], name, value)


                class EviChildren(Entity):
                    """
                    Container for all EVI detail info
                    
                    .. attribute:: neighbors
                    
                    	EVPN Neighbor table
                    	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors>`
                    
                    .. attribute:: ethernet_auto_discoveries
                    
                    	EVPN Ethernet Auto\-Discovery table
                    	**type**\:  :py:class:`EthernetAutoDiscoveries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries>`
                    
                    .. attribute:: inclusive_multicasts
                    
                    	L2VPN EVPN IMCAST table
                    	**type**\:  :py:class:`InclusiveMulticasts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts>`
                    
                    .. attribute:: route_targets
                    
                    	L2VPN EVPN EVI RT Child Table
                    	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets>`
                    
                    .. attribute:: macs
                    
                    	L2VPN EVPN EVI MAC table
                    	**type**\:  :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Nodes.Node.EviDetail.EviChildren, self).__init__()

                        self.yang_name = "evi-children"
                        self.yang_parent_name = "evi-detail"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("neighbors", ("neighbors", Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors)), ("ethernet-auto-discoveries", ("ethernet_auto_discoveries", Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries)), ("inclusive-multicasts", ("inclusive_multicasts", Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts)), ("route-targets", ("route_targets", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets)), ("macs", ("macs", Evpn.Nodes.Node.EviDetail.EviChildren.Macs))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.neighbors = Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors()
                        self.neighbors.parent = self
                        self._children_name_map["neighbors"] = "neighbors"
                        self._children_yang_names.add("neighbors")

                        self.ethernet_auto_discoveries = Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries()
                        self.ethernet_auto_discoveries.parent = self
                        self._children_name_map["ethernet_auto_discoveries"] = "ethernet-auto-discoveries"
                        self._children_yang_names.add("ethernet-auto-discoveries")

                        self.inclusive_multicasts = Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts()
                        self.inclusive_multicasts.parent = self
                        self._children_name_map["inclusive_multicasts"] = "inclusive-multicasts"
                        self._children_yang_names.add("inclusive-multicasts")

                        self.route_targets = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets()
                        self.route_targets.parent = self
                        self._children_name_map["route_targets"] = "route-targets"
                        self._children_yang_names.add("route-targets")

                        self.macs = Evpn.Nodes.Node.EviDetail.EviChildren.Macs()
                        self.macs.parent = self
                        self._children_name_map["macs"] = "macs"
                        self._children_yang_names.add("macs")
                        self._segment_path = lambda: "evi-children"


                    class Neighbors(Entity):
                        """
                        EVPN Neighbor table
                        
                        .. attribute:: neighbor
                        
                        	EVPN Neighbor table
                        	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors, self).__init__()

                            self.yang_name = "neighbors"
                            self.yang_parent_name = "evi-children"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("neighbor", ("neighbor", Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor))])
                            self._leafs = OrderedDict()

                            self.neighbor = YList(self)
                            self._segment_path = lambda: "neighbors"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors, [], name, value)


                        class Neighbor(Entity):
                            """
                            EVPN Neighbor table
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: neighbor_ip
                            
                            	Neighbor IP
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: evi_xr
                            
                            	E\-VPN id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: neighbor
                            
                            	Neighbor IP
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor, self).__init__()

                                self.yang_name = "neighbor"
                                self.yang_parent_name = "neighbors"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('evi', YLeaf(YType.int32, 'evi')),
                                    ('neighbor_ip', YLeaf(YType.str, 'neighbor-ip')),
                                    ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                    ('neighbor', YLeaf(YType.str, 'neighbor')),
                                ])
                                self.evi = None
                                self.neighbor_ip = None
                                self.evi_xr = None
                                self.neighbor = None
                                self._segment_path = lambda: "neighbor"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor, ['evi', 'neighbor_ip', 'evi_xr', 'neighbor'], name, value)


                    class EthernetAutoDiscoveries(Entity):
                        """
                        EVPN Ethernet Auto\-Discovery table
                        
                        .. attribute:: ethernet_auto_discovery
                        
                        	EVPN Ethernet Auto\-Discovery Entry
                        	**type**\: list of  		 :py:class:`EthernetAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries, self).__init__()

                            self.yang_name = "ethernet-auto-discoveries"
                            self.yang_parent_name = "evi-children"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ethernet-auto-discovery", ("ethernet_auto_discovery", Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery))])
                            self._leafs = OrderedDict()

                            self.ethernet_auto_discovery = YList(self)
                            self._segment_path = lambda: "ethernet-auto-discoveries"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries, [], name, value)


                        class EthernetAutoDiscovery(Entity):
                            """
                            EVPN Ethernet Auto\-Discovery Entry
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: esi1
                            
                            	ES id (part 1/5)
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi2
                            
                            	ES id (part 2/5)
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi3
                            
                            	ES id (part 3/5)
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi4
                            
                            	ES id (part 4/5)
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: esi5
                            
                            	ES id (part 5/5)
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            .. attribute:: ethernet_tag
                            
                            	Ethernet Tag ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ethernet_vpnid
                            
                            	E\-VPN id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Service Type
                            	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                            
                            .. attribute:: ethernet_tag_xr
                            
                            	Ethernet Tag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_next_hop
                            
                            	Local nexthop IP
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: local_label
                            
                            	Associated local label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_local_ead
                            
                            	Indication of EthernetAutoDiscovery Route is local
                            	**type**\: bool
                            
                            .. attribute:: encap
                            
                            	Encap type of local or remote EAD
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: redundancy_single_active
                            
                            	Single\-active redundancy configured at remote EAD
                            	**type**\: bool
                            
                            .. attribute:: redundancy_single_flow_active
                            
                            	Single\-flow\-active redundancy configured at remote EAD
                            	**type**\: bool
                            
                            .. attribute:: num_paths
                            
                            	 Number of items in path list buffer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ethernet_segment_identifier
                            
                            	Ethernet Segment id
                            	**type**\: list of  		 :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier>`
                            
                            .. attribute:: path_buffer
                            
                            	Path List Buffer
                            	**type**\: list of  		 :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery, self).__init__()

                                self.yang_name = "ethernet-auto-discovery"
                                self.yang_parent_name = "ethernet-auto-discoveries"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("ethernet-segment-identifier", ("ethernet_segment_identifier", Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier)), ("path-buffer", ("path_buffer", Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer))])
                                self._leafs = OrderedDict([
                                    ('evi', YLeaf(YType.int32, 'evi')),
                                    ('esi1', YLeaf(YType.str, 'esi1')),
                                    ('esi2', YLeaf(YType.str, 'esi2')),
                                    ('esi3', YLeaf(YType.str, 'esi3')),
                                    ('esi4', YLeaf(YType.str, 'esi4')),
                                    ('esi5', YLeaf(YType.str, 'esi5')),
                                    ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                    ('ethernet_vpnid', YLeaf(YType.uint32, 'ethernet-vpnid')),
                                    ('type', YLeaf(YType.enumeration, 'type')),
                                    ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                    ('local_next_hop', YLeaf(YType.str, 'local-next-hop')),
                                    ('local_label', YLeaf(YType.uint32, 'local-label')),
                                    ('is_local_ead', YLeaf(YType.boolean, 'is-local-ead')),
                                    ('encap', YLeaf(YType.uint8, 'encap')),
                                    ('redundancy_single_active', YLeaf(YType.boolean, 'redundancy-single-active')),
                                    ('redundancy_single_flow_active', YLeaf(YType.boolean, 'redundancy-single-flow-active')),
                                    ('num_paths', YLeaf(YType.uint32, 'num-paths')),
                                ])
                                self.evi = None
                                self.esi1 = None
                                self.esi2 = None
                                self.esi3 = None
                                self.esi4 = None
                                self.esi5 = None
                                self.ethernet_tag = None
                                self.ethernet_vpnid = None
                                self.type = None
                                self.ethernet_tag_xr = None
                                self.local_next_hop = None
                                self.local_label = None
                                self.is_local_ead = None
                                self.encap = None
                                self.redundancy_single_active = None
                                self.redundancy_single_flow_active = None
                                self.num_paths = None

                                self.ethernet_segment_identifier = YList(self)
                                self.path_buffer = YList(self)
                                self._segment_path = lambda: "ethernet-auto-discovery"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery, ['evi', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'ethernet_tag', 'ethernet_vpnid', 'type', 'ethernet_tag_xr', 'local_next_hop', 'local_label', 'is_local_ead', 'encap', 'redundancy_single_active', 'redundancy_single_flow_active', 'num_paths'], name, value)


                            class EthernetSegmentIdentifier(Entity):
                                """
                                Ethernet Segment id
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier, self).__init__()

                                    self.yang_name = "ethernet-segment-identifier"
                                    self.yang_parent_name = "ethernet-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint8, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "ethernet-segment-identifier"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier, ['entry'], name, value)


                            class PathBuffer(Entity):
                                """
                                Path List Buffer
                                
                                .. attribute:: next_hop
                                
                                	Next\-hop IP address (v6 format)
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: output_label
                                
                                	Output Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: srte_tunnel
                                
                                	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer, self).__init__()

                                    self.yang_name = "path-buffer"
                                    self.yang_parent_name = "ethernet-auto-discovery"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('next_hop', YLeaf(YType.str, 'next-hop')),
                                        ('output_label', YLeaf(YType.uint32, 'output-label')),
                                        ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                                    ])
                                    self.next_hop = None
                                    self.output_label = None
                                    self.srte_tunnel = None
                                    self._segment_path = lambda: "path-buffer"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                    class InclusiveMulticasts(Entity):
                        """
                        L2VPN EVPN IMCAST table
                        
                        .. attribute:: inclusive_multicast
                        
                        	L2VPN EVPN IMCAST table
                        	**type**\: list of  		 :py:class:`InclusiveMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts, self).__init__()

                            self.yang_name = "inclusive-multicasts"
                            self.yang_parent_name = "evi-children"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("inclusive-multicast", ("inclusive_multicast", Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast))])
                            self._leafs = OrderedDict()

                            self.inclusive_multicast = YList(self)
                            self._segment_path = lambda: "inclusive-multicasts"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts, [], name, value)


                        class InclusiveMulticast(Entity):
                            """
                            L2VPN EVPN IMCAST table
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ethernet_tag
                            
                            	Ethernet Tag
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: originating_ip
                            
                            	Originating IP
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: evi_xr
                            
                            	E\-VPN id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ethernet_tag_xr
                            
                            	Ethernet Tag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: originating_ip_xr
                            
                            	Originating IP
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: next_hop
                            
                            	IP of nexthop
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_local_entry
                            
                            	Local entry
                            	**type**\: bool
                            
                            .. attribute:: is_proxy_entry
                            
                            	Proxy entry
                            	**type**\: bool
                            
                            .. attribute:: encap_type
                            
                            	Encap type of local or remote IMCAST route
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast, self).__init__()

                                self.yang_name = "inclusive-multicast"
                                self.yang_parent_name = "inclusive-multicasts"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('evi', YLeaf(YType.int32, 'evi')),
                                    ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                    ('originating_ip', YLeaf(YType.str, 'originating-ip')),
                                    ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                    ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                    ('originating_ip_xr', YLeaf(YType.str, 'originating-ip-xr')),
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('output_label', YLeaf(YType.uint32, 'output-label')),
                                    ('is_local_entry', YLeaf(YType.boolean, 'is-local-entry')),
                                    ('is_proxy_entry', YLeaf(YType.boolean, 'is-proxy-entry')),
                                    ('encap_type', YLeaf(YType.uint8, 'encap-type')),
                                ])
                                self.evi = None
                                self.ethernet_tag = None
                                self.originating_ip = None
                                self.evi_xr = None
                                self.ethernet_tag_xr = None
                                self.originating_ip_xr = None
                                self.next_hop = None
                                self.output_label = None
                                self.is_local_entry = None
                                self.is_proxy_entry = None
                                self.encap_type = None
                                self._segment_path = lambda: "inclusive-multicast"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast, ['evi', 'ethernet_tag', 'originating_ip', 'evi_xr', 'ethernet_tag_xr', 'originating_ip_xr', 'next_hop', 'output_label', 'is_local_entry', 'is_proxy_entry', 'encap_type'], name, value)


                    class RouteTargets(Entity):
                        """
                        L2VPN EVPN EVI RT Child Table
                        
                        .. attribute:: route_target
                        
                        	L2VPN EVPN EVI RT Table
                        	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets, self).__init__()

                            self.yang_name = "route-targets"
                            self.yang_parent_name = "evi-children"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("route-target", ("route_target", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget))])
                            self._leafs = OrderedDict()

                            self.route_target = YList(self)
                            self._segment_path = lambda: "route-targets"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets, [], name, value)


                        class RouteTarget(Entity):
                            """
                            L2VPN EVPN EVI RT Table
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: role
                            
                            	Role of the route target
                            	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetRole>`
                            
                            .. attribute:: type
                            
                            	Type of the route target
                            	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTarget>`
                            
                            .. attribute:: format
                            
                            	Format of the route target
                            	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetFormat>`
                            
                            .. attribute:: as_
                            
                            	Two or Four byte AS Number
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: as_index
                            
                            	RT AS Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: addr_index
                            
                            	RT IP Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address
                            
                            	RT IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: route_target
                            
                            	Route Target
                            	**type**\:  :py:class:`RouteTarget_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_>`
                            
                            .. attribute:: bd_name
                            
                            	Bridge Domain Name
                            	**type**\: str
                            
                            .. attribute:: evi_xr
                            
                            	VPN ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: route_target_role
                            
                            	RT Role
                            	**type**\:  :py:class:`L2vpnAdRtRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRtRole>`
                            
                            .. attribute:: route_target_stitching
                            
                            	RT Stitching
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "route-targets"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("route-target", ("route_target", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('evi', YLeaf(YType.int32, 'evi')),
                                    ('role', YLeaf(YType.enumeration, 'role')),
                                    ('type', YLeaf(YType.enumeration, 'type')),
                                    ('format', YLeaf(YType.enumeration, 'format')),
                                    ('as_', YLeaf(YType.uint32, 'as')),
                                    ('as_index', YLeaf(YType.uint32, 'as-index')),
                                    ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                    ('address', YLeaf(YType.str, 'address')),
                                    ('bd_name', YLeaf(YType.str, 'bd-name')),
                                    ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                    ('route_target_role', YLeaf(YType.enumeration, 'route-target-role')),
                                    ('route_target_stitching', YLeaf(YType.boolean, 'route-target-stitching')),
                                ])
                                self.evi = None
                                self.role = None
                                self.type = None
                                self.format = None
                                self.as_ = None
                                self.as_index = None
                                self.addr_index = None
                                self.address = None
                                self.bd_name = None
                                self.evi_xr = None
                                self.route_target_role = None
                                self.route_target_stitching = None

                                self.route_target = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_()
                                self.route_target.parent = self
                                self._children_name_map["route_target"] = "route-target"
                                self._children_yang_names.add("route-target")
                                self._segment_path = lambda: "route-target"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget, ['evi', 'role', 'type', 'format', 'as_', 'as_index', 'addr_index', 'address', 'bd_name', 'evi_xr', 'route_target_role', 'route_target_stitching'], name, value)


                            class RouteTarget_(Entity):
                                """
                                Route Target
                                
                                .. attribute:: two_byte_as
                                
                                	two byte as
                                	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs>`
                                
                                .. attribute:: four_byte_as
                                
                                	four byte as
                                	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs>`
                                
                                .. attribute:: v4_addr
                                
                                	v4 addr
                                	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr>`
                                
                                .. attribute:: es_import
                                
                                	es import
                                	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport>`
                                
                                .. attribute:: rt
                                
                                	RT
                                	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_, self).__init__()

                                    self.yang_name = "route-target"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr)), ("es-import", ("es_import", Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('rt', YLeaf(YType.enumeration, 'rt')),
                                    ])
                                    self.rt = None

                                    self.two_byte_as = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs()
                                    self.two_byte_as.parent = self
                                    self._children_name_map["two_byte_as"] = "two-byte-as"
                                    self._children_yang_names.add("two-byte-as")

                                    self.four_byte_as = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs()
                                    self.four_byte_as.parent = self
                                    self._children_name_map["four_byte_as"] = "four-byte-as"
                                    self._children_yang_names.add("four-byte-as")

                                    self.v4_addr = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr()
                                    self.v4_addr.parent = self
                                    self._children_name_map["v4_addr"] = "v4-addr"
                                    self._children_yang_names.add("v4-addr")

                                    self.es_import = Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport()
                                    self.es_import.parent = self
                                    self._children_name_map["es_import"] = "es-import"
                                    self._children_yang_names.add("es-import")
                                    self._segment_path = lambda: "route-target"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_, ['rt'], name, value)


                                class TwoByteAs(Entity):
                                    """
                                    two byte as
                                    
                                    .. attribute:: two_byte_as
                                    
                                    	2 Byte AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: four_byte_index
                                    
                                    	4 Byte Index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs, self).__init__()

                                        self.yang_name = "two-byte-as"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                            ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                        ])
                                        self.two_byte_as = None
                                        self.four_byte_index = None
                                        self._segment_path = lambda: "two-byte-as"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                                class FourByteAs(Entity):
                                    """
                                    four byte as
                                    
                                    .. attribute:: four_byte_as
                                    
                                    	4 Byte AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: two_byte_index
                                    
                                    	2 Byte Index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs, self).__init__()

                                        self.yang_name = "four-byte-as"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                            ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                        ])
                                        self.four_byte_as = None
                                        self.two_byte_index = None
                                        self._segment_path = lambda: "four-byte-as"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                                class V4Addr(Entity):
                                    """
                                    v4 addr
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 Address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: two_byte_index
                                    
                                    	2 Byte Index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr, self).__init__()

                                        self.yang_name = "v4-addr"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                            ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                        ])
                                        self.ipv4_address = None
                                        self.two_byte_index = None
                                        self._segment_path = lambda: "v4-addr"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                                class EsImport(Entity):
                                    """
                                    es import
                                    
                                    .. attribute:: high_bytes
                                    
                                    	Top 4 bytes of ES Import
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: low_bytes
                                    
                                    	Low 2 bytes of ES Import
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'evpn-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport, self).__init__()

                                        self.yang_name = "es-import"
                                        self.yang_parent_name = "route-target"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                            ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                        ])
                                        self.high_bytes = None
                                        self.low_bytes = None
                                        self._segment_path = lambda: "es-import"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport, ['high_bytes', 'low_bytes'], name, value)


                    class Macs(Entity):
                        """
                        L2VPN EVPN EVI MAC table
                        
                        .. attribute:: mac
                        
                        	L2VPN EVPN MAC table
                        	**type**\: list of  		 :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EviDetail.EviChildren.Macs, self).__init__()

                            self.yang_name = "macs"
                            self.yang_parent_name = "evi-children"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("mac", ("mac", Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac))])
                            self._leafs = OrderedDict()

                            self.mac = YList(self)
                            self._segment_path = lambda: "macs"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Macs, [], name, value)


                        class Mac(Entity):
                            """
                            L2VPN EVPN MAC table
                            
                            .. attribute:: evi
                            
                            	EVPN id
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: ethernet_tag
                            
                            	Ethernet Tag ID
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: mac_address
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: ip_address
                            
                            	IP Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ethernet_tag_xr
                            
                            	Ethernet Tag
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mac_address_xr
                            
                            	MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: ip_address_xr
                            
                            	IP address (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: local_label
                            
                            	Associated local label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_paths
                            
                            	 Number of items in path list buffer
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_local_mac
                            
                            	Indication of MAC being locally generated
                            	**type**\: bool
                            
                            .. attribute:: is_proxy_entry
                            
                            	Proxy entry
                            	**type**\: bool
                            
                            .. attribute:: is_remote_mac
                            
                            	Indication of MAC being remotely generated
                            	**type**\: bool
                            
                            .. attribute:: soo_nexthop
                            
                            	SOO nexthop (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipnh_address
                            
                            	IP nexthop address (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: esi_port_key
                            
                            	ESI port key
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: local_encap_type
                            
                            	Encap type of local MAC
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: remote_encap_type
                            
                            	Encap type of remote MAC
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: learned_bridge_port_name
                            
                            	Port the MAC was learned on
                            	**type**\: str
                            
                            .. attribute:: local_seq_id
                            
                            	local seq id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: remote_seq_id
                            
                            	remote seq id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_l3_label
                            
                            	local l3 label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: router_mac_address
                            
                            	Router MAC address
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                            
                            .. attribute:: mac_flush_requested
                            
                            	Number of flushes requested 
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: mac_flush_received
                            
                            	Number of flushes received 
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: internal_label
                            
                            	MPLS Internal Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: resolved
                            
                            	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                            	**type**\: bool
                            
                            .. attribute:: local_is_static
                            
                            	Indication if Local MAC is statically configured
                            	**type**\: bool
                            
                            .. attribute:: remote_is_static
                            
                            	Indication if Remote MAC is statically configured
                            	**type**\: bool
                            
                            .. attribute:: local_ethernet_segment_identifier
                            
                            	Local Ethernet Segment id
                            	**type**\: list of  		 :py:class:`LocalEthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier>`
                            
                            .. attribute:: remote_ethernet_segment_identifier
                            
                            	Remote Ethernet Segment id
                            	**type**\: list of  		 :py:class:`RemoteEthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier>`
                            
                            .. attribute:: path_buffer
                            
                            	Path List Buffer
                            	**type**\: list of  		 :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "macs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("local-ethernet-segment-identifier", ("local_ethernet_segment_identifier", Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier)), ("remote-ethernet-segment-identifier", ("remote_ethernet_segment_identifier", Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier)), ("path-buffer", ("path_buffer", Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer))])
                                self._leafs = OrderedDict([
                                    ('evi', YLeaf(YType.int32, 'evi')),
                                    ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                                    ('ip_address', YLeaf(YType.str, 'ip-address')),
                                    ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                    ('mac_address_xr', YLeaf(YType.str, 'mac-address-xr')),
                                    ('ip_address_xr', YLeaf(YType.str, 'ip-address-xr')),
                                    ('local_label', YLeaf(YType.uint32, 'local-label')),
                                    ('num_paths', YLeaf(YType.uint32, 'num-paths')),
                                    ('is_local_mac', YLeaf(YType.boolean, 'is-local-mac')),
                                    ('is_proxy_entry', YLeaf(YType.boolean, 'is-proxy-entry')),
                                    ('is_remote_mac', YLeaf(YType.boolean, 'is-remote-mac')),
                                    ('soo_nexthop', YLeaf(YType.str, 'soo-nexthop')),
                                    ('ipnh_address', YLeaf(YType.str, 'ipnh-address')),
                                    ('esi_port_key', YLeaf(YType.uint16, 'esi-port-key')),
                                    ('local_encap_type', YLeaf(YType.uint8, 'local-encap-type')),
                                    ('remote_encap_type', YLeaf(YType.uint8, 'remote-encap-type')),
                                    ('learned_bridge_port_name', YLeaf(YType.str, 'learned-bridge-port-name')),
                                    ('local_seq_id', YLeaf(YType.uint32, 'local-seq-id')),
                                    ('remote_seq_id', YLeaf(YType.uint32, 'remote-seq-id')),
                                    ('local_l3_label', YLeaf(YType.uint32, 'local-l3-label')),
                                    ('router_mac_address', YLeaf(YType.str, 'router-mac-address')),
                                    ('mac_flush_requested', YLeaf(YType.uint16, 'mac-flush-requested')),
                                    ('mac_flush_received', YLeaf(YType.uint16, 'mac-flush-received')),
                                    ('internal_label', YLeaf(YType.uint32, 'internal-label')),
                                    ('resolved', YLeaf(YType.boolean, 'resolved')),
                                    ('local_is_static', YLeaf(YType.boolean, 'local-is-static')),
                                    ('remote_is_static', YLeaf(YType.boolean, 'remote-is-static')),
                                ])
                                self.evi = None
                                self.ethernet_tag = None
                                self.mac_address = None
                                self.ip_address = None
                                self.ethernet_tag_xr = None
                                self.mac_address_xr = None
                                self.ip_address_xr = None
                                self.local_label = None
                                self.num_paths = None
                                self.is_local_mac = None
                                self.is_proxy_entry = None
                                self.is_remote_mac = None
                                self.soo_nexthop = None
                                self.ipnh_address = None
                                self.esi_port_key = None
                                self.local_encap_type = None
                                self.remote_encap_type = None
                                self.learned_bridge_port_name = None
                                self.local_seq_id = None
                                self.remote_seq_id = None
                                self.local_l3_label = None
                                self.router_mac_address = None
                                self.mac_flush_requested = None
                                self.mac_flush_received = None
                                self.internal_label = None
                                self.resolved = None
                                self.local_is_static = None
                                self.remote_is_static = None

                                self.local_ethernet_segment_identifier = YList(self)
                                self.remote_ethernet_segment_identifier = YList(self)
                                self.path_buffer = YList(self)
                                self._segment_path = lambda: "mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac, ['evi', 'ethernet_tag', 'mac_address', 'ip_address', 'ethernet_tag_xr', 'mac_address_xr', 'ip_address_xr', 'local_label', 'num_paths', 'is_local_mac', 'is_proxy_entry', 'is_remote_mac', 'soo_nexthop', 'ipnh_address', 'esi_port_key', 'local_encap_type', 'remote_encap_type', 'learned_bridge_port_name', 'local_seq_id', 'remote_seq_id', 'local_l3_label', 'router_mac_address', 'mac_flush_requested', 'mac_flush_received', 'internal_label', 'resolved', 'local_is_static', 'remote_is_static'], name, value)


                            class LocalEthernetSegmentIdentifier(Entity):
                                """
                                Local Ethernet Segment id
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier, self).__init__()

                                    self.yang_name = "local-ethernet-segment-identifier"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint8, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "local-ethernet-segment-identifier"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier, ['entry'], name, value)


                            class RemoteEthernetSegmentIdentifier(Entity):
                                """
                                Remote Ethernet Segment id
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier, self).__init__()

                                    self.yang_name = "remote-ethernet-segment-identifier"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint8, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "remote-ethernet-segment-identifier"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier, ['entry'], name, value)


                            class PathBuffer(Entity):
                                """
                                Path List Buffer
                                
                                .. attribute:: next_hop
                                
                                	Next\-hop IP address (v6 format)
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: output_label
                                
                                	Output Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: srte_tunnel
                                
                                	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer, self).__init__()

                                    self.yang_name = "path-buffer"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('next_hop', YLeaf(YType.str, 'next-hop')),
                                        ('output_label', YLeaf(YType.uint32, 'output-label')),
                                        ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                                    ])
                                    self.next_hop = None
                                    self.output_label = None
                                    self.srte_tunnel = None
                                    self._segment_path = lambda: "path-buffer"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


            class InternalLabels(Entity):
                """
                EVPN Internal Label Table
                
                .. attribute:: internal_label
                
                	L2VPN EVPN Internal Label
                	**type**\: list of  		 :py:class:`InternalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.InternalLabels.InternalLabel>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Nodes.Node.InternalLabels, self).__init__()

                    self.yang_name = "internal-labels"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("internal-label", ("internal_label", Evpn.Nodes.Node.InternalLabels.InternalLabel))])
                    self._leafs = OrderedDict()

                    self.internal_label = YList(self)
                    self._segment_path = lambda: "internal-labels"

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Nodes.Node.InternalLabels, [], name, value)


                class InternalLabel(Entity):
                    """
                    L2VPN EVPN Internal Label
                    
                    .. attribute:: evi
                    
                    	EVPN id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: esi1
                    
                    	ES id (part 1/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi2
                    
                    	ES id (part 2/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi3
                    
                    	ES id (part 3/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi4
                    
                    	ES id (part 4/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi5
                    
                    	ES id (part 5/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: ethernet_tag
                    
                    	Ethernet Tag ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evi_xr
                    
                    	EVPN id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: esi
                    
                    	Ethernet Segment id
                    	**type**\: str
                    
                    	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                    
                    .. attribute:: tag
                    
                    	Label Tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_label
                    
                    	MPLS Internal Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: encap
                    
                    	Encap type of remote EAD/ES, EAD/EVI and MAC routes
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: mac_num_paths
                    
                    	Number of items in the MAC path buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ead_num_paths
                    
                    	Number of items in the ead path buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: evi_num_paths
                    
                    	Number of items in the evi path buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sum_num_paths
                    
                    	Number of items in the sum path buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sum_num_active_paths
                    
                    	Number of items in the sum path buffer that are Active Paths
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: resolved
                    
                    	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                    	**type**\: bool
                    
                    .. attribute:: ecmp_disable
                    
                    	ECMP Disable Per EVI Resolution
                    	**type**\: bool
                    
                    .. attribute:: redundancy_single_active
                    
                    	Single\-active redundancy configured at remote ES
                    	**type**\: bool
                    
                    .. attribute:: redundancy_single_flow_active
                    
                    	Single\-flow\-active redundancy at remote ES (MST\-AG)
                    	**type**\: bool
                    
                    .. attribute:: mac_path_buffer
                    
                    	MAC Path list buffer
                    	**type**\: list of  		 :py:class:`MacPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.InternalLabels.InternalLabel.MacPathBuffer>`
                    
                    .. attribute:: ead_path_buffer
                    
                    	EAD/ES Path list buffer
                    	**type**\: list of  		 :py:class:`EadPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.InternalLabels.InternalLabel.EadPathBuffer>`
                    
                    .. attribute:: evi_path_buffer
                    
                    	EAD/EVI Path list buffer
                    	**type**\: list of  		 :py:class:`EviPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.InternalLabels.InternalLabel.EviPathBuffer>`
                    
                    .. attribute:: summary_path_buffer
                    
                    	Summary Path list buffer
                    	**type**\: list of  		 :py:class:`SummaryPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.InternalLabels.InternalLabel.SummaryPathBuffer>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Nodes.Node.InternalLabels.InternalLabel, self).__init__()

                        self.yang_name = "internal-label"
                        self.yang_parent_name = "internal-labels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("mac-path-buffer", ("mac_path_buffer", Evpn.Nodes.Node.InternalLabels.InternalLabel.MacPathBuffer)), ("ead-path-buffer", ("ead_path_buffer", Evpn.Nodes.Node.InternalLabels.InternalLabel.EadPathBuffer)), ("evi-path-buffer", ("evi_path_buffer", Evpn.Nodes.Node.InternalLabels.InternalLabel.EviPathBuffer)), ("summary-path-buffer", ("summary_path_buffer", Evpn.Nodes.Node.InternalLabels.InternalLabel.SummaryPathBuffer))])
                        self._leafs = OrderedDict([
                            ('evi', YLeaf(YType.int32, 'evi')),
                            ('esi1', YLeaf(YType.str, 'esi1')),
                            ('esi2', YLeaf(YType.str, 'esi2')),
                            ('esi3', YLeaf(YType.str, 'esi3')),
                            ('esi4', YLeaf(YType.str, 'esi4')),
                            ('esi5', YLeaf(YType.str, 'esi5')),
                            ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                            ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                            ('esi', YLeaf(YType.str, 'esi')),
                            ('tag', YLeaf(YType.uint32, 'tag')),
                            ('internal_label', YLeaf(YType.uint32, 'internal-label')),
                            ('encap', YLeaf(YType.uint8, 'encap')),
                            ('mac_num_paths', YLeaf(YType.uint32, 'mac-num-paths')),
                            ('ead_num_paths', YLeaf(YType.uint32, 'ead-num-paths')),
                            ('evi_num_paths', YLeaf(YType.uint32, 'evi-num-paths')),
                            ('sum_num_paths', YLeaf(YType.uint32, 'sum-num-paths')),
                            ('sum_num_active_paths', YLeaf(YType.uint32, 'sum-num-active-paths')),
                            ('resolved', YLeaf(YType.boolean, 'resolved')),
                            ('ecmp_disable', YLeaf(YType.boolean, 'ecmp-disable')),
                            ('redundancy_single_active', YLeaf(YType.boolean, 'redundancy-single-active')),
                            ('redundancy_single_flow_active', YLeaf(YType.boolean, 'redundancy-single-flow-active')),
                        ])
                        self.evi = None
                        self.esi1 = None
                        self.esi2 = None
                        self.esi3 = None
                        self.esi4 = None
                        self.esi5 = None
                        self.ethernet_tag = None
                        self.evi_xr = None
                        self.esi = None
                        self.tag = None
                        self.internal_label = None
                        self.encap = None
                        self.mac_num_paths = None
                        self.ead_num_paths = None
                        self.evi_num_paths = None
                        self.sum_num_paths = None
                        self.sum_num_active_paths = None
                        self.resolved = None
                        self.ecmp_disable = None
                        self.redundancy_single_active = None
                        self.redundancy_single_flow_active = None

                        self.mac_path_buffer = YList(self)
                        self.ead_path_buffer = YList(self)
                        self.evi_path_buffer = YList(self)
                        self.summary_path_buffer = YList(self)
                        self._segment_path = lambda: "internal-label"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Nodes.Node.InternalLabels.InternalLabel, ['evi', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'ethernet_tag', 'evi_xr', 'esi', 'tag', 'internal_label', 'encap', 'mac_num_paths', 'ead_num_paths', 'evi_num_paths', 'sum_num_paths', 'sum_num_active_paths', 'resolved', 'ecmp_disable', 'redundancy_single_active', 'redundancy_single_flow_active'], name, value)


                    class MacPathBuffer(Entity):
                        """
                        MAC Path list buffer
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srte_tunnel
                        
                        	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.InternalLabels.InternalLabel.MacPathBuffer, self).__init__()

                            self.yang_name = "mac-path-buffer"
                            self.yang_parent_name = "internal-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('output_label', YLeaf(YType.uint32, 'output-label')),
                                ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                            ])
                            self.next_hop = None
                            self.output_label = None
                            self.srte_tunnel = None
                            self._segment_path = lambda: "mac-path-buffer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.InternalLabels.InternalLabel.MacPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                    class EadPathBuffer(Entity):
                        """
                        EAD/ES Path list buffer
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srte_tunnel
                        
                        	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.InternalLabels.InternalLabel.EadPathBuffer, self).__init__()

                            self.yang_name = "ead-path-buffer"
                            self.yang_parent_name = "internal-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('output_label', YLeaf(YType.uint32, 'output-label')),
                                ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                            ])
                            self.next_hop = None
                            self.output_label = None
                            self.srte_tunnel = None
                            self._segment_path = lambda: "ead-path-buffer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.InternalLabels.InternalLabel.EadPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                    class EviPathBuffer(Entity):
                        """
                        EAD/EVI Path list buffer
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srte_tunnel
                        
                        	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.InternalLabels.InternalLabel.EviPathBuffer, self).__init__()

                            self.yang_name = "evi-path-buffer"
                            self.yang_parent_name = "internal-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('output_label', YLeaf(YType.uint32, 'output-label')),
                                ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                            ])
                            self.next_hop = None
                            self.output_label = None
                            self.srte_tunnel = None
                            self._segment_path = lambda: "evi-path-buffer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.InternalLabels.InternalLabel.EviPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                    class SummaryPathBuffer(Entity):
                        """
                        Summary Path list buffer
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: srte_tunnel
                        
                        	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.InternalLabels.InternalLabel.SummaryPathBuffer, self).__init__()

                            self.yang_name = "summary-path-buffer"
                            self.yang_parent_name = "internal-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('output_label', YLeaf(YType.uint32, 'output-label')),
                                ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                            ])
                            self.next_hop = None
                            self.output_label = None
                            self.srte_tunnel = None
                            self._segment_path = lambda: "summary-path-buffer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.InternalLabels.InternalLabel.SummaryPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


            class EthernetSegments(Entity):
                """
                EVPN Ethernet\-Segment Table
                
                .. attribute:: ethernet_segment
                
                	EVPN Ethernet\-Segment Entry
                	**type**\: list of  		 :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Nodes.Node.EthernetSegments, self).__init__()

                    self.yang_name = "ethernet-segments"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ethernet-segment", ("ethernet_segment", Evpn.Nodes.Node.EthernetSegments.EthernetSegment))])
                    self._leafs = OrderedDict()

                    self.ethernet_segment = YList(self)
                    self._segment_path = lambda: "ethernet-segments"

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Nodes.Node.EthernetSegments, [], name, value)


                class EthernetSegment(Entity):
                    """
                    EVPN Ethernet\-Segment Entry
                    
                    .. attribute:: interface_name
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: esi1
                    
                    	ES id (part 1/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi2
                    
                    	ES id (part 2/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi3
                    
                    	ES id (part 3/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi4
                    
                    	ES id (part 4/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi5
                    
                    	ES id (part 5/5)
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                    
                    .. attribute:: esi_type
                    
                    	ESI Type
                    	**type**\:  :py:class:`L2vpnEvpnEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnEsi>`
                    
                    .. attribute:: esi_system_identifier
                    
                    	ESI System Identifier
                    	**type**\: str
                    
                    .. attribute:: esi_port_key
                    
                    	ESI Port Key
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: esi_system_priority
                    
                    	ESI System Priority
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ethernet_segment_name
                    
                    	Ethernet Segment Name
                    	**type**\: str
                    
                    .. attribute:: ethernet_segment_state
                    
                    	State of the ethernet segment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: if_handle
                    
                    	Main port ifhandle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: main_port_role
                    
                    	Main port redundancy group role
                    	**type**\:  :py:class:`L2vpnRgRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnRgRole>`
                    
                    .. attribute:: main_port_mac
                    
                    	Main Port MAC Address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: num_up_p_ws
                    
                    	Number of PWs in Up state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_target
                    
                    	ES\-Import Route Target
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: rt_origin
                    
                    	Origin of operational ES\-Import RT
                    	**type**\:  :py:class:`L2vpnEvpnRtOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnRtOrigin>`
                    
                    .. attribute:: es_bgp_gates
                    
                    	ES BGP Gates
                    	**type**\: str
                    
                    .. attribute:: es_l2fib_gates
                    
                    	ES L2FIB Gates
                    	**type**\: str
                    
                    .. attribute:: mac_flushing_mode_config
                    
                    	Configured MAC Flushing mode
                    	**type**\:  :py:class:`L2vpnEvpnMfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnMfMode>`
                    
                    .. attribute:: load_balance_mode_config
                    
                    	Configured load balancing mode
                    	**type**\:  :py:class:`L2vpnEvpnLbMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnLbMode>`
                    
                    .. attribute:: load_balance_mode_is_default
                    
                    	Load balancing mode is default
                    	**type**\: bool
                    
                    .. attribute:: load_balance_mode_oper
                    
                    	Operational load balancing mode
                    	**type**\:  :py:class:`L2vpnEvpnLbMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnLbMode>`
                    
                    .. attribute:: force_single_home
                    
                    	Ethernet\-Segment forced to single home
                    	**type**\: bool
                    
                    .. attribute:: source_mac_oper
                    
                    	Operational Source MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: source_mac_origin
                    
                    	Origin of operational source MAC address
                    	**type**\:  :py:class:`L2vpnEvpnSmacSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnSmacSrc>`
                    
                    .. attribute:: peering_timer
                    
                    	Configured timer for triggering DF election (seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: peering_timer_left
                    
                    	Milliseconds left on DF election timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: recovery_timer
                    
                    	Configured timer for (STP) recovery (seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: recovery_timer_left
                    
                    	Milliseconds left on (STP) recovery timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: carving_timer
                    
                    	Configured timer for delaying DF election (seconds)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: carving_timer_left
                    
                    	Milliseconds left on carving timer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: millisecond
                    
                    .. attribute:: service_carving_mode
                    
                    	Service carving mode
                    	**type**\:  :py:class:`L2vpnEvpnScMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnScMode>`
                    
                    .. attribute:: primary_services_input
                    
                    	Input string of Primary services ESI/I\-SIDs
                    	**type**\: str
                    
                    .. attribute:: secondary_services_input
                    
                    	Input string of Secondary services ESI/I\-SIDs
                    	**type**\: str
                    
                    .. attribute:: forwarder_ports
                    
                    	Count of Forwarders (AC, AC PW, VFI PW)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: permanent_forwarder_ports
                    
                    	Count of Forwarders with permanent service
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: elected_forwarder_ports
                    
                    	Count of Forwarders with elected service
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_elected_forwarder_ports
                    
                    	Count of Forwarders with not elected service
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: not_config_forwarder_ports
                    
                    	Count of forwarders with missing config detected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mp_protected
                    
                    	MP is protected and not under EVPN control
                    	**type**\: bool
                    
                    .. attribute:: nve_anycast_vtep
                    
                    	Anycast VTEP mode on NVE main\-interface
                    	**type**\: bool
                    
                    .. attribute:: nve_ingress_replication
                    
                    	Ingress\-Replication is configured on NVE main\-interface
                    	**type**\: bool
                    
                    .. attribute:: local_split_horizon_group_label_valid
                    
                    	Local split horizon group label is valid
                    	**type**\: bool
                    
                    .. attribute:: local_split_horizon_group_label
                    
                    	Local split horizon group label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ethernet_segment_identifier
                    
                    	Ethernet Segment id
                    	**type**\: list of  		 :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier>`
                    
                    .. attribute:: primary_service
                    
                    	List of Primary services ESI/I\-SIDs
                    	**type**\: list of  		 :py:class:`PrimaryService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.PrimaryService>`
                    
                    .. attribute:: secondary_service
                    
                    	List of Secondary services ESI/I\-SIDs
                    	**type**\: list of  		 :py:class:`SecondaryService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.SecondaryService>`
                    
                    .. attribute:: service_carving_i_sidelected_result
                    
                    	Elected ISID service carving results
                    	**type**\: list of  		 :py:class:`ServiceCarvingISidelectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult>`
                    
                    .. attribute:: service_carving_isid_not_elected_result
                    
                    	Not elected ISID service carving results
                    	**type**\: list of  		 :py:class:`ServiceCarvingIsidNotElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult>`
                    
                    .. attribute:: service_carving_evi_elected_result
                    
                    	Elected EVI service carving results
                    	**type**\: list of  		 :py:class:`ServiceCarvingEviElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult>`
                    
                    .. attribute:: service_carving_evi_not_elected_result
                    
                    	Not elected EVI service carving results
                    	**type**\: list of  		 :py:class:`ServiceCarvingEviNotElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult>`
                    
                    .. attribute:: next_hop
                    
                    	List of nexthop IPv6 addresses
                    	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop>`
                    
                    .. attribute:: service_carving_vpws_permanent_result
                    
                    	Permanent EVPN VPWS service carving results
                    	**type**\: list of  		 :py:class:`ServiceCarvingVpwsPermanentResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult>`
                    
                    .. attribute:: remote_split_horizon_group_label
                    
                    	Remote split horizon group labels
                    	**type**\: list of  		 :py:class:`RemoteSplitHorizonGroupLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment, self).__init__()

                        self.yang_name = "ethernet-segment"
                        self.yang_parent_name = "ethernet-segments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ethernet-segment-identifier", ("ethernet_segment_identifier", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier)), ("primary-service", ("primary_service", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.PrimaryService)), ("secondary-service", ("secondary_service", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.SecondaryService)), ("service-carving-i-sidelected-result", ("service_carving_i_sidelected_result", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult)), ("service-carving-isid-not-elected-result", ("service_carving_isid_not_elected_result", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult)), ("service-carving-evi-elected-result", ("service_carving_evi_elected_result", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult)), ("service-carving-evi-not-elected-result", ("service_carving_evi_not_elected_result", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult)), ("next-hop", ("next_hop", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop)), ("service-carving-vpws-permanent-result", ("service_carving_vpws_permanent_result", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult)), ("remote-split-horizon-group-label", ("remote_split_horizon_group_label", Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel))])
                        self._leafs = OrderedDict([
                            ('interface_name', YLeaf(YType.str, 'interface-name')),
                            ('esi1', YLeaf(YType.str, 'esi1')),
                            ('esi2', YLeaf(YType.str, 'esi2')),
                            ('esi3', YLeaf(YType.str, 'esi3')),
                            ('esi4', YLeaf(YType.str, 'esi4')),
                            ('esi5', YLeaf(YType.str, 'esi5')),
                            ('esi_type', YLeaf(YType.enumeration, 'esi-type')),
                            ('esi_system_identifier', YLeaf(YType.str, 'esi-system-identifier')),
                            ('esi_port_key', YLeaf(YType.uint32, 'esi-port-key')),
                            ('esi_system_priority', YLeaf(YType.uint32, 'esi-system-priority')),
                            ('ethernet_segment_name', YLeaf(YType.str, 'ethernet-segment-name')),
                            ('ethernet_segment_state', YLeaf(YType.uint32, 'ethernet-segment-state')),
                            ('if_handle', YLeaf(YType.str, 'if-handle')),
                            ('main_port_role', YLeaf(YType.enumeration, 'main-port-role')),
                            ('main_port_mac', YLeaf(YType.str, 'main-port-mac')),
                            ('num_up_p_ws', YLeaf(YType.uint32, 'num-up-p-ws')),
                            ('route_target', YLeaf(YType.str, 'route-target')),
                            ('rt_origin', YLeaf(YType.enumeration, 'rt-origin')),
                            ('es_bgp_gates', YLeaf(YType.str, 'es-bgp-gates')),
                            ('es_l2fib_gates', YLeaf(YType.str, 'es-l2fib-gates')),
                            ('mac_flushing_mode_config', YLeaf(YType.enumeration, 'mac-flushing-mode-config')),
                            ('load_balance_mode_config', YLeaf(YType.enumeration, 'load-balance-mode-config')),
                            ('load_balance_mode_is_default', YLeaf(YType.boolean, 'load-balance-mode-is-default')),
                            ('load_balance_mode_oper', YLeaf(YType.enumeration, 'load-balance-mode-oper')),
                            ('force_single_home', YLeaf(YType.boolean, 'force-single-home')),
                            ('source_mac_oper', YLeaf(YType.str, 'source-mac-oper')),
                            ('source_mac_origin', YLeaf(YType.enumeration, 'source-mac-origin')),
                            ('peering_timer', YLeaf(YType.uint32, 'peering-timer')),
                            ('peering_timer_left', YLeaf(YType.uint32, 'peering-timer-left')),
                            ('recovery_timer', YLeaf(YType.uint32, 'recovery-timer')),
                            ('recovery_timer_left', YLeaf(YType.uint32, 'recovery-timer-left')),
                            ('carving_timer', YLeaf(YType.uint32, 'carving-timer')),
                            ('carving_timer_left', YLeaf(YType.uint32, 'carving-timer-left')),
                            ('service_carving_mode', YLeaf(YType.enumeration, 'service-carving-mode')),
                            ('primary_services_input', YLeaf(YType.str, 'primary-services-input')),
                            ('secondary_services_input', YLeaf(YType.str, 'secondary-services-input')),
                            ('forwarder_ports', YLeaf(YType.uint32, 'forwarder-ports')),
                            ('permanent_forwarder_ports', YLeaf(YType.uint32, 'permanent-forwarder-ports')),
                            ('elected_forwarder_ports', YLeaf(YType.uint32, 'elected-forwarder-ports')),
                            ('not_elected_forwarder_ports', YLeaf(YType.uint32, 'not-elected-forwarder-ports')),
                            ('not_config_forwarder_ports', YLeaf(YType.uint32, 'not-config-forwarder-ports')),
                            ('mp_protected', YLeaf(YType.boolean, 'mp-protected')),
                            ('nve_anycast_vtep', YLeaf(YType.boolean, 'nve-anycast-vtep')),
                            ('nve_ingress_replication', YLeaf(YType.boolean, 'nve-ingress-replication')),
                            ('local_split_horizon_group_label_valid', YLeaf(YType.boolean, 'local-split-horizon-group-label-valid')),
                            ('local_split_horizon_group_label', YLeaf(YType.uint32, 'local-split-horizon-group-label')),
                        ])
                        self.interface_name = None
                        self.esi1 = None
                        self.esi2 = None
                        self.esi3 = None
                        self.esi4 = None
                        self.esi5 = None
                        self.esi_type = None
                        self.esi_system_identifier = None
                        self.esi_port_key = None
                        self.esi_system_priority = None
                        self.ethernet_segment_name = None
                        self.ethernet_segment_state = None
                        self.if_handle = None
                        self.main_port_role = None
                        self.main_port_mac = None
                        self.num_up_p_ws = None
                        self.route_target = None
                        self.rt_origin = None
                        self.es_bgp_gates = None
                        self.es_l2fib_gates = None
                        self.mac_flushing_mode_config = None
                        self.load_balance_mode_config = None
                        self.load_balance_mode_is_default = None
                        self.load_balance_mode_oper = None
                        self.force_single_home = None
                        self.source_mac_oper = None
                        self.source_mac_origin = None
                        self.peering_timer = None
                        self.peering_timer_left = None
                        self.recovery_timer = None
                        self.recovery_timer_left = None
                        self.carving_timer = None
                        self.carving_timer_left = None
                        self.service_carving_mode = None
                        self.primary_services_input = None
                        self.secondary_services_input = None
                        self.forwarder_ports = None
                        self.permanent_forwarder_ports = None
                        self.elected_forwarder_ports = None
                        self.not_elected_forwarder_ports = None
                        self.not_config_forwarder_ports = None
                        self.mp_protected = None
                        self.nve_anycast_vtep = None
                        self.nve_ingress_replication = None
                        self.local_split_horizon_group_label_valid = None
                        self.local_split_horizon_group_label = None

                        self.ethernet_segment_identifier = YList(self)
                        self.primary_service = YList(self)
                        self.secondary_service = YList(self)
                        self.service_carving_i_sidelected_result = YList(self)
                        self.service_carving_isid_not_elected_result = YList(self)
                        self.service_carving_evi_elected_result = YList(self)
                        self.service_carving_evi_not_elected_result = YList(self)
                        self.next_hop = YList(self)
                        self.service_carving_vpws_permanent_result = YList(self)
                        self.remote_split_horizon_group_label = YList(self)
                        self._segment_path = lambda: "ethernet-segment"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment, ['interface_name', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'esi_type', 'esi_system_identifier', 'esi_port_key', 'esi_system_priority', 'ethernet_segment_name', 'ethernet_segment_state', 'if_handle', 'main_port_role', 'main_port_mac', 'num_up_p_ws', 'route_target', 'rt_origin', 'es_bgp_gates', 'es_l2fib_gates', 'mac_flushing_mode_config', 'load_balance_mode_config', 'load_balance_mode_is_default', 'load_balance_mode_oper', 'force_single_home', 'source_mac_oper', 'source_mac_origin', 'peering_timer', 'peering_timer_left', 'recovery_timer', 'recovery_timer_left', 'carving_timer', 'carving_timer_left', 'service_carving_mode', 'primary_services_input', 'secondary_services_input', 'forwarder_ports', 'permanent_forwarder_ports', 'elected_forwarder_ports', 'not_elected_forwarder_ports', 'not_config_forwarder_ports', 'mp_protected', 'nve_anycast_vtep', 'nve_ingress_replication', 'local_split_horizon_group_label_valid', 'local_split_horizon_group_label'], name, value)


                    class EthernetSegmentIdentifier(Entity):
                        """
                        Ethernet Segment id
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier, self).__init__()

                            self.yang_name = "ethernet-segment-identifier"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint8, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "ethernet-segment-identifier"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier, ['entry'], name, value)


                    class PrimaryService(Entity):
                        """
                        List of Primary services ESI/I\-SIDs
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.PrimaryService, self).__init__()

                            self.yang_name = "primary-service"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "primary-service"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.PrimaryService, ['entry'], name, value)


                    class SecondaryService(Entity):
                        """
                        List of Secondary services ESI/I\-SIDs
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.SecondaryService, self).__init__()

                            self.yang_name = "secondary-service"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "secondary-service"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.SecondaryService, ['entry'], name, value)


                    class ServiceCarvingISidelectedResult(Entity):
                        """
                        Elected ISID service carving results
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult, self).__init__()

                            self.yang_name = "service-carving-i-sidelected-result"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "service-carving-i-sidelected-result"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult, ['entry'], name, value)


                    class ServiceCarvingIsidNotElectedResult(Entity):
                        """
                        Not elected ISID service carving results
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult, self).__init__()

                            self.yang_name = "service-carving-isid-not-elected-result"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "service-carving-isid-not-elected-result"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult, ['entry'], name, value)


                    class ServiceCarvingEviElectedResult(Entity):
                        """
                        Elected EVI service carving results
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult, self).__init__()

                            self.yang_name = "service-carving-evi-elected-result"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "service-carving-evi-elected-result"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult, ['entry'], name, value)


                    class ServiceCarvingEviNotElectedResult(Entity):
                        """
                        Not elected EVI service carving results
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult, self).__init__()

                            self.yang_name = "service-carving-evi-not-elected-result"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "service-carving-evi-not-elected-result"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult, ['entry'], name, value)


                    class NextHop(Entity):
                        """
                        List of nexthop IPv6 addresses
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ])
                            self.next_hop = None
                            self._segment_path = lambda: "next-hop"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop, ['next_hop'], name, value)


                    class ServiceCarvingVpwsPermanentResult(Entity):
                        """
                        Permanent EVPN VPWS service carving results
                        
                        .. attribute:: vpn_id
                        
                        	VPN ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Service Type
                        	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult, self).__init__()

                            self.yang_name = "service-carving-vpws-permanent-result"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vpn_id', YLeaf(YType.uint32, 'vpn-id')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('ethernet_tag', YLeaf(YType.uint32, 'ethernet-tag')),
                            ])
                            self.vpn_id = None
                            self.type = None
                            self.ethernet_tag = None
                            self._segment_path = lambda: "service-carving-vpws-permanent-result"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult, ['vpn_id', 'type', 'ethernet_tag'], name, value)


                    class RemoteSplitHorizonGroupLabel(Entity):
                        """
                        Remote split horizon group labels
                        
                        .. attribute:: next_hop
                        
                        	Next\-hop IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: label
                        
                        	Split horizon label associated with next\-hop address
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel, self).__init__()

                            self.yang_name = "remote-split-horizon-group-label"
                            self.yang_parent_name = "ethernet-segment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('label', YLeaf(YType.uint32, 'label')),
                            ])
                            self.next_hop = None
                            self.label = None
                            self._segment_path = lambda: "remote-split-horizon-group-label"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel, ['next_hop', 'label'], name, value)


            class AcIds(Entity):
                """
                EVPN AC ID table
                
                .. attribute:: ac_id
                
                	EVPN AC ID table
                	**type**\: list of  		 :py:class:`AcId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Nodes.Node.AcIds.AcId>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Nodes.Node.AcIds, self).__init__()

                    self.yang_name = "ac-ids"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ac-id", ("ac_id", Evpn.Nodes.Node.AcIds.AcId))])
                    self._leafs = OrderedDict()

                    self.ac_id = YList(self)
                    self._segment_path = lambda: "ac-ids"

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Nodes.Node.AcIds, [], name, value)


                class AcId(Entity):
                    """
                    EVPN AC ID table
                    
                    .. attribute:: evi
                    
                    	EVPN id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ac_id
                    
                    	AC ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: neighbor
                    
                    	Neighbor IP
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Nodes.Node.AcIds.AcId, self).__init__()

                        self.yang_name = "ac-id"
                        self.yang_parent_name = "ac-ids"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evi', YLeaf(YType.int32, 'evi')),
                            ('ac_id', YLeaf(YType.int32, 'ac-id')),
                            ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                            ('neighbor', YLeaf(YType.str, 'neighbor')),
                        ])
                        self.evi = None
                        self.ac_id = None
                        self.evi_xr = None
                        self.neighbor = None
                        self._segment_path = lambda: "ac-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Nodes.Node.AcIds.AcId, ['evi', 'ac_id', 'evi_xr', 'neighbor'], name, value)


    class Active(Entity):
        """
        Active EVPN operational data
        
        .. attribute:: evis
        
        	L2VPN EVPN EVI Table
        	**type**\:  :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.Evis>`
        
        .. attribute:: summary
        
        	L2VPN EVPN Summary
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.Summary>`
        
        .. attribute:: evi_detail
        
        	L2VPN EVI Detail Table
        	**type**\:  :py:class:`EviDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail>`
        
        .. attribute:: internal_labels
        
        	EVPN Internal Label Table
        	**type**\:  :py:class:`InternalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.InternalLabels>`
        
        .. attribute:: ethernet_segments
        
        	EVPN Ethernet\-Segment Table
        	**type**\:  :py:class:`EthernetSegments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments>`
        
        .. attribute:: ac_ids
        
        	EVPN AC ID table
        	**type**\:  :py:class:`AcIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.AcIds>`
        
        

        """

        _prefix = 'evpn-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Evpn.Active, self).__init__()

            self.yang_name = "active"
            self.yang_parent_name = "evpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("evis", ("evis", Evpn.Active.Evis)), ("summary", ("summary", Evpn.Active.Summary)), ("evi-detail", ("evi_detail", Evpn.Active.EviDetail)), ("internal-labels", ("internal_labels", Evpn.Active.InternalLabels)), ("ethernet-segments", ("ethernet_segments", Evpn.Active.EthernetSegments)), ("ac-ids", ("ac_ids", Evpn.Active.AcIds))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.evis = Evpn.Active.Evis()
            self.evis.parent = self
            self._children_name_map["evis"] = "evis"
            self._children_yang_names.add("evis")

            self.summary = Evpn.Active.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._children_yang_names.add("summary")

            self.evi_detail = Evpn.Active.EviDetail()
            self.evi_detail.parent = self
            self._children_name_map["evi_detail"] = "evi-detail"
            self._children_yang_names.add("evi-detail")

            self.internal_labels = Evpn.Active.InternalLabels()
            self.internal_labels.parent = self
            self._children_name_map["internal_labels"] = "internal-labels"
            self._children_yang_names.add("internal-labels")

            self.ethernet_segments = Evpn.Active.EthernetSegments()
            self.ethernet_segments.parent = self
            self._children_name_map["ethernet_segments"] = "ethernet-segments"
            self._children_yang_names.add("ethernet-segments")

            self.ac_ids = Evpn.Active.AcIds()
            self.ac_ids.parent = self
            self._children_name_map["ac_ids"] = "ac-ids"
            self._children_yang_names.add("ac-ids")
            self._segment_path = lambda: "active"
            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/%s" % self._segment_path()


        class Evis(Entity):
            """
            L2VPN EVPN EVI Table
            
            .. attribute:: evi
            
            	L2VPN EVPN EVI Entry
            	**type**\: list of  		 :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.Evis.Evi>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Active.Evis, self).__init__()

                self.yang_name = "evis"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evi", ("evi", Evpn.Active.Evis.Evi))])
                self._leafs = OrderedDict()

                self.evi = YList(self)
                self._segment_path = lambda: "evis"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Active.Evis, [], name, value)


            class Evi(Entity):
                """
                L2VPN EVPN EVI Entry
                
                .. attribute:: evi  (key)
                
                	EVPN id
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bd_name
                
                	Bridge domain name
                	**type**\: str
                
                .. attribute:: type
                
                	Service Type
                	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Active.Evis.Evi, self).__init__()

                    self.yang_name = "evi"
                    self.yang_parent_name = "evis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['evi']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('evi', YLeaf(YType.int32, 'evi')),
                        ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                        ('bd_name', YLeaf(YType.str, 'bd-name')),
                        ('type', YLeaf(YType.enumeration, 'type')),
                    ])
                    self.evi = None
                    self.evi_xr = None
                    self.bd_name = None
                    self.type = None
                    self._segment_path = lambda: "evi" + "[evi='" + str(self.evi) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Active.Evis.Evi, ['evi', 'evi_xr', 'bd_name', 'type'], name, value)


        class Summary(Entity):
            """
            L2VPN EVPN Summary
            
            .. attribute:: router_id
            
            	EVPN Router ID
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: as_
            
            	BGP AS number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ev_is
            
            	Number of EVI DB Entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_mac_routes
            
            	Number of Local MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv4_mac_routes
            
            	Number of Local IPv4 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv6_mac_routes
            
            	Number of Local IPv6 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_global_mac_routes
            
            	Number of ES\:Global MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mac_routes
            
            	Number of Remote MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_soo_mac_routes
            
            	Number of Remote Soo MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv4_mac_routes
            
            	Number of Remote IPv4 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv6_mac_routes
            
            	Number of Remote IPv6 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_imcast_routes
            
            	Number of Local IMCAST Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_imcast_routes
            
            	Number of Remote IMCAST Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: labels
            
            	Number of Internal Labels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_entries
            
            	Number of ES Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: neighbor_entries
            
            	Number of neighbor Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ead_routes
            
            	Number of Local EAD Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ead_routes
            
            	Number of Remote EAD Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: global_source_mac
            
            	Global Source MAC Address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: peering_time
            
            	EVPN ES Peering Time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: recovery_time
            
            	EVPN ES Recovery Time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: carving_time
            
            	EVPN ES Carving Time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: mac_secure_move_count
            
            	Number of moves within the move interval before locking the MAC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_secure_move_interval
            
            	Interval to watch for subsequent mac moves before locking the MAC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_secure_freeze_time
            
            	Length of time to lock the mac after a MAC security violation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_secure_retry_count
            
            	Number of times to retry after a MAC un\-freezes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cost_out
            
            	EVPN Node Cost\-out
            	**type**\: bool
            
            .. attribute:: startup_cost_in_time
            
            	EVPN Node startup cost\-in Time (minutes)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: minute
            
            .. attribute:: l2rib_throttle
            
            	Send to L2RIB Throttled
            	**type**\: bool
            
            .. attribute:: logging_df_election_enabled
            
            	Logging EVPN Designated Forwarder changes enabled
            	**type**\: bool
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Active.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('router_id', YLeaf(YType.str, 'router-id')),
                    ('as_', YLeaf(YType.uint32, 'as')),
                    ('ev_is', YLeaf(YType.uint32, 'ev-is')),
                    ('local_mac_routes', YLeaf(YType.uint32, 'local-mac-routes')),
                    ('local_ipv4_mac_routes', YLeaf(YType.uint32, 'local-ipv4-mac-routes')),
                    ('local_ipv6_mac_routes', YLeaf(YType.uint32, 'local-ipv6-mac-routes')),
                    ('es_global_mac_routes', YLeaf(YType.uint32, 'es-global-mac-routes')),
                    ('remote_mac_routes', YLeaf(YType.uint32, 'remote-mac-routes')),
                    ('remote_soo_mac_routes', YLeaf(YType.uint32, 'remote-soo-mac-routes')),
                    ('remote_ipv4_mac_routes', YLeaf(YType.uint32, 'remote-ipv4-mac-routes')),
                    ('remote_ipv6_mac_routes', YLeaf(YType.uint32, 'remote-ipv6-mac-routes')),
                    ('local_imcast_routes', YLeaf(YType.uint32, 'local-imcast-routes')),
                    ('remote_imcast_routes', YLeaf(YType.uint32, 'remote-imcast-routes')),
                    ('labels', YLeaf(YType.uint32, 'labels')),
                    ('es_entries', YLeaf(YType.uint32, 'es-entries')),
                    ('neighbor_entries', YLeaf(YType.uint32, 'neighbor-entries')),
                    ('local_ead_routes', YLeaf(YType.uint32, 'local-ead-routes')),
                    ('remote_ead_routes', YLeaf(YType.uint32, 'remote-ead-routes')),
                    ('global_source_mac', YLeaf(YType.str, 'global-source-mac')),
                    ('peering_time', YLeaf(YType.uint32, 'peering-time')),
                    ('recovery_time', YLeaf(YType.uint32, 'recovery-time')),
                    ('carving_time', YLeaf(YType.uint32, 'carving-time')),
                    ('mac_secure_move_count', YLeaf(YType.uint32, 'mac-secure-move-count')),
                    ('mac_secure_move_interval', YLeaf(YType.uint32, 'mac-secure-move-interval')),
                    ('mac_secure_freeze_time', YLeaf(YType.uint32, 'mac-secure-freeze-time')),
                    ('mac_secure_retry_count', YLeaf(YType.uint32, 'mac-secure-retry-count')),
                    ('cost_out', YLeaf(YType.boolean, 'cost-out')),
                    ('startup_cost_in_time', YLeaf(YType.uint32, 'startup-cost-in-time')),
                    ('l2rib_throttle', YLeaf(YType.boolean, 'l2rib-throttle')),
                    ('logging_df_election_enabled', YLeaf(YType.boolean, 'logging-df-election-enabled')),
                ])
                self.router_id = None
                self.as_ = None
                self.ev_is = None
                self.local_mac_routes = None
                self.local_ipv4_mac_routes = None
                self.local_ipv6_mac_routes = None
                self.es_global_mac_routes = None
                self.remote_mac_routes = None
                self.remote_soo_mac_routes = None
                self.remote_ipv4_mac_routes = None
                self.remote_ipv6_mac_routes = None
                self.local_imcast_routes = None
                self.remote_imcast_routes = None
                self.labels = None
                self.es_entries = None
                self.neighbor_entries = None
                self.local_ead_routes = None
                self.remote_ead_routes = None
                self.global_source_mac = None
                self.peering_time = None
                self.recovery_time = None
                self.carving_time = None
                self.mac_secure_move_count = None
                self.mac_secure_move_interval = None
                self.mac_secure_freeze_time = None
                self.mac_secure_retry_count = None
                self.cost_out = None
                self.startup_cost_in_time = None
                self.l2rib_throttle = None
                self.logging_df_election_enabled = None
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Active.Summary, ['router_id', 'as_', 'ev_is', 'local_mac_routes', 'local_ipv4_mac_routes', 'local_ipv6_mac_routes', 'es_global_mac_routes', 'remote_mac_routes', 'remote_soo_mac_routes', 'remote_ipv4_mac_routes', 'remote_ipv6_mac_routes', 'local_imcast_routes', 'remote_imcast_routes', 'labels', 'es_entries', 'neighbor_entries', 'local_ead_routes', 'remote_ead_routes', 'global_source_mac', 'peering_time', 'recovery_time', 'carving_time', 'mac_secure_move_count', 'mac_secure_move_interval', 'mac_secure_freeze_time', 'mac_secure_retry_count', 'cost_out', 'startup_cost_in_time', 'l2rib_throttle', 'logging_df_election_enabled'], name, value)


        class EviDetail(Entity):
            """
            L2VPN EVI Detail Table
            
            .. attribute:: elements
            
            	EVI BGP RT Detail Info Elements
            	**type**\:  :py:class:`Elements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements>`
            
            .. attribute:: evi_children
            
            	Container for all EVI detail info
            	**type**\:  :py:class:`EviChildren <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Active.EviDetail, self).__init__()

                self.yang_name = "evi-detail"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("elements", ("elements", Evpn.Active.EviDetail.Elements)), ("evi-children", ("evi_children", Evpn.Active.EviDetail.EviChildren))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.elements = Evpn.Active.EviDetail.Elements()
                self.elements.parent = self
                self._children_name_map["elements"] = "elements"
                self._children_yang_names.add("elements")

                self.evi_children = Evpn.Active.EviDetail.EviChildren()
                self.evi_children.parent = self
                self._children_name_map["evi_children"] = "evi-children"
                self._children_yang_names.add("evi-children")
                self._segment_path = lambda: "evi-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/%s" % self._segment_path()


            class Elements(Entity):
                """
                EVI BGP RT Detail Info Elements
                
                .. attribute:: element
                
                	EVI BGP RT Detail Info
                	**type**\: list of  		 :py:class:`Element <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Active.EviDetail.Elements, self).__init__()

                    self.yang_name = "elements"
                    self.yang_parent_name = "evi-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("element", ("element", Evpn.Active.EviDetail.Elements.Element))])
                    self._leafs = OrderedDict()

                    self.element = YList(self)
                    self._segment_path = lambda: "elements"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Active.EviDetail.Elements, [], name, value)


                class Element(Entity):
                    """
                    EVI BGP RT Detail Info
                    
                    .. attribute:: evi  (key)
                    
                    	EVPN id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: flow_label
                    
                    	Flow Label Information
                    	**type**\:  :py:class:`FlowLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.FlowLabel>`
                    
                    .. attribute:: rd_auto
                    
                    	Automatic Route Distingtuisher
                    	**type**\:  :py:class:`RdAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto>`
                    
                    .. attribute:: rd_configured
                    
                    	Configured Route Distinguisher
                    	**type**\:  :py:class:`RdConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured>`
                    
                    .. attribute:: rt_auto
                    
                    	Automatic Route Target
                    	**type**\:  :py:class:`RtAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto>`
                    
                    .. attribute:: rt_auto_stitching
                    
                    	Automatic Route Target Stitching
                    	**type**\:  :py:class:`RtAutoStitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching>`
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: description
                    
                    	EVI description
                    	**type**\: str
                    
                    .. attribute:: bd_name
                    
                    	Bridge domain name
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                    
                    .. attribute:: unicast_label
                    
                    	Unicast Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_label
                    
                    	Multicast Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cw_disable
                    
                    	Control\-Word Disable
                    	**type**\: bool
                    
                    .. attribute:: table_policy_name
                    
                    	Table\-policy Name
                    	**type**\: str
                    
                    .. attribute:: forward_class
                    
                    	Forward Class attribute
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rt_import_block_set
                    
                    	Is Import RT None set
                    	**type**\: bool
                    
                    .. attribute:: rt_export_block_set
                    
                    	Is Export RT None set
                    	**type**\: bool
                    
                    .. attribute:: advertise_mac
                    
                    	Advertise MAC\-only routes on this EVI
                    	**type**\: bool
                    
                    .. attribute:: advertise_bvi_mac
                    
                    	Advertise BVI MACs routes on this EVI
                    	**type**\: bool
                    
                    .. attribute:: aliasing_disabled
                    
                    	Route Aliasing is disabled
                    	**type**\: bool
                    
                    .. attribute:: unknown_unicast_flooding_disabled
                    
                    	Unknown\-unicast flooding is disabled
                    	**type**\: bool
                    
                    .. attribute:: reoriginate_disabled
                    
                    	Route Re\-origination is disabled
                    	**type**\: bool
                    
                    .. attribute:: stitching
                    
                    	EVPN Instance is Regular/Stitching side
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: encapsulation
                    
                    	EVPN Instance encapsulation
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EviDetail.Elements.Element, self).__init__()

                        self.yang_name = "element"
                        self.yang_parent_name = "elements"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['evi']
                        self._child_container_classes = OrderedDict([("flow-label", ("flow_label", Evpn.Active.EviDetail.Elements.Element.FlowLabel)), ("rd-auto", ("rd_auto", Evpn.Active.EviDetail.Elements.Element.RdAuto)), ("rd-configured", ("rd_configured", Evpn.Active.EviDetail.Elements.Element.RdConfigured)), ("rt-auto", ("rt_auto", Evpn.Active.EviDetail.Elements.Element.RtAuto)), ("rt-auto-stitching", ("rt_auto_stitching", Evpn.Active.EviDetail.Elements.Element.RtAutoStitching))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evi', YLeaf(YType.int32, 'evi')),
                            ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                            ('description', YLeaf(YType.str, 'description')),
                            ('bd_name', YLeaf(YType.str, 'bd-name')),
                            ('type', YLeaf(YType.enumeration, 'type')),
                            ('unicast_label', YLeaf(YType.uint32, 'unicast-label')),
                            ('multicast_label', YLeaf(YType.uint32, 'multicast-label')),
                            ('cw_disable', YLeaf(YType.boolean, 'cw-disable')),
                            ('table_policy_name', YLeaf(YType.str, 'table-policy-name')),
                            ('forward_class', YLeaf(YType.uint8, 'forward-class')),
                            ('rt_import_block_set', YLeaf(YType.boolean, 'rt-import-block-set')),
                            ('rt_export_block_set', YLeaf(YType.boolean, 'rt-export-block-set')),
                            ('advertise_mac', YLeaf(YType.boolean, 'advertise-mac')),
                            ('advertise_bvi_mac', YLeaf(YType.boolean, 'advertise-bvi-mac')),
                            ('aliasing_disabled', YLeaf(YType.boolean, 'aliasing-disabled')),
                            ('unknown_unicast_flooding_disabled', YLeaf(YType.boolean, 'unknown-unicast-flooding-disabled')),
                            ('reoriginate_disabled', YLeaf(YType.boolean, 'reoriginate-disabled')),
                            ('stitching', YLeaf(YType.uint8, 'stitching')),
                            ('encapsulation', YLeaf(YType.uint8, 'encapsulation')),
                        ])
                        self.evi = None
                        self.evi_xr = None
                        self.description = None
                        self.bd_name = None
                        self.type = None
                        self.unicast_label = None
                        self.multicast_label = None
                        self.cw_disable = None
                        self.table_policy_name = None
                        self.forward_class = None
                        self.rt_import_block_set = None
                        self.rt_export_block_set = None
                        self.advertise_mac = None
                        self.advertise_bvi_mac = None
                        self.aliasing_disabled = None
                        self.unknown_unicast_flooding_disabled = None
                        self.reoriginate_disabled = None
                        self.stitching = None
                        self.encapsulation = None

                        self.flow_label = Evpn.Active.EviDetail.Elements.Element.FlowLabel()
                        self.flow_label.parent = self
                        self._children_name_map["flow_label"] = "flow-label"
                        self._children_yang_names.add("flow-label")

                        self.rd_auto = Evpn.Active.EviDetail.Elements.Element.RdAuto()
                        self.rd_auto.parent = self
                        self._children_name_map["rd_auto"] = "rd-auto"
                        self._children_yang_names.add("rd-auto")

                        self.rd_configured = Evpn.Active.EviDetail.Elements.Element.RdConfigured()
                        self.rd_configured.parent = self
                        self._children_name_map["rd_configured"] = "rd-configured"
                        self._children_yang_names.add("rd-configured")

                        self.rt_auto = Evpn.Active.EviDetail.Elements.Element.RtAuto()
                        self.rt_auto.parent = self
                        self._children_name_map["rt_auto"] = "rt-auto"
                        self._children_yang_names.add("rt-auto")

                        self.rt_auto_stitching = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching()
                        self.rt_auto_stitching.parent = self
                        self._children_name_map["rt_auto_stitching"] = "rt-auto-stitching"
                        self._children_yang_names.add("rt-auto-stitching")
                        self._segment_path = lambda: "element" + "[evi='" + str(self.evi) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/elements/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EviDetail.Elements.Element, ['evi', 'evi_xr', 'description', 'bd_name', 'type', 'unicast_label', 'multicast_label', 'cw_disable', 'table_policy_name', 'forward_class', 'rt_import_block_set', 'rt_export_block_set', 'advertise_mac', 'advertise_bvi_mac', 'aliasing_disabled', 'unknown_unicast_flooding_disabled', 'reoriginate_disabled', 'stitching', 'encapsulation'], name, value)


                    class FlowLabel(Entity):
                        """
                        Flow Label Information
                        
                        .. attribute:: static_flow_label
                        
                        	Static flow label
                        	**type**\: bool
                        
                        .. attribute:: global_flow_label
                        
                        	Globally configured flow label
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.Elements.Element.FlowLabel, self).__init__()

                            self.yang_name = "flow-label"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('static_flow_label', YLeaf(YType.boolean, 'static-flow-label')),
                                ('global_flow_label', YLeaf(YType.boolean, 'global-flow-label')),
                            ])
                            self.static_flow_label = None
                            self.global_flow_label = None
                            self._segment_path = lambda: "flow-label"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.FlowLabel, ['static_flow_label', 'global_flow_label'], name, value)


                    class RdAuto(Entity):
                        """
                        Automatic Route Distingtuisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:  :py:class:`L2vpnAdRd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRd>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.Elements.Element.RdAuto, self).__init__()

                            self.yang_name = "rd-auto"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("auto", ("auto", Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto)), ("two-byte-as", ("two_byte_as", Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rd', YLeaf(YType.enumeration, 'rd')),
                            ])
                            self.rd = None

                            self.auto = Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto()
                            self.auto.parent = self
                            self._children_name_map["auto"] = "auto"
                            self._children_yang_names.add("auto")

                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")
                            self._segment_path = lambda: "rd-auto"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdAuto, ['rd'], name, value)


                        class Auto(Entity):
                            """
                            auto
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto, self).__init__()

                                self.yang_name = "auto"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', YLeaf(YType.str, 'router-id')),
                                    ('auto_index', YLeaf(YType.uint16, 'auto-index')),
                                ])
                                self.router_id = None
                                self.auto_index = None
                                self._segment_path = lambda: "auto"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto, ['router_id', 'auto_index'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                    class RdConfigured(Entity):
                        """
                        Configured Route Distinguisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:  :py:class:`L2vpnAdRd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRd>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.Elements.Element.RdConfigured, self).__init__()

                            self.yang_name = "rd-configured"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("auto", ("auto", Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto)), ("two-byte-as", ("two_byte_as", Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rd', YLeaf(YType.enumeration, 'rd')),
                            ])
                            self.rd = None

                            self.auto = Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto()
                            self.auto.parent = self
                            self._children_name_map["auto"] = "auto"
                            self._children_yang_names.add("auto")

                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")
                            self._segment_path = lambda: "rd-configured"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdConfigured, ['rd'], name, value)


                        class Auto(Entity):
                            """
                            auto
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto, self).__init__()

                                self.yang_name = "auto"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', YLeaf(YType.str, 'router-id')),
                                    ('auto_index', YLeaf(YType.uint16, 'auto-index')),
                                ])
                                self.router_id = None
                                self.auto_index = None
                                self._segment_path = lambda: "auto"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto, ['router_id', 'auto_index'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                    class RtAuto(Entity):
                        """
                        Automatic Route Target
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr>`
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.Elements.Element.RtAuto, self).__init__()

                            self.yang_name = "rt-auto"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr)), ("es-import", ("es_import", Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rt', YLeaf(YType.enumeration, 'rt')),
                            ])
                            self.rt = None

                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")

                            self.es_import = Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport()
                            self.es_import.parent = self
                            self._children_name_map["es_import"] = "es-import"
                            self._children_yang_names.add("es-import")
                            self._segment_path = lambda: "rt-auto"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAuto, ['rt'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                        class EsImport(Entity):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport, self).__init__()

                                self.yang_name = "es-import"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                    ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                ])
                                self.high_bytes = None
                                self.low_bytes = None
                                self._segment_path = lambda: "es-import"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport, ['high_bytes', 'low_bytes'], name, value)


                    class RtAutoStitching(Entity):
                        """
                        Automatic Route Target Stitching
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr>`
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching, self).__init__()

                            self.yang_name = "rt-auto-stitching"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr)), ("es-import", ("es_import", Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rt', YLeaf(YType.enumeration, 'rt')),
                            ])
                            self.rt = None

                            self.two_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")

                            self.es_import = Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport()
                            self.es_import.parent = self
                            self._children_name_map["es_import"] = "es-import"
                            self._children_yang_names.add("es-import")
                            self._segment_path = lambda: "rt-auto-stitching"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching, ['rt'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                        class EsImport(Entity):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport, self).__init__()

                                self.yang_name = "es-import"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                    ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                ])
                                self.high_bytes = None
                                self.low_bytes = None
                                self._segment_path = lambda: "es-import"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport, ['high_bytes', 'low_bytes'], name, value)


            class EviChildren(Entity):
                """
                Container for all EVI detail info
                
                .. attribute:: neighbors
                
                	EVPN Neighbor table
                	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Neighbors>`
                
                .. attribute:: ethernet_auto_discoveries
                
                	EVPN Ethernet Auto\-Discovery table
                	**type**\:  :py:class:`EthernetAutoDiscoveries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries>`
                
                .. attribute:: inclusive_multicasts
                
                	L2VPN EVPN IMCAST table
                	**type**\:  :py:class:`InclusiveMulticasts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts>`
                
                .. attribute:: route_targets
                
                	L2VPN EVPN EVI RT Child Table
                	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets>`
                
                .. attribute:: macs
                
                	L2VPN EVPN EVI MAC table
                	**type**\:  :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Active.EviDetail.EviChildren, self).__init__()

                    self.yang_name = "evi-children"
                    self.yang_parent_name = "evi-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("neighbors", ("neighbors", Evpn.Active.EviDetail.EviChildren.Neighbors)), ("ethernet-auto-discoveries", ("ethernet_auto_discoveries", Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries)), ("inclusive-multicasts", ("inclusive_multicasts", Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts)), ("route-targets", ("route_targets", Evpn.Active.EviDetail.EviChildren.RouteTargets)), ("macs", ("macs", Evpn.Active.EviDetail.EviChildren.Macs))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.neighbors = Evpn.Active.EviDetail.EviChildren.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")

                    self.ethernet_auto_discoveries = Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries()
                    self.ethernet_auto_discoveries.parent = self
                    self._children_name_map["ethernet_auto_discoveries"] = "ethernet-auto-discoveries"
                    self._children_yang_names.add("ethernet-auto-discoveries")

                    self.inclusive_multicasts = Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts()
                    self.inclusive_multicasts.parent = self
                    self._children_name_map["inclusive_multicasts"] = "inclusive-multicasts"
                    self._children_yang_names.add("inclusive-multicasts")

                    self.route_targets = Evpn.Active.EviDetail.EviChildren.RouteTargets()
                    self.route_targets.parent = self
                    self._children_name_map["route_targets"] = "route-targets"
                    self._children_yang_names.add("route-targets")

                    self.macs = Evpn.Active.EviDetail.EviChildren.Macs()
                    self.macs.parent = self
                    self._children_name_map["macs"] = "macs"
                    self._children_yang_names.add("macs")
                    self._segment_path = lambda: "evi-children"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/%s" % self._segment_path()


                class Neighbors(Entity):
                    """
                    EVPN Neighbor table
                    
                    .. attribute:: neighbor
                    
                    	EVPN Neighbor table
                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EviDetail.EviChildren.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("neighbor", ("neighbor", Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor))])
                        self._leafs = OrderedDict()

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        EVPN Neighbor table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: neighbor_ip
                        
                        	Neighbor IP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor
                        
                        	Neighbor IP
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('neighbor_ip', YLeaf(YType.str, 'neighbor-ip')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('neighbor', YLeaf(YType.str, 'neighbor')),
                            ])
                            self.evi = None
                            self.neighbor_ip = None
                            self.evi_xr = None
                            self.neighbor = None
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/neighbors/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor, ['evi', 'neighbor_ip', 'evi_xr', 'neighbor'], name, value)


                class EthernetAutoDiscoveries(Entity):
                    """
                    EVPN Ethernet Auto\-Discovery table
                    
                    .. attribute:: ethernet_auto_discovery
                    
                    	EVPN Ethernet Auto\-Discovery Entry
                    	**type**\: list of  		 :py:class:`EthernetAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries, self).__init__()

                        self.yang_name = "ethernet-auto-discoveries"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ethernet-auto-discovery", ("ethernet_auto_discovery", Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery))])
                        self._leafs = OrderedDict()

                        self.ethernet_auto_discovery = YList(self)
                        self._segment_path = lambda: "ethernet-auto-discoveries"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries, [], name, value)


                    class EthernetAutoDiscovery(Entity):
                        """
                        EVPN Ethernet Auto\-Discovery Entry
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: esi1
                        
                        	ES id (part 1/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi2
                        
                        	ES id (part 2/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi3
                        
                        	ES id (part 3/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi4
                        
                        	ES id (part 4/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi5
                        
                        	ES id (part 5/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_vpnid
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Service Type
                        	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_next_hop
                        
                        	Local nexthop IP
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_ead
                        
                        	Indication of EthernetAutoDiscovery Route is local
                        	**type**\: bool
                        
                        .. attribute:: encap
                        
                        	Encap type of local or remote EAD
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: redundancy_single_active
                        
                        	Single\-active redundancy configured at remote EAD
                        	**type**\: bool
                        
                        .. attribute:: redundancy_single_flow_active
                        
                        	Single\-flow\-active redundancy configured at remote EAD
                        	**type**\: bool
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ethernet_segment_identifier
                        
                        	Ethernet Segment id
                        	**type**\: list of  		 :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier>`
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of  		 :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery, self).__init__()

                            self.yang_name = "ethernet-auto-discovery"
                            self.yang_parent_name = "ethernet-auto-discoveries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ethernet-segment-identifier", ("ethernet_segment_identifier", Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier)), ("path-buffer", ("path_buffer", Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer))])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('esi1', YLeaf(YType.str, 'esi1')),
                                ('esi2', YLeaf(YType.str, 'esi2')),
                                ('esi3', YLeaf(YType.str, 'esi3')),
                                ('esi4', YLeaf(YType.str, 'esi4')),
                                ('esi5', YLeaf(YType.str, 'esi5')),
                                ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                ('ethernet_vpnid', YLeaf(YType.uint32, 'ethernet-vpnid')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                ('local_next_hop', YLeaf(YType.str, 'local-next-hop')),
                                ('local_label', YLeaf(YType.uint32, 'local-label')),
                                ('is_local_ead', YLeaf(YType.boolean, 'is-local-ead')),
                                ('encap', YLeaf(YType.uint8, 'encap')),
                                ('redundancy_single_active', YLeaf(YType.boolean, 'redundancy-single-active')),
                                ('redundancy_single_flow_active', YLeaf(YType.boolean, 'redundancy-single-flow-active')),
                                ('num_paths', YLeaf(YType.uint32, 'num-paths')),
                            ])
                            self.evi = None
                            self.esi1 = None
                            self.esi2 = None
                            self.esi3 = None
                            self.esi4 = None
                            self.esi5 = None
                            self.ethernet_tag = None
                            self.ethernet_vpnid = None
                            self.type = None
                            self.ethernet_tag_xr = None
                            self.local_next_hop = None
                            self.local_label = None
                            self.is_local_ead = None
                            self.encap = None
                            self.redundancy_single_active = None
                            self.redundancy_single_flow_active = None
                            self.num_paths = None

                            self.ethernet_segment_identifier = YList(self)
                            self.path_buffer = YList(self)
                            self._segment_path = lambda: "ethernet-auto-discovery"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/ethernet-auto-discoveries/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery, ['evi', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'ethernet_tag', 'ethernet_vpnid', 'type', 'ethernet_tag_xr', 'local_next_hop', 'local_label', 'is_local_ead', 'encap', 'redundancy_single_active', 'redundancy_single_flow_active', 'num_paths'], name, value)


                        class EthernetSegmentIdentifier(Entity):
                            """
                            Ethernet Segment id
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier, self).__init__()

                                self.yang_name = "ethernet-segment-identifier"
                                self.yang_parent_name = "ethernet-auto-discovery"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.uint8, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "ethernet-segment-identifier"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier, ['entry'], name, value)


                        class PathBuffer(Entity):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srte_tunnel
                            
                            	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer, self).__init__()

                                self.yang_name = "path-buffer"
                                self.yang_parent_name = "ethernet-auto-discovery"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('output_label', YLeaf(YType.uint32, 'output-label')),
                                    ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                                ])
                                self.next_hop = None
                                self.output_label = None
                                self.srte_tunnel = None
                                self._segment_path = lambda: "path-buffer"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class InclusiveMulticasts(Entity):
                    """
                    L2VPN EVPN IMCAST table
                    
                    .. attribute:: inclusive_multicast
                    
                    	L2VPN EVPN IMCAST table
                    	**type**\: list of  		 :py:class:`InclusiveMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts, self).__init__()

                        self.yang_name = "inclusive-multicasts"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("inclusive-multicast", ("inclusive_multicast", Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast))])
                        self._leafs = OrderedDict()

                        self.inclusive_multicast = YList(self)
                        self._segment_path = lambda: "inclusive-multicasts"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts, [], name, value)


                    class InclusiveMulticast(Entity):
                        """
                        L2VPN EVPN IMCAST table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: originating_ip
                        
                        	Originating IP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: originating_ip_xr
                        
                        	Originating IP
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: next_hop
                        
                        	IP of nexthop
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_entry
                        
                        	Local entry
                        	**type**\: bool
                        
                        .. attribute:: is_proxy_entry
                        
                        	Proxy entry
                        	**type**\: bool
                        
                        .. attribute:: encap_type
                        
                        	Encap type of local or remote IMCAST route
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast, self).__init__()

                            self.yang_name = "inclusive-multicast"
                            self.yang_parent_name = "inclusive-multicasts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                ('originating_ip', YLeaf(YType.str, 'originating-ip')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                ('originating_ip_xr', YLeaf(YType.str, 'originating-ip-xr')),
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('output_label', YLeaf(YType.uint32, 'output-label')),
                                ('is_local_entry', YLeaf(YType.boolean, 'is-local-entry')),
                                ('is_proxy_entry', YLeaf(YType.boolean, 'is-proxy-entry')),
                                ('encap_type', YLeaf(YType.uint8, 'encap-type')),
                            ])
                            self.evi = None
                            self.ethernet_tag = None
                            self.originating_ip = None
                            self.evi_xr = None
                            self.ethernet_tag_xr = None
                            self.originating_ip_xr = None
                            self.next_hop = None
                            self.output_label = None
                            self.is_local_entry = None
                            self.is_proxy_entry = None
                            self.encap_type = None
                            self._segment_path = lambda: "inclusive-multicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/inclusive-multicasts/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast, ['evi', 'ethernet_tag', 'originating_ip', 'evi_xr', 'ethernet_tag_xr', 'originating_ip_xr', 'next_hop', 'output_label', 'is_local_entry', 'is_proxy_entry', 'encap_type'], name, value)


                class RouteTargets(Entity):
                    """
                    L2VPN EVPN EVI RT Child Table
                    
                    .. attribute:: route_target
                    
                    	L2VPN EVPN EVI RT Table
                    	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EviDetail.EviChildren.RouteTargets, self).__init__()

                        self.yang_name = "route-targets"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("route-target", ("route_target", Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget))])
                        self._leafs = OrderedDict()

                        self.route_target = YList(self)
                        self._segment_path = lambda: "route-targets"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets, [], name, value)


                    class RouteTarget(Entity):
                        """
                        L2VPN EVPN EVI RT Table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: role
                        
                        	Role of the route target
                        	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetRole>`
                        
                        .. attribute:: type
                        
                        	Type of the route target
                        	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTarget>`
                        
                        .. attribute:: format
                        
                        	Format of the route target
                        	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetFormat>`
                        
                        .. attribute:: as_
                        
                        	Two or Four byte AS Number
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	RT AS Index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: addr_index
                        
                        	RT IP Index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	RT IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:  :py:class:`RouteTarget_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_>`
                        
                        .. attribute:: bd_name
                        
                        	Bridge Domain Name
                        	**type**\: str
                        
                        .. attribute:: evi_xr
                        
                        	VPN ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: route_target_role
                        
                        	RT Role
                        	**type**\:  :py:class:`L2vpnAdRtRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRtRole>`
                        
                        .. attribute:: route_target_stitching
                        
                        	RT Stitching
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget, self).__init__()

                            self.yang_name = "route-target"
                            self.yang_parent_name = "route-targets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("route-target", ("route_target", Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('role', YLeaf(YType.enumeration, 'role')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('format', YLeaf(YType.enumeration, 'format')),
                                ('as_', YLeaf(YType.uint32, 'as')),
                                ('as_index', YLeaf(YType.uint32, 'as-index')),
                                ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('bd_name', YLeaf(YType.str, 'bd-name')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('route_target_role', YLeaf(YType.enumeration, 'route-target-role')),
                                ('route_target_stitching', YLeaf(YType.boolean, 'route-target-stitching')),
                            ])
                            self.evi = None
                            self.role = None
                            self.type = None
                            self.format = None
                            self.as_ = None
                            self.as_index = None
                            self.addr_index = None
                            self.address = None
                            self.bd_name = None
                            self.evi_xr = None
                            self.route_target_role = None
                            self.route_target_stitching = None

                            self.route_target = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_()
                            self.route_target.parent = self
                            self._children_name_map["route_target"] = "route-target"
                            self._children_yang_names.add("route-target")
                            self._segment_path = lambda: "route-target"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/route-targets/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget, ['evi', 'role', 'type', 'format', 'as_', 'as_index', 'addr_index', 'address', 'bd_name', 'evi_xr', 'route_target_role', 'route_target_stitching'], name, value)


                        class RouteTarget_(Entity):
                            """
                            Route Target
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr>`
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "route-target"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr)), ("es-import", ("es_import", Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rt', YLeaf(YType.enumeration, 'rt')),
                                ])
                                self.rt = None

                                self.two_byte_as = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs()
                                self.two_byte_as.parent = self
                                self._children_name_map["two_byte_as"] = "two-byte-as"
                                self._children_yang_names.add("two-byte-as")

                                self.four_byte_as = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs()
                                self.four_byte_as.parent = self
                                self._children_name_map["four_byte_as"] = "four-byte-as"
                                self._children_yang_names.add("four-byte-as")

                                self.v4_addr = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr()
                                self.v4_addr.parent = self
                                self._children_name_map["v4_addr"] = "v4-addr"
                                self._children_yang_names.add("v4-addr")

                                self.es_import = Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport()
                                self.es_import.parent = self
                                self._children_name_map["es_import"] = "es-import"
                                self._children_yang_names.add("es-import")
                                self._segment_path = lambda: "route-target"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/route-targets/route-target/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_, ['rt'], name, value)


                            class TwoByteAs(Entity):
                                """
                                two byte as
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs, self).__init__()

                                    self.yang_name = "two-byte-as"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                        ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                    ])
                                    self.two_byte_as = None
                                    self.four_byte_index = None
                                    self._segment_path = lambda: "two-byte-as"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                            class FourByteAs(Entity):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs, self).__init__()

                                    self.yang_name = "four-byte-as"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.four_byte_as = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "four-byte-as"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                            class V4Addr(Entity):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr, self).__init__()

                                    self.yang_name = "v4-addr"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.ipv4_address = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "v4-addr"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                            class EsImport(Entity):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport, self).__init__()

                                    self.yang_name = "es-import"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                        ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                    ])
                                    self.high_bytes = None
                                    self.low_bytes = None
                                    self._segment_path = lambda: "es-import"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport, ['high_bytes', 'low_bytes'], name, value)


                class Macs(Entity):
                    """
                    L2VPN EVPN EVI MAC table
                    
                    .. attribute:: mac
                    
                    	L2VPN EVPN MAC table
                    	**type**\: list of  		 :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs.Mac>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EviDetail.EviChildren.Macs, self).__init__()

                        self.yang_name = "macs"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("mac", ("mac", Evpn.Active.EviDetail.EviChildren.Macs.Mac))])
                        self._leafs = OrderedDict()

                        self.mac = YList(self)
                        self._segment_path = lambda: "macs"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Macs, [], name, value)


                    class Mac(Entity):
                        """
                        L2VPN EVPN MAC table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: ip_address
                        
                        	IP Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_address_xr
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: ip_address_xr
                        
                        	IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_mac
                        
                        	Indication of MAC being locally generated
                        	**type**\: bool
                        
                        .. attribute:: is_proxy_entry
                        
                        	Proxy entry
                        	**type**\: bool
                        
                        .. attribute:: is_remote_mac
                        
                        	Indication of MAC being remotely generated
                        	**type**\: bool
                        
                        .. attribute:: soo_nexthop
                        
                        	SOO nexthop (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipnh_address
                        
                        	IP nexthop address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: esi_port_key
                        
                        	ESI port key
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: local_encap_type
                        
                        	Encap type of local MAC
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_encap_type
                        
                        	Encap type of remote MAC
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: learned_bridge_port_name
                        
                        	Port the MAC was learned on
                        	**type**\: str
                        
                        .. attribute:: local_seq_id
                        
                        	local seq id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_seq_id
                        
                        	remote seq id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_l3_label
                        
                        	local l3 label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_mac_address
                        
                        	Router MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mac_flush_requested
                        
                        	Number of flushes requested 
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac_flush_received
                        
                        	Number of flushes received 
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: internal_label
                        
                        	MPLS Internal Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resolved
                        
                        	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                        	**type**\: bool
                        
                        .. attribute:: local_is_static
                        
                        	Indication if Local MAC is statically configured
                        	**type**\: bool
                        
                        .. attribute:: remote_is_static
                        
                        	Indication if Remote MAC is statically configured
                        	**type**\: bool
                        
                        .. attribute:: local_ethernet_segment_identifier
                        
                        	Local Ethernet Segment id
                        	**type**\: list of  		 :py:class:`LocalEthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier>`
                        
                        .. attribute:: remote_ethernet_segment_identifier
                        
                        	Remote Ethernet Segment id
                        	**type**\: list of  		 :py:class:`RemoteEthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier>`
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of  		 :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Active.EviDetail.EviChildren.Macs.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "macs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("local-ethernet-segment-identifier", ("local_ethernet_segment_identifier", Evpn.Active.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier)), ("remote-ethernet-segment-identifier", ("remote_ethernet_segment_identifier", Evpn.Active.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier)), ("path-buffer", ("path_buffer", Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer))])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                ('mac_address', YLeaf(YType.str, 'mac-address')),
                                ('ip_address', YLeaf(YType.str, 'ip-address')),
                                ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                ('mac_address_xr', YLeaf(YType.str, 'mac-address-xr')),
                                ('ip_address_xr', YLeaf(YType.str, 'ip-address-xr')),
                                ('local_label', YLeaf(YType.uint32, 'local-label')),
                                ('num_paths', YLeaf(YType.uint32, 'num-paths')),
                                ('is_local_mac', YLeaf(YType.boolean, 'is-local-mac')),
                                ('is_proxy_entry', YLeaf(YType.boolean, 'is-proxy-entry')),
                                ('is_remote_mac', YLeaf(YType.boolean, 'is-remote-mac')),
                                ('soo_nexthop', YLeaf(YType.str, 'soo-nexthop')),
                                ('ipnh_address', YLeaf(YType.str, 'ipnh-address')),
                                ('esi_port_key', YLeaf(YType.uint16, 'esi-port-key')),
                                ('local_encap_type', YLeaf(YType.uint8, 'local-encap-type')),
                                ('remote_encap_type', YLeaf(YType.uint8, 'remote-encap-type')),
                                ('learned_bridge_port_name', YLeaf(YType.str, 'learned-bridge-port-name')),
                                ('local_seq_id', YLeaf(YType.uint32, 'local-seq-id')),
                                ('remote_seq_id', YLeaf(YType.uint32, 'remote-seq-id')),
                                ('local_l3_label', YLeaf(YType.uint32, 'local-l3-label')),
                                ('router_mac_address', YLeaf(YType.str, 'router-mac-address')),
                                ('mac_flush_requested', YLeaf(YType.uint16, 'mac-flush-requested')),
                                ('mac_flush_received', YLeaf(YType.uint16, 'mac-flush-received')),
                                ('internal_label', YLeaf(YType.uint32, 'internal-label')),
                                ('resolved', YLeaf(YType.boolean, 'resolved')),
                                ('local_is_static', YLeaf(YType.boolean, 'local-is-static')),
                                ('remote_is_static', YLeaf(YType.boolean, 'remote-is-static')),
                            ])
                            self.evi = None
                            self.ethernet_tag = None
                            self.mac_address = None
                            self.ip_address = None
                            self.ethernet_tag_xr = None
                            self.mac_address_xr = None
                            self.ip_address_xr = None
                            self.local_label = None
                            self.num_paths = None
                            self.is_local_mac = None
                            self.is_proxy_entry = None
                            self.is_remote_mac = None
                            self.soo_nexthop = None
                            self.ipnh_address = None
                            self.esi_port_key = None
                            self.local_encap_type = None
                            self.remote_encap_type = None
                            self.learned_bridge_port_name = None
                            self.local_seq_id = None
                            self.remote_seq_id = None
                            self.local_l3_label = None
                            self.router_mac_address = None
                            self.mac_flush_requested = None
                            self.mac_flush_received = None
                            self.internal_label = None
                            self.resolved = None
                            self.local_is_static = None
                            self.remote_is_static = None

                            self.local_ethernet_segment_identifier = YList(self)
                            self.remote_ethernet_segment_identifier = YList(self)
                            self.path_buffer = YList(self)
                            self._segment_path = lambda: "mac"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/macs/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Macs.Mac, ['evi', 'ethernet_tag', 'mac_address', 'ip_address', 'ethernet_tag_xr', 'mac_address_xr', 'ip_address_xr', 'local_label', 'num_paths', 'is_local_mac', 'is_proxy_entry', 'is_remote_mac', 'soo_nexthop', 'ipnh_address', 'esi_port_key', 'local_encap_type', 'remote_encap_type', 'learned_bridge_port_name', 'local_seq_id', 'remote_seq_id', 'local_l3_label', 'router_mac_address', 'mac_flush_requested', 'mac_flush_received', 'internal_label', 'resolved', 'local_is_static', 'remote_is_static'], name, value)


                        class LocalEthernetSegmentIdentifier(Entity):
                            """
                            Local Ethernet Segment id
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier, self).__init__()

                                self.yang_name = "local-ethernet-segment-identifier"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.uint8, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "local-ethernet-segment-identifier"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/macs/mac/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier, ['entry'], name, value)


                        class RemoteEthernetSegmentIdentifier(Entity):
                            """
                            Remote Ethernet Segment id
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier, self).__init__()

                                self.yang_name = "remote-ethernet-segment-identifier"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.uint8, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "remote-ethernet-segment-identifier"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/macs/mac/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier, ['entry'], name, value)


                        class PathBuffer(Entity):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srte_tunnel
                            
                            	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer, self).__init__()

                                self.yang_name = "path-buffer"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('output_label', YLeaf(YType.uint32, 'output-label')),
                                    ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                                ])
                                self.next_hop = None
                                self.output_label = None
                                self.srte_tunnel = None
                                self._segment_path = lambda: "path-buffer"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/evi-detail/evi-children/macs/mac/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


        class InternalLabels(Entity):
            """
            EVPN Internal Label Table
            
            .. attribute:: internal_label
            
            	L2VPN EVPN Internal Label
            	**type**\: list of  		 :py:class:`InternalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.InternalLabels.InternalLabel>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Active.InternalLabels, self).__init__()

                self.yang_name = "internal-labels"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("internal-label", ("internal_label", Evpn.Active.InternalLabels.InternalLabel))])
                self._leafs = OrderedDict()

                self.internal_label = YList(self)
                self._segment_path = lambda: "internal-labels"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Active.InternalLabels, [], name, value)


            class InternalLabel(Entity):
                """
                L2VPN EVPN Internal Label
                
                .. attribute:: evi
                
                	EVPN id
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: esi1
                
                	ES id (part 1/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi2
                
                	ES id (part 2/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi3
                
                	ES id (part 3/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi4
                
                	ES id (part 4/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi5
                
                	ES id (part 5/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: ethernet_tag
                
                	Ethernet Tag ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	EVPN id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esi
                
                	Ethernet Segment id
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: tag
                
                	Label Tag
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: internal_label
                
                	MPLS Internal Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: encap
                
                	Encap type of remote EAD/ES, EAD/EVI and MAC routes
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: mac_num_paths
                
                	Number of items in the MAC path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ead_num_paths
                
                	Number of items in the ead path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: evi_num_paths
                
                	Number of items in the evi path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sum_num_paths
                
                	Number of items in the sum path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sum_num_active_paths
                
                	Number of items in the sum path buffer that are Active Paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: resolved
                
                	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                	**type**\: bool
                
                .. attribute:: ecmp_disable
                
                	ECMP Disable Per EVI Resolution
                	**type**\: bool
                
                .. attribute:: redundancy_single_active
                
                	Single\-active redundancy configured at remote ES
                	**type**\: bool
                
                .. attribute:: redundancy_single_flow_active
                
                	Single\-flow\-active redundancy at remote ES (MST\-AG)
                	**type**\: bool
                
                .. attribute:: mac_path_buffer
                
                	MAC Path list buffer
                	**type**\: list of  		 :py:class:`MacPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.InternalLabels.InternalLabel.MacPathBuffer>`
                
                .. attribute:: ead_path_buffer
                
                	EAD/ES Path list buffer
                	**type**\: list of  		 :py:class:`EadPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.InternalLabels.InternalLabel.EadPathBuffer>`
                
                .. attribute:: evi_path_buffer
                
                	EAD/EVI Path list buffer
                	**type**\: list of  		 :py:class:`EviPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.InternalLabels.InternalLabel.EviPathBuffer>`
                
                .. attribute:: summary_path_buffer
                
                	Summary Path list buffer
                	**type**\: list of  		 :py:class:`SummaryPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.InternalLabels.InternalLabel.SummaryPathBuffer>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Active.InternalLabels.InternalLabel, self).__init__()

                    self.yang_name = "internal-label"
                    self.yang_parent_name = "internal-labels"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("mac-path-buffer", ("mac_path_buffer", Evpn.Active.InternalLabels.InternalLabel.MacPathBuffer)), ("ead-path-buffer", ("ead_path_buffer", Evpn.Active.InternalLabels.InternalLabel.EadPathBuffer)), ("evi-path-buffer", ("evi_path_buffer", Evpn.Active.InternalLabels.InternalLabel.EviPathBuffer)), ("summary-path-buffer", ("summary_path_buffer", Evpn.Active.InternalLabels.InternalLabel.SummaryPathBuffer))])
                    self._leafs = OrderedDict([
                        ('evi', YLeaf(YType.int32, 'evi')),
                        ('esi1', YLeaf(YType.str, 'esi1')),
                        ('esi2', YLeaf(YType.str, 'esi2')),
                        ('esi3', YLeaf(YType.str, 'esi3')),
                        ('esi4', YLeaf(YType.str, 'esi4')),
                        ('esi5', YLeaf(YType.str, 'esi5')),
                        ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                        ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                        ('esi', YLeaf(YType.str, 'esi')),
                        ('tag', YLeaf(YType.uint32, 'tag')),
                        ('internal_label', YLeaf(YType.uint32, 'internal-label')),
                        ('encap', YLeaf(YType.uint8, 'encap')),
                        ('mac_num_paths', YLeaf(YType.uint32, 'mac-num-paths')),
                        ('ead_num_paths', YLeaf(YType.uint32, 'ead-num-paths')),
                        ('evi_num_paths', YLeaf(YType.uint32, 'evi-num-paths')),
                        ('sum_num_paths', YLeaf(YType.uint32, 'sum-num-paths')),
                        ('sum_num_active_paths', YLeaf(YType.uint32, 'sum-num-active-paths')),
                        ('resolved', YLeaf(YType.boolean, 'resolved')),
                        ('ecmp_disable', YLeaf(YType.boolean, 'ecmp-disable')),
                        ('redundancy_single_active', YLeaf(YType.boolean, 'redundancy-single-active')),
                        ('redundancy_single_flow_active', YLeaf(YType.boolean, 'redundancy-single-flow-active')),
                    ])
                    self.evi = None
                    self.esi1 = None
                    self.esi2 = None
                    self.esi3 = None
                    self.esi4 = None
                    self.esi5 = None
                    self.ethernet_tag = None
                    self.evi_xr = None
                    self.esi = None
                    self.tag = None
                    self.internal_label = None
                    self.encap = None
                    self.mac_num_paths = None
                    self.ead_num_paths = None
                    self.evi_num_paths = None
                    self.sum_num_paths = None
                    self.sum_num_active_paths = None
                    self.resolved = None
                    self.ecmp_disable = None
                    self.redundancy_single_active = None
                    self.redundancy_single_flow_active = None

                    self.mac_path_buffer = YList(self)
                    self.ead_path_buffer = YList(self)
                    self.evi_path_buffer = YList(self)
                    self.summary_path_buffer = YList(self)
                    self._segment_path = lambda: "internal-label"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/internal-labels/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Active.InternalLabels.InternalLabel, ['evi', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'ethernet_tag', 'evi_xr', 'esi', 'tag', 'internal_label', 'encap', 'mac_num_paths', 'ead_num_paths', 'evi_num_paths', 'sum_num_paths', 'sum_num_active_paths', 'resolved', 'ecmp_disable', 'redundancy_single_active', 'redundancy_single_flow_active'], name, value)


                class MacPathBuffer(Entity):
                    """
                    MAC Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.InternalLabels.InternalLabel.MacPathBuffer, self).__init__()

                        self.yang_name = "mac-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "mac-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.InternalLabels.InternalLabel.MacPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class EadPathBuffer(Entity):
                    """
                    EAD/ES Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.InternalLabels.InternalLabel.EadPathBuffer, self).__init__()

                        self.yang_name = "ead-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "ead-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.InternalLabels.InternalLabel.EadPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class EviPathBuffer(Entity):
                    """
                    EAD/EVI Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.InternalLabels.InternalLabel.EviPathBuffer, self).__init__()

                        self.yang_name = "evi-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "evi-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.InternalLabels.InternalLabel.EviPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class SummaryPathBuffer(Entity):
                    """
                    Summary Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.InternalLabels.InternalLabel.SummaryPathBuffer, self).__init__()

                        self.yang_name = "summary-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "summary-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.InternalLabels.InternalLabel.SummaryPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


        class EthernetSegments(Entity):
            """
            EVPN Ethernet\-Segment Table
            
            .. attribute:: ethernet_segment
            
            	EVPN Ethernet\-Segment Entry
            	**type**\: list of  		 :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Active.EthernetSegments, self).__init__()

                self.yang_name = "ethernet-segments"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("ethernet-segment", ("ethernet_segment", Evpn.Active.EthernetSegments.EthernetSegment))])
                self._leafs = OrderedDict()

                self.ethernet_segment = YList(self)
                self._segment_path = lambda: "ethernet-segments"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Active.EthernetSegments, [], name, value)


            class EthernetSegment(Entity):
                """
                EVPN Ethernet\-Segment Entry
                
                .. attribute:: interface_name
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: esi1
                
                	ES id (part 1/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi2
                
                	ES id (part 2/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi3
                
                	ES id (part 3/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi4
                
                	ES id (part 4/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi5
                
                	ES id (part 5/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi_type
                
                	ESI Type
                	**type**\:  :py:class:`L2vpnEvpnEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnEsi>`
                
                .. attribute:: esi_system_identifier
                
                	ESI System Identifier
                	**type**\: str
                
                .. attribute:: esi_port_key
                
                	ESI Port Key
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esi_system_priority
                
                	ESI System Priority
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_segment_name
                
                	Ethernet Segment Name
                	**type**\: str
                
                .. attribute:: ethernet_segment_state
                
                	State of the ethernet segment
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: if_handle
                
                	Main port ifhandle
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: main_port_role
                
                	Main port redundancy group role
                	**type**\:  :py:class:`L2vpnRgRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnRgRole>`
                
                .. attribute:: main_port_mac
                
                	Main Port MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: num_up_p_ws
                
                	Number of PWs in Up state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_target
                
                	ES\-Import Route Target
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: rt_origin
                
                	Origin of operational ES\-Import RT
                	**type**\:  :py:class:`L2vpnEvpnRtOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnRtOrigin>`
                
                .. attribute:: es_bgp_gates
                
                	ES BGP Gates
                	**type**\: str
                
                .. attribute:: es_l2fib_gates
                
                	ES L2FIB Gates
                	**type**\: str
                
                .. attribute:: mac_flushing_mode_config
                
                	Configured MAC Flushing mode
                	**type**\:  :py:class:`L2vpnEvpnMfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnMfMode>`
                
                .. attribute:: load_balance_mode_config
                
                	Configured load balancing mode
                	**type**\:  :py:class:`L2vpnEvpnLbMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnLbMode>`
                
                .. attribute:: load_balance_mode_is_default
                
                	Load balancing mode is default
                	**type**\: bool
                
                .. attribute:: load_balance_mode_oper
                
                	Operational load balancing mode
                	**type**\:  :py:class:`L2vpnEvpnLbMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnLbMode>`
                
                .. attribute:: force_single_home
                
                	Ethernet\-Segment forced to single home
                	**type**\: bool
                
                .. attribute:: source_mac_oper
                
                	Operational Source MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: source_mac_origin
                
                	Origin of operational source MAC address
                	**type**\:  :py:class:`L2vpnEvpnSmacSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnSmacSrc>`
                
                .. attribute:: peering_timer
                
                	Configured timer for triggering DF election (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: peering_timer_left
                
                	Milliseconds left on DF election timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: recovery_timer
                
                	Configured timer for (STP) recovery (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: recovery_timer_left
                
                	Milliseconds left on (STP) recovery timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: carving_timer
                
                	Configured timer for delaying DF election (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: carving_timer_left
                
                	Milliseconds left on carving timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: service_carving_mode
                
                	Service carving mode
                	**type**\:  :py:class:`L2vpnEvpnScMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnScMode>`
                
                .. attribute:: primary_services_input
                
                	Input string of Primary services ESI/I\-SIDs
                	**type**\: str
                
                .. attribute:: secondary_services_input
                
                	Input string of Secondary services ESI/I\-SIDs
                	**type**\: str
                
                .. attribute:: forwarder_ports
                
                	Count of Forwarders (AC, AC PW, VFI PW)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: permanent_forwarder_ports
                
                	Count of Forwarders with permanent service
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: elected_forwarder_ports
                
                	Count of Forwarders with elected service
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_elected_forwarder_ports
                
                	Count of Forwarders with not elected service
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_config_forwarder_ports
                
                	Count of forwarders with missing config detected
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mp_protected
                
                	MP is protected and not under EVPN control
                	**type**\: bool
                
                .. attribute:: nve_anycast_vtep
                
                	Anycast VTEP mode on NVE main\-interface
                	**type**\: bool
                
                .. attribute:: nve_ingress_replication
                
                	Ingress\-Replication is configured on NVE main\-interface
                	**type**\: bool
                
                .. attribute:: local_split_horizon_group_label_valid
                
                	Local split horizon group label is valid
                	**type**\: bool
                
                .. attribute:: local_split_horizon_group_label
                
                	Local split horizon group label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_segment_identifier
                
                	Ethernet Segment id
                	**type**\: list of  		 :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier>`
                
                .. attribute:: primary_service
                
                	List of Primary services ESI/I\-SIDs
                	**type**\: list of  		 :py:class:`PrimaryService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.PrimaryService>`
                
                .. attribute:: secondary_service
                
                	List of Secondary services ESI/I\-SIDs
                	**type**\: list of  		 :py:class:`SecondaryService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.SecondaryService>`
                
                .. attribute:: service_carving_i_sidelected_result
                
                	Elected ISID service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingISidelectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult>`
                
                .. attribute:: service_carving_isid_not_elected_result
                
                	Not elected ISID service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingIsidNotElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult>`
                
                .. attribute:: service_carving_evi_elected_result
                
                	Elected EVI service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingEviElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult>`
                
                .. attribute:: service_carving_evi_not_elected_result
                
                	Not elected EVI service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingEviNotElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult>`
                
                .. attribute:: next_hop
                
                	List of nexthop IPv6 addresses
                	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.NextHop>`
                
                .. attribute:: service_carving_vpws_permanent_result
                
                	Permanent EVPN VPWS service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingVpwsPermanentResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult>`
                
                .. attribute:: remote_split_horizon_group_label
                
                	Remote split horizon group labels
                	**type**\: list of  		 :py:class:`RemoteSplitHorizonGroupLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Active.EthernetSegments.EthernetSegment, self).__init__()

                    self.yang_name = "ethernet-segment"
                    self.yang_parent_name = "ethernet-segments"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ethernet-segment-identifier", ("ethernet_segment_identifier", Evpn.Active.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier)), ("primary-service", ("primary_service", Evpn.Active.EthernetSegments.EthernetSegment.PrimaryService)), ("secondary-service", ("secondary_service", Evpn.Active.EthernetSegments.EthernetSegment.SecondaryService)), ("service-carving-i-sidelected-result", ("service_carving_i_sidelected_result", Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult)), ("service-carving-isid-not-elected-result", ("service_carving_isid_not_elected_result", Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult)), ("service-carving-evi-elected-result", ("service_carving_evi_elected_result", Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult)), ("service-carving-evi-not-elected-result", ("service_carving_evi_not_elected_result", Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult)), ("next-hop", ("next_hop", Evpn.Active.EthernetSegments.EthernetSegment.NextHop)), ("service-carving-vpws-permanent-result", ("service_carving_vpws_permanent_result", Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult)), ("remote-split-horizon-group-label", ("remote_split_horizon_group_label", Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel))])
                    self._leafs = OrderedDict([
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('esi1', YLeaf(YType.str, 'esi1')),
                        ('esi2', YLeaf(YType.str, 'esi2')),
                        ('esi3', YLeaf(YType.str, 'esi3')),
                        ('esi4', YLeaf(YType.str, 'esi4')),
                        ('esi5', YLeaf(YType.str, 'esi5')),
                        ('esi_type', YLeaf(YType.enumeration, 'esi-type')),
                        ('esi_system_identifier', YLeaf(YType.str, 'esi-system-identifier')),
                        ('esi_port_key', YLeaf(YType.uint32, 'esi-port-key')),
                        ('esi_system_priority', YLeaf(YType.uint32, 'esi-system-priority')),
                        ('ethernet_segment_name', YLeaf(YType.str, 'ethernet-segment-name')),
                        ('ethernet_segment_state', YLeaf(YType.uint32, 'ethernet-segment-state')),
                        ('if_handle', YLeaf(YType.str, 'if-handle')),
                        ('main_port_role', YLeaf(YType.enumeration, 'main-port-role')),
                        ('main_port_mac', YLeaf(YType.str, 'main-port-mac')),
                        ('num_up_p_ws', YLeaf(YType.uint32, 'num-up-p-ws')),
                        ('route_target', YLeaf(YType.str, 'route-target')),
                        ('rt_origin', YLeaf(YType.enumeration, 'rt-origin')),
                        ('es_bgp_gates', YLeaf(YType.str, 'es-bgp-gates')),
                        ('es_l2fib_gates', YLeaf(YType.str, 'es-l2fib-gates')),
                        ('mac_flushing_mode_config', YLeaf(YType.enumeration, 'mac-flushing-mode-config')),
                        ('load_balance_mode_config', YLeaf(YType.enumeration, 'load-balance-mode-config')),
                        ('load_balance_mode_is_default', YLeaf(YType.boolean, 'load-balance-mode-is-default')),
                        ('load_balance_mode_oper', YLeaf(YType.enumeration, 'load-balance-mode-oper')),
                        ('force_single_home', YLeaf(YType.boolean, 'force-single-home')),
                        ('source_mac_oper', YLeaf(YType.str, 'source-mac-oper')),
                        ('source_mac_origin', YLeaf(YType.enumeration, 'source-mac-origin')),
                        ('peering_timer', YLeaf(YType.uint32, 'peering-timer')),
                        ('peering_timer_left', YLeaf(YType.uint32, 'peering-timer-left')),
                        ('recovery_timer', YLeaf(YType.uint32, 'recovery-timer')),
                        ('recovery_timer_left', YLeaf(YType.uint32, 'recovery-timer-left')),
                        ('carving_timer', YLeaf(YType.uint32, 'carving-timer')),
                        ('carving_timer_left', YLeaf(YType.uint32, 'carving-timer-left')),
                        ('service_carving_mode', YLeaf(YType.enumeration, 'service-carving-mode')),
                        ('primary_services_input', YLeaf(YType.str, 'primary-services-input')),
                        ('secondary_services_input', YLeaf(YType.str, 'secondary-services-input')),
                        ('forwarder_ports', YLeaf(YType.uint32, 'forwarder-ports')),
                        ('permanent_forwarder_ports', YLeaf(YType.uint32, 'permanent-forwarder-ports')),
                        ('elected_forwarder_ports', YLeaf(YType.uint32, 'elected-forwarder-ports')),
                        ('not_elected_forwarder_ports', YLeaf(YType.uint32, 'not-elected-forwarder-ports')),
                        ('not_config_forwarder_ports', YLeaf(YType.uint32, 'not-config-forwarder-ports')),
                        ('mp_protected', YLeaf(YType.boolean, 'mp-protected')),
                        ('nve_anycast_vtep', YLeaf(YType.boolean, 'nve-anycast-vtep')),
                        ('nve_ingress_replication', YLeaf(YType.boolean, 'nve-ingress-replication')),
                        ('local_split_horizon_group_label_valid', YLeaf(YType.boolean, 'local-split-horizon-group-label-valid')),
                        ('local_split_horizon_group_label', YLeaf(YType.uint32, 'local-split-horizon-group-label')),
                    ])
                    self.interface_name = None
                    self.esi1 = None
                    self.esi2 = None
                    self.esi3 = None
                    self.esi4 = None
                    self.esi5 = None
                    self.esi_type = None
                    self.esi_system_identifier = None
                    self.esi_port_key = None
                    self.esi_system_priority = None
                    self.ethernet_segment_name = None
                    self.ethernet_segment_state = None
                    self.if_handle = None
                    self.main_port_role = None
                    self.main_port_mac = None
                    self.num_up_p_ws = None
                    self.route_target = None
                    self.rt_origin = None
                    self.es_bgp_gates = None
                    self.es_l2fib_gates = None
                    self.mac_flushing_mode_config = None
                    self.load_balance_mode_config = None
                    self.load_balance_mode_is_default = None
                    self.load_balance_mode_oper = None
                    self.force_single_home = None
                    self.source_mac_oper = None
                    self.source_mac_origin = None
                    self.peering_timer = None
                    self.peering_timer_left = None
                    self.recovery_timer = None
                    self.recovery_timer_left = None
                    self.carving_timer = None
                    self.carving_timer_left = None
                    self.service_carving_mode = None
                    self.primary_services_input = None
                    self.secondary_services_input = None
                    self.forwarder_ports = None
                    self.permanent_forwarder_ports = None
                    self.elected_forwarder_ports = None
                    self.not_elected_forwarder_ports = None
                    self.not_config_forwarder_ports = None
                    self.mp_protected = None
                    self.nve_anycast_vtep = None
                    self.nve_ingress_replication = None
                    self.local_split_horizon_group_label_valid = None
                    self.local_split_horizon_group_label = None

                    self.ethernet_segment_identifier = YList(self)
                    self.primary_service = YList(self)
                    self.secondary_service = YList(self)
                    self.service_carving_i_sidelected_result = YList(self)
                    self.service_carving_isid_not_elected_result = YList(self)
                    self.service_carving_evi_elected_result = YList(self)
                    self.service_carving_evi_not_elected_result = YList(self)
                    self.next_hop = YList(self)
                    self.service_carving_vpws_permanent_result = YList(self)
                    self.remote_split_horizon_group_label = YList(self)
                    self._segment_path = lambda: "ethernet-segment"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment, ['interface_name', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'esi_type', 'esi_system_identifier', 'esi_port_key', 'esi_system_priority', 'ethernet_segment_name', 'ethernet_segment_state', 'if_handle', 'main_port_role', 'main_port_mac', 'num_up_p_ws', 'route_target', 'rt_origin', 'es_bgp_gates', 'es_l2fib_gates', 'mac_flushing_mode_config', 'load_balance_mode_config', 'load_balance_mode_is_default', 'load_balance_mode_oper', 'force_single_home', 'source_mac_oper', 'source_mac_origin', 'peering_timer', 'peering_timer_left', 'recovery_timer', 'recovery_timer_left', 'carving_timer', 'carving_timer_left', 'service_carving_mode', 'primary_services_input', 'secondary_services_input', 'forwarder_ports', 'permanent_forwarder_ports', 'elected_forwarder_ports', 'not_elected_forwarder_ports', 'not_config_forwarder_ports', 'mp_protected', 'nve_anycast_vtep', 'nve_ingress_replication', 'local_split_horizon_group_label_valid', 'local_split_horizon_group_label'], name, value)


                class EthernetSegmentIdentifier(Entity):
                    """
                    Ethernet Segment id
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier, self).__init__()

                        self.yang_name = "ethernet-segment-identifier"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint8, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "ethernet-segment-identifier"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier, ['entry'], name, value)


                class PrimaryService(Entity):
                    """
                    List of Primary services ESI/I\-SIDs
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.PrimaryService, self).__init__()

                        self.yang_name = "primary-service"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "primary-service"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.PrimaryService, ['entry'], name, value)


                class SecondaryService(Entity):
                    """
                    List of Secondary services ESI/I\-SIDs
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.SecondaryService, self).__init__()

                        self.yang_name = "secondary-service"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "secondary-service"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.SecondaryService, ['entry'], name, value)


                class ServiceCarvingISidelectedResult(Entity):
                    """
                    Elected ISID service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult, self).__init__()

                        self.yang_name = "service-carving-i-sidelected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-i-sidelected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult, ['entry'], name, value)


                class ServiceCarvingIsidNotElectedResult(Entity):
                    """
                    Not elected ISID service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult, self).__init__()

                        self.yang_name = "service-carving-isid-not-elected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-isid-not-elected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult, ['entry'], name, value)


                class ServiceCarvingEviElectedResult(Entity):
                    """
                    Elected EVI service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult, self).__init__()

                        self.yang_name = "service-carving-evi-elected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-evi-elected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult, ['entry'], name, value)


                class ServiceCarvingEviNotElectedResult(Entity):
                    """
                    Not elected EVI service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult, self).__init__()

                        self.yang_name = "service-carving-evi-not-elected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-evi-not-elected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult, ['entry'], name, value)


                class NextHop(Entity):
                    """
                    List of nexthop IPv6 addresses
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.NextHop, self).__init__()

                        self.yang_name = "next-hop"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                        ])
                        self.next_hop = None
                        self._segment_path = lambda: "next-hop"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.NextHop, ['next_hop'], name, value)


                class ServiceCarvingVpwsPermanentResult(Entity):
                    """
                    Permanent EVPN VPWS service carving results
                    
                    .. attribute:: vpn_id
                    
                    	VPN ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                    
                    .. attribute:: ethernet_tag
                    
                    	Ethernet Tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult, self).__init__()

                        self.yang_name = "service-carving-vpws-permanent-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vpn_id', YLeaf(YType.uint32, 'vpn-id')),
                            ('type', YLeaf(YType.enumeration, 'type')),
                            ('ethernet_tag', YLeaf(YType.uint32, 'ethernet-tag')),
                        ])
                        self.vpn_id = None
                        self.type = None
                        self.ethernet_tag = None
                        self._segment_path = lambda: "service-carving-vpws-permanent-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult, ['vpn_id', 'type', 'ethernet_tag'], name, value)


                class RemoteSplitHorizonGroupLabel(Entity):
                    """
                    Remote split horizon group labels
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: label
                    
                    	Split horizon label associated with next\-hop address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel, self).__init__()

                        self.yang_name = "remote-split-horizon-group-label"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('label', YLeaf(YType.uint32, 'label')),
                        ])
                        self.next_hop = None
                        self.label = None
                        self._segment_path = lambda: "remote-split-horizon-group-label"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel, ['next_hop', 'label'], name, value)


        class AcIds(Entity):
            """
            EVPN AC ID table
            
            .. attribute:: ac_id
            
            	EVPN AC ID table
            	**type**\: list of  		 :py:class:`AcId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Active.AcIds.AcId>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Active.AcIds, self).__init__()

                self.yang_name = "ac-ids"
                self.yang_parent_name = "active"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("ac-id", ("ac_id", Evpn.Active.AcIds.AcId))])
                self._leafs = OrderedDict()

                self.ac_id = YList(self)
                self._segment_path = lambda: "ac-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Active.AcIds, [], name, value)


            class AcId(Entity):
                """
                EVPN AC ID table
                
                .. attribute:: evi
                
                	EVPN id
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ac_id
                
                	AC ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: neighbor
                
                	Neighbor IP
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Active.AcIds.AcId, self).__init__()

                    self.yang_name = "ac-id"
                    self.yang_parent_name = "ac-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('evi', YLeaf(YType.int32, 'evi')),
                        ('ac_id', YLeaf(YType.int32, 'ac-id')),
                        ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                        ('neighbor', YLeaf(YType.str, 'neighbor')),
                    ])
                    self.evi = None
                    self.ac_id = None
                    self.evi_xr = None
                    self.neighbor = None
                    self._segment_path = lambda: "ac-id"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/active/ac-ids/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Active.AcIds.AcId, ['evi', 'ac_id', 'evi_xr', 'neighbor'], name, value)


    class Standby(Entity):
        """
        Standby EVPN operational data
        
        .. attribute:: evis
        
        	L2VPN EVPN EVI Table
        	**type**\:  :py:class:`Evis <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.Evis>`
        
        .. attribute:: summary
        
        	L2VPN EVPN Summary
        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.Summary>`
        
        .. attribute:: evi_detail
        
        	L2VPN EVI Detail Table
        	**type**\:  :py:class:`EviDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail>`
        
        .. attribute:: internal_labels
        
        	EVPN Internal Label Table
        	**type**\:  :py:class:`InternalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.InternalLabels>`
        
        .. attribute:: ethernet_segments
        
        	EVPN Ethernet\-Segment Table
        	**type**\:  :py:class:`EthernetSegments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments>`
        
        .. attribute:: ac_ids
        
        	EVPN AC ID table
        	**type**\:  :py:class:`AcIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.AcIds>`
        
        

        """

        _prefix = 'evpn-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(Evpn.Standby, self).__init__()

            self.yang_name = "standby"
            self.yang_parent_name = "evpn"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("evis", ("evis", Evpn.Standby.Evis)), ("summary", ("summary", Evpn.Standby.Summary)), ("evi-detail", ("evi_detail", Evpn.Standby.EviDetail)), ("internal-labels", ("internal_labels", Evpn.Standby.InternalLabels)), ("ethernet-segments", ("ethernet_segments", Evpn.Standby.EthernetSegments)), ("ac-ids", ("ac_ids", Evpn.Standby.AcIds))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.evis = Evpn.Standby.Evis()
            self.evis.parent = self
            self._children_name_map["evis"] = "evis"
            self._children_yang_names.add("evis")

            self.summary = Evpn.Standby.Summary()
            self.summary.parent = self
            self._children_name_map["summary"] = "summary"
            self._children_yang_names.add("summary")

            self.evi_detail = Evpn.Standby.EviDetail()
            self.evi_detail.parent = self
            self._children_name_map["evi_detail"] = "evi-detail"
            self._children_yang_names.add("evi-detail")

            self.internal_labels = Evpn.Standby.InternalLabels()
            self.internal_labels.parent = self
            self._children_name_map["internal_labels"] = "internal-labels"
            self._children_yang_names.add("internal-labels")

            self.ethernet_segments = Evpn.Standby.EthernetSegments()
            self.ethernet_segments.parent = self
            self._children_name_map["ethernet_segments"] = "ethernet-segments"
            self._children_yang_names.add("ethernet-segments")

            self.ac_ids = Evpn.Standby.AcIds()
            self.ac_ids.parent = self
            self._children_name_map["ac_ids"] = "ac-ids"
            self._children_yang_names.add("ac-ids")
            self._segment_path = lambda: "standby"
            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/%s" % self._segment_path()


        class Evis(Entity):
            """
            L2VPN EVPN EVI Table
            
            .. attribute:: evi
            
            	L2VPN EVPN EVI Entry
            	**type**\: list of  		 :py:class:`Evi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.Evis.Evi>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Standby.Evis, self).__init__()

                self.yang_name = "evis"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("evi", ("evi", Evpn.Standby.Evis.Evi))])
                self._leafs = OrderedDict()

                self.evi = YList(self)
                self._segment_path = lambda: "evis"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Standby.Evis, [], name, value)


            class Evi(Entity):
                """
                L2VPN EVPN EVI Entry
                
                .. attribute:: evi  (key)
                
                	EVPN id
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: bd_name
                
                	Bridge domain name
                	**type**\: str
                
                .. attribute:: type
                
                	Service Type
                	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Standby.Evis.Evi, self).__init__()

                    self.yang_name = "evi"
                    self.yang_parent_name = "evis"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['evi']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('evi', YLeaf(YType.int32, 'evi')),
                        ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                        ('bd_name', YLeaf(YType.str, 'bd-name')),
                        ('type', YLeaf(YType.enumeration, 'type')),
                    ])
                    self.evi = None
                    self.evi_xr = None
                    self.bd_name = None
                    self.type = None
                    self._segment_path = lambda: "evi" + "[evi='" + str(self.evi) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evis/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Standby.Evis.Evi, ['evi', 'evi_xr', 'bd_name', 'type'], name, value)


        class Summary(Entity):
            """
            L2VPN EVPN Summary
            
            .. attribute:: router_id
            
            	EVPN Router ID
            	**type**\: str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: as_
            
            	BGP AS number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ev_is
            
            	Number of EVI DB Entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_mac_routes
            
            	Number of Local MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv4_mac_routes
            
            	Number of Local IPv4 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ipv6_mac_routes
            
            	Number of Local IPv6 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_global_mac_routes
            
            	Number of ES\:Global MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_mac_routes
            
            	Number of Remote MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_soo_mac_routes
            
            	Number of Remote Soo MAC Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv4_mac_routes
            
            	Number of Remote IPv4 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ipv6_mac_routes
            
            	Number of Remote IPv6 MAC\-IP Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_imcast_routes
            
            	Number of Local IMCAST Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_imcast_routes
            
            	Number of Remote IMCAST Routes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: labels
            
            	Number of Internal Labels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: es_entries
            
            	Number of ES Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: neighbor_entries
            
            	Number of neighbor Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: local_ead_routes
            
            	Number of Local EAD Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: remote_ead_routes
            
            	Number of Remote EAD Entries in DB
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: global_source_mac
            
            	Global Source MAC Address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: peering_time
            
            	EVPN ES Peering Time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: recovery_time
            
            	EVPN ES Recovery Time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: carving_time
            
            	EVPN ES Carving Time (seconds)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: mac_secure_move_count
            
            	Number of moves within the move interval before locking the MAC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_secure_move_interval
            
            	Interval to watch for subsequent mac moves before locking the MAC
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_secure_freeze_time
            
            	Length of time to lock the mac after a MAC security violation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_secure_retry_count
            
            	Number of times to retry after a MAC un\-freezes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cost_out
            
            	EVPN Node Cost\-out
            	**type**\: bool
            
            .. attribute:: startup_cost_in_time
            
            	EVPN Node startup cost\-in Time (minutes)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: minute
            
            .. attribute:: l2rib_throttle
            
            	Send to L2RIB Throttled
            	**type**\: bool
            
            .. attribute:: logging_df_election_enabled
            
            	Logging EVPN Designated Forwarder changes enabled
            	**type**\: bool
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Standby.Summary, self).__init__()

                self.yang_name = "summary"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('router_id', YLeaf(YType.str, 'router-id')),
                    ('as_', YLeaf(YType.uint32, 'as')),
                    ('ev_is', YLeaf(YType.uint32, 'ev-is')),
                    ('local_mac_routes', YLeaf(YType.uint32, 'local-mac-routes')),
                    ('local_ipv4_mac_routes', YLeaf(YType.uint32, 'local-ipv4-mac-routes')),
                    ('local_ipv6_mac_routes', YLeaf(YType.uint32, 'local-ipv6-mac-routes')),
                    ('es_global_mac_routes', YLeaf(YType.uint32, 'es-global-mac-routes')),
                    ('remote_mac_routes', YLeaf(YType.uint32, 'remote-mac-routes')),
                    ('remote_soo_mac_routes', YLeaf(YType.uint32, 'remote-soo-mac-routes')),
                    ('remote_ipv4_mac_routes', YLeaf(YType.uint32, 'remote-ipv4-mac-routes')),
                    ('remote_ipv6_mac_routes', YLeaf(YType.uint32, 'remote-ipv6-mac-routes')),
                    ('local_imcast_routes', YLeaf(YType.uint32, 'local-imcast-routes')),
                    ('remote_imcast_routes', YLeaf(YType.uint32, 'remote-imcast-routes')),
                    ('labels', YLeaf(YType.uint32, 'labels')),
                    ('es_entries', YLeaf(YType.uint32, 'es-entries')),
                    ('neighbor_entries', YLeaf(YType.uint32, 'neighbor-entries')),
                    ('local_ead_routes', YLeaf(YType.uint32, 'local-ead-routes')),
                    ('remote_ead_routes', YLeaf(YType.uint32, 'remote-ead-routes')),
                    ('global_source_mac', YLeaf(YType.str, 'global-source-mac')),
                    ('peering_time', YLeaf(YType.uint32, 'peering-time')),
                    ('recovery_time', YLeaf(YType.uint32, 'recovery-time')),
                    ('carving_time', YLeaf(YType.uint32, 'carving-time')),
                    ('mac_secure_move_count', YLeaf(YType.uint32, 'mac-secure-move-count')),
                    ('mac_secure_move_interval', YLeaf(YType.uint32, 'mac-secure-move-interval')),
                    ('mac_secure_freeze_time', YLeaf(YType.uint32, 'mac-secure-freeze-time')),
                    ('mac_secure_retry_count', YLeaf(YType.uint32, 'mac-secure-retry-count')),
                    ('cost_out', YLeaf(YType.boolean, 'cost-out')),
                    ('startup_cost_in_time', YLeaf(YType.uint32, 'startup-cost-in-time')),
                    ('l2rib_throttle', YLeaf(YType.boolean, 'l2rib-throttle')),
                    ('logging_df_election_enabled', YLeaf(YType.boolean, 'logging-df-election-enabled')),
                ])
                self.router_id = None
                self.as_ = None
                self.ev_is = None
                self.local_mac_routes = None
                self.local_ipv4_mac_routes = None
                self.local_ipv6_mac_routes = None
                self.es_global_mac_routes = None
                self.remote_mac_routes = None
                self.remote_soo_mac_routes = None
                self.remote_ipv4_mac_routes = None
                self.remote_ipv6_mac_routes = None
                self.local_imcast_routes = None
                self.remote_imcast_routes = None
                self.labels = None
                self.es_entries = None
                self.neighbor_entries = None
                self.local_ead_routes = None
                self.remote_ead_routes = None
                self.global_source_mac = None
                self.peering_time = None
                self.recovery_time = None
                self.carving_time = None
                self.mac_secure_move_count = None
                self.mac_secure_move_interval = None
                self.mac_secure_freeze_time = None
                self.mac_secure_retry_count = None
                self.cost_out = None
                self.startup_cost_in_time = None
                self.l2rib_throttle = None
                self.logging_df_election_enabled = None
                self._segment_path = lambda: "summary"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Standby.Summary, ['router_id', 'as_', 'ev_is', 'local_mac_routes', 'local_ipv4_mac_routes', 'local_ipv6_mac_routes', 'es_global_mac_routes', 'remote_mac_routes', 'remote_soo_mac_routes', 'remote_ipv4_mac_routes', 'remote_ipv6_mac_routes', 'local_imcast_routes', 'remote_imcast_routes', 'labels', 'es_entries', 'neighbor_entries', 'local_ead_routes', 'remote_ead_routes', 'global_source_mac', 'peering_time', 'recovery_time', 'carving_time', 'mac_secure_move_count', 'mac_secure_move_interval', 'mac_secure_freeze_time', 'mac_secure_retry_count', 'cost_out', 'startup_cost_in_time', 'l2rib_throttle', 'logging_df_election_enabled'], name, value)


        class EviDetail(Entity):
            """
            L2VPN EVI Detail Table
            
            .. attribute:: elements
            
            	EVI BGP RT Detail Info Elements
            	**type**\:  :py:class:`Elements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements>`
            
            .. attribute:: evi_children
            
            	Container for all EVI detail info
            	**type**\:  :py:class:`EviChildren <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Standby.EviDetail, self).__init__()

                self.yang_name = "evi-detail"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("elements", ("elements", Evpn.Standby.EviDetail.Elements)), ("evi-children", ("evi_children", Evpn.Standby.EviDetail.EviChildren))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict()

                self.elements = Evpn.Standby.EviDetail.Elements()
                self.elements.parent = self
                self._children_name_map["elements"] = "elements"
                self._children_yang_names.add("elements")

                self.evi_children = Evpn.Standby.EviDetail.EviChildren()
                self.evi_children.parent = self
                self._children_name_map["evi_children"] = "evi-children"
                self._children_yang_names.add("evi-children")
                self._segment_path = lambda: "evi-detail"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/%s" % self._segment_path()


            class Elements(Entity):
                """
                EVI BGP RT Detail Info Elements
                
                .. attribute:: element
                
                	EVI BGP RT Detail Info
                	**type**\: list of  		 :py:class:`Element <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Standby.EviDetail.Elements, self).__init__()

                    self.yang_name = "elements"
                    self.yang_parent_name = "evi-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("element", ("element", Evpn.Standby.EviDetail.Elements.Element))])
                    self._leafs = OrderedDict()

                    self.element = YList(self)
                    self._segment_path = lambda: "elements"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Standby.EviDetail.Elements, [], name, value)


                class Element(Entity):
                    """
                    EVI BGP RT Detail Info
                    
                    .. attribute:: evi  (key)
                    
                    	EVPN id
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: flow_label
                    
                    	Flow Label Information
                    	**type**\:  :py:class:`FlowLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.FlowLabel>`
                    
                    .. attribute:: rd_auto
                    
                    	Automatic Route Distingtuisher
                    	**type**\:  :py:class:`RdAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto>`
                    
                    .. attribute:: rd_configured
                    
                    	Configured Route Distinguisher
                    	**type**\:  :py:class:`RdConfigured <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured>`
                    
                    .. attribute:: rt_auto
                    
                    	Automatic Route Target
                    	**type**\:  :py:class:`RtAuto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto>`
                    
                    .. attribute:: rt_auto_stitching
                    
                    	Automatic Route Target Stitching
                    	**type**\:  :py:class:`RtAutoStitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching>`
                    
                    .. attribute:: evi_xr
                    
                    	E\-VPN id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: description
                    
                    	EVI description
                    	**type**\: str
                    
                    .. attribute:: bd_name
                    
                    	Bridge domain name
                    	**type**\: str
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                    
                    .. attribute:: unicast_label
                    
                    	Unicast Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: multicast_label
                    
                    	Multicast Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cw_disable
                    
                    	Control\-Word Disable
                    	**type**\: bool
                    
                    .. attribute:: table_policy_name
                    
                    	Table\-policy Name
                    	**type**\: str
                    
                    .. attribute:: forward_class
                    
                    	Forward Class attribute
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: rt_import_block_set
                    
                    	Is Import RT None set
                    	**type**\: bool
                    
                    .. attribute:: rt_export_block_set
                    
                    	Is Export RT None set
                    	**type**\: bool
                    
                    .. attribute:: advertise_mac
                    
                    	Advertise MAC\-only routes on this EVI
                    	**type**\: bool
                    
                    .. attribute:: advertise_bvi_mac
                    
                    	Advertise BVI MACs routes on this EVI
                    	**type**\: bool
                    
                    .. attribute:: aliasing_disabled
                    
                    	Route Aliasing is disabled
                    	**type**\: bool
                    
                    .. attribute:: unknown_unicast_flooding_disabled
                    
                    	Unknown\-unicast flooding is disabled
                    	**type**\: bool
                    
                    .. attribute:: reoriginate_disabled
                    
                    	Route Re\-origination is disabled
                    	**type**\: bool
                    
                    .. attribute:: stitching
                    
                    	EVPN Instance is Regular/Stitching side
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    .. attribute:: encapsulation
                    
                    	EVPN Instance encapsulation
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EviDetail.Elements.Element, self).__init__()

                        self.yang_name = "element"
                        self.yang_parent_name = "elements"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['evi']
                        self._child_container_classes = OrderedDict([("flow-label", ("flow_label", Evpn.Standby.EviDetail.Elements.Element.FlowLabel)), ("rd-auto", ("rd_auto", Evpn.Standby.EviDetail.Elements.Element.RdAuto)), ("rd-configured", ("rd_configured", Evpn.Standby.EviDetail.Elements.Element.RdConfigured)), ("rt-auto", ("rt_auto", Evpn.Standby.EviDetail.Elements.Element.RtAuto)), ("rt-auto-stitching", ("rt_auto_stitching", Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('evi', YLeaf(YType.int32, 'evi')),
                            ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                            ('description', YLeaf(YType.str, 'description')),
                            ('bd_name', YLeaf(YType.str, 'bd-name')),
                            ('type', YLeaf(YType.enumeration, 'type')),
                            ('unicast_label', YLeaf(YType.uint32, 'unicast-label')),
                            ('multicast_label', YLeaf(YType.uint32, 'multicast-label')),
                            ('cw_disable', YLeaf(YType.boolean, 'cw-disable')),
                            ('table_policy_name', YLeaf(YType.str, 'table-policy-name')),
                            ('forward_class', YLeaf(YType.uint8, 'forward-class')),
                            ('rt_import_block_set', YLeaf(YType.boolean, 'rt-import-block-set')),
                            ('rt_export_block_set', YLeaf(YType.boolean, 'rt-export-block-set')),
                            ('advertise_mac', YLeaf(YType.boolean, 'advertise-mac')),
                            ('advertise_bvi_mac', YLeaf(YType.boolean, 'advertise-bvi-mac')),
                            ('aliasing_disabled', YLeaf(YType.boolean, 'aliasing-disabled')),
                            ('unknown_unicast_flooding_disabled', YLeaf(YType.boolean, 'unknown-unicast-flooding-disabled')),
                            ('reoriginate_disabled', YLeaf(YType.boolean, 'reoriginate-disabled')),
                            ('stitching', YLeaf(YType.uint8, 'stitching')),
                            ('encapsulation', YLeaf(YType.uint8, 'encapsulation')),
                        ])
                        self.evi = None
                        self.evi_xr = None
                        self.description = None
                        self.bd_name = None
                        self.type = None
                        self.unicast_label = None
                        self.multicast_label = None
                        self.cw_disable = None
                        self.table_policy_name = None
                        self.forward_class = None
                        self.rt_import_block_set = None
                        self.rt_export_block_set = None
                        self.advertise_mac = None
                        self.advertise_bvi_mac = None
                        self.aliasing_disabled = None
                        self.unknown_unicast_flooding_disabled = None
                        self.reoriginate_disabled = None
                        self.stitching = None
                        self.encapsulation = None

                        self.flow_label = Evpn.Standby.EviDetail.Elements.Element.FlowLabel()
                        self.flow_label.parent = self
                        self._children_name_map["flow_label"] = "flow-label"
                        self._children_yang_names.add("flow-label")

                        self.rd_auto = Evpn.Standby.EviDetail.Elements.Element.RdAuto()
                        self.rd_auto.parent = self
                        self._children_name_map["rd_auto"] = "rd-auto"
                        self._children_yang_names.add("rd-auto")

                        self.rd_configured = Evpn.Standby.EviDetail.Elements.Element.RdConfigured()
                        self.rd_configured.parent = self
                        self._children_name_map["rd_configured"] = "rd-configured"
                        self._children_yang_names.add("rd-configured")

                        self.rt_auto = Evpn.Standby.EviDetail.Elements.Element.RtAuto()
                        self.rt_auto.parent = self
                        self._children_name_map["rt_auto"] = "rt-auto"
                        self._children_yang_names.add("rt-auto")

                        self.rt_auto_stitching = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching()
                        self.rt_auto_stitching.parent = self
                        self._children_name_map["rt_auto_stitching"] = "rt-auto-stitching"
                        self._children_yang_names.add("rt-auto-stitching")
                        self._segment_path = lambda: "element" + "[evi='" + str(self.evi) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/elements/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element, ['evi', 'evi_xr', 'description', 'bd_name', 'type', 'unicast_label', 'multicast_label', 'cw_disable', 'table_policy_name', 'forward_class', 'rt_import_block_set', 'rt_export_block_set', 'advertise_mac', 'advertise_bvi_mac', 'aliasing_disabled', 'unknown_unicast_flooding_disabled', 'reoriginate_disabled', 'stitching', 'encapsulation'], name, value)


                    class FlowLabel(Entity):
                        """
                        Flow Label Information
                        
                        .. attribute:: static_flow_label
                        
                        	Static flow label
                        	**type**\: bool
                        
                        .. attribute:: global_flow_label
                        
                        	Globally configured flow label
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.Elements.Element.FlowLabel, self).__init__()

                            self.yang_name = "flow-label"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('static_flow_label', YLeaf(YType.boolean, 'static-flow-label')),
                                ('global_flow_label', YLeaf(YType.boolean, 'global-flow-label')),
                            ])
                            self.static_flow_label = None
                            self.global_flow_label = None
                            self._segment_path = lambda: "flow-label"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.FlowLabel, ['static_flow_label', 'global_flow_label'], name, value)


                    class RdAuto(Entity):
                        """
                        Automatic Route Distingtuisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:  :py:class:`L2vpnAdRd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRd>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.Elements.Element.RdAuto, self).__init__()

                            self.yang_name = "rd-auto"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("auto", ("auto", Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto)), ("two-byte-as", ("two_byte_as", Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rd', YLeaf(YType.enumeration, 'rd')),
                            ])
                            self.rd = None

                            self.auto = Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto()
                            self.auto.parent = self
                            self._children_name_map["auto"] = "auto"
                            self._children_yang_names.add("auto")

                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")
                            self._segment_path = lambda: "rd-auto"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdAuto, ['rd'], name, value)


                        class Auto(Entity):
                            """
                            auto
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto, self).__init__()

                                self.yang_name = "auto"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', YLeaf(YType.str, 'router-id')),
                                    ('auto_index', YLeaf(YType.uint16, 'auto-index')),
                                ])
                                self.router_id = None
                                self.auto_index = None
                                self._segment_path = lambda: "auto"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto, ['router_id', 'auto_index'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rd-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                    class RdConfigured(Entity):
                        """
                        Configured Route Distinguisher
                        
                        .. attribute:: auto
                        
                        	auto
                        	**type**\:  :py:class:`Auto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto>`
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr>`
                        
                        .. attribute:: rd
                        
                        	RD
                        	**type**\:  :py:class:`L2vpnAdRd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRd>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.Elements.Element.RdConfigured, self).__init__()

                            self.yang_name = "rd-configured"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("auto", ("auto", Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto)), ("two-byte-as", ("two_byte_as", Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rd', YLeaf(YType.enumeration, 'rd')),
                            ])
                            self.rd = None

                            self.auto = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto()
                            self.auto.parent = self
                            self._children_name_map["auto"] = "auto"
                            self._children_yang_names.add("auto")

                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")
                            self._segment_path = lambda: "rd-configured"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdConfigured, ['rd'], name, value)


                        class Auto(Entity):
                            """
                            auto
                            
                            .. attribute:: router_id
                            
                            	BGP Router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: auto_index
                            
                            	Auto\-generated Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto, self).__init__()

                                self.yang_name = "auto"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('router_id', YLeaf(YType.str, 'router-id')),
                                    ('auto_index', YLeaf(YType.uint16, 'auto-index')),
                                ])
                                self.router_id = None
                                self.auto_index = None
                                self._segment_path = lambda: "auto"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto, ['router_id', 'auto_index'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rd-configured"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                    class RtAuto(Entity):
                        """
                        Automatic Route Target
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr>`
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.Elements.Element.RtAuto, self).__init__()

                            self.yang_name = "rt-auto"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr)), ("es-import", ("es_import", Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rt', YLeaf(YType.enumeration, 'rt')),
                            ])
                            self.rt = None

                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")

                            self.es_import = Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport()
                            self.es_import.parent = self
                            self._children_name_map["es_import"] = "es-import"
                            self._children_yang_names.add("es-import")
                            self._segment_path = lambda: "rt-auto"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAuto, ['rt'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                        class EsImport(Entity):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport, self).__init__()

                                self.yang_name = "es-import"
                                self.yang_parent_name = "rt-auto"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                    ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                ])
                                self.high_bytes = None
                                self.low_bytes = None
                                self._segment_path = lambda: "es-import"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport, ['high_bytes', 'low_bytes'], name, value)


                    class RtAutoStitching(Entity):
                        """
                        Automatic Route Target Stitching
                        
                        .. attribute:: two_byte_as
                        
                        	two byte as
                        	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs>`
                        
                        .. attribute:: four_byte_as
                        
                        	four byte as
                        	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs>`
                        
                        .. attribute:: v4_addr
                        
                        	v4 addr
                        	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr>`
                        
                        .. attribute:: es_import
                        
                        	es import
                        	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport>`
                        
                        .. attribute:: rt
                        
                        	RT
                        	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching, self).__init__()

                            self.yang_name = "rt-auto-stitching"
                            self.yang_parent_name = "element"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr)), ("es-import", ("es_import", Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rt', YLeaf(YType.enumeration, 'rt')),
                            ])
                            self.rt = None

                            self.two_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs()
                            self.two_byte_as.parent = self
                            self._children_name_map["two_byte_as"] = "two-byte-as"
                            self._children_yang_names.add("two-byte-as")

                            self.four_byte_as = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs()
                            self.four_byte_as.parent = self
                            self._children_name_map["four_byte_as"] = "four-byte-as"
                            self._children_yang_names.add("four-byte-as")

                            self.v4_addr = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr()
                            self.v4_addr.parent = self
                            self._children_name_map["v4_addr"] = "v4-addr"
                            self._children_yang_names.add("v4-addr")

                            self.es_import = Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport()
                            self.es_import.parent = self
                            self._children_name_map["es_import"] = "es-import"
                            self._children_yang_names.add("es-import")
                            self._segment_path = lambda: "rt-auto-stitching"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching, ['rt'], name, value)


                        class TwoByteAs(Entity):
                            """
                            two byte as
                            
                            .. attribute:: two_byte_as
                            
                            	2 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: four_byte_index
                            
                            	4 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs, self).__init__()

                                self.yang_name = "two-byte-as"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                    ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                ])
                                self.two_byte_as = None
                                self.four_byte_index = None
                                self._segment_path = lambda: "two-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                        class FourByteAs(Entity):
                            """
                            four byte as
                            
                            .. attribute:: four_byte_as
                            
                            	4 Byte AS Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs, self).__init__()

                                self.yang_name = "four-byte-as"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.four_byte_as = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "four-byte-as"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                        class V4Addr(Entity):
                            """
                            v4 addr
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 Address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: two_byte_index
                            
                            	2 Byte Index
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr, self).__init__()

                                self.yang_name = "v4-addr"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                    ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                ])
                                self.ipv4_address = None
                                self.two_byte_index = None
                                self._segment_path = lambda: "v4-addr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                        class EsImport(Entity):
                            """
                            es import
                            
                            .. attribute:: high_bytes
                            
                            	Top 4 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: low_bytes
                            
                            	Low 2 bytes of ES Import
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport, self).__init__()

                                self.yang_name = "es-import"
                                self.yang_parent_name = "rt-auto-stitching"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                    ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                ])
                                self.high_bytes = None
                                self.low_bytes = None
                                self._segment_path = lambda: "es-import"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport, ['high_bytes', 'low_bytes'], name, value)


            class EviChildren(Entity):
                """
                Container for all EVI detail info
                
                .. attribute:: neighbors
                
                	EVPN Neighbor table
                	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Neighbors>`
                
                .. attribute:: ethernet_auto_discoveries
                
                	EVPN Ethernet Auto\-Discovery table
                	**type**\:  :py:class:`EthernetAutoDiscoveries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries>`
                
                .. attribute:: inclusive_multicasts
                
                	L2VPN EVPN IMCAST table
                	**type**\:  :py:class:`InclusiveMulticasts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts>`
                
                .. attribute:: route_targets
                
                	L2VPN EVPN EVI RT Child Table
                	**type**\:  :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets>`
                
                .. attribute:: macs
                
                	L2VPN EVPN EVI MAC table
                	**type**\:  :py:class:`Macs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Standby.EviDetail.EviChildren, self).__init__()

                    self.yang_name = "evi-children"
                    self.yang_parent_name = "evi-detail"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("neighbors", ("neighbors", Evpn.Standby.EviDetail.EviChildren.Neighbors)), ("ethernet-auto-discoveries", ("ethernet_auto_discoveries", Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries)), ("inclusive-multicasts", ("inclusive_multicasts", Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts)), ("route-targets", ("route_targets", Evpn.Standby.EviDetail.EviChildren.RouteTargets)), ("macs", ("macs", Evpn.Standby.EviDetail.EviChildren.Macs))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.neighbors = Evpn.Standby.EviDetail.EviChildren.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._children_yang_names.add("neighbors")

                    self.ethernet_auto_discoveries = Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries()
                    self.ethernet_auto_discoveries.parent = self
                    self._children_name_map["ethernet_auto_discoveries"] = "ethernet-auto-discoveries"
                    self._children_yang_names.add("ethernet-auto-discoveries")

                    self.inclusive_multicasts = Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts()
                    self.inclusive_multicasts.parent = self
                    self._children_name_map["inclusive_multicasts"] = "inclusive-multicasts"
                    self._children_yang_names.add("inclusive-multicasts")

                    self.route_targets = Evpn.Standby.EviDetail.EviChildren.RouteTargets()
                    self.route_targets.parent = self
                    self._children_name_map["route_targets"] = "route-targets"
                    self._children_yang_names.add("route-targets")

                    self.macs = Evpn.Standby.EviDetail.EviChildren.Macs()
                    self.macs.parent = self
                    self._children_name_map["macs"] = "macs"
                    self._children_yang_names.add("macs")
                    self._segment_path = lambda: "evi-children"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/%s" % self._segment_path()


                class Neighbors(Entity):
                    """
                    EVPN Neighbor table
                    
                    .. attribute:: neighbor
                    
                    	EVPN Neighbor table
                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EviDetail.EviChildren.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("neighbor", ("neighbor", Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor))])
                        self._leafs = OrderedDict()

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        EVPN Neighbor table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: neighbor_ip
                        
                        	Neighbor IP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: neighbor
                        
                        	Neighbor IP
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('neighbor_ip', YLeaf(YType.str, 'neighbor-ip')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('neighbor', YLeaf(YType.str, 'neighbor')),
                            ])
                            self.evi = None
                            self.neighbor_ip = None
                            self.evi_xr = None
                            self.neighbor = None
                            self._segment_path = lambda: "neighbor"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/neighbors/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor, ['evi', 'neighbor_ip', 'evi_xr', 'neighbor'], name, value)


                class EthernetAutoDiscoveries(Entity):
                    """
                    EVPN Ethernet Auto\-Discovery table
                    
                    .. attribute:: ethernet_auto_discovery
                    
                    	EVPN Ethernet Auto\-Discovery Entry
                    	**type**\: list of  		 :py:class:`EthernetAutoDiscovery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries, self).__init__()

                        self.yang_name = "ethernet-auto-discoveries"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ethernet-auto-discovery", ("ethernet_auto_discovery", Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery))])
                        self._leafs = OrderedDict()

                        self.ethernet_auto_discovery = YList(self)
                        self._segment_path = lambda: "ethernet-auto-discoveries"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries, [], name, value)


                    class EthernetAutoDiscovery(Entity):
                        """
                        EVPN Ethernet Auto\-Discovery Entry
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: esi1
                        
                        	ES id (part 1/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi2
                        
                        	ES id (part 2/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi3
                        
                        	ES id (part 3/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi4
                        
                        	ES id (part 4/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: esi5
                        
                        	ES id (part 5/5)
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_vpnid
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Service Type
                        	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_next_hop
                        
                        	Local nexthop IP
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_ead
                        
                        	Indication of EthernetAutoDiscovery Route is local
                        	**type**\: bool
                        
                        .. attribute:: encap
                        
                        	Encap type of local or remote EAD
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: redundancy_single_active
                        
                        	Single\-active redundancy configured at remote EAD
                        	**type**\: bool
                        
                        .. attribute:: redundancy_single_flow_active
                        
                        	Single\-flow\-active redundancy configured at remote EAD
                        	**type**\: bool
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ethernet_segment_identifier
                        
                        	Ethernet Segment id
                        	**type**\: list of  		 :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier>`
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of  		 :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery, self).__init__()

                            self.yang_name = "ethernet-auto-discovery"
                            self.yang_parent_name = "ethernet-auto-discoveries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ethernet-segment-identifier", ("ethernet_segment_identifier", Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier)), ("path-buffer", ("path_buffer", Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer))])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('esi1', YLeaf(YType.str, 'esi1')),
                                ('esi2', YLeaf(YType.str, 'esi2')),
                                ('esi3', YLeaf(YType.str, 'esi3')),
                                ('esi4', YLeaf(YType.str, 'esi4')),
                                ('esi5', YLeaf(YType.str, 'esi5')),
                                ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                ('ethernet_vpnid', YLeaf(YType.uint32, 'ethernet-vpnid')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                ('local_next_hop', YLeaf(YType.str, 'local-next-hop')),
                                ('local_label', YLeaf(YType.uint32, 'local-label')),
                                ('is_local_ead', YLeaf(YType.boolean, 'is-local-ead')),
                                ('encap', YLeaf(YType.uint8, 'encap')),
                                ('redundancy_single_active', YLeaf(YType.boolean, 'redundancy-single-active')),
                                ('redundancy_single_flow_active', YLeaf(YType.boolean, 'redundancy-single-flow-active')),
                                ('num_paths', YLeaf(YType.uint32, 'num-paths')),
                            ])
                            self.evi = None
                            self.esi1 = None
                            self.esi2 = None
                            self.esi3 = None
                            self.esi4 = None
                            self.esi5 = None
                            self.ethernet_tag = None
                            self.ethernet_vpnid = None
                            self.type = None
                            self.ethernet_tag_xr = None
                            self.local_next_hop = None
                            self.local_label = None
                            self.is_local_ead = None
                            self.encap = None
                            self.redundancy_single_active = None
                            self.redundancy_single_flow_active = None
                            self.num_paths = None

                            self.ethernet_segment_identifier = YList(self)
                            self.path_buffer = YList(self)
                            self._segment_path = lambda: "ethernet-auto-discovery"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/ethernet-auto-discoveries/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery, ['evi', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'ethernet_tag', 'ethernet_vpnid', 'type', 'ethernet_tag_xr', 'local_next_hop', 'local_label', 'is_local_ead', 'encap', 'redundancy_single_active', 'redundancy_single_flow_active', 'num_paths'], name, value)


                        class EthernetSegmentIdentifier(Entity):
                            """
                            Ethernet Segment id
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier, self).__init__()

                                self.yang_name = "ethernet-segment-identifier"
                                self.yang_parent_name = "ethernet-auto-discovery"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.uint8, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "ethernet-segment-identifier"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.EthernetSegmentIdentifier, ['entry'], name, value)


                        class PathBuffer(Entity):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srte_tunnel
                            
                            	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer, self).__init__()

                                self.yang_name = "path-buffer"
                                self.yang_parent_name = "ethernet-auto-discovery"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('output_label', YLeaf(YType.uint32, 'output-label')),
                                    ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                                ])
                                self.next_hop = None
                                self.output_label = None
                                self.srte_tunnel = None
                                self._segment_path = lambda: "path-buffer"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/ethernet-auto-discoveries/ethernet-auto-discovery/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class InclusiveMulticasts(Entity):
                    """
                    L2VPN EVPN IMCAST table
                    
                    .. attribute:: inclusive_multicast
                    
                    	L2VPN EVPN IMCAST table
                    	**type**\: list of  		 :py:class:`InclusiveMulticast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts, self).__init__()

                        self.yang_name = "inclusive-multicasts"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("inclusive-multicast", ("inclusive_multicast", Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast))])
                        self._leafs = OrderedDict()

                        self.inclusive_multicast = YList(self)
                        self._segment_path = lambda: "inclusive-multicasts"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts, [], name, value)


                    class InclusiveMulticast(Entity):
                        """
                        L2VPN EVPN IMCAST table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: originating_ip
                        
                        	Originating IP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: evi_xr
                        
                        	E\-VPN id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: originating_ip_xr
                        
                        	Originating IP
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: next_hop
                        
                        	IP of nexthop
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: output_label
                        
                        	Output label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_entry
                        
                        	Local entry
                        	**type**\: bool
                        
                        .. attribute:: is_proxy_entry
                        
                        	Proxy entry
                        	**type**\: bool
                        
                        .. attribute:: encap_type
                        
                        	Encap type of local or remote IMCAST route
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast, self).__init__()

                            self.yang_name = "inclusive-multicast"
                            self.yang_parent_name = "inclusive-multicasts"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                ('originating_ip', YLeaf(YType.str, 'originating-ip')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                ('originating_ip_xr', YLeaf(YType.str, 'originating-ip-xr')),
                                ('next_hop', YLeaf(YType.str, 'next-hop')),
                                ('output_label', YLeaf(YType.uint32, 'output-label')),
                                ('is_local_entry', YLeaf(YType.boolean, 'is-local-entry')),
                                ('is_proxy_entry', YLeaf(YType.boolean, 'is-proxy-entry')),
                                ('encap_type', YLeaf(YType.uint8, 'encap-type')),
                            ])
                            self.evi = None
                            self.ethernet_tag = None
                            self.originating_ip = None
                            self.evi_xr = None
                            self.ethernet_tag_xr = None
                            self.originating_ip_xr = None
                            self.next_hop = None
                            self.output_label = None
                            self.is_local_entry = None
                            self.is_proxy_entry = None
                            self.encap_type = None
                            self._segment_path = lambda: "inclusive-multicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/inclusive-multicasts/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast, ['evi', 'ethernet_tag', 'originating_ip', 'evi_xr', 'ethernet_tag_xr', 'originating_ip_xr', 'next_hop', 'output_label', 'is_local_entry', 'is_proxy_entry', 'encap_type'], name, value)


                class RouteTargets(Entity):
                    """
                    L2VPN EVPN EVI RT Child Table
                    
                    .. attribute:: route_target
                    
                    	L2VPN EVPN EVI RT Table
                    	**type**\: list of  		 :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EviDetail.EviChildren.RouteTargets, self).__init__()

                        self.yang_name = "route-targets"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("route-target", ("route_target", Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget))])
                        self._leafs = OrderedDict()

                        self.route_target = YList(self)
                        self._segment_path = lambda: "route-targets"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets, [], name, value)


                    class RouteTarget(Entity):
                        """
                        L2VPN EVPN EVI RT Table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: role
                        
                        	Role of the route target
                        	**type**\:  :py:class:`BgpRouteTargetRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetRole>`
                        
                        .. attribute:: type
                        
                        	Type of the route target
                        	**type**\:  :py:class:`BgpRouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTarget>`
                        
                        .. attribute:: format
                        
                        	Format of the route target
                        	**type**\:  :py:class:`BgpRouteTargetFormat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.BgpRouteTargetFormat>`
                        
                        .. attribute:: as_
                        
                        	Two or Four byte AS Number
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: as_index
                        
                        	RT AS Index
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: addr_index
                        
                        	RT IP Index
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: address
                        
                        	RT IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:  :py:class:`RouteTarget_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_>`
                        
                        .. attribute:: bd_name
                        
                        	Bridge Domain Name
                        	**type**\: str
                        
                        .. attribute:: evi_xr
                        
                        	VPN ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: route_target_role
                        
                        	RT Role
                        	**type**\:  :py:class:`L2vpnAdRtRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRtRole>`
                        
                        .. attribute:: route_target_stitching
                        
                        	RT Stitching
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget, self).__init__()

                            self.yang_name = "route-target"
                            self.yang_parent_name = "route-targets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("route-target", ("route_target", Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('role', YLeaf(YType.enumeration, 'role')),
                                ('type', YLeaf(YType.enumeration, 'type')),
                                ('format', YLeaf(YType.enumeration, 'format')),
                                ('as_', YLeaf(YType.uint32, 'as')),
                                ('as_index', YLeaf(YType.uint32, 'as-index')),
                                ('addr_index', YLeaf(YType.uint32, 'addr-index')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('bd_name', YLeaf(YType.str, 'bd-name')),
                                ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                                ('route_target_role', YLeaf(YType.enumeration, 'route-target-role')),
                                ('route_target_stitching', YLeaf(YType.boolean, 'route-target-stitching')),
                            ])
                            self.evi = None
                            self.role = None
                            self.type = None
                            self.format = None
                            self.as_ = None
                            self.as_index = None
                            self.addr_index = None
                            self.address = None
                            self.bd_name = None
                            self.evi_xr = None
                            self.route_target_role = None
                            self.route_target_stitching = None

                            self.route_target = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_()
                            self.route_target.parent = self
                            self._children_name_map["route_target"] = "route-target"
                            self._children_yang_names.add("route-target")
                            self._segment_path = lambda: "route-target"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/route-targets/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget, ['evi', 'role', 'type', 'format', 'as_', 'as_index', 'addr_index', 'address', 'bd_name', 'evi_xr', 'route_target_role', 'route_target_stitching'], name, value)


                        class RouteTarget_(Entity):
                            """
                            Route Target
                            
                            .. attribute:: two_byte_as
                            
                            	two byte as
                            	**type**\:  :py:class:`TwoByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs>`
                            
                            .. attribute:: four_byte_as
                            
                            	four byte as
                            	**type**\:  :py:class:`FourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs>`
                            
                            .. attribute:: v4_addr
                            
                            	v4 addr
                            	**type**\:  :py:class:`V4Addr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr>`
                            
                            .. attribute:: es_import
                            
                            	es import
                            	**type**\:  :py:class:`EsImport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport>`
                            
                            .. attribute:: rt
                            
                            	RT
                            	**type**\:  :py:class:`L2vpnAdRt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnAdRt>`
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "route-target"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("two-byte-as", ("two_byte_as", Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs)), ("four-byte-as", ("four_byte_as", Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs)), ("v4-addr", ("v4_addr", Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr)), ("es-import", ("es_import", Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('rt', YLeaf(YType.enumeration, 'rt')),
                                ])
                                self.rt = None

                                self.two_byte_as = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs()
                                self.two_byte_as.parent = self
                                self._children_name_map["two_byte_as"] = "two-byte-as"
                                self._children_yang_names.add("two-byte-as")

                                self.four_byte_as = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs()
                                self.four_byte_as.parent = self
                                self._children_name_map["four_byte_as"] = "four-byte-as"
                                self._children_yang_names.add("four-byte-as")

                                self.v4_addr = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr()
                                self.v4_addr.parent = self
                                self._children_name_map["v4_addr"] = "v4-addr"
                                self._children_yang_names.add("v4-addr")

                                self.es_import = Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport()
                                self.es_import.parent = self
                                self._children_name_map["es_import"] = "es-import"
                                self._children_yang_names.add("es-import")
                                self._segment_path = lambda: "route-target"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/route-targets/route-target/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_, ['rt'], name, value)


                            class TwoByteAs(Entity):
                                """
                                two byte as
                                
                                .. attribute:: two_byte_as
                                
                                	2 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: four_byte_index
                                
                                	4 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs, self).__init__()

                                    self.yang_name = "two-byte-as"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('two_byte_as', YLeaf(YType.uint16, 'two-byte-as')),
                                        ('four_byte_index', YLeaf(YType.uint32, 'four-byte-index')),
                                    ])
                                    self.two_byte_as = None
                                    self.four_byte_index = None
                                    self._segment_path = lambda: "two-byte-as"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs, ['two_byte_as', 'four_byte_index'], name, value)


                            class FourByteAs(Entity):
                                """
                                four byte as
                                
                                .. attribute:: four_byte_as
                                
                                	4 Byte AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs, self).__init__()

                                    self.yang_name = "four-byte-as"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('four_byte_as', YLeaf(YType.uint32, 'four-byte-as')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.four_byte_as = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "four-byte-as"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs, ['four_byte_as', 'two_byte_index'], name, value)


                            class V4Addr(Entity):
                                """
                                v4 addr
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 Address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: two_byte_index
                                
                                	2 Byte Index
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr, self).__init__()

                                    self.yang_name = "v4-addr"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('two_byte_index', YLeaf(YType.uint16, 'two-byte-index')),
                                    ])
                                    self.ipv4_address = None
                                    self.two_byte_index = None
                                    self._segment_path = lambda: "v4-addr"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr, ['ipv4_address', 'two_byte_index'], name, value)


                            class EsImport(Entity):
                                """
                                es import
                                
                                .. attribute:: high_bytes
                                
                                	Top 4 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: low_bytes
                                
                                	Low 2 bytes of ES Import
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'evpn-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport, self).__init__()

                                    self.yang_name = "es-import"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('high_bytes', YLeaf(YType.uint32, 'high-bytes')),
                                        ('low_bytes', YLeaf(YType.uint16, 'low-bytes')),
                                    ])
                                    self.high_bytes = None
                                    self.low_bytes = None
                                    self._segment_path = lambda: "es-import"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/route-targets/route-target/route-target/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport, ['high_bytes', 'low_bytes'], name, value)


                class Macs(Entity):
                    """
                    L2VPN EVPN EVI MAC table
                    
                    .. attribute:: mac
                    
                    	L2VPN EVPN MAC table
                    	**type**\: list of  		 :py:class:`Mac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs.Mac>`
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EviDetail.EviChildren.Macs, self).__init__()

                        self.yang_name = "macs"
                        self.yang_parent_name = "evi-children"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("mac", ("mac", Evpn.Standby.EviDetail.EviChildren.Macs.Mac))])
                        self._leafs = OrderedDict()

                        self.mac = YList(self)
                        self._segment_path = lambda: "macs"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Macs, [], name, value)


                    class Mac(Entity):
                        """
                        L2VPN EVPN MAC table
                        
                        .. attribute:: evi
                        
                        	EVPN id
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ethernet_tag
                        
                        	Ethernet Tag ID
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: mac_address
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: ip_address
                        
                        	IP Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ethernet_tag_xr
                        
                        	Ethernet Tag
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mac_address_xr
                        
                        	MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: ip_address_xr
                        
                        	IP address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: local_label
                        
                        	Associated local label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: num_paths
                        
                        	 Number of items in path list buffer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_local_mac
                        
                        	Indication of MAC being locally generated
                        	**type**\: bool
                        
                        .. attribute:: is_proxy_entry
                        
                        	Proxy entry
                        	**type**\: bool
                        
                        .. attribute:: is_remote_mac
                        
                        	Indication of MAC being remotely generated
                        	**type**\: bool
                        
                        .. attribute:: soo_nexthop
                        
                        	SOO nexthop (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipnh_address
                        
                        	IP nexthop address (v6 format)
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: esi_port_key
                        
                        	ESI port key
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: local_encap_type
                        
                        	Encap type of local MAC
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: remote_encap_type
                        
                        	Encap type of remote MAC
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: learned_bridge_port_name
                        
                        	Port the MAC was learned on
                        	**type**\: str
                        
                        .. attribute:: local_seq_id
                        
                        	local seq id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: remote_seq_id
                        
                        	remote seq id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_l3_label
                        
                        	local l3 label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: router_mac_address
                        
                        	Router MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: mac_flush_requested
                        
                        	Number of flushes requested 
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: mac_flush_received
                        
                        	Number of flushes received 
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: internal_label
                        
                        	MPLS Internal Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: resolved
                        
                        	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                        	**type**\: bool
                        
                        .. attribute:: local_is_static
                        
                        	Indication if Local MAC is statically configured
                        	**type**\: bool
                        
                        .. attribute:: remote_is_static
                        
                        	Indication if Remote MAC is statically configured
                        	**type**\: bool
                        
                        .. attribute:: local_ethernet_segment_identifier
                        
                        	Local Ethernet Segment id
                        	**type**\: list of  		 :py:class:`LocalEthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier>`
                        
                        .. attribute:: remote_ethernet_segment_identifier
                        
                        	Remote Ethernet Segment id
                        	**type**\: list of  		 :py:class:`RemoteEthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier>`
                        
                        .. attribute:: path_buffer
                        
                        	Path List Buffer
                        	**type**\: list of  		 :py:class:`PathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer>`
                        
                        

                        """

                        _prefix = 'evpn-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(Evpn.Standby.EviDetail.EviChildren.Macs.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "macs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("local-ethernet-segment-identifier", ("local_ethernet_segment_identifier", Evpn.Standby.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier)), ("remote-ethernet-segment-identifier", ("remote_ethernet_segment_identifier", Evpn.Standby.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier)), ("path-buffer", ("path_buffer", Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer))])
                            self._leafs = OrderedDict([
                                ('evi', YLeaf(YType.int32, 'evi')),
                                ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                                ('mac_address', YLeaf(YType.str, 'mac-address')),
                                ('ip_address', YLeaf(YType.str, 'ip-address')),
                                ('ethernet_tag_xr', YLeaf(YType.uint32, 'ethernet-tag-xr')),
                                ('mac_address_xr', YLeaf(YType.str, 'mac-address-xr')),
                                ('ip_address_xr', YLeaf(YType.str, 'ip-address-xr')),
                                ('local_label', YLeaf(YType.uint32, 'local-label')),
                                ('num_paths', YLeaf(YType.uint32, 'num-paths')),
                                ('is_local_mac', YLeaf(YType.boolean, 'is-local-mac')),
                                ('is_proxy_entry', YLeaf(YType.boolean, 'is-proxy-entry')),
                                ('is_remote_mac', YLeaf(YType.boolean, 'is-remote-mac')),
                                ('soo_nexthop', YLeaf(YType.str, 'soo-nexthop')),
                                ('ipnh_address', YLeaf(YType.str, 'ipnh-address')),
                                ('esi_port_key', YLeaf(YType.uint16, 'esi-port-key')),
                                ('local_encap_type', YLeaf(YType.uint8, 'local-encap-type')),
                                ('remote_encap_type', YLeaf(YType.uint8, 'remote-encap-type')),
                                ('learned_bridge_port_name', YLeaf(YType.str, 'learned-bridge-port-name')),
                                ('local_seq_id', YLeaf(YType.uint32, 'local-seq-id')),
                                ('remote_seq_id', YLeaf(YType.uint32, 'remote-seq-id')),
                                ('local_l3_label', YLeaf(YType.uint32, 'local-l3-label')),
                                ('router_mac_address', YLeaf(YType.str, 'router-mac-address')),
                                ('mac_flush_requested', YLeaf(YType.uint16, 'mac-flush-requested')),
                                ('mac_flush_received', YLeaf(YType.uint16, 'mac-flush-received')),
                                ('internal_label', YLeaf(YType.uint32, 'internal-label')),
                                ('resolved', YLeaf(YType.boolean, 'resolved')),
                                ('local_is_static', YLeaf(YType.boolean, 'local-is-static')),
                                ('remote_is_static', YLeaf(YType.boolean, 'remote-is-static')),
                            ])
                            self.evi = None
                            self.ethernet_tag = None
                            self.mac_address = None
                            self.ip_address = None
                            self.ethernet_tag_xr = None
                            self.mac_address_xr = None
                            self.ip_address_xr = None
                            self.local_label = None
                            self.num_paths = None
                            self.is_local_mac = None
                            self.is_proxy_entry = None
                            self.is_remote_mac = None
                            self.soo_nexthop = None
                            self.ipnh_address = None
                            self.esi_port_key = None
                            self.local_encap_type = None
                            self.remote_encap_type = None
                            self.learned_bridge_port_name = None
                            self.local_seq_id = None
                            self.remote_seq_id = None
                            self.local_l3_label = None
                            self.router_mac_address = None
                            self.mac_flush_requested = None
                            self.mac_flush_received = None
                            self.internal_label = None
                            self.resolved = None
                            self.local_is_static = None
                            self.remote_is_static = None

                            self.local_ethernet_segment_identifier = YList(self)
                            self.remote_ethernet_segment_identifier = YList(self)
                            self.path_buffer = YList(self)
                            self._segment_path = lambda: "mac"
                            self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/macs/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Macs.Mac, ['evi', 'ethernet_tag', 'mac_address', 'ip_address', 'ethernet_tag_xr', 'mac_address_xr', 'ip_address_xr', 'local_label', 'num_paths', 'is_local_mac', 'is_proxy_entry', 'is_remote_mac', 'soo_nexthop', 'ipnh_address', 'esi_port_key', 'local_encap_type', 'remote_encap_type', 'learned_bridge_port_name', 'local_seq_id', 'remote_seq_id', 'local_l3_label', 'router_mac_address', 'mac_flush_requested', 'mac_flush_received', 'internal_label', 'resolved', 'local_is_static', 'remote_is_static'], name, value)


                        class LocalEthernetSegmentIdentifier(Entity):
                            """
                            Local Ethernet Segment id
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier, self).__init__()

                                self.yang_name = "local-ethernet-segment-identifier"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.uint8, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "local-ethernet-segment-identifier"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/macs/mac/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Macs.Mac.LocalEthernetSegmentIdentifier, ['entry'], name, value)


                        class RemoteEthernetSegmentIdentifier(Entity):
                            """
                            Remote Ethernet Segment id
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier, self).__init__()

                                self.yang_name = "remote-ethernet-segment-identifier"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.uint8, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "remote-ethernet-segment-identifier"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/macs/mac/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Macs.Mac.RemoteEthernetSegmentIdentifier, ['entry'], name, value)


                        class PathBuffer(Entity):
                            """
                            Path List Buffer
                            
                            .. attribute:: next_hop
                            
                            	Next\-hop IP address (v6 format)
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: output_label
                            
                            	Output Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: srte_tunnel
                            
                            	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            

                            """

                            _prefix = 'evpn-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer, self).__init__()

                                self.yang_name = "path-buffer"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('next_hop', YLeaf(YType.str, 'next-hop')),
                                    ('output_label', YLeaf(YType.uint32, 'output-label')),
                                    ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                                ])
                                self.next_hop = None
                                self.output_label = None
                                self.srte_tunnel = None
                                self._segment_path = lambda: "path-buffer"
                                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/evi-detail/evi-children/macs/mac/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


        class InternalLabels(Entity):
            """
            EVPN Internal Label Table
            
            .. attribute:: internal_label
            
            	L2VPN EVPN Internal Label
            	**type**\: list of  		 :py:class:`InternalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.InternalLabels.InternalLabel>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Standby.InternalLabels, self).__init__()

                self.yang_name = "internal-labels"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("internal-label", ("internal_label", Evpn.Standby.InternalLabels.InternalLabel))])
                self._leafs = OrderedDict()

                self.internal_label = YList(self)
                self._segment_path = lambda: "internal-labels"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Standby.InternalLabels, [], name, value)


            class InternalLabel(Entity):
                """
                L2VPN EVPN Internal Label
                
                .. attribute:: evi
                
                	EVPN id
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: esi1
                
                	ES id (part 1/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi2
                
                	ES id (part 2/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi3
                
                	ES id (part 3/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi4
                
                	ES id (part 4/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi5
                
                	ES id (part 5/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: ethernet_tag
                
                	Ethernet Tag ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	EVPN id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esi
                
                	Ethernet Segment id
                	**type**\: str
                
                	**pattern:** ([0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2})\*)?
                
                .. attribute:: tag
                
                	Label Tag
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: internal_label
                
                	MPLS Internal Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: encap
                
                	Encap type of remote EAD/ES, EAD/EVI and MAC routes
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: mac_num_paths
                
                	Number of items in the MAC path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ead_num_paths
                
                	Number of items in the ead path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: evi_num_paths
                
                	Number of items in the evi path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sum_num_paths
                
                	Number of items in the sum path buffer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: sum_num_active_paths
                
                	Number of items in the sum path buffer that are Active Paths
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: resolved
                
                	Internal Label has resolved per\-ES EAD and per\-EVI EAD or MAC routes
                	**type**\: bool
                
                .. attribute:: ecmp_disable
                
                	ECMP Disable Per EVI Resolution
                	**type**\: bool
                
                .. attribute:: redundancy_single_active
                
                	Single\-active redundancy configured at remote ES
                	**type**\: bool
                
                .. attribute:: redundancy_single_flow_active
                
                	Single\-flow\-active redundancy at remote ES (MST\-AG)
                	**type**\: bool
                
                .. attribute:: mac_path_buffer
                
                	MAC Path list buffer
                	**type**\: list of  		 :py:class:`MacPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.InternalLabels.InternalLabel.MacPathBuffer>`
                
                .. attribute:: ead_path_buffer
                
                	EAD/ES Path list buffer
                	**type**\: list of  		 :py:class:`EadPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.InternalLabels.InternalLabel.EadPathBuffer>`
                
                .. attribute:: evi_path_buffer
                
                	EAD/EVI Path list buffer
                	**type**\: list of  		 :py:class:`EviPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.InternalLabels.InternalLabel.EviPathBuffer>`
                
                .. attribute:: summary_path_buffer
                
                	Summary Path list buffer
                	**type**\: list of  		 :py:class:`SummaryPathBuffer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.InternalLabels.InternalLabel.SummaryPathBuffer>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Standby.InternalLabels.InternalLabel, self).__init__()

                    self.yang_name = "internal-label"
                    self.yang_parent_name = "internal-labels"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("mac-path-buffer", ("mac_path_buffer", Evpn.Standby.InternalLabels.InternalLabel.MacPathBuffer)), ("ead-path-buffer", ("ead_path_buffer", Evpn.Standby.InternalLabels.InternalLabel.EadPathBuffer)), ("evi-path-buffer", ("evi_path_buffer", Evpn.Standby.InternalLabels.InternalLabel.EviPathBuffer)), ("summary-path-buffer", ("summary_path_buffer", Evpn.Standby.InternalLabels.InternalLabel.SummaryPathBuffer))])
                    self._leafs = OrderedDict([
                        ('evi', YLeaf(YType.int32, 'evi')),
                        ('esi1', YLeaf(YType.str, 'esi1')),
                        ('esi2', YLeaf(YType.str, 'esi2')),
                        ('esi3', YLeaf(YType.str, 'esi3')),
                        ('esi4', YLeaf(YType.str, 'esi4')),
                        ('esi5', YLeaf(YType.str, 'esi5')),
                        ('ethernet_tag', YLeaf(YType.int32, 'ethernet-tag')),
                        ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                        ('esi', YLeaf(YType.str, 'esi')),
                        ('tag', YLeaf(YType.uint32, 'tag')),
                        ('internal_label', YLeaf(YType.uint32, 'internal-label')),
                        ('encap', YLeaf(YType.uint8, 'encap')),
                        ('mac_num_paths', YLeaf(YType.uint32, 'mac-num-paths')),
                        ('ead_num_paths', YLeaf(YType.uint32, 'ead-num-paths')),
                        ('evi_num_paths', YLeaf(YType.uint32, 'evi-num-paths')),
                        ('sum_num_paths', YLeaf(YType.uint32, 'sum-num-paths')),
                        ('sum_num_active_paths', YLeaf(YType.uint32, 'sum-num-active-paths')),
                        ('resolved', YLeaf(YType.boolean, 'resolved')),
                        ('ecmp_disable', YLeaf(YType.boolean, 'ecmp-disable')),
                        ('redundancy_single_active', YLeaf(YType.boolean, 'redundancy-single-active')),
                        ('redundancy_single_flow_active', YLeaf(YType.boolean, 'redundancy-single-flow-active')),
                    ])
                    self.evi = None
                    self.esi1 = None
                    self.esi2 = None
                    self.esi3 = None
                    self.esi4 = None
                    self.esi5 = None
                    self.ethernet_tag = None
                    self.evi_xr = None
                    self.esi = None
                    self.tag = None
                    self.internal_label = None
                    self.encap = None
                    self.mac_num_paths = None
                    self.ead_num_paths = None
                    self.evi_num_paths = None
                    self.sum_num_paths = None
                    self.sum_num_active_paths = None
                    self.resolved = None
                    self.ecmp_disable = None
                    self.redundancy_single_active = None
                    self.redundancy_single_flow_active = None

                    self.mac_path_buffer = YList(self)
                    self.ead_path_buffer = YList(self)
                    self.evi_path_buffer = YList(self)
                    self.summary_path_buffer = YList(self)
                    self._segment_path = lambda: "internal-label"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/internal-labels/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Standby.InternalLabels.InternalLabel, ['evi', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'ethernet_tag', 'evi_xr', 'esi', 'tag', 'internal_label', 'encap', 'mac_num_paths', 'ead_num_paths', 'evi_num_paths', 'sum_num_paths', 'sum_num_active_paths', 'resolved', 'ecmp_disable', 'redundancy_single_active', 'redundancy_single_flow_active'], name, value)


                class MacPathBuffer(Entity):
                    """
                    MAC Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.InternalLabels.InternalLabel.MacPathBuffer, self).__init__()

                        self.yang_name = "mac-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "mac-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.InternalLabels.InternalLabel.MacPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class EadPathBuffer(Entity):
                    """
                    EAD/ES Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.InternalLabels.InternalLabel.EadPathBuffer, self).__init__()

                        self.yang_name = "ead-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "ead-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.InternalLabels.InternalLabel.EadPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class EviPathBuffer(Entity):
                    """
                    EAD/EVI Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.InternalLabels.InternalLabel.EviPathBuffer, self).__init__()

                        self.yang_name = "evi-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "evi-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.InternalLabels.InternalLabel.EviPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


                class SummaryPathBuffer(Entity):
                    """
                    Summary Path list buffer
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: output_label
                    
                    	Output Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srte_tunnel
                    
                    	Segment\-Routing Traffic Engineering Tunnel Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.InternalLabels.InternalLabel.SummaryPathBuffer, self).__init__()

                        self.yang_name = "summary-path-buffer"
                        self.yang_parent_name = "internal-label"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('output_label', YLeaf(YType.uint32, 'output-label')),
                            ('srte_tunnel', YLeaf(YType.str, 'srte-tunnel')),
                        ])
                        self.next_hop = None
                        self.output_label = None
                        self.srte_tunnel = None
                        self._segment_path = lambda: "summary-path-buffer"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/internal-labels/internal-label/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.InternalLabels.InternalLabel.SummaryPathBuffer, ['next_hop', 'output_label', 'srte_tunnel'], name, value)


        class EthernetSegments(Entity):
            """
            EVPN Ethernet\-Segment Table
            
            .. attribute:: ethernet_segment
            
            	EVPN Ethernet\-Segment Entry
            	**type**\: list of  		 :py:class:`EthernetSegment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Standby.EthernetSegments, self).__init__()

                self.yang_name = "ethernet-segments"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("ethernet-segment", ("ethernet_segment", Evpn.Standby.EthernetSegments.EthernetSegment))])
                self._leafs = OrderedDict()

                self.ethernet_segment = YList(self)
                self._segment_path = lambda: "ethernet-segments"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Standby.EthernetSegments, [], name, value)


            class EthernetSegment(Entity):
                """
                EVPN Ethernet\-Segment Entry
                
                .. attribute:: interface_name
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: esi1
                
                	ES id (part 1/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi2
                
                	ES id (part 2/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi3
                
                	ES id (part 3/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi4
                
                	ES id (part 4/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi5
                
                	ES id (part 5/5)
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: esi_type
                
                	ESI Type
                	**type**\:  :py:class:`L2vpnEvpnEsi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnEsi>`
                
                .. attribute:: esi_system_identifier
                
                	ESI System Identifier
                	**type**\: str
                
                .. attribute:: esi_port_key
                
                	ESI Port Key
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: esi_system_priority
                
                	ESI System Priority
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_segment_name
                
                	Ethernet Segment Name
                	**type**\: str
                
                .. attribute:: ethernet_segment_state
                
                	State of the ethernet segment
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: if_handle
                
                	Main port ifhandle
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
                .. attribute:: main_port_role
                
                	Main port redundancy group role
                	**type**\:  :py:class:`L2vpnRgRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnRgRole>`
                
                .. attribute:: main_port_mac
                
                	Main Port MAC Address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: num_up_p_ws
                
                	Number of PWs in Up state
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: route_target
                
                	ES\-Import Route Target
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: rt_origin
                
                	Origin of operational ES\-Import RT
                	**type**\:  :py:class:`L2vpnEvpnRtOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnRtOrigin>`
                
                .. attribute:: es_bgp_gates
                
                	ES BGP Gates
                	**type**\: str
                
                .. attribute:: es_l2fib_gates
                
                	ES L2FIB Gates
                	**type**\: str
                
                .. attribute:: mac_flushing_mode_config
                
                	Configured MAC Flushing mode
                	**type**\:  :py:class:`L2vpnEvpnMfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnMfMode>`
                
                .. attribute:: load_balance_mode_config
                
                	Configured load balancing mode
                	**type**\:  :py:class:`L2vpnEvpnLbMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnLbMode>`
                
                .. attribute:: load_balance_mode_is_default
                
                	Load balancing mode is default
                	**type**\: bool
                
                .. attribute:: load_balance_mode_oper
                
                	Operational load balancing mode
                	**type**\:  :py:class:`L2vpnEvpnLbMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnLbMode>`
                
                .. attribute:: force_single_home
                
                	Ethernet\-Segment forced to single home
                	**type**\: bool
                
                .. attribute:: source_mac_oper
                
                	Operational Source MAC address
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: source_mac_origin
                
                	Origin of operational source MAC address
                	**type**\:  :py:class:`L2vpnEvpnSmacSrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnSmacSrc>`
                
                .. attribute:: peering_timer
                
                	Configured timer for triggering DF election (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: peering_timer_left
                
                	Milliseconds left on DF election timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: recovery_timer
                
                	Configured timer for (STP) recovery (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: recovery_timer_left
                
                	Milliseconds left on (STP) recovery timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: carving_timer
                
                	Configured timer for delaying DF election (seconds)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: second
                
                .. attribute:: carving_timer_left
                
                	Milliseconds left on carving timer
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: millisecond
                
                .. attribute:: service_carving_mode
                
                	Service carving mode
                	**type**\:  :py:class:`L2vpnEvpnScMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpnScMode>`
                
                .. attribute:: primary_services_input
                
                	Input string of Primary services ESI/I\-SIDs
                	**type**\: str
                
                .. attribute:: secondary_services_input
                
                	Input string of Secondary services ESI/I\-SIDs
                	**type**\: str
                
                .. attribute:: forwarder_ports
                
                	Count of Forwarders (AC, AC PW, VFI PW)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: permanent_forwarder_ports
                
                	Count of Forwarders with permanent service
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: elected_forwarder_ports
                
                	Count of Forwarders with elected service
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_elected_forwarder_ports
                
                	Count of Forwarders with not elected service
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: not_config_forwarder_ports
                
                	Count of forwarders with missing config detected
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: mp_protected
                
                	MP is protected and not under EVPN control
                	**type**\: bool
                
                .. attribute:: nve_anycast_vtep
                
                	Anycast VTEP mode on NVE main\-interface
                	**type**\: bool
                
                .. attribute:: nve_ingress_replication
                
                	Ingress\-Replication is configured on NVE main\-interface
                	**type**\: bool
                
                .. attribute:: local_split_horizon_group_label_valid
                
                	Local split horizon group label is valid
                	**type**\: bool
                
                .. attribute:: local_split_horizon_group_label
                
                	Local split horizon group label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: ethernet_segment_identifier
                
                	Ethernet Segment id
                	**type**\: list of  		 :py:class:`EthernetSegmentIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier>`
                
                .. attribute:: primary_service
                
                	List of Primary services ESI/I\-SIDs
                	**type**\: list of  		 :py:class:`PrimaryService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.PrimaryService>`
                
                .. attribute:: secondary_service
                
                	List of Secondary services ESI/I\-SIDs
                	**type**\: list of  		 :py:class:`SecondaryService <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.SecondaryService>`
                
                .. attribute:: service_carving_i_sidelected_result
                
                	Elected ISID service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingISidelectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult>`
                
                .. attribute:: service_carving_isid_not_elected_result
                
                	Not elected ISID service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingIsidNotElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult>`
                
                .. attribute:: service_carving_evi_elected_result
                
                	Elected EVI service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingEviElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult>`
                
                .. attribute:: service_carving_evi_not_elected_result
                
                	Not elected EVI service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingEviNotElectedResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult>`
                
                .. attribute:: next_hop
                
                	List of nexthop IPv6 addresses
                	**type**\: list of  		 :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.NextHop>`
                
                .. attribute:: service_carving_vpws_permanent_result
                
                	Permanent EVPN VPWS service carving results
                	**type**\: list of  		 :py:class:`ServiceCarvingVpwsPermanentResult <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult>`
                
                .. attribute:: remote_split_horizon_group_label
                
                	Remote split horizon group labels
                	**type**\: list of  		 :py:class:`RemoteSplitHorizonGroupLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel>`
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Standby.EthernetSegments.EthernetSegment, self).__init__()

                    self.yang_name = "ethernet-segment"
                    self.yang_parent_name = "ethernet-segments"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ethernet-segment-identifier", ("ethernet_segment_identifier", Evpn.Standby.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier)), ("primary-service", ("primary_service", Evpn.Standby.EthernetSegments.EthernetSegment.PrimaryService)), ("secondary-service", ("secondary_service", Evpn.Standby.EthernetSegments.EthernetSegment.SecondaryService)), ("service-carving-i-sidelected-result", ("service_carving_i_sidelected_result", Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult)), ("service-carving-isid-not-elected-result", ("service_carving_isid_not_elected_result", Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult)), ("service-carving-evi-elected-result", ("service_carving_evi_elected_result", Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult)), ("service-carving-evi-not-elected-result", ("service_carving_evi_not_elected_result", Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult)), ("next-hop", ("next_hop", Evpn.Standby.EthernetSegments.EthernetSegment.NextHop)), ("service-carving-vpws-permanent-result", ("service_carving_vpws_permanent_result", Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult)), ("remote-split-horizon-group-label", ("remote_split_horizon_group_label", Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel))])
                    self._leafs = OrderedDict([
                        ('interface_name', YLeaf(YType.str, 'interface-name')),
                        ('esi1', YLeaf(YType.str, 'esi1')),
                        ('esi2', YLeaf(YType.str, 'esi2')),
                        ('esi3', YLeaf(YType.str, 'esi3')),
                        ('esi4', YLeaf(YType.str, 'esi4')),
                        ('esi5', YLeaf(YType.str, 'esi5')),
                        ('esi_type', YLeaf(YType.enumeration, 'esi-type')),
                        ('esi_system_identifier', YLeaf(YType.str, 'esi-system-identifier')),
                        ('esi_port_key', YLeaf(YType.uint32, 'esi-port-key')),
                        ('esi_system_priority', YLeaf(YType.uint32, 'esi-system-priority')),
                        ('ethernet_segment_name', YLeaf(YType.str, 'ethernet-segment-name')),
                        ('ethernet_segment_state', YLeaf(YType.uint32, 'ethernet-segment-state')),
                        ('if_handle', YLeaf(YType.str, 'if-handle')),
                        ('main_port_role', YLeaf(YType.enumeration, 'main-port-role')),
                        ('main_port_mac', YLeaf(YType.str, 'main-port-mac')),
                        ('num_up_p_ws', YLeaf(YType.uint32, 'num-up-p-ws')),
                        ('route_target', YLeaf(YType.str, 'route-target')),
                        ('rt_origin', YLeaf(YType.enumeration, 'rt-origin')),
                        ('es_bgp_gates', YLeaf(YType.str, 'es-bgp-gates')),
                        ('es_l2fib_gates', YLeaf(YType.str, 'es-l2fib-gates')),
                        ('mac_flushing_mode_config', YLeaf(YType.enumeration, 'mac-flushing-mode-config')),
                        ('load_balance_mode_config', YLeaf(YType.enumeration, 'load-balance-mode-config')),
                        ('load_balance_mode_is_default', YLeaf(YType.boolean, 'load-balance-mode-is-default')),
                        ('load_balance_mode_oper', YLeaf(YType.enumeration, 'load-balance-mode-oper')),
                        ('force_single_home', YLeaf(YType.boolean, 'force-single-home')),
                        ('source_mac_oper', YLeaf(YType.str, 'source-mac-oper')),
                        ('source_mac_origin', YLeaf(YType.enumeration, 'source-mac-origin')),
                        ('peering_timer', YLeaf(YType.uint32, 'peering-timer')),
                        ('peering_timer_left', YLeaf(YType.uint32, 'peering-timer-left')),
                        ('recovery_timer', YLeaf(YType.uint32, 'recovery-timer')),
                        ('recovery_timer_left', YLeaf(YType.uint32, 'recovery-timer-left')),
                        ('carving_timer', YLeaf(YType.uint32, 'carving-timer')),
                        ('carving_timer_left', YLeaf(YType.uint32, 'carving-timer-left')),
                        ('service_carving_mode', YLeaf(YType.enumeration, 'service-carving-mode')),
                        ('primary_services_input', YLeaf(YType.str, 'primary-services-input')),
                        ('secondary_services_input', YLeaf(YType.str, 'secondary-services-input')),
                        ('forwarder_ports', YLeaf(YType.uint32, 'forwarder-ports')),
                        ('permanent_forwarder_ports', YLeaf(YType.uint32, 'permanent-forwarder-ports')),
                        ('elected_forwarder_ports', YLeaf(YType.uint32, 'elected-forwarder-ports')),
                        ('not_elected_forwarder_ports', YLeaf(YType.uint32, 'not-elected-forwarder-ports')),
                        ('not_config_forwarder_ports', YLeaf(YType.uint32, 'not-config-forwarder-ports')),
                        ('mp_protected', YLeaf(YType.boolean, 'mp-protected')),
                        ('nve_anycast_vtep', YLeaf(YType.boolean, 'nve-anycast-vtep')),
                        ('nve_ingress_replication', YLeaf(YType.boolean, 'nve-ingress-replication')),
                        ('local_split_horizon_group_label_valid', YLeaf(YType.boolean, 'local-split-horizon-group-label-valid')),
                        ('local_split_horizon_group_label', YLeaf(YType.uint32, 'local-split-horizon-group-label')),
                    ])
                    self.interface_name = None
                    self.esi1 = None
                    self.esi2 = None
                    self.esi3 = None
                    self.esi4 = None
                    self.esi5 = None
                    self.esi_type = None
                    self.esi_system_identifier = None
                    self.esi_port_key = None
                    self.esi_system_priority = None
                    self.ethernet_segment_name = None
                    self.ethernet_segment_state = None
                    self.if_handle = None
                    self.main_port_role = None
                    self.main_port_mac = None
                    self.num_up_p_ws = None
                    self.route_target = None
                    self.rt_origin = None
                    self.es_bgp_gates = None
                    self.es_l2fib_gates = None
                    self.mac_flushing_mode_config = None
                    self.load_balance_mode_config = None
                    self.load_balance_mode_is_default = None
                    self.load_balance_mode_oper = None
                    self.force_single_home = None
                    self.source_mac_oper = None
                    self.source_mac_origin = None
                    self.peering_timer = None
                    self.peering_timer_left = None
                    self.recovery_timer = None
                    self.recovery_timer_left = None
                    self.carving_timer = None
                    self.carving_timer_left = None
                    self.service_carving_mode = None
                    self.primary_services_input = None
                    self.secondary_services_input = None
                    self.forwarder_ports = None
                    self.permanent_forwarder_ports = None
                    self.elected_forwarder_ports = None
                    self.not_elected_forwarder_ports = None
                    self.not_config_forwarder_ports = None
                    self.mp_protected = None
                    self.nve_anycast_vtep = None
                    self.nve_ingress_replication = None
                    self.local_split_horizon_group_label_valid = None
                    self.local_split_horizon_group_label = None

                    self.ethernet_segment_identifier = YList(self)
                    self.primary_service = YList(self)
                    self.secondary_service = YList(self)
                    self.service_carving_i_sidelected_result = YList(self)
                    self.service_carving_isid_not_elected_result = YList(self)
                    self.service_carving_evi_elected_result = YList(self)
                    self.service_carving_evi_not_elected_result = YList(self)
                    self.next_hop = YList(self)
                    self.service_carving_vpws_permanent_result = YList(self)
                    self.remote_split_horizon_group_label = YList(self)
                    self._segment_path = lambda: "ethernet-segment"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment, ['interface_name', 'esi1', 'esi2', 'esi3', 'esi4', 'esi5', 'esi_type', 'esi_system_identifier', 'esi_port_key', 'esi_system_priority', 'ethernet_segment_name', 'ethernet_segment_state', 'if_handle', 'main_port_role', 'main_port_mac', 'num_up_p_ws', 'route_target', 'rt_origin', 'es_bgp_gates', 'es_l2fib_gates', 'mac_flushing_mode_config', 'load_balance_mode_config', 'load_balance_mode_is_default', 'load_balance_mode_oper', 'force_single_home', 'source_mac_oper', 'source_mac_origin', 'peering_timer', 'peering_timer_left', 'recovery_timer', 'recovery_timer_left', 'carving_timer', 'carving_timer_left', 'service_carving_mode', 'primary_services_input', 'secondary_services_input', 'forwarder_ports', 'permanent_forwarder_ports', 'elected_forwarder_ports', 'not_elected_forwarder_ports', 'not_config_forwarder_ports', 'mp_protected', 'nve_anycast_vtep', 'nve_ingress_replication', 'local_split_horizon_group_label_valid', 'local_split_horizon_group_label'], name, value)


                class EthernetSegmentIdentifier(Entity):
                    """
                    Ethernet Segment id
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier, self).__init__()

                        self.yang_name = "ethernet-segment-identifier"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint8, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "ethernet-segment-identifier"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.EthernetSegmentIdentifier, ['entry'], name, value)


                class PrimaryService(Entity):
                    """
                    List of Primary services ESI/I\-SIDs
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.PrimaryService, self).__init__()

                        self.yang_name = "primary-service"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "primary-service"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.PrimaryService, ['entry'], name, value)


                class SecondaryService(Entity):
                    """
                    List of Secondary services ESI/I\-SIDs
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.SecondaryService, self).__init__()

                        self.yang_name = "secondary-service"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "secondary-service"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.SecondaryService, ['entry'], name, value)


                class ServiceCarvingISidelectedResult(Entity):
                    """
                    Elected ISID service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult, self).__init__()

                        self.yang_name = "service-carving-i-sidelected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-i-sidelected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingISidelectedResult, ['entry'], name, value)


                class ServiceCarvingIsidNotElectedResult(Entity):
                    """
                    Not elected ISID service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult, self).__init__()

                        self.yang_name = "service-carving-isid-not-elected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-isid-not-elected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingIsidNotElectedResult, ['entry'], name, value)


                class ServiceCarvingEviElectedResult(Entity):
                    """
                    Elected EVI service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult, self).__init__()

                        self.yang_name = "service-carving-evi-elected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-evi-elected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviElectedResult, ['entry'], name, value)


                class ServiceCarvingEviNotElectedResult(Entity):
                    """
                    Not elected EVI service carving results
                    
                    .. attribute:: entry
                    
                    	
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult, self).__init__()

                        self.yang_name = "service-carving-evi-not-elected-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('entry', YLeaf(YType.uint32, 'entry')),
                        ])
                        self.entry = None
                        self._segment_path = lambda: "service-carving-evi-not-elected-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingEviNotElectedResult, ['entry'], name, value)


                class NextHop(Entity):
                    """
                    List of nexthop IPv6 addresses
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.NextHop, self).__init__()

                        self.yang_name = "next-hop"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                        ])
                        self.next_hop = None
                        self._segment_path = lambda: "next-hop"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.NextHop, ['next_hop'], name, value)


                class ServiceCarvingVpwsPermanentResult(Entity):
                    """
                    Permanent EVPN VPWS service carving results
                    
                    .. attribute:: vpn_id
                    
                    	VPN ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: type
                    
                    	Service Type
                    	**type**\:  :py:class:`L2vpnEvpn <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.L2vpnEvpn>`
                    
                    .. attribute:: ethernet_tag
                    
                    	Ethernet Tag
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult, self).__init__()

                        self.yang_name = "service-carving-vpws-permanent-result"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vpn_id', YLeaf(YType.uint32, 'vpn-id')),
                            ('type', YLeaf(YType.enumeration, 'type')),
                            ('ethernet_tag', YLeaf(YType.uint32, 'ethernet-tag')),
                        ])
                        self.vpn_id = None
                        self.type = None
                        self.ethernet_tag = None
                        self._segment_path = lambda: "service-carving-vpws-permanent-result"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.ServiceCarvingVpwsPermanentResult, ['vpn_id', 'type', 'ethernet_tag'], name, value)


                class RemoteSplitHorizonGroupLabel(Entity):
                    """
                    Remote split horizon group labels
                    
                    .. attribute:: next_hop
                    
                    	Next\-hop IP address (v6 format)
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: label
                    
                    	Split horizon label associated with next\-hop address
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'evpn-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel, self).__init__()

                        self.yang_name = "remote-split-horizon-group-label"
                        self.yang_parent_name = "ethernet-segment"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('next_hop', YLeaf(YType.str, 'next-hop')),
                            ('label', YLeaf(YType.uint32, 'label')),
                        ])
                        self.next_hop = None
                        self.label = None
                        self._segment_path = lambda: "remote-split-horizon-group-label"
                        self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ethernet-segments/ethernet-segment/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel, ['next_hop', 'label'], name, value)


        class AcIds(Entity):
            """
            EVPN AC ID table
            
            .. attribute:: ac_id
            
            	EVPN AC ID table
            	**type**\: list of  		 :py:class:`AcId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper.Evpn.Standby.AcIds.AcId>`
            
            

            """

            _prefix = 'evpn-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(Evpn.Standby.AcIds, self).__init__()

                self.yang_name = "ac-ids"
                self.yang_parent_name = "standby"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("ac-id", ("ac_id", Evpn.Standby.AcIds.AcId))])
                self._leafs = OrderedDict()

                self.ac_id = YList(self)
                self._segment_path = lambda: "ac-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Evpn.Standby.AcIds, [], name, value)


            class AcId(Entity):
                """
                EVPN AC ID table
                
                .. attribute:: evi
                
                	EVPN id
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: ac_id
                
                	AC ID
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: evi_xr
                
                	E\-VPN id
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: neighbor
                
                	Neighbor IP
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'evpn-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(Evpn.Standby.AcIds.AcId, self).__init__()

                    self.yang_name = "ac-id"
                    self.yang_parent_name = "ac-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('evi', YLeaf(YType.int32, 'evi')),
                        ('ac_id', YLeaf(YType.int32, 'ac-id')),
                        ('evi_xr', YLeaf(YType.uint32, 'evi-xr')),
                        ('neighbor', YLeaf(YType.str, 'neighbor')),
                    ])
                    self.evi = None
                    self.ac_id = None
                    self.evi_xr = None
                    self.neighbor = None
                    self._segment_path = lambda: "ac-id"
                    self._absolute_path = lambda: "Cisco-IOS-XR-evpn-oper:evpn/standby/ac-ids/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Evpn.Standby.AcIds.AcId, ['evi', 'ac_id', 'evi_xr', 'neighbor'], name, value)

    def clone_ptr(self):
        self._top_entity = Evpn()
        return self._top_entity

