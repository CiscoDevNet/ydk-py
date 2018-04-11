""" Cisco_IOS_XR_fretta_bcm_dpa_resources_datatypes 

This module contains a collection of generally useful
derived YANG data types.

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



