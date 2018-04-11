""" Cisco_IOS_XR_fretta_bcm_dpa_resources_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fretta\-bcm\-dpa\-resources package operational data.

This module contains definitions
for the following management objects\:
  dpa\: Stats Data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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

    .. data:: mplspwe_port = 17

    	mplspweport

    .. data:: mhpwe_port = 18

    	mhpweport

    .. data:: l2xc = 19

    	l2xc

    .. data:: l2vpnstats = 20

    	l2vpnstats

    .. data:: l1_ports_tats = 21

    	l1portstats

    .. data:: l3intf = 22

    	l3intf

    .. data:: l3intfrxstats = 23

    	l3intfrxstats

    .. data:: ip_route = 24

    	iproute

    .. data:: ip6_route = 25

    	ip6route

    .. data:: punt_policy_stats = 26

    	puntpolicystats

    .. data:: ip_punt_policy = 27

    	ippuntpolicy

    .. data:: ip6_punt_policy = 28

    	ip6puntpolicy

    .. data:: isis_punt_policy = 29

    	isispuntpolicy

    .. data:: ipnh_group = 30

    	ipnhgroup

    .. data:: ip6nh_group = 31

    	ip6nhgroup

    .. data:: ipnh = 32

    	ipnh

    .. data:: ip6nh = 33

    	ip6nh

    .. data:: ipvrf = 34

    	ipvrf

    .. data:: mplsnh = 35

    	mplsnh

    .. data:: mpls_label = 36

    	mplslabel

    .. data:: dnx_trap = 37

    	dnx trap

    .. data:: punt = 38

    	punt

    .. data:: punt_police_r = 39

    	puntpolicer

    .. data:: punt_lpts_police_r = 40

    	puntlptspolicer

    .. data:: punt_stats = 41

    	puntstats

    .. data:: tm_port = 42

    	tmport

    .. data:: span_session = 43

    	spansession

    .. data:: police_rstats = 44

    	policerstats

    .. data:: tm_ports_tats = 45

    	tmportstats

    .. data:: l3intftxstats = 46

    	l3intftxstats

    .. data:: mplstetxstats = 47

    	mplstetxstats

    .. data:: mplslblstats = 48

    	mplslblstats

    .. data:: police_r = 49

    	policer

    .. data:: l2intfrxstats = 50

    	l2intfrxstats

    .. data:: l2intftxstats = 51

    	l2intftxstats

    .. data:: dnx_pbr_tt_ipv4 = 52

    	dnx pbr tt ipv4

    .. data:: dnx_pbr_tt_ipv6 = 53

    	dnx pbr tt ipv6

    .. data:: bfdhwoff = 54

    	bfdhwoff

    .. data:: global_ = 55

    	global

    .. data:: lag_port = 56

    	lagport

    .. data:: qos_profile = 57

    	qosprofile

    .. data:: tmrate_profile = 58

    	tmrateprofile

    .. data:: dnx_port_range = 59

    	dnx port range

    .. data:: ipacl = 60

    	ipacl

    .. data:: ip6acl = 61

    	ip6acl

    .. data:: sched_tree = 62

    	schedtree

    .. data:: tmcos = 63

    	tmcos

    .. data:: statsagg = 64

    	statsagg

    .. data:: nhprotect = 65

    	nhprotect

    .. data:: sampler = 66

    	sampler

    .. data:: l2qos = 67

    	l2qos

    .. data:: peer_qos = 68

    	peerqos

    .. data:: ipqos = 69

    	ipqos

    .. data:: ip6qos = 70

    	ip6qos

    .. data:: mplsqos = 71

    	mplsqos

    .. data:: qosid = 72

    	qosid

    .. data:: extlif = 73

    	extlif

    .. data:: elif_ = 74

    	elif

    .. data:: ingaclstats = 75

    	ingaclstats

    .. data:: egraclstats = 76

    	egraclstats

    .. data:: edpl = 77

    	edpl

    .. data:: cfmmaid = 78

    	cfmmaid

    .. data:: cfmdefmps = 79

    	cfmdefmps

    .. data:: cfmofflmep = 80

    	cfmofflmep

    .. data:: cfmoffrmep = 81

    	cfmoffrmep

    .. data:: cfmnonoff = 82

    	cfmnonoff

    .. data:: cfmhwoffrxstats = 83

    	cfmhwoffrxstats

    .. data:: ipmc_route = 84

    	ipmcroute

    .. data:: l2ipmc_route = 85

    	l2ipmcroute

    .. data:: ipmco_list = 86

    	ipmcolist

    .. data:: l2mco_list = 87

    	l2mcolist

    .. data:: ipmc_merge_do_list = 88

    	ipmcmergedolist

    .. data:: sgfgid_list = 89

    	sgfgidlist

    .. data:: meshmc = 90

    	meshmc

    .. data:: l2_bridge = 91

    	l2bridge

    .. data:: l2_bridge_port = 92

    	l2bridgeport

    .. data:: l2_bridge_mac = 93

    	l2bridgemac

    .. data:: l2brmac = 94

    	l2brmac

    .. data:: ip_tunnel_decap = 95

    	iptunneldecap

    .. data:: l2vlan_range = 96

    	l2vlanrange

    .. data:: ip_tunnel_encap = 97

    	iptunnelencap

    .. data:: rawget = 98

    	rawget

    .. data:: ip6mc_route = 99

    	ip6mcroute

    .. data:: l2evpnact_remote_peer_id = 100

    	l2evpnactremotepeerid

    .. data:: l2evpnact_local_shl = 101

    	l2evpnactlocalshl

    .. data:: l2evpnact_remote_shl = 102

    	l2evpnactremoteshl

    .. data:: evpn_iml_range = 103

    	evpn imlrange

    .. data:: l2_bridge_o_list = 104

    	l2bridgeolist

    .. data:: l2acl = 105

    	l2acl

    .. data:: l2evpn_nh = 106

    	l2evpn nh

    .. data:: l2_bridge_port_sc = 107

    	l2bridgeport sc

    .. data:: l3intfmctxstats = 108

    	l3intfmctxstats

    .. data:: tidl_sample = 109

    	tidl sample

    .. data:: tidl_ref_sample = 110

    	tidl ref sample

    .. data:: ipacl_prefix = 111

    	ipaclprefix

    .. data:: ip6acl_prefix = 112

    	ip6aclprefix

    .. data:: ipacl_port = 113

    	ipaclport

    .. data:: scaleacl = 114

    	scaleacl

    .. data:: ipmcf_hop = 115

    	ipmcfhop

    .. data:: bundle_swoff = 116

    	bundle swoff

    .. data:: mcidswoff = 117

    	mcidswoff

    .. data:: dest_map = 118

    	destmap

    .. data:: l2_bridge_port_pw = 119

    	l2bridgeport pw

    .. data:: l2evpnact_local_shlstats = 120

    	l2evpnactlocalshlstats

    .. data:: test_hidden = 121

    	testhidden

    .. data:: test_local = 122

    	testlocal

    .. data:: test_repeated = 123

    	testrepeated

    .. data:: limd = 124

    	limd

    .. data:: litap = 125

    	litap

    .. data:: test_xtf = 126

    	test xtf

    .. data:: ipmcrxstats = 127

    	ipmcrxstats

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

    mplspwe_port = Enum.YLeaf(17, "mplspwe-port")

    mhpwe_port = Enum.YLeaf(18, "mhpwe-port")

    l2xc = Enum.YLeaf(19, "l2xc")

    l2vpnstats = Enum.YLeaf(20, "l2vpnstats")

    l1_ports_tats = Enum.YLeaf(21, "l1-ports-tats")

    l3intf = Enum.YLeaf(22, "l3intf")

    l3intfrxstats = Enum.YLeaf(23, "l3intfrxstats")

    ip_route = Enum.YLeaf(24, "ip-route")

    ip6_route = Enum.YLeaf(25, "ip6-route")

    punt_policy_stats = Enum.YLeaf(26, "punt-policy-stats")

    ip_punt_policy = Enum.YLeaf(27, "ip-punt-policy")

    ip6_punt_policy = Enum.YLeaf(28, "ip6-punt-policy")

    isis_punt_policy = Enum.YLeaf(29, "isis-punt-policy")

    ipnh_group = Enum.YLeaf(30, "ipnh-group")

    ip6nh_group = Enum.YLeaf(31, "ip6nh-group")

    ipnh = Enum.YLeaf(32, "ipnh")

    ip6nh = Enum.YLeaf(33, "ip6nh")

    ipvrf = Enum.YLeaf(34, "ipvrf")

    mplsnh = Enum.YLeaf(35, "mplsnh")

    mpls_label = Enum.YLeaf(36, "mpls-label")

    dnx_trap = Enum.YLeaf(37, "dnx-trap")

    punt = Enum.YLeaf(38, "punt")

    punt_police_r = Enum.YLeaf(39, "punt-police-r")

    punt_lpts_police_r = Enum.YLeaf(40, "punt-lpts-police-r")

    punt_stats = Enum.YLeaf(41, "punt-stats")

    tm_port = Enum.YLeaf(42, "tm-port")

    span_session = Enum.YLeaf(43, "span-session")

    police_rstats = Enum.YLeaf(44, "police-rstats")

    tm_ports_tats = Enum.YLeaf(45, "tm-ports-tats")

    l3intftxstats = Enum.YLeaf(46, "l3intftxstats")

    mplstetxstats = Enum.YLeaf(47, "mplstetxstats")

    mplslblstats = Enum.YLeaf(48, "mplslblstats")

    police_r = Enum.YLeaf(49, "police-r")

    l2intfrxstats = Enum.YLeaf(50, "l2intfrxstats")

    l2intftxstats = Enum.YLeaf(51, "l2intftxstats")

    dnx_pbr_tt_ipv4 = Enum.YLeaf(52, "dnx-pbr-tt-ipv4")

    dnx_pbr_tt_ipv6 = Enum.YLeaf(53, "dnx-pbr-tt-ipv6")

    bfdhwoff = Enum.YLeaf(54, "bfdhwoff")

    global_ = Enum.YLeaf(55, "global")

    lag_port = Enum.YLeaf(56, "lag-port")

    qos_profile = Enum.YLeaf(57, "qos-profile")

    tmrate_profile = Enum.YLeaf(58, "tmrate-profile")

    dnx_port_range = Enum.YLeaf(59, "dnx-port-range")

    ipacl = Enum.YLeaf(60, "ipacl")

    ip6acl = Enum.YLeaf(61, "ip6acl")

    sched_tree = Enum.YLeaf(62, "sched-tree")

    tmcos = Enum.YLeaf(63, "tmcos")

    statsagg = Enum.YLeaf(64, "statsagg")

    nhprotect = Enum.YLeaf(65, "nhprotect")

    sampler = Enum.YLeaf(66, "sampler")

    l2qos = Enum.YLeaf(67, "l2qos")

    peer_qos = Enum.YLeaf(68, "peer-qos")

    ipqos = Enum.YLeaf(69, "ipqos")

    ip6qos = Enum.YLeaf(70, "ip6qos")

    mplsqos = Enum.YLeaf(71, "mplsqos")

    qosid = Enum.YLeaf(72, "qosid")

    extlif = Enum.YLeaf(73, "extlif")

    elif_ = Enum.YLeaf(74, "elif")

    ingaclstats = Enum.YLeaf(75, "ingaclstats")

    egraclstats = Enum.YLeaf(76, "egraclstats")

    edpl = Enum.YLeaf(77, "edpl")

    cfmmaid = Enum.YLeaf(78, "cfmmaid")

    cfmdefmps = Enum.YLeaf(79, "cfmdefmps")

    cfmofflmep = Enum.YLeaf(80, "cfmofflmep")

    cfmoffrmep = Enum.YLeaf(81, "cfmoffrmep")

    cfmnonoff = Enum.YLeaf(82, "cfmnonoff")

    cfmhwoffrxstats = Enum.YLeaf(83, "cfmhwoffrxstats")

    ipmc_route = Enum.YLeaf(84, "ipmc-route")

    l2ipmc_route = Enum.YLeaf(85, "l2ipmc-route")

    ipmco_list = Enum.YLeaf(86, "ipmco-list")

    l2mco_list = Enum.YLeaf(87, "l2mco-list")

    ipmc_merge_do_list = Enum.YLeaf(88, "ipmc-merge-do-list")

    sgfgid_list = Enum.YLeaf(89, "sgfgid-list")

    meshmc = Enum.YLeaf(90, "meshmc")

    l2_bridge = Enum.YLeaf(91, "l2-bridge")

    l2_bridge_port = Enum.YLeaf(92, "l2-bridge-port")

    l2_bridge_mac = Enum.YLeaf(93, "l2-bridge-mac")

    l2brmac = Enum.YLeaf(94, "l2brmac")

    ip_tunnel_decap = Enum.YLeaf(95, "ip-tunnel-decap")

    l2vlan_range = Enum.YLeaf(96, "l2vlan-range")

    ip_tunnel_encap = Enum.YLeaf(97, "ip-tunnel-encap")

    rawget = Enum.YLeaf(98, "rawget")

    ip6mc_route = Enum.YLeaf(99, "ip6mc-route")

    l2evpnact_remote_peer_id = Enum.YLeaf(100, "l2evpnact-remote-peer-id")

    l2evpnact_local_shl = Enum.YLeaf(101, "l2evpnact-local-shl")

    l2evpnact_remote_shl = Enum.YLeaf(102, "l2evpnact-remote-shl")

    evpn_iml_range = Enum.YLeaf(103, "evpn-iml-range")

    l2_bridge_o_list = Enum.YLeaf(104, "l2-bridge-o-list")

    l2acl = Enum.YLeaf(105, "l2acl")

    l2evpn_nh = Enum.YLeaf(106, "l2evpn-nh")

    l2_bridge_port_sc = Enum.YLeaf(107, "l2-bridge-port-sc")

    l3intfmctxstats = Enum.YLeaf(108, "l3intfmctxstats")

    tidl_sample = Enum.YLeaf(109, "tidl-sample")

    tidl_ref_sample = Enum.YLeaf(110, "tidl-ref-sample")

    ipacl_prefix = Enum.YLeaf(111, "ipacl-prefix")

    ip6acl_prefix = Enum.YLeaf(112, "ip6acl-prefix")

    ipacl_port = Enum.YLeaf(113, "ipacl-port")

    scaleacl = Enum.YLeaf(114, "scaleacl")

    ipmcf_hop = Enum.YLeaf(115, "ipmcf-hop")

    bundle_swoff = Enum.YLeaf(116, "bundle-swoff")

    mcidswoff = Enum.YLeaf(117, "mcidswoff")

    dest_map = Enum.YLeaf(118, "dest-map")

    l2_bridge_port_pw = Enum.YLeaf(119, "l2-bridge-port-pw")

    l2evpnact_local_shlstats = Enum.YLeaf(120, "l2evpnact-local-shlstats")

    test_hidden = Enum.YLeaf(121, "test-hidden")

    test_local = Enum.YLeaf(122, "test-local")

    test_repeated = Enum.YLeaf(123, "test-repeated")

    limd = Enum.YLeaf(124, "limd")

    litap = Enum.YLeaf(125, "litap")

    test_xtf = Enum.YLeaf(126, "test-xtf")

    ipmcrxstats = Enum.YLeaf(127, "ipmcrxstats")



class Dpa(Entity):
    """
    Stats Data
    
    .. attribute:: resources
    
    	DPA Resources Data
    	**type**\:  :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources>`
    
    .. attribute:: stats
    
    	Voq or Trap Data
    	**type**\:  :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats>`
    
    

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
        self._child_container_classes = OrderedDict([("resources", ("resources", Dpa.Resources)), ("stats", ("stats", Dpa.Stats))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.resources = Dpa.Resources()
        self.resources.parent = self
        self._children_name_map["resources"] = "resources"
        self._children_yang_names.add("resources")

        self.stats = Dpa.Stats()
        self.stats.parent = self
        self._children_name_map["stats"] = "stats"
        self._children_yang_names.add("stats")
        self._segment_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa"


    class Resources(Entity):
        """
        DPA Resources Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes>`
        
        

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
            self._child_container_classes = OrderedDict([("nodes", ("nodes", Dpa.Resources.Nodes))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.nodes = Dpa.Resources.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "resources"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/%s" % self._segment_path()


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node>`
            
            

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("node", ("node", Dpa.Resources.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/resources/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Resources.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: table_datas
                
                	DPA Resources table
                	**type**\:  :py:class:`TableDatas <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas>`
                
                

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
                    self._child_container_classes = OrderedDict([("table-datas", ("table_datas", Dpa.Resources.Nodes.Node.TableDatas))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_name', YLeaf(YType.str, 'node-name')),
                    ])
                    self.node_name = None

                    self.table_datas = Dpa.Resources.Nodes.Node.TableDatas()
                    self.table_datas.parent = self
                    self._children_name_map["table_datas"] = "table-datas"
                    self._children_yang_names.add("table-datas")
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/resources/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Resources.Nodes.Node, ['node_name'], name, value)


                class TableDatas(Entity):
                    """
                    DPA Resources table
                    
                    .. attribute:: table_data
                    
                    	DPA Resources table
                    	**type**\: list of  		 :py:class:`TableData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData>`
                    
                    

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
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("table-data", ("table_data", Dpa.Resources.Nodes.Node.TableDatas.TableData))])
                        self._leafs = OrderedDict()

                        self.table_data = YList(self)
                        self._segment_path = lambda: "table-datas"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas, [], name, value)


                    class TableData(Entity):
                        """
                        DPA Resources table
                        
                        .. attribute:: resource  (key)
                        
                        	Resource type
                        	**type**\:  :py:class:`DpaTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.DpaTable>`
                        
                        .. attribute:: table_id
                        
                        	table id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: name
                        
                        	name
                        	**type**\: str
                        
                        	**length:** 0..64
                        
                        .. attribute:: is_global
                        
                        	is global
                        	**type**\: bool
                        
                        .. attribute:: num_npus
                        
                        	num npus
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: table_specific_list
                        
                        	table specific list
                        	**type**\: str
                        
                        .. attribute:: npu_tblr
                        
                        	npu tblr
                        	**type**\: list of  		 :py:class:`NpuTblr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr>`
                        
                        

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
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("npu-tblr", ("npu_tblr", Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr))])
                            self._leafs = OrderedDict([
                                ('resource', YLeaf(YType.enumeration, 'resource')),
                                ('table_id', YLeaf(YType.uint32, 'table-id')),
                                ('name', YLeaf(YType.str, 'name')),
                                ('is_global', YLeaf(YType.boolean, 'is-global')),
                                ('num_npus', YLeaf(YType.uint32, 'num-npus')),
                                ('table_specific_list', YLeaf(YType.str, 'table-specific-list')),
                            ])
                            self.resource = None
                            self.table_id = None
                            self.name = None
                            self.is_global = None
                            self.num_npus = None
                            self.table_specific_list = None

                            self.npu_tblr = YList(self)
                            self._segment_path = lambda: "table-data" + "[resource='" + str(self.resource) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas.TableData, ['resource', 'table_id', 'name', 'is_global', 'num_npus', 'table_specific_list'], name, value)


                        class NpuTblr(Entity):
                            """
                            npu tblr
                            
                            .. attribute:: npu_id
                            
                            	npu id
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_objs
                            
                            	num objs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: create_req
                            
                            	create req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: create_ok
                            
                            	create ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delete_req
                            
                            	delete req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delete_ok
                            
                            	delete ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: update_req
                            
                            	update req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: update_ok
                            
                            	update ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: eod_req
                            
                            	eod req
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: eod_ok
                            
                            	eod ok
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_hw_fail
                            
                            	err hw fail
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_ref_resolve
                            
                            	err ref resolve
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_notfound
                            
                            	err db notfound
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_exists
                            
                            	err db exists
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: err_db_nomem
                            
                            	err db nomem
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

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
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('npu_id', YLeaf(YType.uint32, 'npu-id')),
                                    ('num_objs', YLeaf(YType.uint32, 'num-objs')),
                                    ('create_req', YLeaf(YType.uint32, 'create-req')),
                                    ('create_ok', YLeaf(YType.uint32, 'create-ok')),
                                    ('delete_req', YLeaf(YType.uint32, 'delete-req')),
                                    ('delete_ok', YLeaf(YType.uint32, 'delete-ok')),
                                    ('update_req', YLeaf(YType.uint32, 'update-req')),
                                    ('update_ok', YLeaf(YType.uint32, 'update-ok')),
                                    ('eod_req', YLeaf(YType.uint32, 'eod-req')),
                                    ('eod_ok', YLeaf(YType.uint32, 'eod-ok')),
                                    ('err_hw_fail', YLeaf(YType.uint32, 'err-hw-fail')),
                                    ('err_ref_resolve', YLeaf(YType.uint32, 'err-ref-resolve')),
                                    ('err_db_notfound', YLeaf(YType.uint32, 'err-db-notfound')),
                                    ('err_db_exists', YLeaf(YType.uint32, 'err-db-exists')),
                                    ('err_db_nomem', YLeaf(YType.uint32, 'err-db-nomem')),
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
                                self._segment_path = lambda: "npu-tblr"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr, ['npu_id', 'num_objs', 'create_req', 'create_ok', 'delete_req', 'delete_ok', 'update_req', 'update_ok', 'eod_req', 'eod_ok', 'err_hw_fail', 'err_ref_resolve', 'err_db_notfound', 'err_db_exists', 'err_db_nomem'], name, value)


    class Stats(Entity):
        """
        Voq or Trap Data
        
        .. attribute:: nodes
        
        	DPA data for available nodes
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes>`
        
        

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
            self._child_container_classes = OrderedDict([("nodes", ("nodes", Dpa.Stats.Nodes))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.nodes = Dpa.Stats.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")
            self._segment_path = lambda: "stats"
            self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/%s" % self._segment_path()


        class Nodes(Entity):
            """
            DPA data for available nodes
            
            .. attribute:: node
            
            	DPA operational data for a particular node
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node>`
            
            

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
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("node", ("node", Dpa.Stats.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/stats/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Dpa.Stats.Nodes, [], name, value)


            class Node(Entity):
                """
                DPA operational data for a particular node
                
                .. attribute:: node_name  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: asic_statistics
                
                	ASIC statistics table
                	**type**\:  :py:class:`AsicStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics>`
                
                .. attribute:: npu_numbers
                
                	Ingress Stats
                	**type**\:  :py:class:`NpuNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers>`
                
                

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
                    self._child_container_classes = OrderedDict([("asic-statistics", ("asic_statistics", Dpa.Stats.Nodes.Node.AsicStatistics)), ("npu-numbers", ("npu_numbers", Dpa.Stats.Nodes.Node.NpuNumbers))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('node_name', YLeaf(YType.str, 'node-name')),
                    ])
                    self.node_name = None

                    self.asic_statistics = Dpa.Stats.Nodes.Node.AsicStatistics()
                    self.asic_statistics.parent = self
                    self._children_name_map["asic_statistics"] = "asic-statistics"
                    self._children_yang_names.add("asic-statistics")

                    self.npu_numbers = Dpa.Stats.Nodes.Node.NpuNumbers()
                    self.npu_numbers.parent = self
                    self._children_name_map["npu_numbers"] = "npu-numbers"
                    self._children_yang_names.add("npu-numbers")
                    self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fretta-bcm-dpa-resources-oper:dpa/stats/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Dpa.Stats.Nodes.Node, ['node_name'], name, value)


                class AsicStatistics(Entity):
                    """
                    ASIC statistics table
                    
                    .. attribute:: asic_statistics_for_npu_ids
                    
                    	ASIC statistics
                    	**type**\:  :py:class:`AsicStatisticsForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds>`
                    
                    .. attribute:: asic_statistics_detail_for_npu_ids
                    
                    	Detailed ASIC statistics
                    	**type**\:  :py:class:`AsicStatisticsDetailForNpuIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds>`
                    
                    

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
                        self._child_container_classes = OrderedDict([("asic-statistics-for-npu-ids", ("asic_statistics_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds)), ("asic-statistics-detail-for-npu-ids", ("asic_statistics_detail_for_npu_ids", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict()

                        self.asic_statistics_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds()
                        self.asic_statistics_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_for_npu_ids"] = "asic-statistics-for-npu-ids"
                        self._children_yang_names.add("asic-statistics-for-npu-ids")

                        self.asic_statistics_detail_for_npu_ids = Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds()
                        self.asic_statistics_detail_for_npu_ids.parent = self
                        self._children_name_map["asic_statistics_detail_for_npu_ids"] = "asic-statistics-detail-for-npu-ids"
                        self._children_yang_names.add("asic-statistics-detail-for-npu-ids")
                        self._segment_path = lambda: "asic-statistics"


                    class AsicStatisticsForNpuIds(Entity):
                        """
                        ASIC statistics
                        
                        .. attribute:: asic_statistics_for_npu_id
                        
                        	ASIC statistics for a particular NPU
                        	**type**\: list of  		 :py:class:`AsicStatisticsForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId>`
                        
                        

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
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("asic-statistics-for-npu-id", ("asic_statistics_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId))])
                            self._leafs = OrderedDict()

                            self.asic_statistics_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-for-npu-ids"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds, [], name, value)


                        class AsicStatisticsForNpuId(Entity):
                            """
                            ASIC statistics for a particular NPU
                            
                            .. attribute:: npu_id  (key)
                            
                            	NPU number
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics>`
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\: bool
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

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
                                self._child_container_classes = OrderedDict([("statistics", ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('npu_id', YLeaf(YType.int32, 'npu-id')),
                                    ('valid', YLeaf(YType.boolean, 'valid')),
                                    ('rack_number', YLeaf(YType.uint32, 'rack-number')),
                                    ('slot_number', YLeaf(YType.uint32, 'slot-number')),
                                    ('asic_instance', YLeaf(YType.uint32, 'asic-instance')),
                                    ('chip_version', YLeaf(YType.uint16, 'chip-version')),
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
                                self._children_yang_names.add("statistics")
                                self._segment_path = lambda: "asic-statistics-for-npu-id" + "[npu-id='" + str(self.npu_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId, ['npu_id', 'valid', 'rack_number', 'slot_number', 'asic_instance', 'chip_version'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: nbi_rx_total_byte_cnt
                                
                                	Total bytes sent from NIF to IRE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_rx_total_pkt_cnt
                                
                                	Total packets sent from NIF to IRE
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_cpu_pkt_cnt
                                
                                	CPU ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_nif_pkt_cnt
                                
                                	NIF received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_oamp_pkt_cnt
                                
                                	OAMP ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_olp_pkt_cnt
                                
                                	OLP ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_rcy_pkt_cnt
                                
                                	Recycling ingress received packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ire_fdt_if_cnt
                                
                                	Performance counter of the FDT interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: idr_mmu_if_cnt
                                
                                	Performance counter of the MMU interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: idr_ocb_if_cnt
                                
                                	Performance counter of the OCB interface
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_enqueue_pkt_cnt
                                
                                	Counts enqueued packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_dequeue_pkt_cnt
                                
                                	Counts dequeued packets
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_deleted_pkt_cnt
                                
                                	Counts matched packets discarded in the DEQ process
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: iqm_enq_discarded_pkt_cnt
                                
                                	Counts all packets discarded at the ENQ pipe
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_egq_pkt_cnt
                                
                                	EGQ packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_enq_pkt_cnt
                                
                                	ENQ packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_fdt_pkt_cnt
                                
                                	FDT packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_cfg_event_cnt
                                
                                	Configurable event counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: ipt_cfg_byte_cnt
                                
                                	Configurable bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: fdt_ipt_desc_cell_cnt
                                
                                	Descriptor cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_ire_desc_cell_cnt
                                
                                	IRE internal descriptor cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdt_transmitted_data_cells_cnt
                                
                                	Counts all transmitted data cells
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p1_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p2_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_p3_cell_in_cnt
                                
                                	FDR total incoming cell counter at pipe 3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fdr_cell_in_cnt_total
                                
                                	FDR total incoming cell counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p1
                                
                                	FDA input cell counter P1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p2
                                
                                	FDA input cell counter P2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_cnt_p3
                                
                                	FDA input cell counter P3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_tdm_cnt
                                
                                	FDA input cell counter TDM
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_meshmc_cnt
                                
                                	FDA input cell counter MESHMC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_in_ipt_cnt
                                
                                	FDA input cell counter IPT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p1
                                
                                	FDA output cell counter P1
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p2
                                
                                	FDA output cell counter P2
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_cnt_p3
                                
                                	FDA output cell counter P3
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_tdm_cnt
                                
                                	FDA output cell counter TDM
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_meshmc_cnt
                                
                                	FDA output cell counter MESHMC
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_cells_out_ipt_cnt
                                
                                	FDA output cell counter IPT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_egq_drop_cnt
                                
                                	FDA EGQ drop counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: fda_egq_meshmc_drop_cnt
                                
                                	FDA EGQ MESHMC drop counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_fqp_pkt_cnt
                                
                                	FQP2EPE packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_uc_pkt_cnt
                                
                                	PQP2FQP unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_discard_uc_pkt_cnt
                                
                                	PQP discarded unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_uc_bytes_cnt
                                
                                	PQP2FQP unicast bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_pqp_mc_pkt_cnt
                                
                                	PQP2FQP multicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_discard_mc_pkt_cnt
                                
                                	PQP discarded multicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_pqp_mc_bytes_cnt
                                
                                	PQP2FQP multicast bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: egq_ehp_uc_pkt_cnt
                                
                                	EHP2PQP unicast packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_high_pkt_cnt
                                
                                	EHP2PQP multicast high packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_low_pkt_cnt
                                
                                	EHP2PQP multicast low packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_deleted_pkt_cnt
                                
                                	EHP2PQP discarded packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_high_discard_cnt
                                
                                	Number of multicast high packets discarded because multicast FIFO is full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_ehp_mc_low_discard_cnt
                                
                                	Number of multicast low packets discarded because multicast FIFO is full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_lag_pruning_discard_cnt
                                
                                	Number of packet descriptors discarded due to LAG multicast pruning
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_pmf_discard_cnt
                                
                                	Number of packet descriptors discarded due to ERPP PMF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: egq_erpp_vlan_mbr_discard_cnt
                                
                                	Number of packet descriptors discarded because of egress VLAN membership
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: epni_epe_byte_cnt
                                
                                	EPE2PNI bytes counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: epni_epe_pkt_cnt
                                
                                	EPE2PNI packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: epni_epe_discard_cnt
                                
                                	EPE discarded packet counter
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: nbi_tx_total_byte_cnt
                                
                                	Total bytes sent from EGQ to NIF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: nbi_tx_total_pkt_cnt
                                
                                	Total packets sent from EGQ to NIF
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('nbi_rx_total_byte_cnt', YLeaf(YType.uint64, 'nbi-rx-total-byte-cnt')),
                                        ('nbi_rx_total_pkt_cnt', YLeaf(YType.uint64, 'nbi-rx-total-pkt-cnt')),
                                        ('ire_cpu_pkt_cnt', YLeaf(YType.uint64, 'ire-cpu-pkt-cnt')),
                                        ('ire_nif_pkt_cnt', YLeaf(YType.uint64, 'ire-nif-pkt-cnt')),
                                        ('ire_oamp_pkt_cnt', YLeaf(YType.uint64, 'ire-oamp-pkt-cnt')),
                                        ('ire_olp_pkt_cnt', YLeaf(YType.uint64, 'ire-olp-pkt-cnt')),
                                        ('ire_rcy_pkt_cnt', YLeaf(YType.uint64, 'ire-rcy-pkt-cnt')),
                                        ('ire_fdt_if_cnt', YLeaf(YType.uint64, 'ire-fdt-if-cnt')),
                                        ('idr_mmu_if_cnt', YLeaf(YType.uint64, 'idr-mmu-if-cnt')),
                                        ('idr_ocb_if_cnt', YLeaf(YType.uint64, 'idr-ocb-if-cnt')),
                                        ('iqm_enqueue_pkt_cnt', YLeaf(YType.uint64, 'iqm-enqueue-pkt-cnt')),
                                        ('iqm_dequeue_pkt_cnt', YLeaf(YType.uint64, 'iqm-dequeue-pkt-cnt')),
                                        ('iqm_deleted_pkt_cnt', YLeaf(YType.uint64, 'iqm-deleted-pkt-cnt')),
                                        ('iqm_enq_discarded_pkt_cnt', YLeaf(YType.uint64, 'iqm-enq-discarded-pkt-cnt')),
                                        ('ipt_egq_pkt_cnt', YLeaf(YType.uint64, 'ipt-egq-pkt-cnt')),
                                        ('ipt_enq_pkt_cnt', YLeaf(YType.uint64, 'ipt-enq-pkt-cnt')),
                                        ('ipt_fdt_pkt_cnt', YLeaf(YType.uint64, 'ipt-fdt-pkt-cnt')),
                                        ('ipt_cfg_event_cnt', YLeaf(YType.uint64, 'ipt-cfg-event-cnt')),
                                        ('ipt_cfg_byte_cnt', YLeaf(YType.uint64, 'ipt-cfg-byte-cnt')),
                                        ('fdt_ipt_desc_cell_cnt', YLeaf(YType.uint64, 'fdt-ipt-desc-cell-cnt')),
                                        ('fdt_ire_desc_cell_cnt', YLeaf(YType.uint64, 'fdt-ire-desc-cell-cnt')),
                                        ('fdt_transmitted_data_cells_cnt', YLeaf(YType.uint64, 'fdt-transmitted-data-cells-cnt')),
                                        ('fdr_p1_cell_in_cnt', YLeaf(YType.uint64, 'fdr-p1-cell-in-cnt')),
                                        ('fdr_p2_cell_in_cnt', YLeaf(YType.uint64, 'fdr-p2-cell-in-cnt')),
                                        ('fdr_p3_cell_in_cnt', YLeaf(YType.uint64, 'fdr-p3-cell-in-cnt')),
                                        ('fdr_cell_in_cnt_total', YLeaf(YType.uint64, 'fdr-cell-in-cnt-total')),
                                        ('fda_cells_in_cnt_p1', YLeaf(YType.uint64, 'fda-cells-in-cnt-p1')),
                                        ('fda_cells_in_cnt_p2', YLeaf(YType.uint64, 'fda-cells-in-cnt-p2')),
                                        ('fda_cells_in_cnt_p3', YLeaf(YType.uint64, 'fda-cells-in-cnt-p3')),
                                        ('fda_cells_in_tdm_cnt', YLeaf(YType.uint64, 'fda-cells-in-tdm-cnt')),
                                        ('fda_cells_in_meshmc_cnt', YLeaf(YType.uint64, 'fda-cells-in-meshmc-cnt')),
                                        ('fda_cells_in_ipt_cnt', YLeaf(YType.uint64, 'fda-cells-in-ipt-cnt')),
                                        ('fda_cells_out_cnt_p1', YLeaf(YType.uint64, 'fda-cells-out-cnt-p1')),
                                        ('fda_cells_out_cnt_p2', YLeaf(YType.uint64, 'fda-cells-out-cnt-p2')),
                                        ('fda_cells_out_cnt_p3', YLeaf(YType.uint64, 'fda-cells-out-cnt-p3')),
                                        ('fda_cells_out_tdm_cnt', YLeaf(YType.uint64, 'fda-cells-out-tdm-cnt')),
                                        ('fda_cells_out_meshmc_cnt', YLeaf(YType.uint64, 'fda-cells-out-meshmc-cnt')),
                                        ('fda_cells_out_ipt_cnt', YLeaf(YType.uint64, 'fda-cells-out-ipt-cnt')),
                                        ('fda_egq_drop_cnt', YLeaf(YType.uint64, 'fda-egq-drop-cnt')),
                                        ('fda_egq_meshmc_drop_cnt', YLeaf(YType.uint64, 'fda-egq-meshmc-drop-cnt')),
                                        ('egq_fqp_pkt_cnt', YLeaf(YType.uint64, 'egq-fqp-pkt-cnt')),
                                        ('egq_pqp_uc_pkt_cnt', YLeaf(YType.uint64, 'egq-pqp-uc-pkt-cnt')),
                                        ('egq_pqp_discard_uc_pkt_cnt', YLeaf(YType.uint64, 'egq-pqp-discard-uc-pkt-cnt')),
                                        ('egq_pqp_uc_bytes_cnt', YLeaf(YType.uint64, 'egq-pqp-uc-bytes-cnt')),
                                        ('egq_pqp_mc_pkt_cnt', YLeaf(YType.uint64, 'egq-pqp-mc-pkt-cnt')),
                                        ('egq_pqp_discard_mc_pkt_cnt', YLeaf(YType.uint64, 'egq-pqp-discard-mc-pkt-cnt')),
                                        ('egq_pqp_mc_bytes_cnt', YLeaf(YType.uint64, 'egq-pqp-mc-bytes-cnt')),
                                        ('egq_ehp_uc_pkt_cnt', YLeaf(YType.uint64, 'egq-ehp-uc-pkt-cnt')),
                                        ('egq_ehp_mc_high_pkt_cnt', YLeaf(YType.uint64, 'egq-ehp-mc-high-pkt-cnt')),
                                        ('egq_ehp_mc_low_pkt_cnt', YLeaf(YType.uint64, 'egq-ehp-mc-low-pkt-cnt')),
                                        ('egq_deleted_pkt_cnt', YLeaf(YType.uint64, 'egq-deleted-pkt-cnt')),
                                        ('egq_ehp_mc_high_discard_cnt', YLeaf(YType.uint64, 'egq-ehp-mc-high-discard-cnt')),
                                        ('egq_ehp_mc_low_discard_cnt', YLeaf(YType.uint64, 'egq-ehp-mc-low-discard-cnt')),
                                        ('egq_erpp_lag_pruning_discard_cnt', YLeaf(YType.uint64, 'egq-erpp-lag-pruning-discard-cnt')),
                                        ('egq_erpp_pmf_discard_cnt', YLeaf(YType.uint64, 'egq-erpp-pmf-discard-cnt')),
                                        ('egq_erpp_vlan_mbr_discard_cnt', YLeaf(YType.uint64, 'egq-erpp-vlan-mbr-discard-cnt')),
                                        ('epni_epe_byte_cnt', YLeaf(YType.uint64, 'epni-epe-byte-cnt')),
                                        ('epni_epe_pkt_cnt', YLeaf(YType.uint64, 'epni-epe-pkt-cnt')),
                                        ('epni_epe_discard_cnt', YLeaf(YType.uint64, 'epni-epe-discard-cnt')),
                                        ('nbi_tx_total_byte_cnt', YLeaf(YType.uint64, 'nbi-tx-total-byte-cnt')),
                                        ('nbi_tx_total_pkt_cnt', YLeaf(YType.uint64, 'nbi-tx-total-pkt-cnt')),
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

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsForNpuIds.AsicStatisticsForNpuId.Statistics, ['nbi_rx_total_byte_cnt', 'nbi_rx_total_pkt_cnt', 'ire_cpu_pkt_cnt', 'ire_nif_pkt_cnt', 'ire_oamp_pkt_cnt', 'ire_olp_pkt_cnt', 'ire_rcy_pkt_cnt', 'ire_fdt_if_cnt', 'idr_mmu_if_cnt', 'idr_ocb_if_cnt', 'iqm_enqueue_pkt_cnt', 'iqm_dequeue_pkt_cnt', 'iqm_deleted_pkt_cnt', 'iqm_enq_discarded_pkt_cnt', 'ipt_egq_pkt_cnt', 'ipt_enq_pkt_cnt', 'ipt_fdt_pkt_cnt', 'ipt_cfg_event_cnt', 'ipt_cfg_byte_cnt', 'fdt_ipt_desc_cell_cnt', 'fdt_ire_desc_cell_cnt', 'fdt_transmitted_data_cells_cnt', 'fdr_p1_cell_in_cnt', 'fdr_p2_cell_in_cnt', 'fdr_p3_cell_in_cnt', 'fdr_cell_in_cnt_total', 'fda_cells_in_cnt_p1', 'fda_cells_in_cnt_p2', 'fda_cells_in_cnt_p3', 'fda_cells_in_tdm_cnt', 'fda_cells_in_meshmc_cnt', 'fda_cells_in_ipt_cnt', 'fda_cells_out_cnt_p1', 'fda_cells_out_cnt_p2', 'fda_cells_out_cnt_p3', 'fda_cells_out_tdm_cnt', 'fda_cells_out_meshmc_cnt', 'fda_cells_out_ipt_cnt', 'fda_egq_drop_cnt', 'fda_egq_meshmc_drop_cnt', 'egq_fqp_pkt_cnt', 'egq_pqp_uc_pkt_cnt', 'egq_pqp_discard_uc_pkt_cnt', 'egq_pqp_uc_bytes_cnt', 'egq_pqp_mc_pkt_cnt', 'egq_pqp_discard_mc_pkt_cnt', 'egq_pqp_mc_bytes_cnt', 'egq_ehp_uc_pkt_cnt', 'egq_ehp_mc_high_pkt_cnt', 'egq_ehp_mc_low_pkt_cnt', 'egq_deleted_pkt_cnt', 'egq_ehp_mc_high_discard_cnt', 'egq_ehp_mc_low_discard_cnt', 'egq_erpp_lag_pruning_discard_cnt', 'egq_erpp_pmf_discard_cnt', 'egq_erpp_vlan_mbr_discard_cnt', 'epni_epe_byte_cnt', 'epni_epe_pkt_cnt', 'epni_epe_discard_cnt', 'nbi_tx_total_byte_cnt', 'nbi_tx_total_pkt_cnt'], name, value)


                    class AsicStatisticsDetailForNpuIds(Entity):
                        """
                        Detailed ASIC statistics
                        
                        .. attribute:: asic_statistics_detail_for_npu_id
                        
                        	Detailed ASIC statistics for a particular NPU
                        	**type**\: list of  		 :py:class:`AsicStatisticsDetailForNpuId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId>`
                        
                        

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
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("asic-statistics-detail-for-npu-id", ("asic_statistics_detail_for_npu_id", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId))])
                            self._leafs = OrderedDict()

                            self.asic_statistics_detail_for_npu_id = YList(self)
                            self._segment_path = lambda: "asic-statistics-detail-for-npu-ids"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds, [], name, value)


                        class AsicStatisticsDetailForNpuId(Entity):
                            """
                            Detailed ASIC statistics for a particular
                            NPU
                            
                            .. attribute:: npu_id  (key)
                            
                            	NPU number
                            	**type**\: int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: statistics
                            
                            	Statistics
                            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics>`
                            
                            .. attribute:: valid
                            
                            	Flag to indicate if data is valid
                            	**type**\: bool
                            
                            .. attribute:: rack_number
                            
                            	Rack number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slot_number
                            
                            	Slot number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: asic_instance
                            
                            	ASIC instance
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: chip_version
                            
                            	Chip version
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

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
                                self._child_container_classes = OrderedDict([("statistics", ("statistics", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('npu_id', YLeaf(YType.int32, 'npu-id')),
                                    ('valid', YLeaf(YType.boolean, 'valid')),
                                    ('rack_number', YLeaf(YType.uint32, 'rack-number')),
                                    ('slot_number', YLeaf(YType.uint32, 'slot-number')),
                                    ('asic_instance', YLeaf(YType.uint32, 'asic-instance')),
                                    ('chip_version', YLeaf(YType.uint16, 'chip-version')),
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
                                self._children_yang_names.add("statistics")
                                self._segment_path = lambda: "asic-statistics-detail-for-npu-id" + "[npu-id='" + str(self.npu_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId, ['npu_id', 'valid', 'rack_number', 'slot_number', 'asic_instance', 'chip_version'], name, value)


                            class Statistics(Entity):
                                """
                                Statistics
                                
                                .. attribute:: num_blocks
                                
                                	Number of blocks
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: block_info
                                
                                	Block information
                                	**type**\: list of  		 :py:class:`BlockInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo>`
                                
                                

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("block-info", ("block_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo))])
                                    self._leafs = OrderedDict([
                                        ('num_blocks', YLeaf(YType.uint8, 'num-blocks')),
                                    ])
                                    self.num_blocks = None

                                    self.block_info = YList(self)
                                    self._segment_path = lambda: "statistics"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics, ['num_blocks'], name, value)


                                class BlockInfo(Entity):
                                    """
                                    Block information
                                    
                                    .. attribute:: block_name
                                    
                                    	Block name
                                    	**type**\: str
                                    
                                    	**length:** 0..10
                                    
                                    .. attribute:: num_fields
                                    
                                    	Number of fields
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: field_info
                                    
                                    	Field information
                                    	**type**\: list of  		 :py:class:`FieldInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo>`
                                    
                                    

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
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("field-info", ("field_info", Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo))])
                                        self._leafs = OrderedDict([
                                            ('block_name', YLeaf(YType.str, 'block-name')),
                                            ('num_fields', YLeaf(YType.uint8, 'num-fields')),
                                        ])
                                        self.block_name = None
                                        self.num_fields = None

                                        self.field_info = YList(self)
                                        self._segment_path = lambda: "block-info"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo, ['block_name', 'num_fields'], name, value)


                                    class FieldInfo(Entity):
                                        """
                                        Field information
                                        
                                        .. attribute:: field_name
                                        
                                        	Field name
                                        	**type**\: str
                                        
                                        	**length:** 0..80
                                        
                                        .. attribute:: field_value
                                        
                                        	Field value
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_overflow
                                        
                                        	Flag to indicate overflow
                                        	**type**\: bool
                                        
                                        

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
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('field_name', YLeaf(YType.str, 'field-name')),
                                                ('field_value', YLeaf(YType.uint64, 'field-value')),
                                                ('is_overflow', YLeaf(YType.boolean, 'is-overflow')),
                                            ])
                                            self.field_name = None
                                            self.field_value = None
                                            self.is_overflow = None
                                            self._segment_path = lambda: "field-info"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.AsicStatistics.AsicStatisticsDetailForNpuIds.AsicStatisticsDetailForNpuId.Statistics.BlockInfo.FieldInfo, ['field_name', 'field_value', 'is_overflow'], name, value)


                class NpuNumbers(Entity):
                    """
                    Ingress Stats
                    
                    .. attribute:: npu_number
                    
                    	Stats for a particular npu
                    	**type**\: list of  		 :py:class:`NpuNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber>`
                    
                    

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
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("npu-number", ("npu_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber))])
                        self._leafs = OrderedDict()

                        self.npu_number = YList(self)
                        self._segment_path = lambda: "npu-numbers"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers, [], name, value)


                    class NpuNumber(Entity):
                        """
                        Stats for a particular npu
                        
                        .. attribute:: npu_id  (key)
                        
                        	Npu number
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: display
                        
                        	show npu specific voq or trap stats
                        	**type**\:  :py:class:`Display <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display>`
                        
                        

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
                            self._child_container_classes = OrderedDict([("display", ("display", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('npu_id', YLeaf(YType.int32, 'npu-id')),
                            ])
                            self.npu_id = None

                            self.display = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display()
                            self.display.parent = self
                            self._children_name_map["display"] = "display"
                            self._children_yang_names.add("display")
                            self._segment_path = lambda: "npu-number" + "[npu-id='" + str(self.npu_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber, ['npu_id'], name, value)


                        class Display(Entity):
                            """
                            show npu specific voq or trap stats
                            
                            .. attribute:: base_numbers
                            
                            	Voq stats grouped by voq base numbers
                            	**type**\:  :py:class:`BaseNumbers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers>`
                            
                            .. attribute:: trap_ids
                            
                            	Trap stats for a particular npu
                            	**type**\:  :py:class:`TrapIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds>`
                            
                            .. attribute:: interface_handles
                            
                            	Voq stats grouped by interface handle
                            	**type**\:  :py:class:`InterfaceHandles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles>`
                            
                            

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
                                self._child_container_classes = OrderedDict([("base-numbers", ("base_numbers", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers)), ("trap-ids", ("trap_ids", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds)), ("interface-handles", ("interface_handles", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict()

                                self.base_numbers = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers()
                                self.base_numbers.parent = self
                                self._children_name_map["base_numbers"] = "base-numbers"
                                self._children_yang_names.add("base-numbers")

                                self.trap_ids = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds()
                                self.trap_ids.parent = self
                                self._children_name_map["trap_ids"] = "trap-ids"
                                self._children_yang_names.add("trap-ids")

                                self.interface_handles = Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles()
                                self.interface_handles.parent = self
                                self._children_name_map["interface_handles"] = "interface-handles"
                                self._children_yang_names.add("interface-handles")
                                self._segment_path = lambda: "display"


                            class BaseNumbers(Entity):
                                """
                                Voq stats grouped by voq base numbers
                                
                                .. attribute:: base_number
                                
                                	Voq Base Number for a particular voq
                                	**type**\: list of  		 :py:class:`BaseNumber <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber>`
                                
                                

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("base-number", ("base_number", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber))])
                                    self._leafs = OrderedDict()

                                    self.base_number = YList(self)
                                    self._segment_path = lambda: "base-numbers"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers, [], name, value)


                                class BaseNumber(Entity):
                                    """
                                    Voq Base Number for a particular voq
                                    
                                    .. attribute:: base_number  (key)
                                    
                                    	Interface handle
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\: bool
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\: bool
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of  		 :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat>`
                                    
                                    

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
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("voq-stat", ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat))])
                                        self._leafs = OrderedDict([
                                            ('base_number', YLeaf(YType.uint32, 'base-number')),
                                            ('in_use', YLeaf(YType.boolean, 'in-use')),
                                            ('rack_num', YLeaf(YType.uint8, 'rack-num')),
                                            ('slot_num', YLeaf(YType.uint8, 'slot-num')),
                                            ('npu_num', YLeaf(YType.uint8, 'npu-num')),
                                            ('npu_core', YLeaf(YType.uint8, 'npu-core')),
                                            ('port_num', YLeaf(YType.uint8, 'port-num')),
                                            ('if_handle', YLeaf(YType.uint32, 'if-handle')),
                                            ('sys_port', YLeaf(YType.uint32, 'sys-port')),
                                            ('pp_port', YLeaf(YType.uint32, 'pp-port')),
                                            ('port_speed', YLeaf(YType.uint32, 'port-speed')),
                                            ('voq_base', YLeaf(YType.uint32, 'voq-base')),
                                            ('connector_id', YLeaf(YType.uint32, 'connector-id')),
                                            ('is_local_port', YLeaf(YType.boolean, 'is-local-port')),
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

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber, ['base_number', 'in_use', 'rack_num', 'slot_num', 'npu_num', 'npu_core', 'port_num', 'if_handle', 'sys_port', 'pp_port', 'port_speed', 'voq_base', 'connector_id', 'is_local_port'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

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
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('received_bytes', YLeaf(YType.uint64, 'received-bytes')),
                                                ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                                ('dropped_bytes', YLeaf(YType.uint64, 'dropped-bytes')),
                                                ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                            ])
                                            self.received_bytes = None
                                            self.received_packets = None
                                            self.dropped_bytes = None
                                            self.dropped_packets = None
                                            self._segment_path = lambda: "voq-stat"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.BaseNumbers.BaseNumber.VoqStat, ['received_bytes', 'received_packets', 'dropped_bytes', 'dropped_packets'], name, value)


                            class TrapIds(Entity):
                                """
                                Trap stats for a particular npu
                                
                                .. attribute:: trap_id
                                
                                	Filter by specific trap id
                                	**type**\: list of  		 :py:class:`TrapId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId>`
                                
                                

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("trap-id", ("trap_id", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId))])
                                    self._leafs = OrderedDict()

                                    self.trap_id = YList(self)
                                    self._segment_path = lambda: "trap-ids"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds, [], name, value)


                                class TrapId(Entity):
                                    """
                                    Filter by specific trap id
                                    
                                    .. attribute:: trap_id  (key)
                                    
                                    	Trap ID
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_strength
                                    
                                    	Trap Strength of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: priority
                                    
                                    	Priority of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_id_xr
                                    
                                    	Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: gport
                                    
                                    	Gport of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: fec_id
                                    
                                    	Fec id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: policer_id
                                    
                                    	Id of the policer on the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stats_id
                                    
                                    	Stats Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: encap_id
                                    
                                    	Encap Id of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mc_group
                                    
                                    	McGroup of the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: trap_string
                                    
                                    	Name String of the trap
                                    	**type**\: str
                                    
                                    .. attribute:: id
                                    
                                    	Id for internal use
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: offset
                                    
                                    	Offset for internal use
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: npu_id
                                    
                                    	NpuId on which trap is enabled
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_dropped
                                    
                                    	Number of packets dropped after hitting the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: packet_accepted
                                    
                                    	Number of packets accepted after hitting the trap
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

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
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('trap_id', YLeaf(YType.uint32, 'trap-id')),
                                            ('trap_strength', YLeaf(YType.uint32, 'trap-strength')),
                                            ('priority', YLeaf(YType.uint32, 'priority')),
                                            ('trap_id_xr', YLeaf(YType.uint32, 'trap-id-xr')),
                                            ('gport', YLeaf(YType.uint32, 'gport')),
                                            ('fec_id', YLeaf(YType.uint32, 'fec-id')),
                                            ('policer_id', YLeaf(YType.uint32, 'policer-id')),
                                            ('stats_id', YLeaf(YType.uint32, 'stats-id')),
                                            ('encap_id', YLeaf(YType.uint32, 'encap-id')),
                                            ('mc_group', YLeaf(YType.uint32, 'mc-group')),
                                            ('trap_string', YLeaf(YType.str, 'trap-string')),
                                            ('id', YLeaf(YType.uint32, 'id')),
                                            ('offset', YLeaf(YType.uint64, 'offset')),
                                            ('npu_id', YLeaf(YType.uint64, 'npu-id')),
                                            ('packet_dropped', YLeaf(YType.uint64, 'packet-dropped')),
                                            ('packet_accepted', YLeaf(YType.uint64, 'packet-accepted')),
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

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.TrapIds.TrapId, ['trap_id', 'trap_strength', 'priority', 'trap_id_xr', 'gport', 'fec_id', 'policer_id', 'stats_id', 'encap_id', 'mc_group', 'trap_string', 'id', 'offset', 'npu_id', 'packet_dropped', 'packet_accepted'], name, value)


                            class InterfaceHandles(Entity):
                                """
                                Voq stats grouped by interface handle
                                
                                .. attribute:: interface_handle
                                
                                	Voq stats for a particular interface handle
                                	**type**\: list of  		 :py:class:`InterfaceHandle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle>`
                                
                                

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
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("interface-handle", ("interface_handle", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle))])
                                    self._leafs = OrderedDict()

                                    self.interface_handle = YList(self)
                                    self._segment_path = lambda: "interface-handles"

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
                                    
                                    .. attribute:: in_use
                                    
                                    	Flag to indicate if port is in use
                                    	**type**\: bool
                                    
                                    .. attribute:: rack_num
                                    
                                    	Rack of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: slot_num
                                    
                                    	Slot of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_num
                                    
                                    	NPU of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: npu_core
                                    
                                    	NPU core of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: port_num
                                    
                                    	Port Number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: if_handle
                                    
                                    	IfHandle of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sys_port
                                    
                                    	System port of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pp_port
                                    
                                    	PP Port number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: port_speed
                                    
                                    	Port speed of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: voq_base
                                    
                                    	Voq Base number of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: connector_id
                                    
                                    	Connector id of port
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: is_local_port
                                    
                                    	Flag to indicate if port is local to the node
                                    	**type**\: bool
                                    
                                    .. attribute:: voq_stat
                                    
                                    	Keeps a record of the received and dropped packets and bytes on the port
                                    	**type**\: list of  		 :py:class:`VoqStat <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper.Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat>`
                                    
                                    

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
                                        self._child_container_classes = OrderedDict([])
                                        self._child_list_classes = OrderedDict([("voq-stat", ("voq_stat", Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat))])
                                        self._leafs = OrderedDict([
                                            ('interface_handle', YLeaf(YType.uint32, 'interface-handle')),
                                            ('in_use', YLeaf(YType.boolean, 'in-use')),
                                            ('rack_num', YLeaf(YType.uint8, 'rack-num')),
                                            ('slot_num', YLeaf(YType.uint8, 'slot-num')),
                                            ('npu_num', YLeaf(YType.uint8, 'npu-num')),
                                            ('npu_core', YLeaf(YType.uint8, 'npu-core')),
                                            ('port_num', YLeaf(YType.uint8, 'port-num')),
                                            ('if_handle', YLeaf(YType.uint32, 'if-handle')),
                                            ('sys_port', YLeaf(YType.uint32, 'sys-port')),
                                            ('pp_port', YLeaf(YType.uint32, 'pp-port')),
                                            ('port_speed', YLeaf(YType.uint32, 'port-speed')),
                                            ('voq_base', YLeaf(YType.uint32, 'voq-base')),
                                            ('connector_id', YLeaf(YType.uint32, 'connector-id')),
                                            ('is_local_port', YLeaf(YType.boolean, 'is-local-port')),
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

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle, ['interface_handle', 'in_use', 'rack_num', 'slot_num', 'npu_num', 'npu_core', 'port_num', 'if_handle', 'sys_port', 'pp_port', 'port_speed', 'voq_base', 'connector_id', 'is_local_port'], name, value)


                                    class VoqStat(Entity):
                                        """
                                        Keeps a record of the received and dropped
                                        packets and bytes on the port
                                        
                                        .. attribute:: received_bytes
                                        
                                        	Bytes Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: received_packets
                                        
                                        	Packets Received on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: dropped_bytes
                                        
                                        	Bytes Dropped on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: dropped_packets
                                        
                                        	Packets Dropeed on the port
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

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
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('received_bytes', YLeaf(YType.uint64, 'received-bytes')),
                                                ('received_packets', YLeaf(YType.uint64, 'received-packets')),
                                                ('dropped_bytes', YLeaf(YType.uint64, 'dropped-bytes')),
                                                ('dropped_packets', YLeaf(YType.uint64, 'dropped-packets')),
                                            ])
                                            self.received_bytes = None
                                            self.received_packets = None
                                            self.dropped_bytes = None
                                            self.dropped_packets = None
                                            self._segment_path = lambda: "voq-stat"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Dpa.Stats.Nodes.Node.NpuNumbers.NpuNumber.Display.InterfaceHandles.InterfaceHandle.VoqStat, ['received_bytes', 'received_packets', 'dropped_bytes', 'dropped_packets'], name, value)

    def clone_ptr(self):
        self._top_entity = Dpa()
        return self._top_entity

