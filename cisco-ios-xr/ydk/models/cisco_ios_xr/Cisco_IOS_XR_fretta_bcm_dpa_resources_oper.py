""" Cisco_IOS_XR_fretta_bcm_dpa_resources_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-resources package operational data.

This module contains definitions
for the following management objects\:
  dpa\: Stats Data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DpaTable(Enum):
    """
    DpaTable (Enum Class)

    Dpa table

    .. data:: test_if = 0

    	test if

    .. data:: test_nhg = 1

    	test nhg

    .. data:: test_nh = 2

    	test nh

    .. data:: test_rt = 3

    	test rt

    .. data:: test_dynhg = 4

    	testdynhg

    .. data:: test_ip_punt_policy = 5

    	test ippuntpolicy

    .. data:: test_punt = 6

    	test punt

    .. data:: test_punt_policy_stats = 7

    	testpuntpolicystats

    .. data:: test_async_update = 8

    	testasyncupdate

    .. data:: test_ddel_q = 9

    	test ddel q

    .. data:: bdbvi = 10

    	bdbvi

    .. data:: sys = 11

    	sys

    .. data:: npu = 12

    	npu

    .. data:: npuhwid = 13

    	npuhwid

    .. data:: l1_port = 14

    	l1port

    .. data:: l2_port = 15

    	l2port

    .. data:: l2intf = 16

    	l2intf

    .. data:: mplspwe_port_o_list = 17

    	mplspweport olist

    .. data:: mplspwe_port = 18

    	mplspweport

    .. data:: mhpwe_port = 19

    	mhpweport

    .. data:: l2xc = 20

    	l2xc

    .. data:: l2vpnstats = 21

    	l2vpnstats

    .. data:: l1_ports_tats = 22

    	l1portstats

    .. data:: l3intf = 23

    	l3intf

    .. data:: l3intfrxstats = 24

    	l3intfrxstats

    .. data:: ip_route = 25

    	iproute

    .. data:: ip6_route = 26

    	ip6route

    .. data:: punt_policy_stats = 27

    	puntpolicystats

    .. data:: tep = 28

    	tep

    .. data:: ip_punt_policy = 29

    	ippuntpolicy

    .. data:: ip6_punt_policy = 30

    	ip6puntpolicy

    .. data:: isis_punt_policy = 31

    	isispuntpolicy

    .. data:: ipnh_group = 32

    	ipnhgroup

    .. data:: ip6nh_group = 33

    	ip6nhgroup

    .. data:: ipnh = 34

    	ipnh

    .. data:: ip6nh = 35

    	ip6nh

    .. data:: ipvrf = 36

    	ipvrf

    .. data:: mplsnh = 37

    	mplsnh

    .. data:: mpls_label = 38

    	mplslabel

    .. data:: dnx_trap = 39

    	dnx trap

    .. data:: punt = 40

    	punt

    .. data:: punt_police_r = 41

    	puntpolicer

    .. data:: punt_lpts_police_r = 42

    	puntlptspolicer

    .. data:: punt_stats = 43

    	puntstats

    .. data:: tm_port = 44

    	tmport

    .. data:: span_session = 45

    	spansession

    .. data:: police_rstats = 46

    	policerstats

    .. data:: tm_ports_tats = 47

    	tmportstats

    .. data:: l3intftxstats = 48

    	l3intftxstats

    .. data:: mplstetxstats = 49

    	mplstetxstats

    .. data:: mplslblstats = 50

    	mplslblstats

    .. data:: police_r = 51

    	policer

    .. data:: l2intfrxstats = 52

    	l2intfrxstats

    .. data:: l2intftxstats = 53

    	l2intftxstats

    .. data:: dnx_pbr_tt_ipv4 = 54

    	dnx pbr tt ipv4

    .. data:: dnx_pbr_tt_ipv6 = 55

    	dnx pbr tt ipv6

    .. data:: bfdhwoff = 56

    	bfdhwoff

    .. data:: global_ = 57

    	global

    .. data:: lag_port = 58

    	lagport

    .. data:: qos_profile = 59

    	qosprofile

    .. data:: tmrate_profile = 60

    	tmrateprofile

    .. data:: dnx_port_range = 61

    	dnx port range

    .. data:: ipacl = 62

    	ipacl

    .. data:: ip6acl = 63

    	ip6acl

    .. data:: sched_tree = 64

    	schedtree

    .. data:: tmcos = 65

    	tmcos

    .. data:: statsagg = 66

    	statsagg

    .. data:: nhprotect = 67

    	nhprotect

    .. data:: sampler = 68

    	sampler

    .. data:: l2qos = 69

    	l2qos

    .. data:: peer_qos = 70

    	peerqos

    .. data:: ipqos = 71

    	ipqos

    .. data:: ip6qos = 72

    	ip6qos

    .. data:: mplsqos = 73

    	mplsqos

    .. data:: qosid = 74

    	qosid

    .. data:: extlif = 75

    	extlif

    .. data:: elif_ = 76

    	elif

    .. data:: ingaclstats = 77

    	ingaclstats

    .. data:: egraclstats = 78

    	egraclstats

    .. data:: edpl = 79

    	edpl

    .. data:: erp = 80

    	erp

    .. data:: cfmmaid = 81

    	cfmmaid

    .. data:: cfmdefmps = 82

    	cfmdefmps

    .. data:: cfmofflmep = 83

    	cfmofflmep

    .. data:: cfmoffrmep = 84

    	cfmoffrmep

    .. data:: cfmnonoff = 85

    	cfmnonoff

    .. data:: cfmhwoffrxstats = 86

    	cfmhwoffrxstats

    .. data:: ipmc_route = 87

    	ipmcroute

    .. data:: l2ipmc_route = 88

    	l2ipmcroute

    .. data:: ipmco_list = 89

    	ipmcolist

    .. data:: l2mco_list = 90

    	l2mcolist

    .. data:: ipmc_merge_do_list = 91

    	ipmcmergedolist

    .. data:: sgfgid_list = 92

    	sgfgidlist

    .. data:: meshmc = 93

    	meshmc

    .. data:: l2_bridge = 94

    	l2bridge

    .. data:: l2_bridge_port = 95

    	l2bridgeport

    .. data:: l2_bridge_vni = 96

    	l2bridgevni

    .. data:: l2_bridge_vnidecap = 97

    	l2bridgevnidecap

    .. data:: l2_bridge_mac = 98

    	l2bridgemac

    .. data:: l2brmac = 99

    	l2brmac

    .. data:: ip_tunnel_decap = 100

    	iptunneldecap

    .. data:: l2vlan_range = 101

    	l2vlanrange

    .. data:: ip_tunnel_encap = 102

    	iptunnelencap

    .. data:: rawget = 103

    	rawget

    .. data:: ip6mc_route = 104

    	ip6mcroute

    .. data:: l2evpnact_remote_peer_id = 105

    	l2evpnactremotepeerid

    .. data:: l2evpnact_local_shl = 106

    	l2evpnactlocalshl

    .. data:: l2evpnact_remote_shl = 107

    	l2evpnactremoteshl

    .. data:: evpn_iml_range = 108

    	evpn imlrange

    .. data:: l2_bridge_o_list = 109

    	l2bridgeolist

    .. data:: l2_bridge_vnio_list = 110

    	l2bridgevniolist

    .. data:: l2acl = 111

    	l2acl

    .. data:: l2evpn_nh = 112

    	l2evpn nh

    .. data:: l2_bridge_port_sc = 113

    	l2bridgeport sc

    .. data:: l3intfmctxstats = 114

    	l3intfmctxstats

    .. data:: tidl_sample = 115

    	tidl sample

    .. data:: tidl_ref_sample = 116

    	tidl ref sample

    .. data:: ipacl_prefix = 117

    	ipaclprefix

    .. data:: ip6acl_prefix = 118

    	ip6aclprefix

    .. data:: ipacl_port = 119

    	ipaclport

    .. data:: scaleacl = 120

    	scaleacl

    .. data:: ipmcf_hop = 121

    	ipmcfhop

    .. data:: bundle_swoff = 122

    	bundle swoff

    .. data:: mcidswoff = 123

    	mcidswoff

    .. data:: dest_map = 124

    	destmap

    .. data:: l2_bridge_port_pw = 125

    	l2bridgeport pw

    .. data:: l2evpnact_local_shlstats = 126

    	l2evpnactlocalshlstats

    .. data:: test_hidden = 127

    	testhidden

    .. data:: test_local = 128

    	testlocal

    .. data:: test_repeated = 129

    	testrepeated

    .. data:: limd = 130

    	limd

    .. data:: litap = 131

    	litap

    .. data:: l3intf_proto_stats = 132

    	l3intfprotostats

    .. data:: srv6sid = 133

    	srv6sid

    .. data:: srv6nh = 134

    	srv6nh

    .. data:: redirect_vrf = 135

    	redirectvrf

    .. data:: test_xtf = 136

    	test xtf

    .. data:: ippbr = 137

    	ippbr

    .. data:: ippbrstats = 138

    	ippbrstats

    .. data:: l2_bridge_port_remote_lc = 139

    	l2bridgeport remote lc

    .. data:: mpls_mdt_bud = 140

    	mplsmdtbud

    .. data:: l2mac_static = 141

    	l2macstatic

    .. data:: sr_label_rxstats = 142

    	srlabelrxstats

    .. data:: l2vpnxid = 143

    	l2vpnxid

    .. data:: rpfif = 144

    	rpfif

    """

    test_if = Enum.YLeaf(0, "test-if")

    test_nhg = Enum.YLeaf(1, "test-nhg")

    test_nh = Enum.YLeaf(2, "test-nh")

    test_rt = Enum.YLeaf(3, "test-rt")

    test_dynhg = Enum.YLeaf(4, "test-dynhg")

    test_ip_punt_policy = Enum.YLeaf(5, "test-ip-punt-policy")

    test_punt = Enum.YLeaf(6, "test-punt")

    test_punt_policy_stats = Enum.YLeaf(7, "test-punt-policy-stats")

    test_async_update = Enum.YLeaf(8, "test-async-update")

    test_ddel_q = Enum.YLeaf(9, "test-ddel-q")

    bdbvi = Enum.YLeaf(10, "bdbvi")

    sys = Enum.YLeaf(11, "sys")

    npu = Enum.YLeaf(12, "npu")

    npuhwid = Enum.YLeaf(13, "npuhwid")

    l1_port = Enum.YLeaf(14, "l1-port")

    l2_port = Enum.YLeaf(15, "l2-port")

    l2intf = Enum.YLeaf(16, "l2intf")

    mplspwe_port_o_list = Enum.YLeaf(17, "mplspwe-port-o-list")

    mplspwe_port = Enum.YLeaf(18, "mplspwe-port")

    mhpwe_port = Enum.YLeaf(19, "mhpwe-port")

    l2xc = Enum.YLeaf(20, "l2xc")

    l2vpnstats = Enum.YLeaf(21, "l2vpnstats")

    l1_ports_tats = Enum.YLeaf(22, "l1-ports-tats")

    l3intf = Enum.YLeaf(23, "l3intf")

    l3intfrxstats = Enum.YLeaf(24, "l3intfrxstats")

    ip_route = Enum.YLeaf(25, "ip-route")

    ip6_route = Enum.YLeaf(26, "ip6-route")

    punt_policy_stats = Enum.YLeaf(27, "punt-policy-stats")

    tep = Enum.YLeaf(28, "tep")

    ip_punt_policy = Enum.YLeaf(29, "ip-punt-policy")

    ip6_punt_policy = Enum.YLeaf(30, "ip6-punt-policy")

    isis_punt_policy = Enum.YLeaf(31, "isis-punt-policy")

    ipnh_group = Enum.YLeaf(32, "ipnh-group")

    ip6nh_group = Enum.YLeaf(33, "ip6nh-group")

    ipnh = Enum.YLeaf(34, "ipnh")

    ip6nh = Enum.YLeaf(35, "ip6nh")

    ipvrf = Enum.YLeaf(36, "ipvrf")

    mplsnh = Enum.YLeaf(37, "mplsnh")

    mpls_label = Enum.YLeaf(38, "mpls-label")

    dnx_trap = Enum.YLeaf(39, "dnx-trap")

    punt = Enum.YLeaf(40, "punt")

    punt_police_r = Enum.YLeaf(41, "punt-police-r")

    punt_lpts_police_r = Enum.YLeaf(42, "punt-lpts-police-r")

    punt_stats = Enum.YLeaf(43, "punt-stats")

    tm_port = Enum.YLeaf(44, "tm-port")

    span_session = Enum.YLeaf(45, "span-session")

    police_rstats = Enum.YLeaf(46, "police-rstats")

    tm_ports_tats = Enum.YLeaf(47, "tm-ports-tats")

    l3intftxstats = Enum.YLeaf(48, "l3intftxstats")

    mplstetxstats = Enum.YLeaf(49, "mplstetxstats")

    mplslblstats = Enum.YLeaf(50, "mplslblstats")

    police_r = Enum.YLeaf(51, "police-r")

    l2intfrxstats = Enum.YLeaf(52, "l2intfrxstats")

    l2intftxstats = Enum.YLeaf(53, "l2intftxstats")

    dnx_pbr_tt_ipv4 = Enum.YLeaf(54, "dnx-pbr-tt-ipv4")

    dnx_pbr_tt_ipv6 = Enum.YLeaf(55, "dnx-pbr-tt-ipv6")

    bfdhwoff = Enum.YLeaf(56, "bfdhwoff")

    global_ = Enum.YLeaf(57, "global")

    lag_port = Enum.YLeaf(58, "lag-port")

    qos_profile = Enum.YLeaf(59, "qos-profile")

    tmrate_profile = Enum.YLeaf(60, "tmrate-profile")

    dnx_port_range = Enum.YLeaf(61, "dnx-port-range")

    ipacl = Enum.YLeaf(62, "ipacl")

    ip6acl = Enum.YLeaf(63, "ip6acl")

    sched_tree = Enum.YLeaf(64, "sched-tree")

    tmcos = Enum.YLeaf(65, "tmcos")

    statsagg = Enum.YLeaf(66, "statsagg")

    nhprotect = Enum.YLeaf(67, "nhprotect")

    sampler = Enum.YLeaf(68, "sampler")

    l2qos = Enum.YLeaf(69, "l2qos")

    peer_qos = Enum.YLeaf(70, "peer-qos")

    ipqos = Enum.YLeaf(71, "ipqos")

    ip6qos = Enum.YLeaf(72, "ip6qos")

    mplsqos = Enum.YLeaf(73, "mplsqos")

    qosid = Enum.YLeaf(74, "qosid")

    extlif = Enum.YLeaf(75, "extlif")

    elif_ = Enum.YLeaf(76, "elif")

    ingaclstats = Enum.YLeaf(77, "ingaclstats")

    egraclstats = Enum.YLeaf(78, "egraclstats")

    edpl = Enum.YLeaf(79, "edpl")

    erp = Enum.YLeaf(80, "erp")

    cfmmaid = Enum.YLeaf(81, "cfmmaid")

    cfmdefmps = Enum.YLeaf(82, "cfmdefmps")

    cfmofflmep = Enum.YLeaf(83, "cfmofflmep")

    cfmoffrmep = Enum.YLeaf(84, "cfmoffrmep")

    cfmnonoff = Enum.YLeaf(85, "cfmnonoff")

    cfmhwoffrxstats = Enum.YLeaf(86, "cfmhwoffrxstats")

    ipmc_route = Enum.YLeaf(87, "ipmc-route")

    l2ipmc_route = Enum.YLeaf(88, "l2ipmc-route")

    ipmco_list = Enum.YLeaf(89, "ipmco-list")

    l2mco_list = Enum.YLeaf(90, "l2mco-list")

    ipmc_merge_do_list = Enum.YLeaf(91, "ipmc-merge-do-list")

    sgfgid_list = Enum.YLeaf(92, "sgfgid-list")

    meshmc = Enum.YLeaf(93, "meshmc")

    l2_bridge = Enum.YLeaf(94, "l2-bridge")

    l2_bridge_port = Enum.YLeaf(95, "l2-bridge-port")

    l2_bridge_vni = Enum.YLeaf(96, "l2-bridge-vni")

    l2_bridge_vnidecap = Enum.YLeaf(97, "l2-bridge-vnidecap")

    l2_bridge_mac = Enum.YLeaf(98, "l2-bridge-mac")

    l2brmac = Enum.YLeaf(99, "l2brmac")

    ip_tunnel_decap = Enum.YLeaf(100, "ip-tunnel-decap")

    l2vlan_range = Enum.YLeaf(101, "l2vlan-range")

    ip_tunnel_encap = Enum.YLeaf(102, "ip-tunnel-encap")

    rawget = Enum.YLeaf(103, "rawget")

    ip6mc_route = Enum.YLeaf(104, "ip6mc-route")

    l2evpnact_remote_peer_id = Enum.YLeaf(105, "l2evpnact-remote-peer-id")

    l2evpnact_local_shl = Enum.YLeaf(106, "l2evpnact-local-shl")

    l2evpnact_remote_shl = Enum.YLeaf(107, "l2evpnact-remote-shl")

    evpn_iml_range = Enum.YLeaf(108, "evpn-iml-range")

    l2_bridge_o_list = Enum.YLeaf(109, "l2-bridge-o-list")

    l2_bridge_vnio_list = Enum.YLeaf(110, "l2-bridge-vnio-list")

    l2acl = Enum.YLeaf(111, "l2acl")

    l2evpn_nh = Enum.YLeaf(112, "l2evpn-nh")

    l2_bridge_port_sc = Enum.YLeaf(113, "l2-bridge-port-sc")

    l3intfmctxstats = Enum.YLeaf(114, "l3intfmctxstats")

    tidl_sample = Enum.YLeaf(115, "tidl-sample")

    tidl_ref_sample = Enum.YLeaf(116, "tidl-ref-sample")

    ipacl_prefix = Enum.YLeaf(117, "ipacl-prefix")

    ip6acl_prefix = Enum.YLeaf(118, "ip6acl-prefix")

    ipacl_port = Enum.YLeaf(119, "ipacl-port")

    scaleacl = Enum.YLeaf(120, "scaleacl")

    ipmcf_hop = Enum.YLeaf(121, "ipmcf-hop")

    bundle_swoff = Enum.YLeaf(122, "bundle-swoff")

    mcidswoff = Enum.YLeaf(123, "mcidswoff")

    dest_map = Enum.YLeaf(124, "dest-map")

    l2_bridge_port_pw = Enum.YLeaf(125, "l2-bridge-port-pw")

    l2evpnact_local_shlstats = Enum.YLeaf(126, "l2evpnact-local-shlstats")

    test_hidden = Enum.YLeaf(127, "test-hidden")

    test_local = Enum.YLeaf(128, "test-local")

    test_repeated = Enum.YLeaf(129, "test-repeated")

    limd = Enum.YLeaf(130, "limd")

    litap = Enum.YLeaf(131, "litap")

    l3intf_proto_stats = Enum.YLeaf(132, "l3intf-proto-stats")

    srv6sid = Enum.YLeaf(133, "srv6sid")

    srv6nh = Enum.YLeaf(134, "srv6nh")

    redirect_vrf = Enum.YLeaf(135, "redirect-vrf")

    test_xtf = Enum.YLeaf(136, "test-xtf")

    ippbr = Enum.YLeaf(137, "ippbr")

    ippbrstats = Enum.YLeaf(138, "ippbrstats")

    l2_bridge_port_remote_lc = Enum.YLeaf(139, "l2-bridge-port-remote-lc")

    mpls_mdt_bud = Enum.YLeaf(140, "mpls-mdt-bud")

    l2mac_static = Enum.YLeaf(141, "l2mac-static")

    sr_label_rxstats = Enum.YLeaf(142, "sr-label-rxstats")

    l2vpnxid = Enum.YLeaf(143, "l2vpnxid")

    rpfif = Enum.YLeaf(144, "rpfif")



class Dpa(Entity):
    """
    Stats Data
    
    .. attribute:: stats
    
    	Voq or Trap Data
    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats>`
    
    	**config**\: False
    
    .. attribute:: resources
    
    	OFA Resources Data
    	**type**\:  :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources>`
    
    	**config**\: False
    
    

    """

    _prefix = 'fretta-bcm-dpa-resources-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(Dpa, self).__init__()
        self._top_entity = None

        self.yang_name = "dpa"
        self.yang_parent_name = "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("stats", ("stats", Dpa.Stats)), ("resources", ("resources", Dpa.Resources))])
        self._leafs = OrderedDict()

        self.stats = Dpa.Stats()
        self.stats.parent = self
        self._children_name_map["stats"] = "stats"

        self.resources = Dpa.Resources()
        self.resources.parent = self
        self._children_name_map["resources"] = "resources"
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Dpa, [], name, value)


    class Stats(Entity):
        """
        Voq or Trap Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'fretta-bcm-dpa-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dpa.Stats, self).__init__()

            self.yang_name = "stats"
            self.yang_parent_name = "dpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nodes", ("nodes", Dpa.Stats.Nodes))])
            self._leafs = OrderedDict()

            self.nodes = Dpa.Stats.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._segment_path = lambda: "stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dpa.Stats, [], name, value)


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fretta-bcm-dpa-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dpa.Stats.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "stats"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", Dpa.Stats.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/stats/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Stats.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: asic_statistics
                
                	ASIC statistics table
                	**type**\:  :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics>`
                
                	**config**\: False
                
                .. attribute:: npu_numbers
                
                	Ingress Stats
                	**type**\:  :py:class:`NpuNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers>`
                
                	**config**\: False
                
                

                """

                _prefix = 'fretta-bcm-dpa-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dpa.Stats.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_name']
                    self._child_classes = OrderedDict([("asic-statistics", ("asic_statistics", Dpa.Stats.Nodes.Node.AsicStatistics)), ("npu-numbers", ("npu_numbers", Dpa.Stats.Nodes.Node.NpuNumbers))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ])
                    self.node_name = None

                    self.asic_statistics = Dpa.Stats.Nodes.Node.AsicStatistics()
                    self.asic_statistics.parent = self
                    self._children_name_map["asic_statistics"] = "asic-statistics"

                    self.npu_numbers = Dpa.Stats.Nodes.Node.NpuNumbers()
                    self.npu_numbers.parent = self
                    self._children_name_map["npu_numbers"] = "npu-numbers"
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/stats/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Stats.Nodes.Node, ['node_name'], name, value)


                class AsicStatistics(Entity):
                    """
                    ASIC statistics table
                    
                    .. attribute:: asic_statistics_detail_for_npu_ids
                    
                    	Detailed ASIC statistics
                    	**type**\:  :py:class:`AsicStatisticsDetailForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds>`
                    
                    	**config**\: False
                    
                    .. attribute:: asic_statistics_for_npu_ids
                    
                    	ASIC statistics
                    	**type**\:  :py:class:`AsicStatisticsForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.AsicStatistics, self).__init__()

                        self.yang_name = "asic-statistics"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("asic-statistics-detail-for-npu-ids", ("asic_statistics_detail_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds)), ("asic-statistics-for-npu-ids", ("asic_statistics_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds))])
                        self._leafs = OrderedDict()

                        self.asic_statistics_detail_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds()
                        self.asic_statistics_detail_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_detail_for_npu_ids"] = "asic-statistics-detail-for-npu-ids"

                        self.asic_statistics_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds()
                        self.asic_statistics_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_for_npu_ids"] = "asic-statistics-for-npu-ids"
                        self._segment_path = lambda: "asic-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics, [], name, value)


                    class AsicStatisticsDetailForNpuIds(Entity):
                        """
                        Detailed ASIC statistics
                        
                        .. attribute:: asic_statistics_detail_for_npu_id
                        
                        	Detailed ASIC statistics for a particular NPU
                        	**type**\: list of  		 :py:class:`AsicStatisticsDetailForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-detail-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("asic-statistics-detail-for-npu-id", ("asic_statistics_detail_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId))])
                            self._leafs = OrderedDict()

                            self.asic_statistics_detail_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-detail-for-npu-ids"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, [], name, value)


                        class AsicStatisticsDetailForNpuId(Entity):
                            """
                            Detailed ASIC statistics for a particular
                            NPU
                            
                            .. attribute:: npu_id  (key)
                            
                            	NPU number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics>`
                            
                            	**config**\: False
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-detail-for-npu-id"
                                self.yang_parent_name = "asic-statistics-detail-for-npu-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['npu_id']
                                self._child_classes = OrderedDict([("statistics", ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics))])
                                self._leafs = OrderedDict([
                                    ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                    ('rack_number', (YLeaf(YType.uint32, 'rack-number'), ['int'])),
                                    ('slot_number', (YLeaf(YType.uint32, 'slot-number'), ['int'])),
                                    ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                    ('chip_version', (YLeaf(YType.uint16, 'chip-version'), ['int'])),
                                ])
                                self.npu_id = None
                                self.valid = None
                                self.rack_number = None
                                self.slot_number = None
                                self.asic_instance = None
                                self.chip_version = None

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._segment_path = lambda: "asic-statistics-detail-for-npu-id" + "[npu-id='" + str(self.npu_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, ['npu_id', u'valid', u'rack_number', u'slot_number', u'asic_instance', u'chip_version'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: num_blocks
                                
                                	Number of blocks
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                	**config**\: False
                                
                                .. attribute:: block_info
                                
                                	Block information
                                	**type**\: list of  		 :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-detail-for-npu-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("block-info", ("block_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo))])
                                    self._leafs = OrderedDict([
                                        ('num_blocks', (YLeaf(YType.uint8, 'num-blocks'), ['int'])),
                                    ])
                                    self.num_blocks = None

                                    self.block_info = YList(self)
                                    self._segment_path = lambda: "statistics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, [u'num_blocks'], name, value)


                                class BlockInfo(Entity):
                                    """
                                    Block information
                                    
                                    .. attribute:: block_name
                                    
                                    	Block name
                                    	**type**\: str
                                    
                                    	**length:** 0..10
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: num_fields
                                    
                                    	Number of fields
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: field_info
                                    
                                    	Field information
                                    	**type**\: list of  		 :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, self).__init__()

                                        self.yang_name = "block-info"
                                        self.yang_parent_name = "statistics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("field-info", ("field_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo))])
                                        self._leafs = OrderedDict([
                                            ('block_name', (YLeaf(YType.str, 'block-name'), ['str'])),
                                            ('num_fields', (YLeaf(YType.uint8, 'num-fields'), ['int'])),
                                        ])
                                        self.block_name = None
                                        self.num_fields = None

                                        self.field_info = YList(self)
                                        self._segment_path = lambda: "block-info"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, [u'block_name', u'num_fields'], name, value)


                                    class FieldInfo(Entity):
                                        """
                                        Field information
                                        
                                        .. attribute:: field_name
                                        
                                        	Field name
                                        	**type**\: str
                                        
                                        	**length:** 0..80
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: field_value
                                        
                                        	Field value
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: is_overflow
                                        
                                        	Flag to indicate overflow
                                        	**type**\: bool
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, self).__init__()

                                            self.yang_name = "field-info"
                                            self.yang_parent_name = "block-info"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('field_name', (YLeaf(YType.str, 'field-name'), ['str'])),
                                                ('field_value', (YLeaf(YType.uint64, 'field-value'), ['int'])),
                                                ('is_overflow', (YLeaf(YType.boolean, 'is-overflow'), ['bool'])),
                                            ])
                                            self.field_name = None
                                            self.field_value = None
                                            self.is_overflow = None
                                            self._segment_path = lambda: "field-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, [u'field_name', u'field_value', u'is_overflow'], name, value)







                    class AsicStatisticsForNpuIds(Entity):
                        """
                        ASIC statistics
                        
                        .. attribute:: asic_statistics_for_npu_id
                        
                        	ASIC statistics for a particular NPU
                        	**type**\: list of  		 :py:class:`AsicStatisticsForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, self).__init__()

                            self.yang_name = "asic-statistics-for-npu-ids"
                            self.yang_parent_name = "asic-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("asic-statistics-for-npu-id", ("asic_statistics_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId))])
                            self._leafs = OrderedDict()

                            self.asic_statistics_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-for-npu-ids"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, [], name, value)


                        class AsicStatisticsForNpuId(Entity):
                            """
                            ASIC statistics for a particular NPU
                            
                            .. attribute:: npu_id  (key)
                            
                            	NPU number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics>`
                            
                            	**config**\: False
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\: bool
                            
                            	**config**\: False
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, self).__init__()

                                self.yang_name = "asic-statistics-for-npu-id"
                                self.yang_parent_name = "asic-statistics-for-npu-ids"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['npu_id']
                                self._child_classes = OrderedDict([("statistics", ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics))])
                                self._leafs = OrderedDict([
                                    ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                    ('valid', (YLeaf(YType.boolean, 'valid'), ['bool'])),
                                    ('rack_number', (YLeaf(YType.uint32, 'rack-number'), ['int'])),
                                    ('slot_number', (YLeaf(YType.uint32, 'slot-number'), ['int'])),
                                    ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                                    ('chip_version', (YLeaf(YType.uint16, 'chip-version'), ['int'])),
                                ])
                                self.npu_id = None
                                self.valid = None
                                self.rack_number = None
                                self.slot_number = None
                                self.asic_instance = None
                                self.chip_version = None

                                self.statistics = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics()
                                self.statistics.parent = self
                                self._children_name_map["statistics"] = "statistics"
                                self._segment_path = lambda: "asic-statistics-for-npu-id" + "[npu-id='" + str(self.npu_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, ['npu_id', u'valid', u'rack_number', u'slot_number', u'asic_instance', u'chip_version'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: nbi_rx_total_byte_cnt
                                
                                	Total bytes sent from NIF to IRE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_rx_total_pkt_cnt
                                
                                	Total packets sent from NIF to IRE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_cpu_pkt_cnt
                                
                                	CPU ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_nif_pkt_cnt
                                
                                	NIF received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_oamp_pkt_cnt
                                
                                	OAMP ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_olp_pkt_cnt
                                
                                	OLP ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_rcy_pkt_cnt
                                
                                	Recycling ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ire_fdt_if_cnt
                                
                                	Performance counter of the FDT interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: idr_mmu_if_cnt
                                
                                	Performance counter of the MMU interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: idr_ocb_if_cnt
                                
                                	Performance counter of the OCB interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_enqueue_pkt_cnt
                                
                                	Counts enqueued packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_dequeue_pkt_cnt
                                
                                	Counts dequeued packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_deleted_pkt_cnt
                                
                                	Counts matched packets discarded in the DEQ process
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: iqm_enq_discarded_pkt_cnt
                                
                                	Counts all packets discarded at the ENQ pipe
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_egq_pkt_cnt
                                
                                	EGQ packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_enq_pkt_cnt
                                
                                	ENQ packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_fdt_pkt_cnt
                                
                                	FDT packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_cfg_event_cnt
                                
                                	Configurable event counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: ipt_cfg_byte_cnt
                                
                                	Configurable bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: fdt_ipt_desc_cell_cnt
                                
                                	Descriptor cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdt_ire_desc_cell_cnt
                                
                                	IRE internal descriptor cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdt_transmitted_data_cells_cnt
                                
                                	Counts all transmitted data cells
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_p1_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_p2_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_p3_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fdr_cell_in_cnt_total
                                
                                	FDR total incoming cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_cnt_p1
                                
                                	FDA input cell counter P1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_cnt_p2
                                
                                	FDA input cell counter P2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_cnt_p3
                                
                                	FDA input cell counter P3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_tdm_cnt
                                
                                	FDA input cell counter TDM
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_meshmc_cnt
                                
                                	FDA input cell counter MESHMC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_in_ipt_cnt
                                
                                	FDA input cell counter IPT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_cnt_p1
                                
                                	FDA output cell counter P1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_cnt_p2
                                
                                	FDA output cell counter P2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_cnt_p3
                                
                                	FDA output cell counter P3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_tdm_cnt
                                
                                	FDA output cell counter TDM
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_meshmc_cnt
                                
                                	FDA output cell counter MESHMC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_cells_out_ipt_cnt
                                
                                	FDA output cell counter IPT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_egq_drop_cnt
                                
                                	FDA EGQ drop counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: fda_egq_meshmc_drop_cnt
                                
                                	FDA EGQ MESHMC drop counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_fqp_pkt_cnt
                                
                                	FQP2EPE packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_uc_pkt_cnt
                                
                                	PQP2FQP unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_discard_uc_pkt_cnt
                                
                                	PQP discarded unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_uc_bytes_cnt
                                
                                	PQP2FQP unicast bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_mc_pkt_cnt
                                
                                	PQP2FQP multicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_discard_mc_pkt_cnt
                                
                                	PQP discarded multicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_pqp_mc_bytes_cnt
                                
                                	PQP2FQP multicast bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_ehp_uc_pkt_cnt
                                
                                	EHP2PQP unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_high_pkt_cnt
                                
                                	EHP2PQP multicast high packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_low_pkt_cnt
                                
                                	EHP2PQP multicast low packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_deleted_pkt_cnt
                                
                                	EHP2PQP discarded packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_high_discard_cnt
                                
                                	Number of multicast high packets discarded because multicast FIFO is full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_ehp_mc_low_discard_cnt
                                
                                	Number of multicast low packets discarded because multicast FIFO is full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_erpp_lag_pruning_discard_cnt
                                
                                	Number of packet descriptors discarded due to LAG multicast pruning
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_erpp_pmf_discard_cnt
                                
                                	Number of packet descriptors discarded due to ERPP PMF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: egq_erpp_vlan_mbr_discard_cnt
                                
                                	Number of packet descriptors discarded because of egress VLAN membership
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: epni_epe_byte_cnt
                                
                                	EPE2PNI bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: epni_epe_pkt_cnt
                                
                                	EPE2PNI packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: epni_epe_discard_cnt
                                
                                	EPE discarded packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                .. attribute:: nbi_tx_total_byte_cnt
                                
                                	Total bytes sent from EGQ to NIF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_tx_total_pkt_cnt
                                
                                	Total packets sent from EGQ to NIF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, self).__init__()

                                    self.yang_name = "statistics"
                                    self.yang_parent_name = "asic-statistics-for-npu-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('nbi_rx_total_byte_cnt', (YLeaf(YType.uint64, 'nbi-rx-total-byte-cnt'), ['int'])),
                                        ('nbi_rx_total_pkt_cnt', (YLeaf(YType.uint64, 'nbi-rx-total-pkt-cnt'), ['int'])),
                                        ('ire_cpu_pkt_cnt', (YLeaf(YType.uint64, 'ire-cpu-pkt-cnt'), ['int'])),
                                        ('ire_nif_pkt_cnt', (YLeaf(YType.uint64, 'ire-nif-pkt-cnt'), ['int'])),
                                        ('ire_oamp_pkt_cnt', (YLeaf(YType.uint64, 'ire-oamp-pkt-cnt'), ['int'])),
                                        ('ire_olp_pkt_cnt', (YLeaf(YType.uint64, 'ire-olp-pkt-cnt'), ['int'])),
                                        ('ire_rcy_pkt_cnt', (YLeaf(YType.uint64, 'ire-rcy-pkt-cnt'), ['int'])),
                                        ('ire_fdt_if_cnt', (YLeaf(YType.uint64, 'ire-fdt-if-cnt'), ['int'])),
                                        ('idr_mmu_if_cnt', (YLeaf(YType.uint64, 'idr-mmu-if-cnt'), ['int'])),
                                        ('idr_ocb_if_cnt', (YLeaf(YType.uint64, 'idr-ocb-if-cnt'), ['int'])),
                                        ('iqm_enqueue_pkt_cnt', (YLeaf(YType.uint64, 'iqm-enqueue-pkt-cnt'), ['int'])),
                                        ('iqm_dequeue_pkt_cnt', (YLeaf(YType.uint64, 'iqm-dequeue-pkt-cnt'), ['int'])),
                                        ('iqm_deleted_pkt_cnt', (YLeaf(YType.uint64, 'iqm-deleted-pkt-cnt'), ['int'])),
                                        ('iqm_enq_discarded_pkt_cnt', (YLeaf(YType.uint64, 'iqm-enq-discarded-pkt-cnt'), ['int'])),
                                        ('ipt_egq_pkt_cnt', (YLeaf(YType.uint64, 'ipt-egq-pkt-cnt'), ['int'])),
                                        ('ipt_enq_pkt_cnt', (YLeaf(YType.uint64, 'ipt-enq-pkt-cnt'), ['int'])),
                                        ('ipt_fdt_pkt_cnt', (YLeaf(YType.uint64, 'ipt-fdt-pkt-cnt'), ['int'])),
                                        ('ipt_cfg_event_cnt', (YLeaf(YType.uint64, 'ipt-cfg-event-cnt'), ['int'])),
                                        ('ipt_cfg_byte_cnt', (YLeaf(YType.uint64, 'ipt-cfg-byte-cnt'), ['int'])),
                                        ('fdt_ipt_desc_cell_cnt', (YLeaf(YType.uint64, 'fdt-ipt-desc-cell-cnt'), ['int'])),
                                        ('fdt_ire_desc_cell_cnt', (YLeaf(YType.uint64, 'fdt-ire-desc-cell-cnt'), ['int'])),
                                        ('fdt_transmitted_data_cells_cnt', (YLeaf(YType.uint64, 'fdt-transmitted-data-cells-cnt'), ['int'])),
                                        ('fdr_p1_cell_in_cnt', (YLeaf(YType.uint64, 'fdr-p1-cell-in-cnt'), ['int'])),
                                        ('fdr_p2_cell_in_cnt', (YLeaf(YType.uint64, 'fdr-p2-cell-in-cnt'), ['int'])),
                                        ('fdr_p3_cell_in_cnt', (YLeaf(YType.uint64, 'fdr-p3-cell-in-cnt'), ['int'])),
                                        ('fdr_cell_in_cnt_total', (YLeaf(YType.uint64, 'fdr-cell-in-cnt-total'), ['int'])),
                                        ('fda_cells_in_cnt_p1', (YLeaf(YType.uint64, 'fda-cells-in-cnt-p1'), ['int'])),
                                        ('fda_cells_in_cnt_p2', (YLeaf(YType.uint64, 'fda-cells-in-cnt-p2'), ['int'])),
                                        ('fda_cells_in_cnt_p3', (YLeaf(YType.uint64, 'fda-cells-in-cnt-p3'), ['int'])),
                                        ('fda_cells_in_tdm_cnt', (YLeaf(YType.uint64, 'fda-cells-in-tdm-cnt'), ['int'])),
                                        ('fda_cells_in_meshmc_cnt', (YLeaf(YType.uint64, 'fda-cells-in-meshmc-cnt'), ['int'])),
                                        ('fda_cells_in_ipt_cnt', (YLeaf(YType.uint64, 'fda-cells-in-ipt-cnt'), ['int'])),
                                        ('fda_cells_out_cnt_p1', (YLeaf(YType.uint64, 'fda-cells-out-cnt-p1'), ['int'])),
                                        ('fda_cells_out_cnt_p2', (YLeaf(YType.uint64, 'fda-cells-out-cnt-p2'), ['int'])),
                                        ('fda_cells_out_cnt_p3', (YLeaf(YType.uint64, 'fda-cells-out-cnt-p3'), ['int'])),
                                        ('fda_cells_out_tdm_cnt', (YLeaf(YType.uint64, 'fda-cells-out-tdm-cnt'), ['int'])),
                                        ('fda_cells_out_meshmc_cnt', (YLeaf(YType.uint64, 'fda-cells-out-meshmc-cnt'), ['int'])),
                                        ('fda_cells_out_ipt_cnt', (YLeaf(YType.uint64, 'fda-cells-out-ipt-cnt'), ['int'])),
                                        ('fda_egq_drop_cnt', (YLeaf(YType.uint64, 'fda-egq-drop-cnt'), ['int'])),
                                        ('fda_egq_meshmc_drop_cnt', (YLeaf(YType.uint64, 'fda-egq-meshmc-drop-cnt'), ['int'])),
                                        ('egq_fqp_pkt_cnt', (YLeaf(YType.uint64, 'egq-fqp-pkt-cnt'), ['int'])),
                                        ('egq_pqp_uc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-uc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_discard_uc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-discard-uc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_uc_bytes_cnt', (YLeaf(YType.uint64, 'egq-pqp-uc-bytes-cnt'), ['int'])),
                                        ('egq_pqp_mc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-mc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_discard_mc_pkt_cnt', (YLeaf(YType.uint64, 'egq-pqp-discard-mc-pkt-cnt'), ['int'])),
                                        ('egq_pqp_mc_bytes_cnt', (YLeaf(YType.uint64, 'egq-pqp-mc-bytes-cnt'), ['int'])),
                                        ('egq_ehp_uc_pkt_cnt', (YLeaf(YType.uint64, 'egq-ehp-uc-pkt-cnt'), ['int'])),
                                        ('egq_ehp_mc_high_pkt_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-high-pkt-cnt'), ['int'])),
                                        ('egq_ehp_mc_low_pkt_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-low-pkt-cnt'), ['int'])),
                                        ('egq_deleted_pkt_cnt', (YLeaf(YType.uint64, 'egq-deleted-pkt-cnt'), ['int'])),
                                        ('egq_ehp_mc_high_discard_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-high-discard-cnt'), ['int'])),
                                        ('egq_ehp_mc_low_discard_cnt', (YLeaf(YType.uint64, 'egq-ehp-mc-low-discard-cnt'), ['int'])),
                                        ('egq_erpp_lag_pruning_discard_cnt', (YLeaf(YType.uint64, 'egq-erpp-lag-pruning-discard-cnt'), ['int'])),
                                        ('egq_erpp_pmf_discard_cnt', (YLeaf(YType.uint64, 'egq-erpp-pmf-discard-cnt'), ['int'])),
                                        ('egq_erpp_vlan_mbr_discard_cnt', (YLeaf(YType.uint64, 'egq-erpp-vlan-mbr-discard-cnt'), ['int'])),
                                        ('epni_epe_byte_cnt', (YLeaf(YType.uint64, 'epni-epe-byte-cnt'), ['int'])),
                                        ('epni_epe_pkt_cnt', (YLeaf(YType.uint64, 'epni-epe-pkt-cnt'), ['int'])),
                                        ('epni_epe_discard_cnt', (YLeaf(YType.uint64, 'epni-epe-discard-cnt'), ['int'])),
                                        ('nbi_tx_total_byte_cnt', (YLeaf(YType.uint64, 'nbi-tx-total-byte-cnt'), ['int'])),
                                        ('nbi_tx_total_pkt_cnt', (YLeaf(YType.uint64, 'nbi-tx-total-pkt-cnt'), ['int'])),
                                    ])
                                    self.nbi_rx_total_byte_cnt = None
                                    self.nbi_rx_total_pkt_cnt = None
                                    self.ire_cpu_pkt_cnt = None
                                    self.ire_nif_pkt_cnt = None
                                    self.ire_oamp_pkt_cnt = None
                                    self.ire_olp_pkt_cnt = None
                                    self.ire_rcy_pkt_cnt = None
                                    self.ire_fdt_if_cnt = None
                                    self.idr_mmu_if_cnt = None
                                    self.idr_ocb_if_cnt = None
                                    self.iqm_enqueue_pkt_cnt = None
                                    self.iqm_dequeue_pkt_cnt = None
                                    self.iqm_deleted_pkt_cnt = None
                                    self.iqm_enq_discarded_pkt_cnt = None
                                    self.ipt_egq_pkt_cnt = None
                                    self.ipt_enq_pkt_cnt = None
                                    self.ipt_fdt_pkt_cnt = None
                                    self.ipt_cfg_event_cnt = None
                                    self.ipt_cfg_byte_cnt = None
                                    self.fdt_ipt_desc_cell_cnt = None
                                    self.fdt_ire_desc_cell_cnt = None
                                    self.fdt_transmitted_data_cells_cnt = None
                                    self.fdr_p1_cell_in_cnt = None
                                    self.fdr_p2_cell_in_cnt = None
                                    self.fdr_p3_cell_in_cnt = None
                                    self.fdr_cell_in_cnt_total = None
                                    self.fda_cells_in_cnt_p1 = None
                                    self.fda_cells_in_cnt_p2 = None
                                    self.fda_cells_in_cnt_p3 = None
                                    self.fda_cells_in_tdm_cnt = None
                                    self.fda_cells_in_meshmc_cnt = None
                                    self.fda_cells_in_ipt_cnt = None
                                    self.fda_cells_out_cnt_p1 = None
                                    self.fda_cells_out_cnt_p2 = None
                                    self.fda_cells_out_cnt_p3 = None
                                    self.fda_cells_out_tdm_cnt = None
                                    self.fda_cells_out_meshmc_cnt = None
                                    self.fda_cells_out_ipt_cnt = None
                                    self.fda_egq_drop_cnt = None
                                    self.fda_egq_meshmc_drop_cnt = None
                                    self.egq_fqp_pkt_cnt = None
                                    self.egq_pqp_uc_pkt_cnt = None
                                    self.egq_pqp_discard_uc_pkt_cnt = None
                                    self.egq_pqp_uc_bytes_cnt = None
                                    self.egq_pqp_mc_pkt_cnt = None
                                    self.egq_pqp_discard_mc_pkt_cnt = None
                                    self.egq_pqp_mc_bytes_cnt = None
                                    self.egq_ehp_uc_pkt_cnt = None
                                    self.egq_ehp_mc_high_pkt_cnt = None
                                    self.egq_ehp_mc_low_pkt_cnt = None
                                    self.egq_deleted_pkt_cnt = None
                                    self.egq_ehp_mc_high_discard_cnt = None
                                    self.egq_ehp_mc_low_discard_cnt = None
                                    self.egq_erpp_lag_pruning_discard_cnt = None
                                    self.egq_erpp_pmf_discard_cnt = None
                                    self.egq_erpp_vlan_mbr_discard_cnt = None
                                    self.epni_epe_byte_cnt = None
                                    self.epni_epe_pkt_cnt = None
                                    self.epni_epe_discard_cnt = None
                                    self.nbi_tx_total_byte_cnt = None
                                    self.nbi_tx_total_pkt_cnt = None
                                    self._segment_path = lambda: "statistics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, [u'nbi_rx_total_byte_cnt', u'nbi_rx_total_pkt_cnt', u'ire_cpu_pkt_cnt', u'ire_nif_pkt_cnt', u'ire_oamp_pkt_cnt', u'ire_olp_pkt_cnt', u'ire_rcy_pkt_cnt', u'ire_fdt_if_cnt', u'idr_mmu_if_cnt', u'idr_ocb_if_cnt', u'iqm_enqueue_pkt_cnt', u'iqm_dequeue_pkt_cnt', u'iqm_deleted_pkt_cnt', u'iqm_enq_discarded_pkt_cnt', u'ipt_egq_pkt_cnt', u'ipt_enq_pkt_cnt', u'ipt_fdt_pkt_cnt', u'ipt_cfg_event_cnt', u'ipt_cfg_byte_cnt', u'fdt_ipt_desc_cell_cnt', u'fdt_ire_desc_cell_cnt', u'fdt_transmitted_data_cells_cnt', u'fdr_p1_cell_in_cnt', u'fdr_p2_cell_in_cnt', u'fdr_p3_cell_in_cnt', u'fdr_cell_in_cnt_total', u'fda_cells_in_cnt_p1', u'fda_cells_in_cnt_p2', u'fda_cells_in_cnt_p3', u'fda_cells_in_tdm_cnt', u'fda_cells_in_meshmc_cnt', u'fda_cells_in_ipt_cnt', u'fda_cells_out_cnt_p1', u'fda_cells_out_cnt_p2', u'fda_cells_out_cnt_p3', u'fda_cells_out_tdm_cnt', u'fda_cells_out_meshmc_cnt', u'fda_cells_out_ipt_cnt', u'fda_egq_drop_cnt', u'fda_egq_meshmc_drop_cnt', u'egq_fqp_pkt_cnt', u'egq_pqp_uc_pkt_cnt', u'egq_pqp_discard_uc_pkt_cnt', u'egq_pqp_uc_bytes_cnt', u'egq_pqp_mc_pkt_cnt', u'egq_pqp_discard_mc_pkt_cnt', u'egq_pqp_mc_bytes_cnt', u'egq_ehp_uc_pkt_cnt', u'egq_ehp_mc_high_pkt_cnt', u'egq_ehp_mc_low_pkt_cnt', u'egq_deleted_pkt_cnt', u'egq_ehp_mc_high_discard_cnt', u'egq_ehp_mc_low_discard_cnt', u'egq_erpp_lag_pruning_discard_cnt', u'egq_erpp_pmf_discard_cnt', u'egq_erpp_vlan_mbr_discard_cnt', u'epni_epe_byte_cnt', u'epni_epe_pkt_cnt', u'epni_epe_discard_cnt', u'nbi_tx_total_byte_cnt', u'nbi_tx_total_pkt_cnt'], name, value)






                class NpuNumbers(Entity):
                    """
                    Ingress Stats
                    
                    .. attribute:: npu_number
                    
                    	Stats for a particular npu
                    	**type**\: list of  		 :py:class:`NpuNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Stats.Nodes.Node.NpuNumbers, self).__init__()

                        self.yang_name = "npu-numbers"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("npu-number", ("npu_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber))])
                        self._leafs = OrderedDict()

                        self.npu_number = YList(self)
                        self._segment_path = lambda: "npu-numbers"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers, [], name, value)


                    class NpuNumber(Entity):
                        """
                        Stats for a particular npu
                        
                        .. attribute:: npu_id  (key)
                        
                        	Npu number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: display
                        
                        	show npu specific voq or trap stats
                        	**type**\:  :py:class:`Display <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, self).__init__()

                            self.yang_name = "npu-number"
                            self.yang_parent_name = "npu-numbers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['npu_id']
                            self._child_classes = OrderedDict([("display", ("display", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display))])
                            self._leafs = OrderedDict([
                                ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                            ])
                            self.npu_id = None

                            self.display = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display()
                            self.display.parent = self
                            self._children_name_map["display"] = "display"
                            self._segment_path = lambda: "npu-number" + "[npu-id='" + str(self.npu_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, ['npu_id'], name, value)


                        class Display(Entity):
                            """
                            show npu specific voq or trap stats
                            
                            .. attribute:: trap_ids
                            
                            	Trap stats for a particular npu
                            	**type**\:  :py:class:`TrapIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds>`
                            
                            	**config**\: False
                            
                            .. attribute:: interface_handles
                            
                            	Voq stats grouped by interface handle
                            	**type**\:  :py:class:`InterfaceHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles>`
                            
                            	**config**\: False
                            
                            .. attribute:: base_numbers
                            
                            	Voq stats grouped by voq base numbers
                            	**type**\:  :py:class:`BaseNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers>`
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display, self).__init__()

                                self.yang_name = "display"
                                self.yang_parent_name = "npu-number"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("trap-ids", ("trap_ids", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds)), ("interface-handles", ("interface_handles", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles)), ("base-numbers", ("base_numbers", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers))])
                                self._leafs = OrderedDict()

                                self.trap_ids = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds()
                                self.trap_ids.parent = self
                                self._children_name_map["trap_ids"] = "trap-ids"

                                self.interface_handles = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles()
                                self.interface_handles.parent = self
                                self._children_name_map["interface_handles"] = "interface-handles"

                                self.base_numbers = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers()
                                self.base_numbers.parent = self
                                self._children_name_map["base_numbers"] = "base-numbers"
                                self._segment_path = lambda: "display"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display, [], name, value)


                            class TrapIds(Entity):
                                """
                                Trap stats for a particular npu
                                
                                .. attribute:: trap_id
                                
                                	Filter by specific trap id
                                	**type**\: list of  		 :py:class:`TrapId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, self).__init__()

                                    self.yang_name = "trap-ids"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("trap-id", ("trap_id", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId))])
                                    self._leafs = OrderedDict()

                                    self.trap_id = YList(self)
                                    self._segment_path = lambda: "trap-ids"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, [], name, value)


                                class TrapId(Entity):
                                    """
                                    Filter by specific trap id
                                    
                                    .. attribute:: trap_id  (key)
                                    
                                    	Trap ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trap_strength
                                    
                                    	Trap Strength of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: priority
                                    
                                    	Priority of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trap_id_xr
                                    
                                    	Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: gport
                                    
                                    	Gport of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: fec_id
                                    
                                    	Fec id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: policer_id
                                    
                                    	Id of the policer on the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: stats_id
                                    
                                    	Stats Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: encap_id
                                    
                                    	Encap Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: mc_group
                                    
                                    	McGroup of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: trap_string
                                    
                                    	Name String of the trap
                                    	**type**\: str
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: id
                                    
                                    	Id for internal use
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: offset
                                    
                                    	Offset for internal use
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_id
                                    
                                    	NpuId on which trap is enabled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: packet_dropped
                                    
                                    	Number of packets dropped after hitting the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: packet_accepted
                                    
                                    	Number of packets accepted after hitting the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, self).__init__()

                                        self.yang_name = "trap-id"
                                        self.yang_parent_name = "trap-ids"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['trap_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('trap_id', (YLeaf(YType.uint32, 'trap-id'), ['int'])),
                                            ('trap_strength', (YLeaf(YType.uint32, 'trap-strength'), ['int'])),
                                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                            ('trap_id_xr', (YLeaf(YType.uint32, 'trap-id-xr'), ['int'])),
                                            ('gport', (YLeaf(YType.uint32, 'gport'), ['int'])),
                                            ('fec_id', (YLeaf(YType.uint32, 'fec-id'), ['int'])),
                                            ('policer_id', (YLeaf(YType.uint32, 'policer-id'), ['int'])),
                                            ('stats_id', (YLeaf(YType.uint32, 'stats-id'), ['int'])),
                                            ('encap_id', (YLeaf(YType.uint32, 'encap-id'), ['int'])),
                                            ('mc_group', (YLeaf(YType.uint32, 'mc-group'), ['int'])),
                                            ('trap_string', (YLeaf(YType.str, 'trap-string'), ['str'])),
                                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                                            ('offset', (YLeaf(YType.uint64, 'offset'), ['int'])),
                                            ('npu_id', (YLeaf(YType.uint64, 'npu-id'), ['int'])),
                                            ('packet_dropped', (YLeaf(YType.uint64, 'packet-dropped'), ['int'])),
                                            ('packet_accepted', (YLeaf(YType.uint64, 'packet-accepted'), ['int'])),
                                        ])
                                        self.trap_id = None
                                        self.trap_strength = None
                                        self.priority = None
                                        self.trap_id_xr = None
                                        self.gport = None
                                        self.fec_id = None
                                        self.policer_id = None
                                        self.stats_id = None
                                        self.encap_id = None
                                        self.mc_group = None
                                        self.trap_string = None
                                        self.id = None
                                        self.offset = None
                                        self.npu_id = None
                                        self.packet_dropped = None
                                        self.packet_accepted = None
                                        self._segment_path = lambda: "trap-id" + "[trap-id='" + str(self.trap_id) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, ['trap_id', u'trap_strength', u'priority', u'trap_id_xr', u'gport', u'fec_id', u'policer_id', u'stats_id', u'encap_id', u'mc_group', u'trap_string', u'id', u'offset', u'npu_id', u'packet_dropped', u'packet_accepted'], name, value)




                            class InterfaceHandles(Entity):
                                """
                                Voq stats grouped by interface handle
                                
                                .. attribute:: interface_handle
                                
                                	Voq stats for a particular interface handle
                                	**type**\: list of  		 :py:class:`InterfaceHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, self).__init__()

                                    self.yang_name = "interface-handles"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("interface-handle", ("interface_handle", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle))])
                                    self._leafs = OrderedDict()

                                    self.interface_handle = YList(self)
                                    self._segment_path = lambda: "interface-handles"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles, [], name, value)


                                class InterfaceHandle(Entity):
                                    """
                                    Voq stats for a particular interface
                                    handle
                                    
                                    .. attribute:: interface_handle  (key)
                                    
                                    	Interface Handle
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of  		 :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, self).__init__()

                                        self.yang_name = "interface-handle"
                                        self.yang_parent_name = "interface-handles"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_handle']
                                        self._child_classes = OrderedDict([("voq-stat", ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat))])
                                        self._leafs = OrderedDict([
                                            ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                            ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                            ('rack_num', (YLeaf(YType.uint8, 'rack-num'), ['int'])),
                                            ('slot_num', (YLeaf(YType.uint8, 'slot-num'), ['int'])),
                                            ('npu_num', (YLeaf(YType.uint8, 'npu-num'), ['int'])),
                                            ('npu_core', (YLeaf(YType.uint8, 'npu-core'), ['int'])),
                                            ('port_num', (YLeaf(YType.uint8, 'port-num'), ['int'])),
                                            ('if_handle', (YLeaf(YType.uint32, 'if-handle'), ['int'])),
                                            ('sys_port', (YLeaf(YType.uint32, 'sys-port'), ['int'])),
                                            ('pp_port', (YLeaf(YType.uint32, 'pp-port'), ['int'])),
                                            ('port_speed', (YLeaf(YType.uint32, 'port-speed'), ['int'])),
                                            ('voq_base', (YLeaf(YType.uint32, 'voq-base'), ['int'])),
                                            ('connector_id', (YLeaf(YType.uint32, 'connector-id'), ['int'])),
                                            ('is_local_port', (YLeaf(YType.boolean, 'is-local-port'), ['bool'])),
                                        ])
                                        self.interface_handle = None
                                        self.in_use = None
                                        self.rack_num = None
                                        self.slot_num = None
                                        self.npu_num = None
                                        self.npu_core = None
                                        self.port_num = None
                                        self.if_handle = None
                                        self.sys_port = None
                                        self.pp_port = None
                                        self.port_speed = None
                                        self.voq_base = None
                                        self.connector_id = None
                                        self.is_local_port = None

                                        self.voq_stat = YList(self)
                                        self._segment_path = lambda: "interface-handle" + "[interface-handle='" + str(self.interface_handle) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, ['interface_handle', u'in_use', u'rack_num', u'slot_num', u'npu_num', u'npu_core', u'port_num', u'if_handle', u'sys_port', u'pp_port', u'port_speed', u'voq_base', u'connector_id', u'is_local_port'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "interface-handle"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('received_bytes', (YLeaf(YType.uint64, 'received-bytes'), ['int'])),
                                                ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                                ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                            ])
                                            self.received_bytes = None
                                            self.received_packets = None
                                            self.dropped_bytes = None
                                            self.dropped_packets = None
                                            self._segment_path = lambda: "voq-stat"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, [u'received_bytes', u'received_packets', u'dropped_bytes', u'dropped_packets'], name, value)





                            class BaseNumbers(Entity):
                                """
                                Voq stats grouped by voq base numbers
                                
                                .. attribute:: base_number
                                
                                	Voq Base Number for a particular voq
                                	**type**\: list of  		 :py:class:`BaseNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber>`
                                
                                	**config**\: False
                                
                                

                                """

                                _prefix = 'fretta-bcm-dpa-resources-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, self).__init__()

                                    self.yang_name = "base-numbers"
                                    self.yang_parent_name = "display"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("base-number", ("base_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber))])
                                    self._leafs = OrderedDict()

                                    self.base_number = YList(self)
                                    self._segment_path = lambda: "base-numbers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, [], name, value)


                                class BaseNumber(Entity):
                                    """
                                    Voq Base Number for a particular voq
                                    
                                    .. attribute:: base_number  (key)
                                    
                                    	Interface handle
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\: bool
                                    
                                    	**config**\: False
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of  		 :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat>`
                                    
                                    	**config**\: False
                                    
                                    

                                    """

                                    _prefix = 'fretta-bcm-dpa-resources-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, self).__init__()

                                        self.yang_name = "base-number"
                                        self.yang_parent_name = "base-numbers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['base_number']
                                        self._child_classes = OrderedDict([("voq-stat", ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat))])
                                        self._leafs = OrderedDict([
                                            ('base_number', (YLeaf(YType.uint32, 'base-number'), ['int'])),
                                            ('in_use', (YLeaf(YType.boolean, 'in-use'), ['bool'])),
                                            ('rack_num', (YLeaf(YType.uint8, 'rack-num'), ['int'])),
                                            ('slot_num', (YLeaf(YType.uint8, 'slot-num'), ['int'])),
                                            ('npu_num', (YLeaf(YType.uint8, 'npu-num'), ['int'])),
                                            ('npu_core', (YLeaf(YType.uint8, 'npu-core'), ['int'])),
                                            ('port_num', (YLeaf(YType.uint8, 'port-num'), ['int'])),
                                            ('if_handle', (YLeaf(YType.uint32, 'if-handle'), ['int'])),
                                            ('sys_port', (YLeaf(YType.uint32, 'sys-port'), ['int'])),
                                            ('pp_port', (YLeaf(YType.uint32, 'pp-port'), ['int'])),
                                            ('port_speed', (YLeaf(YType.uint32, 'port-speed'), ['int'])),
                                            ('voq_base', (YLeaf(YType.uint32, 'voq-base'), ['int'])),
                                            ('connector_id', (YLeaf(YType.uint32, 'connector-id'), ['int'])),
                                            ('is_local_port', (YLeaf(YType.boolean, 'is-local-port'), ['bool'])),
                                        ])
                                        self.base_number = None
                                        self.in_use = None
                                        self.rack_num = None
                                        self.slot_num = None
                                        self.npu_num = None
                                        self.npu_core = None
                                        self.port_num = None
                                        self.if_handle = None
                                        self.sys_port = None
                                        self.pp_port = None
                                        self.port_speed = None
                                        self.voq_base = None
                                        self.connector_id = None
                                        self.is_local_port = None

                                        self.voq_stat = YList(self)
                                        self._segment_path = lambda: "base-number" + "[base-number='" + str(self.base_number) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, ['base_number', u'in_use', u'rack_num', u'slot_num', u'npu_num', u'npu_core', u'port_num', u'if_handle', u'sys_port', u'pp_port', u'port_speed', u'voq_base', u'connector_id', u'is_local_port'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**config**\: False
                                        
                                        

                                        """

                                        _prefix = 'fretta-bcm-dpa-resources-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, self).__init__()

                                            self.yang_name = "voq-stat"
                                            self.yang_parent_name = "base-number"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('received_bytes', (YLeaf(YType.uint64, 'received-bytes'), ['int'])),
                                                ('received_packets', (YLeaf(YType.uint64, 'received-packets'), ['int'])),
                                                ('dropped_bytes', (YLeaf(YType.uint64, 'dropped-bytes'), ['int'])),
                                                ('dropped_packets', (YLeaf(YType.uint64, 'dropped-packets'), ['int'])),
                                            ])
                                            self.received_bytes = None
                                            self.received_packets = None
                                            self.dropped_bytes = None
                                            self.dropped_packets = None
                                            self._segment_path = lambda: "voq-stat"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, [u'received_bytes', u'received_packets', u'dropped_bytes', u'dropped_packets'], name, value)











    class Resources(Entity):
        """
        OFA Resources Data
        
        .. attribute:: nodes
        
        	OFA data for available nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes>`
        
        	**config**\: False
        
        

        """

        _prefix = 'fretta-bcm-dpa-resources-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(Dpa.Resources, self).__init__()

            self.yang_name = "resources"
            self.yang_parent_name = "dpa"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("nodes", ("nodes", Dpa.Resources.Nodes))])
            self._leafs = OrderedDict()

            self.nodes = Dpa.Resources.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._segment_path = lambda: "resources"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Dpa.Resources, [], name, value)


        class Nodes(Entity):
            """
            OFA data for available nodes
            
            .. attribute:: node
            
            	OFA operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node>`
            
            	**config**\: False
            
            

            """

            _prefix = 'fretta-bcm-dpa-resources-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(Dpa.Resources.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "resources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", Dpa.Resources.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/resources/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Resources.Nodes, [], name, value)


            class Node(Entity):
                """
                OFA operational data for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                	**config**\: False
                
                .. attribute:: table_datas
                
                	OFA Resources table
                	**type**\:  :py:class:`TableDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas>`
                
                	**config**\: False
                
                

                """

                _prefix = 'fretta-bcm-dpa-resources-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Dpa.Resources.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_name']
                    self._child_classes = OrderedDict([("table-datas", ("table_datas", Dpa.Resources.Nodes.Node.TableDatas))])
                    self._leafs = OrderedDict([
                        ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                    ])
                    self.node_name = None

                    self.table_datas = Dpa.Resources.Nodes.Node.TableDatas()
                    self.table_datas.parent = self
                    self._children_name_map["table_datas"] = "table-datas"
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/resources/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Resources.Nodes.Node, ['node_name'], name, value)


                class TableDatas(Entity):
                    """
                    OFA Resources table
                    
                    .. attribute:: table_data
                    
                    	DPA Resources table
                    	**type**\: list of  		 :py:class:`TableData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData>`
                    
                    	**config**\: False
                    
                    

                    """

                    _prefix = 'fretta-bcm-dpa-resources-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Dpa.Resources.Nodes.Node.TableDatas, self).__init__()

                        self.yang_name = "table-datas"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("table-data", ("table_data", Dpa.Resources.Nodes.Node.TableDatas.TableData))])
                        self._leafs = OrderedDict()

                        self.table_data = YList(self)
                        self._segment_path = lambda: "table-datas"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas, [], name, value)


                    class TableData(Entity):
                        """
                        DPA Resources table
                        
                        .. attribute:: resource  (key)
                        
                        	Resource type
                        	**type**\:  :py:class:`DpaTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.DpaTable>`
                        
                        	**config**\: False
                        
                        .. attribute:: sysdb_avail_npu_mask
                        
                        	sysdb avail npu mask
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**config**\: False
                        
                        .. attribute:: table_id
                        
                        	table id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        	**config**\: False
                        
                        .. attribute:: is_global
                        
                        	is global
                        	**type**\: bool
                        
                        	**config**\: False
                        
                        .. attribute:: num_npus
                        
                        	num npus
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**config**\: False
                        
                        .. attribute:: table_specific_list
                        
                        	table specific list
                        	**type**\: str
                        
                        	**config**\: False
                        
                        .. attribute:: npu_tblr
                        
                        	npu tblr
                        	**type**\: list of  		 :py:class:`NpuTblr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr>`
                        
                        	**config**\: False
                        
                        

                        """

                        _prefix = 'fretta-bcm-dpa-resources-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Dpa.Resources.Nodes.Node.TableDatas.TableData, self).__init__()

                            self.yang_name = "table-data"
                            self.yang_parent_name = "table-datas"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['resource']
                            self._child_classes = OrderedDict([("npu-tblr", ("npu_tblr", Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr))])
                            self._leafs = OrderedDict([
                                ('resource', (YLeaf(YType.enumeration, 'resource'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'DpaTable', '')])),
                                ('sysdb_avail_npu_mask', (YLeaf(YType.uint64, 'sysdb-avail-npu-mask'), ['int'])),
                                ('table_id', (YLeaf(YType.uint32, 'table-id'), ['int'])),
                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                ('is_global', (YLeaf(YType.boolean, 'is-global'), ['bool'])),
                                ('num_npus', (YLeaf(YType.uint32, 'num-npus'), ['int'])),
                                ('table_specific_list', (YLeaf(YType.str, 'table-specific-list'), ['str'])),
                            ])
                            self.resource = None
                            self.sysdb_avail_npu_mask = None
                            self.table_id = None
                            self.name = None
                            self.is_global = None
                            self.num_npus = None
                            self.table_specific_list = None

                            self.npu_tblr = YList(self)
                            self._segment_path = lambda: "table-data" + "[resource='" + str(self.resource) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas.TableData, ['resource', u'sysdb_avail_npu_mask', u'table_id', u'name', u'is_global', u'num_npus', u'table_specific_list'], name, value)


                        class NpuTblr(Entity):
                            """
                            npu tblr
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: num_objs
                            
                            	num objs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: create_req
                            
                            	create req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: create_ok
                            
                            	create ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: delete_req
                            
                            	delete req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: delete_ok
                            
                            	delete ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: update_req
                            
                            	update req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: update_ok
                            
                            	update ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: eod_req
                            
                            	eod req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: eod_ok
                            
                            	eod ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_hw_fail
                            
                            	err hw fail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_ref_resolve
                            
                            	err ref resolve
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_db_notfound
                            
                            	err db notfound
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_db_exists
                            
                            	err db exists
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_db_nomem
                            
                            	err db nomem
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_id_reserve
                            
                            	err id reserve
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_id_release
                            
                            	err id release
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            .. attribute:: err_id_update
                            
                            	err id update
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**config**\: False
                            
                            

                            """

                            _prefix = 'fretta-bcm-dpa-resources-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr, self).__init__()

                                self.yang_name = "npu-tblr"
                                self.yang_parent_name = "table-data"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('npu_id', (YLeaf(YType.uint32, 'npu-id'), ['int'])),
                                    ('num_objs', (YLeaf(YType.uint32, 'num-objs'), ['int'])),
                                    ('create_req', (YLeaf(YType.uint32, 'create-req'), ['int'])),
                                    ('create_ok', (YLeaf(YType.uint32, 'create-ok'), ['int'])),
                                    ('delete_req', (YLeaf(YType.uint32, 'delete-req'), ['int'])),
                                    ('delete_ok', (YLeaf(YType.uint32, 'delete-ok'), ['int'])),
                                    ('update_req', (YLeaf(YType.uint32, 'update-req'), ['int'])),
                                    ('update_ok', (YLeaf(YType.uint32, 'update-ok'), ['int'])),
                                    ('eod_req', (YLeaf(YType.uint32, 'eod-req'), ['int'])),
                                    ('eod_ok', (YLeaf(YType.uint32, 'eod-ok'), ['int'])),
                                    ('err_hw_fail', (YLeaf(YType.uint32, 'err-hw-fail'), ['int'])),
                                    ('err_ref_resolve', (YLeaf(YType.uint32, 'err-ref-resolve'), ['int'])),
                                    ('err_db_notfound', (YLeaf(YType.uint32, 'err-db-notfound'), ['int'])),
                                    ('err_db_exists', (YLeaf(YType.uint32, 'err-db-exists'), ['int'])),
                                    ('err_db_nomem', (YLeaf(YType.uint32, 'err-db-nomem'), ['int'])),
                                    ('err_id_reserve', (YLeaf(YType.uint32, 'err-id-reserve'), ['int'])),
                                    ('err_id_release', (YLeaf(YType.uint32, 'err-id-release'), ['int'])),
                                    ('err_id_update', (YLeaf(YType.uint32, 'err-id-update'), ['int'])),
                                ])
                                self.npu_id = None
                                self.num_objs = None
                                self.create_req = None
                                self.create_ok = None
                                self.delete_req = None
                                self.delete_ok = None
                                self.update_req = None
                                self.update_ok = None
                                self.eod_req = None
                                self.eod_ok = None
                                self.err_hw_fail = None
                                self.err_ref_resolve = None
                                self.err_db_notfound = None
                                self.err_db_exists = None
                                self.err_db_nomem = None
                                self.err_id_reserve = None
                                self.err_id_release = None
                                self.err_id_update = None
                                self._segment_path = lambda: "npu-tblr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr, [u'npu_id', u'num_objs', u'create_req', u'create_ok', u'delete_req', u'delete_ok', u'update_req', u'update_ok', u'eod_req', u'eod_ok', u'err_hw_fail', u'err_ref_resolve', u'err_db_notfound', u'err_db_exists', u'err_db_nomem', u'err_id_reserve', u'err_id_release', u'err_id_update'], name, value)







    def clone_ptr(self):
        self._top_entity = Dpa()
        return self._top_entity



