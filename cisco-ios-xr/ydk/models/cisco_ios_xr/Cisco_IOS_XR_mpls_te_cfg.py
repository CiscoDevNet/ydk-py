""" Cisco_IOS_XR_mpls_te_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-te package configuration.

This module contains definitions
for the following management objects\:
  mpls\-te\: The root of MPLS TE configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BandwidthConstraint(Enum):
    """
    BandwidthConstraint

    Bandwidth constraint

    .. data:: bandwidth_constraint_maximum_allocation_model = 1

    	Maximum Allocation Bandwidth Constaints Model

    """

    bandwidth_constraint_maximum_allocation_model = Enum.YLeaf(1, "bandwidth-constraint-maximum-allocation-model")


class BfdReversePath(Enum):
    """
    BfdReversePath

    Bfd reverse path

    .. data:: bfd_reverse_path_binding_label = 1

    	BindingLabel

    """

    bfd_reverse_path_binding_label = Enum.YLeaf(1, "bfd-reverse-path-binding-label")


class BindingSegmentId(Enum):
    """
    BindingSegmentId

    Binding segment id

    .. data:: any_label = 1

    	AnyLabel

    .. data:: specified_label = 2

    	SpecifiedLabel

    """

    any_label = Enum.YLeaf(1, "any-label")

    specified_label = Enum.YLeaf(2, "specified-label")


class GmplsttiMode(Enum):
    """
    GmplsttiMode

    Gmplstti mode

    .. data:: sm = 1

    	Section Monitoring

    .. data:: pm = 2

    	Path Monitoring

    .. data:: tcm = 3

    	Tandem Connection

    """

    sm = Enum.YLeaf(1, "sm")

    pm = Enum.YLeaf(2, "pm")

    tcm = Enum.YLeaf(3, "tcm")


class IetfMode(Enum):
    """
    IetfMode

    Ietf mode

    .. data:: standard = 3

    	IETF Standard

    """

    standard = Enum.YLeaf(3, "standard")


class LinkNextHop(Enum):
    """
    LinkNextHop

    Link next hop

    .. data:: none = 1

    	No next hop

    .. data:: ipv4_address = 2

    	IPv4 next-hop address

    """

    none = Enum.YLeaf(1, "none")

    ipv4_address = Enum.YLeaf(2, "ipv4-address")


class MplsLcacFloodingIgp(Enum):
    """
    MplsLcacFloodingIgp

    Mpls lcac flooding igp

    .. data:: ospf = 0

    	OSPF

    """

    ospf = Enum.YLeaf(0, "ospf")


class MplsTeAffinityValue(Enum):
    """
    MplsTeAffinityValue

    Mpls te affinity value

    .. data:: hex_value = 1

    	Affinity value in Hex number

    .. data:: bit_position = 2

    	Affinity value by Bit-Position

    """

    hex_value = Enum.YLeaf(1, "hex-value")

    bit_position = Enum.YLeaf(2, "bit-position")


class MplsTeAutorouteMetric(Enum):
    """
    MplsTeAutorouteMetric

    Mpls te autoroute metric

    .. data:: relative = 1

    	Relative

    .. data:: absolute = 2

    	Absolute

    .. data:: constant = 3

    	Constant

    """

    relative = Enum.YLeaf(1, "relative")

    absolute = Enum.YLeaf(2, "absolute")

    constant = Enum.YLeaf(3, "constant")


class MplsTeBackupBandwidthClass(Enum):
    """
    MplsTeBackupBandwidthClass

    Mpls te backup bandwidth class

    .. data:: class0 = 0

    	Class 0

    .. data:: class1 = 1

    	Class 1

    .. data:: any_class = 9

    	Any Class

    """

    class0 = Enum.YLeaf(0, "class0")

    class1 = Enum.YLeaf(1, "class1")

    any_class = Enum.YLeaf(9, "any-class")


class MplsTeBackupBandwidthPool(Enum):
    """
    MplsTeBackupBandwidthPool

    Mpls te backup bandwidth pool

    .. data:: any_pool = 1

    	Any Pool

    .. data:: global_pool = 2

    	Global Pool

    .. data:: sub_pool = 4

    	Sub Pool

    """

    any_pool = Enum.YLeaf(1, "any-pool")

    global_pool = Enum.YLeaf(2, "global-pool")

    sub_pool = Enum.YLeaf(4, "sub-pool")


class MplsTeBandwidthDste(Enum):
    """
    MplsTeBandwidthDste

    Mpls te bandwidth dste

    .. data:: standard_dste = 0

    	IETF-Standard DSTE

    .. data:: pre_standard_dste = 1

    	Pre-Standard DSTE

    """

    standard_dste = Enum.YLeaf(0, "standard-dste")

    pre_standard_dste = Enum.YLeaf(1, "pre-standard-dste")


class MplsTeBandwidthLimit(Enum):
    """
    MplsTeBandwidthLimit

    Mpls te bandwidth limit

    .. data:: unlimited = 64

    	Unlimited

    .. data:: limited = 128

    	Limited

    """

    unlimited = Enum.YLeaf(64, "unlimited")

    limited = Enum.YLeaf(128, "limited")


class MplsTeBfdSessionDownAction(Enum):
    """
    MplsTeBfdSessionDownAction

    Mpls te bfd session down action

    .. data:: re_setup = 1

    	Tear down and resetup

    """

    re_setup = Enum.YLeaf(1, "re-setup")


class MplsTeConfigTunnel(Enum):
    """
    MplsTeConfigTunnel

    Mpls te config tunnel

    .. data:: p2p = 0

    	P2P

    .. data:: p2mp = 1

    	P2MP

    """

    p2p = Enum.YLeaf(0, "p2p")

    p2mp = Enum.YLeaf(1, "p2mp")


class MplsTeIgpProtocol(Enum):
    """
    MplsTeIgpProtocol

    Mpls te igp protocol

    .. data:: none = 0

    	Not set

    .. data:: isis = 1

    	IS IS

    .. data:: ospf = 2

    	OSPF

    """

    none = Enum.YLeaf(0, "none")

    isis = Enum.YLeaf(1, "isis")

    ospf = Enum.YLeaf(2, "ospf")


class MplsTeLogFrrProtection(Enum):
    """
    MplsTeLogFrrProtection

    Mpls te log frr protection

    .. data:: frr_active_primary = 1

    	Track only FRR active on primary LSP

    .. data:: backup = 256

    	backup tunnel

    .. data:: frr_ready_primary = 512

    	Track only FRR ready on primary LSP

    .. data:: primary = 513

    	primary LSP

    .. data:: all = 769

    	all

    """

    frr_active_primary = Enum.YLeaf(1, "frr-active-primary")

    backup = Enum.YLeaf(256, "backup")

    frr_ready_primary = Enum.YLeaf(512, "frr-ready-primary")

    primary = Enum.YLeaf(513, "primary")

    all = Enum.YLeaf(769, "all")


class MplsTeOtnApsProtection(Enum):
    """
    MplsTeOtnApsProtection

    Mpls te otn aps protection

    .. data:: Y_1plus1_unidir_no_aps = 4

    	1PLUS1 UNIDIR NO APS

    .. data:: Y_1plus1_unidir_aps = 8

    	1PLUS1 UNIDIR APS

    .. data:: Y_1plus1_bdir_aps = 16

    	1PLUS1 BIDIR APS

    """

    Y_1plus1_unidir_no_aps = Enum.YLeaf(4, "1plus1-unidir-no-aps")

    Y_1plus1_unidir_aps = Enum.YLeaf(8, "1plus1-unidir-aps")

    Y_1plus1_bdir_aps = Enum.YLeaf(16, "1plus1-bdir-aps")


class MplsTeOtnApsProtectionMode(Enum):
    """
    MplsTeOtnApsProtectionMode

    Mpls te otn aps protection mode

    .. data:: revertive = 1

    	Revertive

    .. data:: non_revertive = 2

    	Non Revertive

    """

    revertive = Enum.YLeaf(1, "revertive")

    non_revertive = Enum.YLeaf(2, "non-revertive")


class MplsTeOtnApsRestorationStyle(Enum):
    """
    MplsTeOtnApsRestorationStyle

    Mpls te otn aps restoration style

    .. data:: keep_failed_lsp = 1

    	Keep Failed Lsp

    .. data:: delete_failed_lsp = 2

    	Delete Failed Lsp

    """

    keep_failed_lsp = Enum.YLeaf(1, "keep-failed-lsp")

    delete_failed_lsp = Enum.YLeaf(2, "delete-failed-lsp")


class MplsTeOtnSncMode(Enum):
    """
    MplsTeOtnSncMode

    Mpls te otn snc mode

    .. data:: snc_n = 1

    	SNC N

    .. data:: snc_i = 2

    	SNC I

    .. data:: snc_s = 3

    	SNC S

    """

    snc_n = Enum.YLeaf(1, "snc-n")

    snc_i = Enum.YLeaf(2, "snc-i")

    snc_s = Enum.YLeaf(3, "snc-s")


class MplsTePathComputationMethod(Enum):
    """
    MplsTePathComputationMethod

    Mpls te path computation method

    .. data:: not_set = 0

    	NotSet

    .. data:: dynamic = 1

    	Dynamic

    .. data:: pce = 2

    	PCE

    .. data:: explicit = 3

    	Explicit

    """

    not_set = Enum.YLeaf(0, "not-set")

    dynamic = Enum.YLeaf(1, "dynamic")

    pce = Enum.YLeaf(2, "pce")

    explicit = Enum.YLeaf(3, "explicit")


class MplsTePathDiversityConformance(Enum):
    """
    MplsTePathDiversityConformance

    Mpls te path diversity conformance

    .. data:: strict = 0

    	Strict

    .. data:: best_effort = 1

    	Best effort

    """

    strict = Enum.YLeaf(0, "strict")

    best_effort = Enum.YLeaf(1, "best-effort")


class MplsTePathOption(Enum):
    """
    MplsTePathOption

    Mpls te path option

    .. data:: not_set = 0

    	Not Set

    .. data:: dynamic = 1

    	Dynamic

    .. data:: explicit_name = 3

    	Explicit, identified by name

    .. data:: explicit_number = 4

    	Explicit, identified by number

    .. data:: no_ero = 5

    	No ERO

    .. data:: sr = 6

    	Segment routing

    """

    not_set = Enum.YLeaf(0, "not-set")

    dynamic = Enum.YLeaf(1, "dynamic")

    explicit_name = Enum.YLeaf(3, "explicit-name")

    explicit_number = Enum.YLeaf(4, "explicit-number")

    no_ero = Enum.YLeaf(5, "no-ero")

    sr = Enum.YLeaf(6, "sr")


class MplsTePathOptionProperty(Enum):
    """
    MplsTePathOptionProperty

    Mpls te path option property

    .. data:: none = 0

    	No property

    .. data:: lockdown = 1

    	Path is not a canditate forreoptimization

    .. data:: verbatim = 4

    	Explicit path does not require topology

    	database

    .. data:: pce = 8

    	Dynamic path found by PCE server

    .. data:: segment_routing = 16

    	Segment Routing path

    """

    none = Enum.YLeaf(0, "none")

    lockdown = Enum.YLeaf(1, "lockdown")

    verbatim = Enum.YLeaf(4, "verbatim")

    pce = Enum.YLeaf(8, "pce")

    segment_routing = Enum.YLeaf(16, "segment-routing")


class MplsTePathOptionProtection(Enum):
    """
    MplsTePathOptionProtection

    Mpls te path option protection

    .. data:: active = 0

    	Active path

    .. data:: protecting = 1

    	Protecting Path

    """

    active = Enum.YLeaf(0, "active")

    protecting = Enum.YLeaf(1, "protecting")


class MplsTePathSelectionInvalidationTimerExpire(Enum):
    """
    MplsTePathSelectionInvalidationTimerExpire

    Mpls te path selection invalidation timer expire

    .. data:: tunnel_action_tear = 1

    	Tear down tunnel.

    .. data:: tunnel_action_drop = 2

    	Drop tunnel traffic.

    """

    tunnel_action_tear = Enum.YLeaf(1, "tunnel-action-tear")

    tunnel_action_drop = Enum.YLeaf(2, "tunnel-action-drop")


class MplsTePathSelectionMetric(Enum):
    """
    MplsTePathSelectionMetric

    Mpls te path selection metric

    .. data:: igp = 1

    	IGP Metric

    .. data:: te = 2

    	TE Metric

    .. data:: delay = 4

    	DELAY Metric

    """

    igp = Enum.YLeaf(1, "igp")

    te = Enum.YLeaf(2, "te")

    delay = Enum.YLeaf(4, "delay")


class MplsTePathSelectionSegmentRoutingAdjacencyProtection(Enum):
    """
    MplsTePathSelectionSegmentRoutingAdjacencyProtection

    Mpls te path selection segment routing adjacency

    protection

    .. data:: not_set = 0

    	Any segment can be used in a path.

    .. data:: adj_unprotected = 1

    	Only unprotected adjacency segments can be used

    	in a path.

    .. data:: adj_protected = 2

    	Only protected adjacency segments can be used

    	in a path.

    """

    not_set = Enum.YLeaf(0, "not-set")

    adj_unprotected = Enum.YLeaf(1, "adj-unprotected")

    adj_protected = Enum.YLeaf(2, "adj-protected")


class MplsTePathSelectionTiebreaker(Enum):
    """
    MplsTePathSelectionTiebreaker

    Mpls te path selection tiebreaker

    .. data:: min_fill = 1

    	Prefer the path with the least-utilized links

    .. data:: max_fill = 2

    	Prefer the path with the most-utilized links

    .. data:: random = 3

    	Prefer a path with links utilized randomly

    """

    min_fill = Enum.YLeaf(1, "min-fill")

    max_fill = Enum.YLeaf(2, "max-fill")

    random = Enum.YLeaf(3, "random")


class MplsTeSigNameOption(Enum):
    """
    MplsTeSigNameOption

    Mpls te sig name option

    .. data:: none = 0

    	None

    .. data:: address = 1

    	Address

    .. data:: name = 2

    	Name

    """

    none = Enum.YLeaf(0, "none")

    address = Enum.YLeaf(1, "address")

    name = Enum.YLeaf(2, "name")


class MplsTeSignaledLabel(Enum):
    """
    MplsTeSignaledLabel

    Mpls te signaled label

    .. data:: not_set = 0

    	Not Set

    .. data:: dwdm = 1

    	DWDM Label (RFC 6205), 50GHz channel spacing

    """

    not_set = Enum.YLeaf(0, "not-set")

    dwdm = Enum.YLeaf(1, "dwdm")


class MplsTeSwitchingCap(Enum):
    """
    MplsTeSwitchingCap

    Mpls te switching cap

    .. data:: psc1 = 1

    	PSC1

    .. data:: lsc = 150

    	LSC

    .. data:: fsc = 200

    	FSC

    """

    psc1 = Enum.YLeaf(1, "psc1")

    lsc = Enum.YLeaf(150, "lsc")

    fsc = Enum.YLeaf(200, "fsc")


class MplsTeSwitchingEncode(Enum):
    """
    MplsTeSwitchingEncode

    Mpls te switching encode

    .. data:: none = 0

    	None

    .. data:: packet = 1

    	Packet

    .. data:: ethernet = 2

    	Ethernet

    .. data:: sondet_sdh = 5

    	SONET SDH

    """

    none = Enum.YLeaf(0, "none")

    packet = Enum.YLeaf(1, "packet")

    ethernet = Enum.YLeaf(2, "ethernet")

    sondet_sdh = Enum.YLeaf(5, "sondet-sdh")


class MplsTeSwitchingEncoding(Enum):
    """
    MplsTeSwitchingEncoding

    Mpls te switching encoding

    .. data:: packet = 1

    	Packet

    .. data:: ethernet = 2

    	Ethernet

    .. data:: sondet_sdh = 5

    	SONET SDH

    """

    packet = Enum.YLeaf(1, "packet")

    ethernet = Enum.YLeaf(2, "ethernet")

    sondet_sdh = Enum.YLeaf(5, "sondet-sdh")


class MplsTeSwitchingIndex(Enum):
    """
    MplsTeSwitchingIndex

    Mpls te switching index

    .. data:: link = 255

    	Link

    """

    link = Enum.YLeaf(255, "link")


class MplsTeTunnelAffinity(Enum):
    """
    MplsTeTunnelAffinity

    Mpls te tunnel affinity

    .. data:: include = 1

    	Include Affinity

    .. data:: include_strict = 2

    	Strictly Include Affinity

    .. data:: exclude = 3

    	Exclude Affinity

    .. data:: exclude_all = 4

    	Exclude All Affinities

    .. data:: ignore = 5

    	Ignore Affinity

    """

    include = Enum.YLeaf(1, "include")

    include_strict = Enum.YLeaf(2, "include-strict")

    exclude = Enum.YLeaf(3, "exclude")

    exclude_all = Enum.YLeaf(4, "exclude-all")

    ignore = Enum.YLeaf(5, "ignore")


class MplsTeTunnelId(Enum):
    """
    MplsTeTunnelId

    Mpls te tunnel id

    .. data:: auto = 0

    	Auto

    .. data:: explicit = 1

    	Explicit

    """

    auto = Enum.YLeaf(0, "auto")

    explicit = Enum.YLeaf(1, "explicit")


class MplsTebfdSession(Enum):
    """
    MplsTebfdSession

    Mpls tebfd session

    .. data:: regular_bfd = 1

    	Regular BFD

    .. data:: sbfd = 2

    	Seamless BFD

    .. data:: redundant_sbfd = 3

    	Redundant SBFD

    """

    regular_bfd = Enum.YLeaf(1, "regular-bfd")

    sbfd = Enum.YLeaf(2, "sbfd")

    redundant_sbfd = Enum.YLeaf(3, "redundant-sbfd")


class MplsTesrlgExclude(Enum):
    """
    MplsTesrlgExclude

    Mpls tesrlg exclude

    .. data:: mandatory = 1

    	SRLG Mandatory Exclude

    .. data:: preferred = 2

    	SRLG Preferred Exclude

    .. data:: weighted = 3

    	SRLG Weighted Exclude

    """

    mandatory = Enum.YLeaf(1, "mandatory")

    preferred = Enum.YLeaf(2, "preferred")

    weighted = Enum.YLeaf(3, "weighted")


class OspfAreaMode(Enum):
    """
    OspfAreaMode

    Ospf area mode

    .. data:: ospf_int = 0

    	OSPF area in integer format

    .. data:: ospfip_addr = 1

    	OSPF area in IP address format

    """

    ospf_int = Enum.YLeaf(0, "ospf-int")

    ospfip_addr = Enum.YLeaf(1, "ospfip-addr")


class OtnDestination(Enum):
    """
    OtnDestination

    Otn destination

    .. data:: number_ed = 0

    	Destination numbered

    .. data:: un_number_ed = 1

    	Destination unnumbered

    """

    number_ed = Enum.YLeaf(0, "number-ed")

    un_number_ed = Enum.YLeaf(1, "un-number-ed")


class OtnPayload(Enum):
    """
    OtnPayload

    Otn payload

    .. data:: unknown = 0

    	Payload unknown

    .. data:: bmp = 50

    	Bmp Payload

    .. data:: gfp_f = 54

    	Gfp_F Payload

    .. data:: gmp = 55

    	GMP Payload

    .. data:: gfp_f_ext = 70

    	Gfp_F_EXT Payload

    """

    unknown = Enum.YLeaf(0, "unknown")

    bmp = Enum.YLeaf(50, "bmp")

    gfp_f = Enum.YLeaf(54, "gfp-f")

    gmp = Enum.YLeaf(55, "gmp")

    gfp_f_ext = Enum.YLeaf(70, "gfp-f-ext")


class OtnProtectionSwitchLockout(Enum):
    """
    OtnProtectionSwitchLockout

    Otn protection switch lockout

    .. data:: none = 0

    	No Lockout

    .. data:: working = 1

    	Lockout Working

    """

    none = Enum.YLeaf(0, "none")

    working = Enum.YLeaf(1, "working")


class OtnSignaledBandwidth(Enum):
    """
    OtnSignaledBandwidth

    Otn signaled bandwidth

    .. data:: odu1 = 1

    	Signalled BW for ODU1

    .. data:: odu2 = 2

    	Signalled BW for ODU2

    .. data:: odu3 = 3

    	Signalled BW for ODU3

    .. data:: odu4 = 4

    	Signalled BW for ODU4

    .. data:: odu0 = 10

    	Signalled BW for ODU0

    .. data:: odu2e = 11

    	Signalled BW for ODU2e

    .. data:: od_uflex_cbr = 20

    	Signalled BW for ODUflex CBR

    .. data:: od_uflex_gfp_resize = 21

    	Signalled BW for ODUflex GFP Resizable

    .. data:: od_uflex_gfp_not_resize = 22

    	Signalled BW for ODUflex GFP not Resizable

    .. data:: odu1e = 23

    	Signalled BW for ODU1e

    .. data:: odu1f = 24

    	Signalled BW for ODU1f

    .. data:: odu2f = 25

    	Signalled BW for ODU2f

    .. data:: odu3e1 = 26

    	Signalled BW for ODU3e1

    .. data:: odu3e2 = 27

    	Signalled BW for ODU3e2

    """

    odu1 = Enum.YLeaf(1, "odu1")

    odu2 = Enum.YLeaf(2, "odu2")

    odu3 = Enum.YLeaf(3, "odu3")

    odu4 = Enum.YLeaf(4, "odu4")

    odu0 = Enum.YLeaf(10, "odu0")

    odu2e = Enum.YLeaf(11, "odu2e")

    od_uflex_cbr = Enum.YLeaf(20, "od-uflex-cbr")

    od_uflex_gfp_resize = Enum.YLeaf(21, "od-uflex-gfp-resize")

    od_uflex_gfp_not_resize = Enum.YLeaf(22, "od-uflex-gfp-not-resize")

    odu1e = Enum.YLeaf(23, "odu1e")

    odu1f = Enum.YLeaf(24, "odu1f")

    odu2f = Enum.YLeaf(25, "odu2f")

    odu3e1 = Enum.YLeaf(26, "odu3e1")

    odu3e2 = Enum.YLeaf(27, "odu3e2")


class OtnSignaledBandwidthFlexFraming(Enum):
    """
    OtnSignaledBandwidthFlexFraming

    Otn signaled bandwidth flex framing

    .. data:: cbr = 20

    	CBR

    .. data:: framed_gfp_fixed = 21

    	GFP fixed framing type

    .. data:: framed_gfp_resize = 22

    	GFP resizeable framing type

    """

    cbr = Enum.YLeaf(20, "cbr")

    framed_gfp_fixed = Enum.YLeaf(21, "framed-gfp-fixed")

    framed_gfp_resize = Enum.YLeaf(22, "framed-gfp-resize")


class OtnStaticUni(Enum):
    """
    OtnStaticUni

    Otn static uni

    .. data:: unknown = 0

    	Uni-Type None

    .. data:: xc = 1

    	Uni-Type XC

    .. data:: termination = 2

    	Uni-Type Termination

    """

    unknown = Enum.YLeaf(0, "unknown")

    xc = Enum.YLeaf(1, "xc")

    termination = Enum.YLeaf(2, "termination")


class PathInvalidationAction(Enum):
    """
    PathInvalidationAction

    Path invalidation action

    .. data:: tear = 1

    	Tear

    .. data:: drop = 2

    	Drop

    """

    tear = Enum.YLeaf(1, "tear")

    drop = Enum.YLeaf(2, "drop")


class RoutePriorityRole(Enum):
    """
    RoutePriorityRole

    Route priority role

    .. data:: route_priority_role_head_back_up = 0

    	TE Route Priority Role Head Backup

    .. data:: route_priority_role_head_primary = 1

    	TE Route Priority Role Head Primary

    .. data:: route_priority_role_middle = 2

    	TE Route Priority Role Middle

    """

    route_priority_role_head_back_up = Enum.YLeaf(0, "route-priority-role-head-back-up")

    route_priority_role_head_primary = Enum.YLeaf(1, "route-priority-role-head-primary")

    route_priority_role_middle = Enum.YLeaf(2, "route-priority-role-middle")


class SrPrepend(Enum):
    """
    SrPrepend

    Sr prepend

    .. data:: none_type = 0

    	NoneType

    .. data:: next_label = 1

    	Next Label

    .. data:: bgp_n_hop = 2

    	BGP NHOP

    """

    none_type = Enum.YLeaf(0, "none-type")

    next_label = Enum.YLeaf(1, "next-label")

    bgp_n_hop = Enum.YLeaf(2, "bgp-n-hop")



class MplsTe(Entity):
    """
    The root of MPLS TE configuration
    
    .. attribute:: diff_serv_traffic_engineering
    
    	Configure Diff\-Serv Traffic\-Engineering
    	**type**\:   :py:class:`DiffServTrafficEngineering <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.DiffServTrafficEngineering>`
    
    .. attribute:: named_tunnels
    
    	Configure MPLS TE tunnel
    	**type**\:   :py:class:`NamedTunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels>`
    
    .. attribute:: gmpls_uni
    
    	GMPLS\-UNI configuration
    	**type**\:   :py:class:`GmplsUni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni>`
    
    .. attribute:: global_attributes
    
    	Configure MPLS TE global attributes
    	**type**\:   :py:class:`GlobalAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes>`
    
    .. attribute:: transport_profile
    
    	MPLS transport profile configuration data
    	**type**\:   :py:class:`TransportProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile>`
    
    .. attribute:: interfaces
    
    	Configure MPLS TE interfaces
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces>`
    
    .. attribute:: gmpls_nni
    
    	GMPLS\-NNI configuration
    	**type**\:   :py:class:`GmplsNni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni>`
    
    .. attribute:: lcac
    
    	LCAC specific MPLS global configuration
    	**type**\:   :py:class:`Lcac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Lcac>`
    
    .. attribute:: enable_traffic_engineering
    
    	Enable MPLS Traffic Engineering
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'mpls-te-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(MplsTe, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-te"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-te-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"diff-serv-traffic-engineering" : ("diff_serv_traffic_engineering", MplsTe.DiffServTrafficEngineering), "named-tunnels" : ("named_tunnels", MplsTe.NamedTunnels), "gmpls-uni" : ("gmpls_uni", MplsTe.GmplsUni), "global-attributes" : ("global_attributes", MplsTe.GlobalAttributes), "transport-profile" : ("transport_profile", MplsTe.TransportProfile), "interfaces" : ("interfaces", MplsTe.Interfaces), "gmpls-nni" : ("gmpls_nni", MplsTe.GmplsNni), "lcac" : ("lcac", MplsTe.Lcac)}
        self._child_list_classes = {}

        self.enable_traffic_engineering = YLeaf(YType.empty, "enable-traffic-engineering")

        self.diff_serv_traffic_engineering = MplsTe.DiffServTrafficEngineering()
        self.diff_serv_traffic_engineering.parent = self
        self._children_name_map["diff_serv_traffic_engineering"] = "diff-serv-traffic-engineering"
        self._children_yang_names.add("diff-serv-traffic-engineering")

        self.named_tunnels = MplsTe.NamedTunnels()
        self.named_tunnels.parent = self
        self._children_name_map["named_tunnels"] = "named-tunnels"
        self._children_yang_names.add("named-tunnels")

        self.gmpls_uni = MplsTe.GmplsUni()
        self.gmpls_uni.parent = self
        self._children_name_map["gmpls_uni"] = "gmpls-uni"
        self._children_yang_names.add("gmpls-uni")

        self.global_attributes = MplsTe.GlobalAttributes()
        self.global_attributes.parent = self
        self._children_name_map["global_attributes"] = "global-attributes"
        self._children_yang_names.add("global-attributes")

        self.transport_profile = MplsTe.TransportProfile()
        self.transport_profile.parent = self
        self._children_name_map["transport_profile"] = "transport-profile"
        self._children_yang_names.add("transport-profile")

        self.interfaces = MplsTe.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.gmpls_nni = MplsTe.GmplsNni()
        self.gmpls_nni.parent = self
        self._children_name_map["gmpls_nni"] = "gmpls-nni"
        self._children_yang_names.add("gmpls-nni")

        self.lcac = MplsTe.Lcac()
        self.lcac.parent = self
        self._children_name_map["lcac"] = "lcac"
        self._children_yang_names.add("lcac")
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te"

    def __setattr__(self, name, value):
        self._perform_setattr(MplsTe, ['enable_traffic_engineering'], name, value)


    class DiffServTrafficEngineering(Entity):
        """
        Configure Diff\-Serv Traffic\-Engineering
        
        .. attribute:: classes
        
        	Configure Diff\-Serv Traffic\-Engineering Classes
        	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.DiffServTrafficEngineering.Classes>`
        
        .. attribute:: bandwidth_constraint_model
        
        	Diff\-Serv Traffic\-Engineering Bandwidth Constraint Model
        	**type**\:   :py:class:`BandwidthConstraint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.BandwidthConstraint>`
        
        .. attribute:: mode_ietf
        
        	Diff\-Serv Traffic\-Engineering IETF mode
        	**type**\:   :py:class:`IetfMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.IetfMode>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.DiffServTrafficEngineering, self).__init__()

            self.yang_name = "diff-serv-traffic-engineering"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"classes" : ("classes", MplsTe.DiffServTrafficEngineering.Classes)}
            self._child_list_classes = {}

            self.bandwidth_constraint_model = YLeaf(YType.enumeration, "bandwidth-constraint-model")

            self.mode_ietf = YLeaf(YType.enumeration, "mode-ietf")

            self.classes = MplsTe.DiffServTrafficEngineering.Classes()
            self.classes.parent = self
            self._children_name_map["classes"] = "classes"
            self._children_yang_names.add("classes")
            self._segment_path = lambda: "diff-serv-traffic-engineering"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.DiffServTrafficEngineering, ['bandwidth_constraint_model', 'mode_ietf'], name, value)


        class Classes(Entity):
            """
            Configure Diff\-Serv Traffic\-Engineering Classes
            
            .. attribute:: class_
            
            	DSTE class number
            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.DiffServTrafficEngineering.Classes.Class_>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.DiffServTrafficEngineering.Classes, self).__init__()

                self.yang_name = "classes"
                self.yang_parent_name = "diff-serv-traffic-engineering"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"class" : ("class_", MplsTe.DiffServTrafficEngineering.Classes.Class_)}

                self.class_ = YList(self)
                self._segment_path = lambda: "classes"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/diff-serv-traffic-engineering/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.DiffServTrafficEngineering.Classes, [], name, value)


            class Class_(Entity):
                """
                DSTE class number
                
                .. attribute:: class_number  <key>
                
                	DS\-TE class number
                	**type**\:  int
                
                	**range:** 0..7
                
                .. attribute:: class_type
                
                	Class type number
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: class_priority
                
                	Class\-type priority
                	**type**\:  int
                
                	**range:** 0..7
                
                .. attribute:: unused
                
                	TRUE to skip classtype and class priority provisioning FALSE to provision them
                	**type**\:  bool
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.DiffServTrafficEngineering.Classes.Class_, self).__init__()

                    self.yang_name = "class"
                    self.yang_parent_name = "classes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.class_number = YLeaf(YType.uint32, "class-number")

                    self.class_type = YLeaf(YType.uint32, "class-type")

                    self.class_priority = YLeaf(YType.uint32, "class-priority")

                    self.unused = YLeaf(YType.boolean, "unused")
                    self._segment_path = lambda: "class" + "[class-number='" + self.class_number.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/diff-serv-traffic-engineering/classes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.DiffServTrafficEngineering.Classes.Class_, ['class_number', 'class_type', 'class_priority', 'unused'], name, value)


    class NamedTunnels(Entity):
        """
        Configure MPLS TE tunnel
        
        .. attribute:: tunnels
        
        	Configure MPLS TE tunnel
        	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels>`
        
        .. attribute:: enable
        
        	Enable Named Tunnels
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.NamedTunnels, self).__init__()

            self.yang_name = "named-tunnels"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"tunnels" : ("tunnels", MplsTe.NamedTunnels.Tunnels)}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.empty, "enable")

            self.tunnels = MplsTe.NamedTunnels.Tunnels()
            self.tunnels.parent = self
            self._children_name_map["tunnels"] = "tunnels"
            self._children_yang_names.add("tunnels")
            self._segment_path = lambda: "named-tunnels"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.NamedTunnels, ['enable'], name, value)


        class Tunnels(Entity):
            """
            Configure MPLS TE tunnel
            
            .. attribute:: tunnel
            
            	Configure a MPLS TE tunnel
            	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.NamedTunnels.Tunnels, self).__init__()

                self.yang_name = "tunnels"
                self.yang_parent_name = "named-tunnels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"tunnel" : ("tunnel", MplsTe.NamedTunnels.Tunnels.Tunnel)}

                self.tunnel = YList(self)
                self._segment_path = lambda: "tunnels"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/named-tunnels/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.NamedTunnels.Tunnels, [], name, value)


            class Tunnel(Entity):
                """
                Configure a MPLS TE tunnel
                
                .. attribute:: tunnel_name  <key>
                
                	Tunnel name
                	**type**\:  str
                
                	**length:** 1..59
                
                .. attribute:: tunnel_type  <key>
                
                	Tunnel Type
                	**type**\:   :py:class:`MplsTeConfigTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeConfigTunnel>`
                
                .. attribute:: tunnel_attributes
                
                	MPLS tunnel attributes
                	**type**\:   :py:class:`TunnelAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes>`
                
                .. attribute:: tunnel_id
                
                	Set the tunnel ID
                	**type**\:   :py:class:`TunnelId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId>`
                
                	**presence node**\: True
                
                .. attribute:: enable
                
                	Always set to true
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.NamedTunnels.Tunnels.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "tunnels"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"tunnel-attributes" : ("tunnel_attributes", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes), "tunnel-id" : ("tunnel_id", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId)}
                    self._child_list_classes = {}

                    self.tunnel_name = YLeaf(YType.str, "tunnel-name")

                    self.tunnel_type = YLeaf(YType.enumeration, "tunnel-type")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.tunnel_attributes = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes()
                    self.tunnel_attributes.parent = self
                    self._children_name_map["tunnel_attributes"] = "tunnel-attributes"
                    self._children_yang_names.add("tunnel-attributes")

                    self.tunnel_id = None
                    self._children_name_map["tunnel_id"] = "tunnel-id"
                    self._children_yang_names.add("tunnel-id")
                    self._segment_path = lambda: "tunnel" + "[tunnel-name='" + self.tunnel_name.get() + "']" + "[tunnel-type='" + self.tunnel_type.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/named-tunnels/tunnels/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel, ['tunnel_name', 'tunnel_type', 'enable'], name, value)


                class TunnelAttributes(Entity):
                    """
                    MPLS tunnel attributes
                    
                    .. attribute:: path_setups
                    
                    	Tunnel path setup table
                    	**type**\:   :py:class:`PathSetups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups>`
                    
                    .. attribute:: shutdown
                    
                    	shutdown the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: forward_class
                    
                    	Forward class value
                    	**type**\:  int
                    
                    	**range:** 1..7
                    
                    .. attribute:: tunnel_path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`TunnelPathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection>`
                    
                    .. attribute:: auto_bandwidth
                    
                    	Tunnel Interface Auto\-bandwidth configuration data
                    	**type**\:   :py:class:`AutoBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth>`
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: destination
                    
                    	Set the destination of the tunnel
                    	**type**\:  str
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: logging
                    
                    	Log tunnel LSP messages
                    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging>`
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: autoroute
                    
                    	Parameters for IGP routing over tunnel
                    	**type**\:   :py:class:`Autoroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute>`
                    
                    .. attribute:: path_selection_metric
                    
                    	Path selection metric to use in path calculation
                    	**type**\:   :py:class:`MplsTePathSelectionMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetric>`
                    
                    .. attribute:: new_style_affinity_affinity_types
                    
                    	Tunnel new style affinity attributes table
                    	**type**\:   :py:class:`NewStyleAffinityAffinityTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enable the soft\-preemption feature on the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: fast_reroute
                    
                    	Specify MPLS tunnel can be fast\-rerouted
                    	**type**\:   :py:class:`FastReroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: load_share
                    
                    	Tunnel loadsharing metric
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes, self).__init__()

                        self.yang_name = "tunnel-attributes"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"path-setups" : ("path_setups", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups), "tunnel-path-selection" : ("tunnel_path_selection", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection), "auto-bandwidth" : ("auto_bandwidth", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth), "priority" : ("priority", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority), "logging" : ("logging", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging), "bandwidth" : ("bandwidth", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth), "autoroute" : ("autoroute", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute), "new-style-affinity-affinity-types" : ("new_style_affinity_affinity_types", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes), "fast-reroute" : ("fast_reroute", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute)}
                        self._child_list_classes = {}

                        self.shutdown = YLeaf(YType.empty, "shutdown")

                        self.forward_class = YLeaf(YType.uint32, "forward-class")

                        self.destination = YLeaf(YType.str, "destination")

                        self.record_route = YLeaf(YType.empty, "record-route")

                        self.path_selection_metric = YLeaf(YType.enumeration, "path-selection-metric")

                        self.soft_preemption = YLeaf(YType.empty, "soft-preemption")

                        self.load_share = YLeaf(YType.uint32, "load-share")

                        self.path_setups = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups()
                        self.path_setups.parent = self
                        self._children_name_map["path_setups"] = "path-setups"
                        self._children_yang_names.add("path-setups")

                        self.tunnel_path_selection = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection()
                        self.tunnel_path_selection.parent = self
                        self._children_name_map["tunnel_path_selection"] = "tunnel-path-selection"
                        self._children_yang_names.add("tunnel-path-selection")

                        self.auto_bandwidth = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth()
                        self.auto_bandwidth.parent = self
                        self._children_name_map["auto_bandwidth"] = "auto-bandwidth"
                        self._children_yang_names.add("auto-bandwidth")

                        self.priority = None
                        self._children_name_map["priority"] = "priority"
                        self._children_yang_names.add("priority")

                        self.logging = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging()
                        self.logging.parent = self
                        self._children_name_map["logging"] = "logging"
                        self._children_yang_names.add("logging")

                        self.bandwidth = None
                        self._children_name_map["bandwidth"] = "bandwidth"
                        self._children_yang_names.add("bandwidth")

                        self.autoroute = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute()
                        self.autoroute.parent = self
                        self._children_name_map["autoroute"] = "autoroute"
                        self._children_yang_names.add("autoroute")

                        self.new_style_affinity_affinity_types = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes()
                        self.new_style_affinity_affinity_types.parent = self
                        self._children_name_map["new_style_affinity_affinity_types"] = "new-style-affinity-affinity-types"
                        self._children_yang_names.add("new-style-affinity-affinity-types")

                        self.fast_reroute = None
                        self._children_name_map["fast_reroute"] = "fast-reroute"
                        self._children_yang_names.add("fast-reroute")
                        self._segment_path = lambda: "tunnel-attributes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes, ['shutdown', 'forward_class', 'destination', 'record_route', 'path_selection_metric', 'soft_preemption', 'load_share'], name, value)


                    class PathSetups(Entity):
                        """
                        Tunnel path setup table
                        
                        .. attribute:: path_setup
                        
                        	Tunnel path setup
                        	**type**\: list of    :py:class:`PathSetup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups, self).__init__()

                            self.yang_name = "path-setups"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"path-setup" : ("path_setup", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup)}

                            self.path_setup = YList(self)
                            self._segment_path = lambda: "path-setups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups, [], name, value)


                        class PathSetup(Entity):
                            """
                            Tunnel path setup
                            
                            .. attribute:: path_setup_name  <key>
                            
                            	Path Name
                            	**type**\:  str
                            
                            .. attribute:: path_computation
                            
                            	Path computation method
                            	**type**\:   :py:class:`PathComputation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: preference
                            
                            	Path preference level
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: enable
                            
                            	Always set to true
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup, self).__init__()

                                self.yang_name = "path-setup"
                                self.yang_parent_name = "path-setups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"path-computation" : ("path_computation", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation)}
                                self._child_list_classes = {}

                                self.path_setup_name = YLeaf(YType.str, "path-setup-name")

                                self.preference = YLeaf(YType.int32, "preference")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.path_computation = None
                                self._children_name_map["path_computation"] = "path-computation"
                                self._children_yang_names.add("path-computation")
                                self._segment_path = lambda: "path-setup" + "[path-setup-name='" + self.path_setup_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup, ['path_setup_name', 'preference', 'enable'], name, value)


                            class PathComputation(Entity):
                                """
                                Path computation method
                                
                                .. attribute:: path_computation_method
                                
                                	Path computation method
                                	**type**\:   :py:class:`MplsTePathComputationMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathComputationMethod>`
                                
                                	**mandatory**\: True
                                
                                .. attribute:: explicit_path_name
                                
                                	Explicit Path Name
                                	**type**\:  str
                                
                                .. attribute:: path_computation_server
                                
                                	Path Computation Server Address
                                	**type**\:  str
                                
                                	**default value**\: 0.0.0.0
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation, self).__init__()

                                    self.yang_name = "path-computation"
                                    self.yang_parent_name = "path-setup"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self.is_presence_container = True

                                    self.path_computation_method = YLeaf(YType.enumeration, "path-computation-method")

                                    self.explicit_path_name = YLeaf(YType.str, "explicit-path-name")

                                    self.path_computation_server = YLeaf(YType.str, "path-computation-server")
                                    self._segment_path = lambda: "path-computation"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.PathSetups.PathSetup.PathComputation, ['path_computation_method', 'explicit_path_name', 'path_computation_server'], name, value)


                    class TunnelPathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: tiebreaker
                        
                        	CSPF tiebreaker to use in path calculation
                        	**type**\:   :py:class:`MplsTePathSelectionTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionTiebreaker>`
                        
                        .. attribute:: path_selection_hop_limit
                        
                        	Path selection hop limit configuration for this specific tunnel
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        .. attribute:: invalidation
                        
                        	Path invalidation configuration for this specific tunnel
                        	**type**\:   :py:class:`Invalidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: path_selection_cost_limit
                        
                        	Path selection cost limit configuration for this specific tunnel
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection, self).__init__()

                            self.yang_name = "tunnel-path-selection"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"invalidation" : ("invalidation", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation)}
                            self._child_list_classes = {}

                            self.tiebreaker = YLeaf(YType.enumeration, "tiebreaker")

                            self.path_selection_hop_limit = YLeaf(YType.uint32, "path-selection-hop-limit")

                            self.path_selection_cost_limit = YLeaf(YType.uint32, "path-selection-cost-limit")

                            self.invalidation = None
                            self._children_name_map["invalidation"] = "invalidation"
                            self._children_yang_names.add("invalidation")
                            self._segment_path = lambda: "tunnel-path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection, ['tiebreaker', 'path_selection_hop_limit', 'path_selection_cost_limit'], name, value)


                        class Invalidation(Entity):
                            """
                            Path invalidation configuration for this
                            specific tunnel
                            
                            .. attribute:: path_invalidation_timeout
                            
                            	Path Invalidation Timeout
                            	**type**\:  int
                            
                            	**range:** 0..60000
                            
                            .. attribute:: path_invalidation_action
                            
                            	Path Invalidation Action
                            	**type**\:   :py:class:`PathInvalidationAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.PathInvalidationAction>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation, self).__init__()

                                self.yang_name = "invalidation"
                                self.yang_parent_name = "tunnel-path-selection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.path_invalidation_timeout = YLeaf(YType.uint32, "path-invalidation-timeout")

                                self.path_invalidation_action = YLeaf(YType.enumeration, "path-invalidation-action")
                                self._segment_path = lambda: "invalidation"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.TunnelPathSelection.Invalidation, ['path_invalidation_timeout', 'path_invalidation_action'], name, value)


                    class AutoBandwidth(Entity):
                        """
                        Tunnel Interface Auto\-bandwidth configuration
                        data
                        
                        .. attribute:: underflow
                        
                        	Configuring the tunnel underflow detection
                        	**type**\:   :py:class:`Underflow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: overflow
                        
                        	Configuring the tunnel overflow detection
                        	**type**\:   :py:class:`Overflow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: bandwidth_limits
                        
                        	Set min/max bandwidth auto\-bw can apply on a tunnel
                        	**type**\:   :py:class:`BandwidthLimits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: adjustment_threshold
                        
                        	Set the bandwidth change threshold to trigger adjustment
                        	**type**\:   :py:class:`AdjustmentThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: underflow_enable
                        
                        	Enable auto bandwidth underflow detection
                        	**type**\:  bool
                        
                        .. attribute:: enabled
                        
                        	This object is only valid for tunnel interfaces and it controls whether that interface has auto\-bw enabled on it or not.The object must be set before any other auto\-bw configuration is supplied for the interface, and must be the last auto\-bw configuration object to be removed 
                        	**type**\:  bool
                        
                        .. attribute:: application_frequency
                        
                        	Set the tunnel auto\-bw application frequency in minutes
                        	**type**\:  int
                        
                        	**range:** 5..10080
                        
                        	**units**\: minute
                        
                        .. attribute:: overflow_enable
                        
                        	Enable auto bandwidth overflow detection
                        	**type**\:  bool
                        
                        .. attribute:: collection_only
                        
                        	Enable bandwidth collection only, no auto\-bw adjustment
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth, self).__init__()

                            self.yang_name = "auto-bandwidth"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"underflow" : ("underflow", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow), "overflow" : ("overflow", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow), "bandwidth-limits" : ("bandwidth_limits", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits), "adjustment-threshold" : ("adjustment_threshold", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold)}
                            self._child_list_classes = {}

                            self.underflow_enable = YLeaf(YType.boolean, "underflow-enable")

                            self.enabled = YLeaf(YType.boolean, "enabled")

                            self.application_frequency = YLeaf(YType.uint32, "application-frequency")

                            self.overflow_enable = YLeaf(YType.boolean, "overflow-enable")

                            self.collection_only = YLeaf(YType.empty, "collection-only")

                            self.underflow = None
                            self._children_name_map["underflow"] = "underflow"
                            self._children_yang_names.add("underflow")

                            self.overflow = None
                            self._children_name_map["overflow"] = "overflow"
                            self._children_yang_names.add("overflow")

                            self.bandwidth_limits = None
                            self._children_name_map["bandwidth_limits"] = "bandwidth-limits"
                            self._children_yang_names.add("bandwidth-limits")

                            self.adjustment_threshold = None
                            self._children_name_map["adjustment_threshold"] = "adjustment-threshold"
                            self._children_yang_names.add("adjustment-threshold")
                            self._segment_path = lambda: "auto-bandwidth"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth, ['underflow_enable', 'enabled', 'application_frequency', 'overflow_enable', 'collection_only'], name, value)


                        class Underflow(Entity):
                            """
                            Configuring the tunnel underflow detection
                            
                            .. attribute:: underflow_threshold_percent
                            
                            	Bandwidth change percent to trigger an underflow
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**mandatory**\: True
                            
                            	**units**\: percentage
                            
                            .. attribute:: underflow_threshold_value
                            
                            	Bandwidth change value to trigger an underflow (kbps)
                            	**type**\:  int
                            
                            	**range:** 10..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: underflow_threshold_limit
                            
                            	Number of consecutive collections exceeding threshold
                            	**type**\:  int
                            
                            	**range:** 1..10
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow, self).__init__()

                                self.yang_name = "underflow"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.underflow_threshold_percent = YLeaf(YType.uint32, "underflow-threshold-percent")

                                self.underflow_threshold_value = YLeaf(YType.uint32, "underflow-threshold-value")

                                self.underflow_threshold_limit = YLeaf(YType.uint32, "underflow-threshold-limit")
                                self._segment_path = lambda: "underflow"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Underflow, ['underflow_threshold_percent', 'underflow_threshold_value', 'underflow_threshold_limit'], name, value)


                        class Overflow(Entity):
                            """
                            Configuring the tunnel overflow detection
                            
                            .. attribute:: overflow_threshold_percent
                            
                            	Bandwidth change percent to trigger an overflow
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**mandatory**\: True
                            
                            	**units**\: percentage
                            
                            .. attribute:: overflow_threshold_value
                            
                            	Bandwidth change value to trigger an overflow (kbps)
                            	**type**\:  int
                            
                            	**range:** 10..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: overflow_threshold_limit
                            
                            	Number of consecutive collections exceeding threshold
                            	**type**\:  int
                            
                            	**range:** 1..10
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow, self).__init__()

                                self.yang_name = "overflow"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.overflow_threshold_percent = YLeaf(YType.uint32, "overflow-threshold-percent")

                                self.overflow_threshold_value = YLeaf(YType.uint32, "overflow-threshold-value")

                                self.overflow_threshold_limit = YLeaf(YType.uint32, "overflow-threshold-limit")
                                self._segment_path = lambda: "overflow"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.Overflow, ['overflow_threshold_percent', 'overflow_threshold_value', 'overflow_threshold_limit'], name, value)


                        class BandwidthLimits(Entity):
                            """
                            Set min/max bandwidth auto\-bw can apply on a
                            tunnel
                            
                            .. attribute:: bandwidth_min_limit
                            
                            	Set minimum bandwidth auto\-bw can apply on a tunnel
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: bandwidth_max_limit
                            
                            	Set maximum bandwidth auto\-bw can apply on a tunnel
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits, self).__init__()

                                self.yang_name = "bandwidth-limits"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.bandwidth_min_limit = YLeaf(YType.uint32, "bandwidth-min-limit")

                                self.bandwidth_max_limit = YLeaf(YType.uint32, "bandwidth-max-limit")
                                self._segment_path = lambda: "bandwidth-limits"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.BandwidthLimits, ['bandwidth_min_limit', 'bandwidth_max_limit'], name, value)


                        class AdjustmentThreshold(Entity):
                            """
                            Set the bandwidth change threshold to trigger
                            adjustment
                            
                            .. attribute:: adjustment_threshold_percent
                            
                            	Bandwidth change percent to trigger adjustment
                            	**type**\:  int
                            
                            	**range:** 1..100
                            
                            	**mandatory**\: True
                            
                            	**units**\: percentage
                            
                            .. attribute:: adjustment_threshold_value
                            
                            	Bandwidth change value to trigger adjustment (kbps)
                            	**type**\:  int
                            
                            	**range:** 10..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: kbit/s
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold, self).__init__()

                                self.yang_name = "adjustment-threshold"
                                self.yang_parent_name = "auto-bandwidth"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.adjustment_threshold_percent = YLeaf(YType.uint32, "adjustment-threshold-percent")

                                self.adjustment_threshold_value = YLeaf(YType.uint32, "adjustment-threshold-value")
                                self._segment_path = lambda: "adjustment-threshold"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.AutoBandwidth.AdjustmentThreshold, ['adjustment_threshold_percent', 'adjustment_threshold_value'], name, value)


                    class Priority(Entity):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority, self).__init__()

                            self.yang_name = "priority"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.setup_priority = YLeaf(YType.uint32, "setup-priority")

                            self.hold_priority = YLeaf(YType.uint32, "hold-priority")
                            self._segment_path = lambda: "priority"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Priority, ['setup_priority', 'hold_priority'], name, value)


                    class Logging(Entity):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: lsp_switch_over_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: all
                        
                        	Log all events for a tunnel
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: record_route_messsage
                        
                        	Log tunnel record\-route messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bfd_state_message
                        
                        	Enable BFD session state change alarm
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging, self).__init__()

                            self.yang_name = "logging"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.lsp_switch_over_change_message = YLeaf(YType.empty, "lsp-switch-over-change-message")

                            self.all = YLeaf(YType.empty, "all")

                            self.record_route_messsage = YLeaf(YType.empty, "record-route-messsage")

                            self.bfd_state_message = YLeaf(YType.empty, "bfd-state-message")

                            self.bandwidth_change_message = YLeaf(YType.empty, "bandwidth-change-message")

                            self.reoptimize_attempts_message = YLeaf(YType.empty, "reoptimize-attempts-message")

                            self.reroute_messsage = YLeaf(YType.empty, "reroute-messsage")

                            self.state_message = YLeaf(YType.empty, "state-message")

                            self.insufficient_bw_message = YLeaf(YType.empty, "insufficient-bw-message")

                            self.reoptimized_message = YLeaf(YType.empty, "reoptimized-message")

                            self.pcalc_failure_message = YLeaf(YType.empty, "pcalc-failure-message")
                            self._segment_path = lambda: "logging"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Logging, ['lsp_switch_over_change_message', 'all', 'record_route_messsage', 'bfd_state_message', 'bandwidth_change_message', 'reoptimize_attempts_message', 'reroute_messsage', 'state_message', 'insufficient_bw_message', 'reoptimized_message', 'pcalc_failure_message'], name, value)


                    class Bandwidth(Entity):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\:   :py:class:`MplsTeBandwidthDste <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDste>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwidth allocation
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**units**\: kbit/s
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth, self).__init__()

                            self.yang_name = "bandwidth"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.dste_type = YLeaf(YType.enumeration, "dste-type")

                            self.class_or_pool_type = YLeaf(YType.uint32, "class-or-pool-type")

                            self.bandwidth = YLeaf(YType.uint32, "bandwidth")
                            self._segment_path = lambda: "bandwidth"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Bandwidth, ['dste_type', 'class_or_pool_type', 'bandwidth'], name, value)


                    class Autoroute(Entity):
                        """
                        Parameters for IGP routing over tunnel
                        
                        .. attribute:: autoroute_announce
                        
                        	Announce tunnel to IGP
                        	**type**\:   :py:class:`AutorouteAnnounce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce>`
                        
                        .. attribute:: destinations
                        
                        	Tunnel Autoroute Destination(s)
                        	**type**\:   :py:class:`Destinations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute, self).__init__()

                            self.yang_name = "autoroute"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"autoroute-announce" : ("autoroute_announce", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce), "destinations" : ("destinations", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations)}
                            self._child_list_classes = {}

                            self.autoroute_announce = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce()
                            self.autoroute_announce.parent = self
                            self._children_name_map["autoroute_announce"] = "autoroute-announce"
                            self._children_yang_names.add("autoroute-announce")

                            self.destinations = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations()
                            self.destinations.parent = self
                            self._children_name_map["destinations"] = "destinations"
                            self._children_yang_names.add("destinations")
                            self._segment_path = lambda: "autoroute"


                        class AutorouteAnnounce(Entity):
                            """
                            Announce tunnel to IGP
                            
                            .. attribute:: exclude_traffic
                            
                            	Exclude traffic on autorouted tunnel
                            	**type**\:   :py:class:`ExcludeTraffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic>`
                            
                            .. attribute:: metric
                            
                            	Specify MPLS tunnel metric
                            	**type**\:   :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric>`
                            
                            .. attribute:: enable
                            
                            	Enable autoroute announce
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: include_ipv6
                            
                            	Specify that the tunnel should be an IPv6 autoroute announce also
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce, self).__init__()

                                self.yang_name = "autoroute-announce"
                                self.yang_parent_name = "autoroute"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"exclude-traffic" : ("exclude_traffic", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic), "metric" : ("metric", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric)}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.include_ipv6 = YLeaf(YType.empty, "include-ipv6")

                                self.exclude_traffic = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic()
                                self.exclude_traffic.parent = self
                                self._children_name_map["exclude_traffic"] = "exclude-traffic"
                                self._children_yang_names.add("exclude-traffic")

                                self.metric = MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric()
                                self.metric.parent = self
                                self._children_name_map["metric"] = "metric"
                                self._children_yang_names.add("metric")
                                self._segment_path = lambda: "autoroute-announce"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce, ['enable', 'include_ipv6'], name, value)


                            class ExcludeTraffic(Entity):
                                """
                                Exclude traffic on autorouted tunnel
                                
                                .. attribute:: segment_routing
                                
                                	Exclude tunnel in IGP for SR prefixes
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic, self).__init__()

                                    self.yang_name = "exclude-traffic"
                                    self.yang_parent_name = "autoroute-announce"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.segment_routing = YLeaf(YType.empty, "segment-routing")
                                    self._segment_path = lambda: "exclude-traffic"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.ExcludeTraffic, ['segment_routing'], name, value)


                            class Metric(Entity):
                                """
                                Specify MPLS tunnel metric
                                
                                .. attribute:: metric_type
                                
                                	Autoroute tunnel metric type
                                	**type**\:   :py:class:`MplsTeAutorouteMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeAutorouteMetric>`
                                
                                .. attribute:: absolute_metric
                                
                                	The absolute metric value
                                	**type**\:  int
                                
                                	**range:** 1..2147483647
                                
                                .. attribute:: relative_metric
                                
                                	The value of the adjustment
                                	**type**\:  int
                                
                                	**range:** \-10..10
                                
                                .. attribute:: constant_metric
                                
                                	The constant metric value
                                	**type**\:  int
                                
                                	**range:** 1..2147483647
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric, self).__init__()

                                    self.yang_name = "metric"
                                    self.yang_parent_name = "autoroute-announce"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.metric_type = YLeaf(YType.enumeration, "metric-type")

                                    self.absolute_metric = YLeaf(YType.uint32, "absolute-metric")

                                    self.relative_metric = YLeaf(YType.int32, "relative-metric")

                                    self.constant_metric = YLeaf(YType.uint32, "constant-metric")
                                    self._segment_path = lambda: "metric"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.AutorouteAnnounce.Metric, ['metric_type', 'absolute_metric', 'relative_metric', 'constant_metric'], name, value)


                        class Destinations(Entity):
                            """
                            Tunnel Autoroute Destination(s)
                            
                            .. attribute:: destination
                            
                            	Destination address to add in RIB
                            	**type**\: list of    :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations.Destination>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations, self).__init__()

                                self.yang_name = "destinations"
                                self.yang_parent_name = "autoroute"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"destination" : ("destination", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations.Destination)}

                                self.destination = YList(self)
                                self._segment_path = lambda: "destinations"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations, [], name, value)


                            class Destination(Entity):
                                """
                                Destination address to add in RIB
                                
                                .. attribute:: destination_address  <key>
                                
                                	IP address of destination
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations.Destination, self).__init__()

                                    self.yang_name = "destination"
                                    self.yang_parent_name = "destinations"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.destination_address = YLeaf(YType.str, "destination-address")
                                    self._segment_path = lambda: "destination" + "[destination-address='" + self.destination_address.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.Autoroute.Destinations.Destination, ['destination_address'], name, value)


                    class NewStyleAffinityAffinityTypes(Entity):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity_affinity_type
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes, self).__init__()

                            self.yang_name = "new-style-affinity-affinity-types"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"new-style-affinity-affinity-type" : ("new_style_affinity_affinity_type", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType), "new-style-affinity-affinity-type-affinity1" : ("new_style_affinity_affinity_type_affinity1", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1), "new-style-affinity-affinity-type-affinity1-affinity2" : ("new_style_affinity_affinity_type_affinity1_affinity2", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10", MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10)}

                            self.new_style_affinity_affinity_type = YList(self)
                            self.new_style_affinity_affinity_type_affinity1 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10 = YList(self)
                            self._segment_path = lambda: "new-style-affinity-affinity-types"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes, [], name, value)


                        class NewStyleAffinityAffinityType(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")
                                self._segment_path = lambda: "new-style-affinity-affinity-type" + "[affinity-type='" + self.affinity_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, ['affinity_type'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, ['affinity_type', 'affinity1'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, ['affinity_type', 'affinity1', 'affinity2'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, ['affinity_type', 'affinity1', 'affinity2', 'affinity3'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")

                                self.affinity10 = YLeaf(YType.str, "affinity10")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']" + "[affinity10='" + self.affinity10.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9', 'affinity10'], name, value)


                    class FastReroute(Entity):
                        """
                        Specify MPLS tunnel can be fast\-rerouted
                        
                        .. attribute:: bandwidth_protection
                        
                        	Bandwidth Protection
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: node_protection
                        
                        	Node Protection
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute, self).__init__()

                            self.yang_name = "fast-reroute"
                            self.yang_parent_name = "tunnel-attributes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bandwidth_protection = YLeaf(YType.uint32, "bandwidth-protection")

                            self.node_protection = YLeaf(YType.uint32, "node-protection")
                            self._segment_path = lambda: "fast-reroute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelAttributes.FastReroute, ['bandwidth_protection', 'node_protection'], name, value)


                class TunnelId(Entity):
                    """
                    Set the tunnel ID
                    
                    .. attribute:: tunnel_id_type
                    
                    	Tunnel ID Type
                    	**type**\:   :py:class:`MplsTeTunnelId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelId>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel ID
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId, self).__init__()

                        self.yang_name = "tunnel-id"
                        self.yang_parent_name = "tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.tunnel_id_type = YLeaf(YType.enumeration, "tunnel-id-type")

                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")
                        self._segment_path = lambda: "tunnel-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.NamedTunnels.Tunnels.Tunnel.TunnelId, ['tunnel_id_type', 'tunnel_id'], name, value)


    class GmplsUni(Entity):
        """
        GMPLS\-UNI configuration
        
        .. attribute:: timers
        
        	GMPLS\-UNI timer configuration
        	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Timers>`
        
        .. attribute:: controllers
        
        	GMPLS\-UNI controllers
        	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.GmplsUni, self).__init__()

            self.yang_name = "gmpls-uni"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"timers" : ("timers", MplsTe.GmplsUni.Timers), "controllers" : ("controllers", MplsTe.GmplsUni.Controllers)}
            self._child_list_classes = {}

            self.timers = MplsTe.GmplsUni.Timers()
            self.timers.parent = self
            self._children_name_map["timers"] = "timers"
            self._children_yang_names.add("timers")

            self.controllers = MplsTe.GmplsUni.Controllers()
            self.controllers.parent = self
            self._children_name_map["controllers"] = "controllers"
            self._children_yang_names.add("controllers")
            self._segment_path = lambda: "gmpls-uni"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()


        class Timers(Entity):
            """
            GMPLS\-UNI timer configuration
            
            .. attribute:: path_option_timers
            
            	GMPLS\-UNI path\-option timer configuration
            	**type**\:   :py:class:`PathOptionTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Timers.PathOptionTimers>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GmplsUni.Timers, self).__init__()

                self.yang_name = "timers"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"path-option-timers" : ("path_option_timers", MplsTe.GmplsUni.Timers.PathOptionTimers)}
                self._child_list_classes = {}

                self.path_option_timers = MplsTe.GmplsUni.Timers.PathOptionTimers()
                self.path_option_timers.parent = self
                self._children_name_map["path_option_timers"] = "path-option-timers"
                self._children_yang_names.add("path-option-timers")
                self._segment_path = lambda: "timers"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-uni/%s" % self._segment_path()


            class PathOptionTimers(Entity):
                """
                GMPLS\-UNI path\-option timer configuration
                
                .. attribute:: holddown
                
                	GMPLS\-UNI path\-option holddown timer configuration
                	**type**\:   :py:class:`Holddown <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GmplsUni.Timers.PathOptionTimers, self).__init__()

                    self.yang_name = "path-option-timers"
                    self.yang_parent_name = "timers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"holddown" : ("holddown", MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown)}
                    self._child_list_classes = {}

                    self.holddown = MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown()
                    self.holddown.parent = self
                    self._children_name_map["holddown"] = "holddown"
                    self._children_yang_names.add("holddown")
                    self._segment_path = lambda: "path-option-timers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-uni/timers/%s" % self._segment_path()


                class Holddown(Entity):
                    """
                    GMPLS\-UNI path\-option holddown timer
                    configuration
                    
                    .. attribute:: minimum
                    
                    	Minimum holddown (seconds)
                    	**type**\:  int
                    
                    	**range:** 5..3600
                    
                    	**units**\: second
                    
                    .. attribute:: maximum
                    
                    	Maximum holddown (seconds)
                    	**type**\:  int
                    
                    	**range:** 5..3600
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown, self).__init__()

                        self.yang_name = "holddown"
                        self.yang_parent_name = "path-option-timers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.minimum = YLeaf(YType.uint32, "minimum")

                        self.maximum = YLeaf(YType.uint32, "maximum")
                        self._segment_path = lambda: "holddown"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-uni/timers/path-option-timers/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown, ['minimum', 'maximum'], name, value)


        class Controllers(Entity):
            """
            GMPLS\-UNI controllers
            
            .. attribute:: controller
            
            	Configure a GMPLS controller
            	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GmplsUni.Controllers, self).__init__()

                self.yang_name = "controllers"
                self.yang_parent_name = "gmpls-uni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"controller" : ("controller", MplsTe.GmplsUni.Controllers.Controller)}

                self.controller = YList(self)
                self._segment_path = lambda: "controllers"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-uni/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GmplsUni.Controllers, [], name, value)


            class Controller(Entity):
                """
                Configure a GMPLS controller
                
                .. attribute:: controller_name  <key>
                
                	Controller name
                	**type**\:  str
                
                .. attribute:: announce
                
                	Announce discovered tunnel properties to system
                	**type**\:   :py:class:`Announce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.Announce>`
                
                .. attribute:: controller_logging
                
                	Controller logging
                	**type**\:   :py:class:`ControllerLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.ControllerLogging>`
                
                .. attribute:: gmpls_unitunnel_head
                
                	GMPLS\-UNI tunnel\-head properties
                	**type**\:   :py:class:`GmplsUnitunnelHead <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead>`
                
                .. attribute:: enable
                
                	Enable GMPLS\-UNI on the link
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GmplsUni.Controllers.Controller, self).__init__()

                    self.yang_name = "controller"
                    self.yang_parent_name = "controllers"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"announce" : ("announce", MplsTe.GmplsUni.Controllers.Controller.Announce), "controller-logging" : ("controller_logging", MplsTe.GmplsUni.Controllers.Controller.ControllerLogging), "gmpls-unitunnel-head" : ("gmpls_unitunnel_head", MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead)}
                    self._child_list_classes = {}

                    self.controller_name = YLeaf(YType.str, "controller-name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.announce = MplsTe.GmplsUni.Controllers.Controller.Announce()
                    self.announce.parent = self
                    self._children_name_map["announce"] = "announce"
                    self._children_yang_names.add("announce")

                    self.controller_logging = MplsTe.GmplsUni.Controllers.Controller.ControllerLogging()
                    self.controller_logging.parent = self
                    self._children_name_map["controller_logging"] = "controller-logging"
                    self._children_yang_names.add("controller-logging")

                    self.gmpls_unitunnel_head = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead()
                    self.gmpls_unitunnel_head.parent = self
                    self._children_name_map["gmpls_unitunnel_head"] = "gmpls-unitunnel-head"
                    self._children_yang_names.add("gmpls-unitunnel-head")
                    self._segment_path = lambda: "controller" + "[controller-name='" + self.controller_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-uni/controllers/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller, ['controller_name', 'enable'], name, value)


                class Announce(Entity):
                    """
                    Announce discovered tunnel properties to
                    system
                    
                    .. attribute:: srl_gs
                    
                    	Enable announcement of discovered SRLGs
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsUni.Controllers.Controller.Announce, self).__init__()

                        self.yang_name = "announce"
                        self.yang_parent_name = "controller"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.srl_gs = YLeaf(YType.empty, "srl-gs")
                        self._segment_path = lambda: "announce"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.Announce, ['srl_gs'], name, value)


                class ControllerLogging(Entity):
                    """
                    Controller logging
                    
                    .. attribute:: discovered_srlg_change_logging
                    
                    	Enable logging of changes to of discovered SRLGs
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsUni.Controllers.Controller.ControllerLogging, self).__init__()

                        self.yang_name = "controller-logging"
                        self.yang_parent_name = "controller"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.discovered_srlg_change_logging = YLeaf(YType.empty, "discovered-srlg-change-logging")
                        self._segment_path = lambda: "controller-logging"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.ControllerLogging, ['discovered_srlg_change_logging'], name, value)


                class GmplsUnitunnelHead(Entity):
                    """
                    GMPLS\-UNI tunnel\-head properties
                    
                    .. attribute:: path_options
                    
                    	Path\-option configuration
                    	**type**\:   :py:class:`PathOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions>`
                    
                    .. attribute:: recording
                    
                    	Tunnel property recording
                    	**type**\:   :py:class:`Recording <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording>`
                    
                    .. attribute:: logging
                    
                    	Tunnel event logging
                    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging>`
                    
                    .. attribute:: tunnel_id
                    
                    	GMPLS\-UNI head tunnel\-id
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: enable
                    
                    	Set link as a GMPLS tunnel head
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: destination
                    
                    	Set the destination of the tunnel
                    	**type**\:  str
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: signalled_name
                    
                    	The name of the tunnel to be included in signalling messages
                    	**type**\:  str
                    
                    	**length:** 1..254
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead, self).__init__()

                        self.yang_name = "gmpls-unitunnel-head"
                        self.yang_parent_name = "controller"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"path-options" : ("path_options", MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions), "recording" : ("recording", MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording), "logging" : ("logging", MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging), "priority" : ("priority", MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority)}
                        self._child_list_classes = {}

                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.destination = YLeaf(YType.str, "destination")

                        self.record_route = YLeaf(YType.empty, "record-route")

                        self.signalled_name = YLeaf(YType.str, "signalled-name")

                        self.path_options = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions()
                        self.path_options.parent = self
                        self._children_name_map["path_options"] = "path-options"
                        self._children_yang_names.add("path-options")

                        self.recording = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording()
                        self.recording.parent = self
                        self._children_name_map["recording"] = "recording"
                        self._children_yang_names.add("recording")

                        self.logging = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging()
                        self.logging.parent = self
                        self._children_name_map["logging"] = "logging"
                        self._children_yang_names.add("logging")

                        self.priority = None
                        self._children_name_map["priority"] = "priority"
                        self._children_yang_names.add("priority")
                        self._segment_path = lambda: "gmpls-unitunnel-head"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead, ['tunnel_id', 'enable', 'destination', 'record_route', 'signalled_name'], name, value)


                    class PathOptions(Entity):
                        """
                        Path\-option configuration
                        
                        .. attribute:: path_option
                        
                        	A Path\-option
                        	**type**\: list of    :py:class:`PathOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions, self).__init__()

                            self.yang_name = "path-options"
                            self.yang_parent_name = "gmpls-unitunnel-head"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"path-option" : ("path_option", MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption)}

                            self.path_option = YList(self)
                            self._segment_path = lambda: "path-options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions, [], name, value)


                        class PathOption(Entity):
                            """
                            A Path\-option
                            
                            .. attribute:: preference_level  <key>
                            
                            	Preference level for this path option
                            	**type**\:  int
                            
                            	**range:** 1..1000
                            
                            .. attribute:: path_type
                            
                            	The type of the path option
                            	**type**\:   :py:class:`MplsTePathOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOption>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: path_id
                            
                            	The ID of the explicit path associated with this option
                            	**type**\:  int
                            
                            	**range:** 1..65535
                            
                            	**default value**\: 1
                            
                            .. attribute:: path_name
                            
                            	The name of the explicit path associated with this option
                            	**type**\:  str
                            
                            .. attribute:: xro_type
                            
                            	The route\-exclusion type
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: xro_attribute_set_name
                            
                            	The name of the XRO attribute set to be used for this path\-option
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: lockdown
                            
                            	Path option properties\: must be Lockdown
                            	**type**\:   :py:class:`MplsTePathOptionProperty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionProperty>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: verbatim
                            
                            	Path option properties\: must be verbatim if set
                            	**type**\:   :py:class:`MplsTePathOptionProperty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionProperty>`
                            
                            	**default value**\: none
                            
                            .. attribute:: signaled_label
                            
                            	Signaled label type
                            	**type**\:   :py:class:`MplsTeSignaledLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeSignaledLabel>`
                            
                            	**default value**\: not-set
                            
                            .. attribute:: dwdm_channel
                            
                            	DWDM channel number
                            	**type**\:  int
                            
                            	**range:** 1..89
                            
                            	**default value**\: 1
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption, self).__init__()

                                self.yang_name = "path-option"
                                self.yang_parent_name = "path-options"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.preference_level = YLeaf(YType.uint32, "preference-level")

                                self.path_type = YLeaf(YType.enumeration, "path-type")

                                self.path_id = YLeaf(YType.uint32, "path-id")

                                self.path_name = YLeaf(YType.str, "path-name")

                                self.xro_type = YLeaf(YType.empty, "xro-type")

                                self.xro_attribute_set_name = YLeaf(YType.str, "xro-attribute-set-name")

                                self.lockdown = YLeaf(YType.enumeration, "lockdown")

                                self.verbatim = YLeaf(YType.enumeration, "verbatim")

                                self.signaled_label = YLeaf(YType.enumeration, "signaled-label")

                                self.dwdm_channel = YLeaf(YType.uint32, "dwdm-channel")
                                self._segment_path = lambda: "path-option" + "[preference-level='" + self.preference_level.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption, ['preference_level', 'path_type', 'path_id', 'path_name', 'xro_type', 'xro_attribute_set_name', 'lockdown', 'verbatim', 'signaled_label', 'dwdm_channel'], name, value)


                    class Recording(Entity):
                        """
                        Tunnel property recording
                        
                        .. attribute:: srlg
                        
                        	Enable SRLG\-recording during signaling
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording, self).__init__()

                            self.yang_name = "recording"
                            self.yang_parent_name = "gmpls-unitunnel-head"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.srlg = YLeaf(YType.empty, "srlg")
                            self._segment_path = lambda: "recording"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording, ['srlg'], name, value)


                    class Logging(Entity):
                        """
                        Tunnel event logging
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging, self).__init__()

                            self.yang_name = "logging"
                            self.yang_parent_name = "gmpls-unitunnel-head"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.state_message = YLeaf(YType.empty, "state-message")
                            self._segment_path = lambda: "logging"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging, ['state_message'], name, value)


                    class Priority(Entity):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority, self).__init__()

                            self.yang_name = "priority"
                            self.yang_parent_name = "gmpls-unitunnel-head"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.setup_priority = YLeaf(YType.uint32, "setup-priority")

                            self.hold_priority = YLeaf(YType.uint32, "hold-priority")
                            self._segment_path = lambda: "priority"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority, ['setup_priority', 'hold_priority'], name, value)


    class GlobalAttributes(Entity):
        """
        Configure MPLS TE global attributes
        
        .. attribute:: auto_tunnel
        
        	Configure auto\-tunnels feature
        	**type**\:   :py:class:`AutoTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel>`
        
        .. attribute:: hardware_out_of_resource
        
        	Configure HW OOR processing in MPLS\-TE
        	**type**\:   :py:class:`HardwareOutOfResource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.HardwareOutOfResource>`
        
        .. attribute:: secondary_router_ids
        
        	Configure MPLS TE Secondary Router ID
        	**type**\:   :py:class:`SecondaryRouterIds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.SecondaryRouterIds>`
        
        .. attribute:: srlg
        
        	Configure SRLG values and MPLS\-TE properties
        	**type**\:   :py:class:`Srlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg>`
        
        .. attribute:: queues
        
        	Configure MPLS TE route priority
        	**type**\:   :py:class:`Queues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Queues>`
        
        .. attribute:: mib
        
        	MPLS\-TE MIB properties
        	**type**\:   :py:class:`Mib <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Mib>`
        
        .. attribute:: attribute_set
        
        	Attribute AttributeSets
        	**type**\:   :py:class:`AttributeSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet>`
        
        .. attribute:: bfd_over_lsp
        
        	BFD over MPLS TE Global Configurations
        	**type**\:   :py:class:`BfdOverLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BfdOverLsp>`
        
        .. attribute:: bandwidth_accounting
        
        	Bandwidth accounting configuration data
        	**type**\:   :py:class:`BandwidthAccounting <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BandwidthAccounting>`
        
        .. attribute:: pce_attributes
        
        	Configuration MPLS TE PCE attributes
        	**type**\:   :py:class:`PceAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes>`
        
        .. attribute:: lsp_out_of_resource
        
        	Configure LSP OOR attributes in MPLS\-TE
        	**type**\:   :py:class:`LspOutOfResource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.LspOutOfResource>`
        
        .. attribute:: soft_preemption
        
        	Soft preemption configuration data
        	**type**\:   :py:class:`SoftPreemption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.SoftPreemption>`
        
        .. attribute:: fast_reroute
        
        	Configure fast reroute attributes
        	**type**\:   :py:class:`FastReroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.FastReroute>`
        
        .. attribute:: path_selection
        
        	Path selection configuration
        	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection>`
        
        .. attribute:: affinity_mappings
        
        	Affinity Mapping Table configuration
        	**type**\:   :py:class:`AffinityMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AffinityMappings>`
        
        .. attribute:: log_nsr_status
        
        	Log NSR status messages
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_issu_status
        
        	Log ISSU status messages
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: reoptimize_link_up
        
        	Enable reoptimization based on link\-up events
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: reoptimize_delay_cleanup_timer
        
        	Reoptimization Delay Cleanup Value (seconds)
        	**type**\:  int
        
        	**range:** 0..300
        
        	**units**\: second
        
        .. attribute:: disable_reoptimize_affinity_failure
        
        	Disable reoptimization after affinity failures
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: maximum_tunnels
        
        	The maximum number of tunnel heads that will be allowed
        	**type**\:  int
        
        	**range:** 1..65536
        
        	**default value**\: 4096
        
        .. attribute:: link_holddown_timer
        
        	Holddown time for links which had Path Errors in seconds
        	**type**\:  int
        
        	**range:** 0..300
        
        	**units**\: second
        
        	**default value**\: 10
        
        .. attribute:: fault_oam
        
        	Enable Fault\-OAM functionality for bidirectional tunnels
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: enable_unequal_load_balancing
        
        	Enable unequal load\-balancing over tunnels to the same destination
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_tail
        
        	Log all tail tunnel events
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: reoptimize_delay_after_frr_timer
        
        	Reoptimization Delay After FRR Value (seconds)
        	**type**\:  int
        
        	**range:** 0..120
        
        	**units**\: second
        
        .. attribute:: auto_bandwidth_collect_frequency
        
        	Auto\-bandwidth global collection frequency in minutes
        	**type**\:  int
        
        	**range:** 1..10080
        
        	**units**\: minute
        
        	**default value**\: 5
        
        .. attribute:: reopt_delay_path_protect_switchover_timer
        
        	Seconds between path protect switchover and tunnel re\-optimization. Set to 0 to disable
        	**type**\:  int
        
        	**range:** 0..604800
        
        	**units**\: second
        
        	**default value**\: 180
        
        .. attribute:: log_all
        
        	Always set to true
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: loose_path_retry_period
        
        	Signalling retry for tunnels terminating outside the headend area
        	**type**\:  int
        
        	**range:** 30..600
        
        	**default value**\: 120
        
        .. attribute:: reoptimize_load_balancing
        
        	Load balance bandwidth during reoptimization
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_head
        
        	Log all head tunnel events
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: path_selection_ignore_overload
        
        	Deprecated \- do not use
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: graceful_preemption_on_bandwidth_reduction
        
        	Enable graceful preemption when there is a bandwidth reduction
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: advertise_explicit_nulls
        
        	Enable explicit\-null advertising to PHOP
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: reoptimize_delay_install_timer
        
        	Reoptimization Delay Install Value (seconds)
        	**type**\:  int
        
        	**range:** 0..3600
        
        	**units**\: second
        
        .. attribute:: reoptimize_delay_after_affinity_failure_timer
        
        	Delay reoptimizing current LSP after affinity failures
        	**type**\:  int
        
        	**range:** 1..604800
        
        	**units**\: second
        
        .. attribute:: log_frr_protection
        
        	Log FRR Protection messages
        	**type**\:   :py:class:`MplsTeLogFrrProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeLogFrrProtection>`
        
        .. attribute:: reoptimize_timer_frequency
        
        	Reoptimize timers period in seconds
        	**type**\:  int
        
        	**range:** 0..604800
        
        	**units**\: second
        
        	**default value**\: 3600
        
        .. attribute:: log_mid
        
        	Log all mid tunnel events
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: log_preemption
        
        	Log tunnel preemption messages
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.GlobalAttributes, self).__init__()

            self.yang_name = "global-attributes"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"auto-tunnel" : ("auto_tunnel", MplsTe.GlobalAttributes.AutoTunnel), "hardware-out-of-resource" : ("hardware_out_of_resource", MplsTe.GlobalAttributes.HardwareOutOfResource), "secondary-router-ids" : ("secondary_router_ids", MplsTe.GlobalAttributes.SecondaryRouterIds), "srlg" : ("srlg", MplsTe.GlobalAttributes.Srlg), "queues" : ("queues", MplsTe.GlobalAttributes.Queues), "mib" : ("mib", MplsTe.GlobalAttributes.Mib), "attribute-set" : ("attribute_set", MplsTe.GlobalAttributes.AttributeSet), "bfd-over-lsp" : ("bfd_over_lsp", MplsTe.GlobalAttributes.BfdOverLsp), "bandwidth-accounting" : ("bandwidth_accounting", MplsTe.GlobalAttributes.BandwidthAccounting), "pce-attributes" : ("pce_attributes", MplsTe.GlobalAttributes.PceAttributes), "lsp-out-of-resource" : ("lsp_out_of_resource", MplsTe.GlobalAttributes.LspOutOfResource), "soft-preemption" : ("soft_preemption", MplsTe.GlobalAttributes.SoftPreemption), "fast-reroute" : ("fast_reroute", MplsTe.GlobalAttributes.FastReroute), "path-selection" : ("path_selection", MplsTe.GlobalAttributes.PathSelection), "affinity-mappings" : ("affinity_mappings", MplsTe.GlobalAttributes.AffinityMappings)}
            self._child_list_classes = {}

            self.log_nsr_status = YLeaf(YType.empty, "log-nsr-status")

            self.log_issu_status = YLeaf(YType.empty, "log-issu-status")

            self.reoptimize_link_up = YLeaf(YType.empty, "reoptimize-link-up")

            self.reoptimize_delay_cleanup_timer = YLeaf(YType.uint32, "reoptimize-delay-cleanup-timer")

            self.disable_reoptimize_affinity_failure = YLeaf(YType.empty, "disable-reoptimize-affinity-failure")

            self.maximum_tunnels = YLeaf(YType.uint32, "maximum-tunnels")

            self.link_holddown_timer = YLeaf(YType.uint32, "link-holddown-timer")

            self.fault_oam = YLeaf(YType.empty, "fault-oam")

            self.enable_unequal_load_balancing = YLeaf(YType.empty, "enable-unequal-load-balancing")

            self.log_tail = YLeaf(YType.empty, "log-tail")

            self.reoptimize_delay_after_frr_timer = YLeaf(YType.uint32, "reoptimize-delay-after-frr-timer")

            self.auto_bandwidth_collect_frequency = YLeaf(YType.uint32, "auto-bandwidth-collect-frequency")

            self.reopt_delay_path_protect_switchover_timer = YLeaf(YType.uint32, "reopt-delay-path-protect-switchover-timer")

            self.log_all = YLeaf(YType.empty, "log-all")

            self.loose_path_retry_period = YLeaf(YType.uint32, "loose-path-retry-period")

            self.reoptimize_load_balancing = YLeaf(YType.empty, "reoptimize-load-balancing")

            self.log_head = YLeaf(YType.empty, "log-head")

            self.path_selection_ignore_overload = YLeaf(YType.empty, "path-selection-ignore-overload")

            self.graceful_preemption_on_bandwidth_reduction = YLeaf(YType.empty, "graceful-preemption-on-bandwidth-reduction")

            self.advertise_explicit_nulls = YLeaf(YType.empty, "advertise-explicit-nulls")

            self.reoptimize_delay_install_timer = YLeaf(YType.uint32, "reoptimize-delay-install-timer")

            self.reoptimize_delay_after_affinity_failure_timer = YLeaf(YType.uint32, "reoptimize-delay-after-affinity-failure-timer")

            self.log_frr_protection = YLeaf(YType.enumeration, "log-frr-protection")

            self.reoptimize_timer_frequency = YLeaf(YType.uint32, "reoptimize-timer-frequency")

            self.log_mid = YLeaf(YType.empty, "log-mid")

            self.log_preemption = YLeaf(YType.empty, "log-preemption")

            self.auto_tunnel = MplsTe.GlobalAttributes.AutoTunnel()
            self.auto_tunnel.parent = self
            self._children_name_map["auto_tunnel"] = "auto-tunnel"
            self._children_yang_names.add("auto-tunnel")

            self.hardware_out_of_resource = MplsTe.GlobalAttributes.HardwareOutOfResource()
            self.hardware_out_of_resource.parent = self
            self._children_name_map["hardware_out_of_resource"] = "hardware-out-of-resource"
            self._children_yang_names.add("hardware-out-of-resource")

            self.secondary_router_ids = MplsTe.GlobalAttributes.SecondaryRouterIds()
            self.secondary_router_ids.parent = self
            self._children_name_map["secondary_router_ids"] = "secondary-router-ids"
            self._children_yang_names.add("secondary-router-ids")

            self.srlg = MplsTe.GlobalAttributes.Srlg()
            self.srlg.parent = self
            self._children_name_map["srlg"] = "srlg"
            self._children_yang_names.add("srlg")

            self.queues = MplsTe.GlobalAttributes.Queues()
            self.queues.parent = self
            self._children_name_map["queues"] = "queues"
            self._children_yang_names.add("queues")

            self.mib = MplsTe.GlobalAttributes.Mib()
            self.mib.parent = self
            self._children_name_map["mib"] = "mib"
            self._children_yang_names.add("mib")

            self.attribute_set = MplsTe.GlobalAttributes.AttributeSet()
            self.attribute_set.parent = self
            self._children_name_map["attribute_set"] = "attribute-set"
            self._children_yang_names.add("attribute-set")

            self.bfd_over_lsp = MplsTe.GlobalAttributes.BfdOverLsp()
            self.bfd_over_lsp.parent = self
            self._children_name_map["bfd_over_lsp"] = "bfd-over-lsp"
            self._children_yang_names.add("bfd-over-lsp")

            self.bandwidth_accounting = MplsTe.GlobalAttributes.BandwidthAccounting()
            self.bandwidth_accounting.parent = self
            self._children_name_map["bandwidth_accounting"] = "bandwidth-accounting"
            self._children_yang_names.add("bandwidth-accounting")

            self.pce_attributes = MplsTe.GlobalAttributes.PceAttributes()
            self.pce_attributes.parent = self
            self._children_name_map["pce_attributes"] = "pce-attributes"
            self._children_yang_names.add("pce-attributes")

            self.lsp_out_of_resource = MplsTe.GlobalAttributes.LspOutOfResource()
            self.lsp_out_of_resource.parent = self
            self._children_name_map["lsp_out_of_resource"] = "lsp-out-of-resource"
            self._children_yang_names.add("lsp-out-of-resource")

            self.soft_preemption = MplsTe.GlobalAttributes.SoftPreemption()
            self.soft_preemption.parent = self
            self._children_name_map["soft_preemption"] = "soft-preemption"
            self._children_yang_names.add("soft-preemption")

            self.fast_reroute = MplsTe.GlobalAttributes.FastReroute()
            self.fast_reroute.parent = self
            self._children_name_map["fast_reroute"] = "fast-reroute"
            self._children_yang_names.add("fast-reroute")

            self.path_selection = MplsTe.GlobalAttributes.PathSelection()
            self.path_selection.parent = self
            self._children_name_map["path_selection"] = "path-selection"
            self._children_yang_names.add("path-selection")

            self.affinity_mappings = MplsTe.GlobalAttributes.AffinityMappings()
            self.affinity_mappings.parent = self
            self._children_name_map["affinity_mappings"] = "affinity-mappings"
            self._children_yang_names.add("affinity-mappings")
            self._segment_path = lambda: "global-attributes"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.GlobalAttributes, ['log_nsr_status', 'log_issu_status', 'reoptimize_link_up', 'reoptimize_delay_cleanup_timer', 'disable_reoptimize_affinity_failure', 'maximum_tunnels', 'link_holddown_timer', 'fault_oam', 'enable_unequal_load_balancing', 'log_tail', 'reoptimize_delay_after_frr_timer', 'auto_bandwidth_collect_frequency', 'reopt_delay_path_protect_switchover_timer', 'log_all', 'loose_path_retry_period', 'reoptimize_load_balancing', 'log_head', 'path_selection_ignore_overload', 'graceful_preemption_on_bandwidth_reduction', 'advertise_explicit_nulls', 'reoptimize_delay_install_timer', 'reoptimize_delay_after_affinity_failure_timer', 'log_frr_protection', 'reoptimize_timer_frequency', 'log_mid', 'log_preemption'], name, value)


        class AutoTunnel(Entity):
            """
            Configure auto\-tunnels feature
            
            .. attribute:: pcc
            
            	Configure auto\-tunnel PCC (Path Computation Client) feature
            	**type**\:   :py:class:`Pcc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Pcc>`
            
            .. attribute:: p2p_auto_tunnel
            
            	Configure P2P auto\-tunnel feature
            	**type**\:   :py:class:`P2PAutoTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel>`
            
            .. attribute:: backup
            
            	Configure auto\-tunnel backup feature
            	**type**\:   :py:class:`Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup>`
            
            .. attribute:: mesh
            
            	Configure auto\-tunnel mesh feature
            	**type**\:   :py:class:`Mesh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh>`
            
            .. attribute:: p2mp_auto_tunnel
            
            	Configure P2MP auto\-tunnel feature
            	**type**\:   :py:class:`P2MpAutoTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.AutoTunnel, self).__init__()

                self.yang_name = "auto-tunnel"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"pcc" : ("pcc", MplsTe.GlobalAttributes.AutoTunnel.Pcc), "p2p-auto-tunnel" : ("p2p_auto_tunnel", MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel), "backup" : ("backup", MplsTe.GlobalAttributes.AutoTunnel.Backup), "mesh" : ("mesh", MplsTe.GlobalAttributes.AutoTunnel.Mesh), "p2mp-auto-tunnel" : ("p2mp_auto_tunnel", MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel)}
                self._child_list_classes = {}

                self.pcc = MplsTe.GlobalAttributes.AutoTunnel.Pcc()
                self.pcc.parent = self
                self._children_name_map["pcc"] = "pcc"
                self._children_yang_names.add("pcc")

                self.p2p_auto_tunnel = MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel()
                self.p2p_auto_tunnel.parent = self
                self._children_name_map["p2p_auto_tunnel"] = "p2p-auto-tunnel"
                self._children_yang_names.add("p2p-auto-tunnel")

                self.backup = MplsTe.GlobalAttributes.AutoTunnel.Backup()
                self.backup.parent = self
                self._children_name_map["backup"] = "backup"
                self._children_yang_names.add("backup")

                self.mesh = MplsTe.GlobalAttributes.AutoTunnel.Mesh()
                self.mesh.parent = self
                self._children_name_map["mesh"] = "mesh"
                self._children_yang_names.add("mesh")

                self.p2mp_auto_tunnel = MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel()
                self.p2mp_auto_tunnel.parent = self
                self._children_name_map["p2mp_auto_tunnel"] = "p2mp-auto-tunnel"
                self._children_yang_names.add("p2mp-auto-tunnel")
                self._segment_path = lambda: "auto-tunnel"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()


            class Pcc(Entity):
                """
                Configure auto\-tunnel PCC (Path Computation
                Client) feature
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\:   :py:class:`TunnelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AutoTunnel.Pcc, self).__init__()

                    self.yang_name = "pcc"
                    self.yang_parent_name = "auto-tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"tunnel-range" : ("tunnel_range", MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange)}
                    self._child_list_classes = {}

                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange()
                    self.tunnel_range.parent = self
                    self._children_name_map["tunnel_range"] = "tunnel-range"
                    self._children_yang_names.add("tunnel-range")
                    self._segment_path = lambda: "pcc"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/%s" % self._segment_path()


                class TunnelRange(Entity):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange, self).__init__()

                        self.yang_name = "tunnel-range"
                        self.yang_parent_name = "pcc"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.min_tunnel_id = YLeaf(YType.uint32, "min-tunnel-id")

                        self.max_tunnel_id = YLeaf(YType.uint32, "max-tunnel-id")
                        self._segment_path = lambda: "tunnel-range"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/pcc/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange, ['min_tunnel_id', 'max_tunnel_id'], name, value)


            class P2PAutoTunnel(Entity):
                """
                Configure P2P auto\-tunnel feature
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\:   :py:class:`TunnelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel, self).__init__()

                    self.yang_name = "p2p-auto-tunnel"
                    self.yang_parent_name = "auto-tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"tunnel-range" : ("tunnel_range", MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange)}
                    self._child_list_classes = {}

                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange()
                    self.tunnel_range.parent = self
                    self._children_name_map["tunnel_range"] = "tunnel-range"
                    self._children_yang_names.add("tunnel-range")
                    self._segment_path = lambda: "p2p-auto-tunnel"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/%s" % self._segment_path()


                class TunnelRange(Entity):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange, self).__init__()

                        self.yang_name = "tunnel-range"
                        self.yang_parent_name = "p2p-auto-tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.min_tunnel_id = YLeaf(YType.uint32, "min-tunnel-id")

                        self.max_tunnel_id = YLeaf(YType.uint32, "max-tunnel-id")
                        self._segment_path = lambda: "tunnel-range"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/p2p-auto-tunnel/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange, ['min_tunnel_id', 'max_tunnel_id'], name, value)


            class Backup(Entity):
                """
                Configure auto\-tunnel backup feature
                
                .. attribute:: affinity_ignore
                
                	Ignore affinity during CSPF for auto backup tunnels
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: timers
                
                	Configure auto\-tunnel backup timers value
                	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers>`
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\:   :py:class:`TunnelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AutoTunnel.Backup, self).__init__()

                    self.yang_name = "backup"
                    self.yang_parent_name = "auto-tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"timers" : ("timers", MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers), "tunnel-range" : ("tunnel_range", MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange)}
                    self._child_list_classes = {}

                    self.affinity_ignore = YLeaf(YType.empty, "affinity-ignore")

                    self.timers = MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers()
                    self.timers.parent = self
                    self._children_name_map["timers"] = "timers"
                    self._children_yang_names.add("timers")

                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange()
                    self.tunnel_range.parent = self
                    self._children_name_map["tunnel_range"] = "tunnel-range"
                    self._children_yang_names.add("tunnel-range")
                    self._segment_path = lambda: "backup"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Backup, ['affinity_ignore'], name, value)


                class Timers(Entity):
                    """
                    Configure auto\-tunnel backup timers value
                    
                    .. attribute:: removal
                    
                    	Configure auto\-tunnel backup removal timers value
                    	**type**\:   :py:class:`Removal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers, self).__init__()

                        self.yang_name = "timers"
                        self.yang_parent_name = "backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"removal" : ("removal", MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal)}
                        self._child_list_classes = {}

                        self.removal = MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal()
                        self.removal.parent = self
                        self._children_name_map["removal"] = "removal"
                        self._children_yang_names.add("removal")
                        self._segment_path = lambda: "timers"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/backup/%s" % self._segment_path()


                    class Removal(Entity):
                        """
                        Configure auto\-tunnel backup removal timers
                        value
                        
                        .. attribute:: unused
                        
                        	Auto\-tunnel backup unused timeout in minutes (0=never timeout)
                        	**type**\:  int
                        
                        	**range:** 0..10080
                        
                        	**units**\: minute
                        
                        	**default value**\: 3600
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal, self).__init__()

                            self.yang_name = "removal"
                            self.yang_parent_name = "timers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.unused = YLeaf(YType.uint32, "unused")
                            self._segment_path = lambda: "removal"
                            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/backup/timers/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal, ['unused'], name, value)


                class TunnelRange(Entity):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange, self).__init__()

                        self.yang_name = "tunnel-range"
                        self.yang_parent_name = "backup"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.min_tunnel_id = YLeaf(YType.uint32, "min-tunnel-id")

                        self.max_tunnel_id = YLeaf(YType.uint32, "max-tunnel-id")
                        self._segment_path = lambda: "tunnel-range"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/backup/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange, ['min_tunnel_id', 'max_tunnel_id'], name, value)


            class Mesh(Entity):
                """
                Configure auto\-tunnel mesh feature
                
                .. attribute:: mesh_groups
                
                	Configure auto\-tunnel mesh group
                	**type**\:   :py:class:`MeshGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups>`
                
                .. attribute:: timers
                
                	Configure auto\-tunnel backup timers value
                	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers>`
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\:   :py:class:`TunnelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AutoTunnel.Mesh, self).__init__()

                    self.yang_name = "mesh"
                    self.yang_parent_name = "auto-tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"mesh-groups" : ("mesh_groups", MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups), "timers" : ("timers", MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers), "tunnel-range" : ("tunnel_range", MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange)}
                    self._child_list_classes = {}

                    self.mesh_groups = MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups()
                    self.mesh_groups.parent = self
                    self._children_name_map["mesh_groups"] = "mesh-groups"
                    self._children_yang_names.add("mesh-groups")

                    self.timers = MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers()
                    self.timers.parent = self
                    self._children_name_map["timers"] = "timers"
                    self._children_yang_names.add("timers")

                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange()
                    self.tunnel_range.parent = self
                    self._children_name_map["tunnel_range"] = "tunnel-range"
                    self._children_yang_names.add("tunnel-range")
                    self._segment_path = lambda: "mesh"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/%s" % self._segment_path()


                class MeshGroups(Entity):
                    """
                    Configure auto\-tunnel mesh group
                    
                    .. attribute:: mesh_group
                    
                    	Auto\-mesh group identifier
                    	**type**\: list of    :py:class:`MeshGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups, self).__init__()

                        self.yang_name = "mesh-groups"
                        self.yang_parent_name = "mesh"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"mesh-group" : ("mesh_group", MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup)}

                        self.mesh_group = YList(self)
                        self._segment_path = lambda: "mesh-groups"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/mesh/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups, [], name, value)


                    class MeshGroup(Entity):
                        """
                        Auto\-mesh group identifier
                        
                        .. attribute:: mesh_group_id  <key>
                        
                        	Mesh group ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destination_list
                        
                        	The name of prefix\-list to be applied to this destination\-list
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: disable
                        
                        	Disables mesh group
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: attribute_set
                        
                        	The name of auto\-mesh attribute set to be applied to this group
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: create
                        
                        	Auto\-mesh group enable object that controls whether this group is configured or not .This object must be set before other configuration supplied for this group
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: one_hop
                        
                        	Automatically create tunnel to all next\-hops
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup, self).__init__()

                            self.yang_name = "mesh-group"
                            self.yang_parent_name = "mesh-groups"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.mesh_group_id = YLeaf(YType.uint32, "mesh-group-id")

                            self.destination_list = YLeaf(YType.str, "destination-list")

                            self.disable = YLeaf(YType.empty, "disable")

                            self.attribute_set = YLeaf(YType.str, "attribute-set")

                            self.create = YLeaf(YType.empty, "create")

                            self.one_hop = YLeaf(YType.empty, "one-hop")
                            self._segment_path = lambda: "mesh-group" + "[mesh-group-id='" + self.mesh_group_id.get() + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/mesh/mesh-groups/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup, ['mesh_group_id', 'destination_list', 'disable', 'attribute_set', 'create', 'one_hop'], name, value)


                class Timers(Entity):
                    """
                    Configure auto\-tunnel backup timers value
                    
                    .. attribute:: removal
                    
                    	Configure auto\-tunnel backup removal timers value
                    	**type**\:   :py:class:`Removal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers, self).__init__()

                        self.yang_name = "timers"
                        self.yang_parent_name = "mesh"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"removal" : ("removal", MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal)}
                        self._child_list_classes = {}

                        self.removal = MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal()
                        self.removal.parent = self
                        self._children_name_map["removal"] = "removal"
                        self._children_yang_names.add("removal")
                        self._segment_path = lambda: "timers"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/mesh/%s" % self._segment_path()


                    class Removal(Entity):
                        """
                        Configure auto\-tunnel backup removal timers
                        value
                        
                        .. attribute:: unused
                        
                        	Auto\-tunnel backup unused timeout in minutes (0=never timeout)
                        	**type**\:  int
                        
                        	**range:** 0..10080
                        
                        	**units**\: minute
                        
                        	**default value**\: 3600
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal, self).__init__()

                            self.yang_name = "removal"
                            self.yang_parent_name = "timers"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.unused = YLeaf(YType.uint32, "unused")
                            self._segment_path = lambda: "removal"
                            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/mesh/timers/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal, ['unused'], name, value)


                class TunnelRange(Entity):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange, self).__init__()

                        self.yang_name = "tunnel-range"
                        self.yang_parent_name = "mesh"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.min_tunnel_id = YLeaf(YType.uint32, "min-tunnel-id")

                        self.max_tunnel_id = YLeaf(YType.uint32, "max-tunnel-id")
                        self._segment_path = lambda: "tunnel-range"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/mesh/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange, ['min_tunnel_id', 'max_tunnel_id'], name, value)


            class P2MpAutoTunnel(Entity):
                """
                Configure P2MP auto\-tunnel feature
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\:   :py:class:`TunnelRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel, self).__init__()

                    self.yang_name = "p2mp-auto-tunnel"
                    self.yang_parent_name = "auto-tunnel"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"tunnel-range" : ("tunnel_range", MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange)}
                    self._child_list_classes = {}

                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange()
                    self.tunnel_range.parent = self
                    self._children_name_map["tunnel_range"] = "tunnel-range"
                    self._children_yang_names.add("tunnel-range")
                    self._segment_path = lambda: "p2mp-auto-tunnel"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/%s" % self._segment_path()


                class TunnelRange(Entity):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange, self).__init__()

                        self.yang_name = "tunnel-range"
                        self.yang_parent_name = "p2mp-auto-tunnel"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.min_tunnel_id = YLeaf(YType.uint32, "min-tunnel-id")

                        self.max_tunnel_id = YLeaf(YType.uint32, "max-tunnel-id")
                        self._segment_path = lambda: "tunnel-range"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/auto-tunnel/p2mp-auto-tunnel/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange, ['min_tunnel_id', 'max_tunnel_id'], name, value)


        class HardwareOutOfResource(Entity):
            """
            Configure HW OOR processing in MPLS\-TE
            
            .. attribute:: oor_red_state
            
            	Configuration for HW OOR Red State
            	**type**\:   :py:class:`OorRedState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState>`
            
            .. attribute:: oor_yellow_state
            
            	Configuration for HW OOR Yellow State
            	**type**\:   :py:class:`OorYellowState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState>`
            
            .. attribute:: oor_green_state
            
            	Configuration for HW OOR Green State
            	**type**\:   :py:class:`OorGreenState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.HardwareOutOfResource, self).__init__()

                self.yang_name = "hardware-out-of-resource"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"oor-red-state" : ("oor_red_state", MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState), "oor-yellow-state" : ("oor_yellow_state", MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState), "oor-green-state" : ("oor_green_state", MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState)}
                self._child_list_classes = {}

                self.oor_red_state = MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState()
                self.oor_red_state.parent = self
                self._children_name_map["oor_red_state"] = "oor-red-state"
                self._children_yang_names.add("oor-red-state")

                self.oor_yellow_state = MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState()
                self.oor_yellow_state.parent = self
                self._children_name_map["oor_yellow_state"] = "oor-yellow-state"
                self._children_yang_names.add("oor-yellow-state")

                self.oor_green_state = MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState()
                self.oor_green_state.parent = self
                self._children_name_map["oor_green_state"] = "oor-green-state"
                self._children_yang_names.add("oor-green-state")
                self._segment_path = lambda: "hardware-out-of-resource"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()


            class OorRedState(Entity):
                """
                Configuration for HW OOR Red State
                
                .. attribute:: oor_node_protection_disable
                
                	Disable FRR node\-protection when the link is in this OOR State
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: oor_available_bandwidth_percentage
                
                	Flood a specific percentage of the available bandwidth
                	**type**\:  int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 100
                
                .. attribute:: oor_accept_lsp_min_bandwidth
                
                	Only accept LSPs with at least the specified bandwidth (in kbps)
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: kbit/s
                
                	**default value**\: 0
                
                .. attribute:: oor_accept_reopt_lsp
                
                	Allow the setup of reoptimized LSPs over the link in this OOR State
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: oor_metric_te_penalty
                
                	Penalty applied to the TE metric of a link in OOR state
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 0
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState, self).__init__()

                    self.yang_name = "oor-red-state"
                    self.yang_parent_name = "hardware-out-of-resource"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.oor_node_protection_disable = YLeaf(YType.empty, "oor-node-protection-disable")

                    self.oor_available_bandwidth_percentage = YLeaf(YType.uint32, "oor-available-bandwidth-percentage")

                    self.oor_accept_lsp_min_bandwidth = YLeaf(YType.int32, "oor-accept-lsp-min-bandwidth")

                    self.oor_accept_reopt_lsp = YLeaf(YType.empty, "oor-accept-reopt-lsp")

                    self.oor_metric_te_penalty = YLeaf(YType.int32, "oor-metric-te-penalty")
                    self._segment_path = lambda: "oor-red-state"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/hardware-out-of-resource/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.HardwareOutOfResource.OorRedState, ['oor_node_protection_disable', 'oor_available_bandwidth_percentage', 'oor_accept_lsp_min_bandwidth', 'oor_accept_reopt_lsp', 'oor_metric_te_penalty'], name, value)


            class OorYellowState(Entity):
                """
                Configuration for HW OOR Yellow State
                
                .. attribute:: oor_node_protection_disable
                
                	Disable FRR node\-protection when the link is in this OOR State
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: oor_available_bandwidth_percentage
                
                	Flood a specific percentage of the available bandwidth
                	**type**\:  int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 100
                
                .. attribute:: oor_accept_lsp_min_bandwidth
                
                	Only accept LSPs with at least the specified bandwidth (in kbps)
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: kbit/s
                
                	**default value**\: 0
                
                .. attribute:: oor_accept_reopt_lsp
                
                	Allow the setup of reoptimized LSPs over the link in this OOR State
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: oor_metric_te_penalty
                
                	Penalty applied to the TE metric of a link in OOR state
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 0
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState, self).__init__()

                    self.yang_name = "oor-yellow-state"
                    self.yang_parent_name = "hardware-out-of-resource"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.oor_node_protection_disable = YLeaf(YType.empty, "oor-node-protection-disable")

                    self.oor_available_bandwidth_percentage = YLeaf(YType.uint32, "oor-available-bandwidth-percentage")

                    self.oor_accept_lsp_min_bandwidth = YLeaf(YType.int32, "oor-accept-lsp-min-bandwidth")

                    self.oor_accept_reopt_lsp = YLeaf(YType.empty, "oor-accept-reopt-lsp")

                    self.oor_metric_te_penalty = YLeaf(YType.int32, "oor-metric-te-penalty")
                    self._segment_path = lambda: "oor-yellow-state"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/hardware-out-of-resource/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.HardwareOutOfResource.OorYellowState, ['oor_node_protection_disable', 'oor_available_bandwidth_percentage', 'oor_accept_lsp_min_bandwidth', 'oor_accept_reopt_lsp', 'oor_metric_te_penalty'], name, value)


            class OorGreenState(Entity):
                """
                Configuration for HW OOR Green State
                
                .. attribute:: oor_recovery_duration
                
                	Period of time (minutes) during which the action in Green state are applied. After this period, the processing in TE goes back to normal state
                	**type**\:  int
                
                	**range:** 0..10080
                
                	**units**\: minute
                
                	**default value**\: 0
                
                .. attribute:: oor_node_protection_disable
                
                	Disable FRR node\-protection when the link is in this OOR State
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: oor_available_bandwidth_percentage
                
                	Flood a specific percentage of the available bandwidth
                	**type**\:  int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 100
                
                .. attribute:: oor_accept_lsp_min_bandwidth
                
                	Only accept LSPs with at least the specified bandwidth (in kbps)
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**units**\: kbit/s
                
                	**default value**\: 0
                
                .. attribute:: oor_accept_reopt_lsp
                
                	Allow the setup of reoptimized LSPs over the link in this OOR State
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: oor_metric_te_penalty
                
                	Penalty applied to the TE metric of a link in OOR state
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                	**default value**\: 0
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState, self).__init__()

                    self.yang_name = "oor-green-state"
                    self.yang_parent_name = "hardware-out-of-resource"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.oor_recovery_duration = YLeaf(YType.uint32, "oor-recovery-duration")

                    self.oor_node_protection_disable = YLeaf(YType.empty, "oor-node-protection-disable")

                    self.oor_available_bandwidth_percentage = YLeaf(YType.uint32, "oor-available-bandwidth-percentage")

                    self.oor_accept_lsp_min_bandwidth = YLeaf(YType.int32, "oor-accept-lsp-min-bandwidth")

                    self.oor_accept_reopt_lsp = YLeaf(YType.empty, "oor-accept-reopt-lsp")

                    self.oor_metric_te_penalty = YLeaf(YType.int32, "oor-metric-te-penalty")
                    self._segment_path = lambda: "oor-green-state"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/hardware-out-of-resource/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.HardwareOutOfResource.OorGreenState, ['oor_recovery_duration', 'oor_node_protection_disable', 'oor_available_bandwidth_percentage', 'oor_accept_lsp_min_bandwidth', 'oor_accept_reopt_lsp', 'oor_metric_te_penalty'], name, value)


        class SecondaryRouterIds(Entity):
            """
            Configure MPLS TE Secondary Router ID
            
            .. attribute:: secondary_router_id
            
            	Secondary Router ID
            	**type**\: list of    :py:class:`SecondaryRouterId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.SecondaryRouterIds, self).__init__()

                self.yang_name = "secondary-router-ids"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"secondary-router-id" : ("secondary_router_id", MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId)}

                self.secondary_router_id = YList(self)
                self._segment_path = lambda: "secondary-router-ids"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.SecondaryRouterIds, [], name, value)


            class SecondaryRouterId(Entity):
                """
                Secondary Router ID
                
                .. attribute:: secondary_router_id_value  <key>
                
                	Secondary TE Router ID
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId, self).__init__()

                    self.yang_name = "secondary-router-id"
                    self.yang_parent_name = "secondary-router-ids"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.secondary_router_id_value = YLeaf(YType.str, "secondary-router-id-value")
                    self._segment_path = lambda: "secondary-router-id" + "[secondary-router-id-value='" + self.secondary_router_id_value.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/secondary-router-ids/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId, ['secondary_router_id_value'], name, value)


        class Srlg(Entity):
            """
            Configure SRLG values and MPLS\-TE properties
            
            .. attribute:: names
            
            	Configure SRLG identified by names
            	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Names>`
            
            .. attribute:: default_admin_weight
            
            	Default Admin weight any SRLG value that does not have one
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**default value**\: 1
            
            .. attribute:: enable
            
            	Enter SRLG property configuration
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.Srlg, self).__init__()

                self.yang_name = "srlg"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"names" : ("names", MplsTe.GlobalAttributes.Srlg.Names)}
                self._child_list_classes = {}

                self.default_admin_weight = YLeaf(YType.int32, "default-admin-weight")

                self.enable = YLeaf(YType.empty, "enable")

                self.names = MplsTe.GlobalAttributes.Srlg.Names()
                self.names.parent = self
                self._children_name_map["names"] = "names"
                self._children_yang_names.add("names")
                self._segment_path = lambda: "srlg"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.Srlg, ['default_admin_weight', 'enable'], name, value)


            class Names(Entity):
                """
                Configure SRLG identified by names
                
                .. attribute:: name
                
                	SRLG name and its MPLS\-TE properties
                	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Names.Name>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.Srlg.Names, self).__init__()

                    self.yang_name = "names"
                    self.yang_parent_name = "srlg"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"name" : ("name", MplsTe.GlobalAttributes.Srlg.Names.Name)}

                    self.name = YList(self)
                    self._segment_path = lambda: "names"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/srlg/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.Srlg.Names, [], name, value)


                class Name(Entity):
                    """
                    SRLG name and its MPLS\-TE properties
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG membership name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: static_srlg_members
                    
                    	Configure static SRLG members list
                    	**type**\:   :py:class:`StaticSrlgMembers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers>`
                    
                    .. attribute:: admin_weight
                    
                    	Administrative weight for the SRLG value
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.Srlg.Names.Name, self).__init__()

                        self.yang_name = "name"
                        self.yang_parent_name = "names"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"static-srlg-members" : ("static_srlg_members", MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers)}
                        self._child_list_classes = {}

                        self.srlg_name = YLeaf(YType.str, "srlg-name")

                        self.admin_weight = YLeaf(YType.int32, "admin-weight")

                        self.static_srlg_members = MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers()
                        self.static_srlg_members.parent = self
                        self._children_name_map["static_srlg_members"] = "static-srlg-members"
                        self._children_yang_names.add("static-srlg-members")
                        self._segment_path = lambda: "name" + "[srlg-name='" + self.srlg_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/srlg/names/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.Srlg.Names.Name, ['srlg_name', 'admin_weight'], name, value)


                    class StaticSrlgMembers(Entity):
                        """
                        Configure static SRLG members list
                        
                        .. attribute:: static_srlg_member
                        
                        	A mapping of the local static SRLG member
                        	**type**\: list of    :py:class:`StaticSrlgMember <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers, self).__init__()

                            self.yang_name = "static-srlg-members"
                            self.yang_parent_name = "name"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"static-srlg-member" : ("static_srlg_member", MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember)}

                            self.static_srlg_member = YList(self)
                            self._segment_path = lambda: "static-srlg-members"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers, [], name, value)


                        class StaticSrlgMember(Entity):
                            """
                            A mapping of the local static SRLG member
                            
                            .. attribute:: from_address  <key>
                            
                            	From address
                            	**type**\:  str
                            
                            .. attribute:: to_address
                            
                            	To Addres
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember, self).__init__()

                                self.yang_name = "static-srlg-member"
                                self.yang_parent_name = "static-srlg-members"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.from_address = YLeaf(YType.str, "from-address")

                                self.to_address = YLeaf(YType.str, "to-address")
                                self._segment_path = lambda: "static-srlg-member" + "[from-address='" + self.from_address.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.Srlg.Names.Name.StaticSrlgMembers.StaticSrlgMember, ['from_address', 'to_address'], name, value)


        class Queues(Entity):
            """
            Configure MPLS TE route priority
            
            .. attribute:: queue
            
            	Configure route priority queue value
            	**type**\: list of    :py:class:`Queue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Queues.Queue>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.Queues, self).__init__()

                self.yang_name = "queues"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"queue" : ("queue", MplsTe.GlobalAttributes.Queues.Queue)}

                self.queue = YList(self)
                self._segment_path = lambda: "queues"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.Queues, [], name, value)


            class Queue(Entity):
                """
                Configure route priority queue value
                
                .. attribute:: role  <key>
                
                	Route Priority Tunnel Role
                	**type**\:   :py:class:`RoutePriorityRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.RoutePriorityRole>`
                
                .. attribute:: value
                
                	Route priority queue value
                	**type**\:  int
                
                	**range:** 0..12
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.Queues.Queue, self).__init__()

                    self.yang_name = "queue"
                    self.yang_parent_name = "queues"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.role = YLeaf(YType.enumeration, "role")

                    self.value = YLeaf(YType.uint32, "value")
                    self._segment_path = lambda: "queue" + "[role='" + self.role.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/queues/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.Queues.Queue, ['role', 'value'], name, value)


        class Mib(Entity):
            """
            MPLS\-TE MIB properties
            
            .. attribute:: midpoint_lsp_stats_collection_disable
            
            	Disables mib midpoint LSP traffic stats collection
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.Mib, self).__init__()

                self.yang_name = "mib"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.midpoint_lsp_stats_collection_disable = YLeaf(YType.empty, "midpoint-lsp-stats-collection-disable")
                self._segment_path = lambda: "mib"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.Mib, ['midpoint_lsp_stats_collection_disable'], name, value)


        class AttributeSet(Entity):
            """
            Attribute AttributeSets
            
            .. attribute:: path_option_attributes
            
            	Path Option Attribute\-Set Table
            	**type**\:   :py:class:`PathOptionAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes>`
            
            .. attribute:: p2mpte_attributes
            
            	P2MP\-TE Tunnel AttributeSets Table
            	**type**\:   :py:class:`P2MpteAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes>`
            
            .. attribute:: p2p_te_attributes
            
            	P2P\-TE Tunnel AttributeSets Table
            	**type**\:   :py:class:`P2PTeAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes>`
            
            .. attribute:: auto_backup_attributes
            
            	Auto\-backup Tunnel Attribute Table
            	**type**\:   :py:class:`AutoBackupAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes>`
            
            .. attribute:: otn_pp_attributes
            
            	OTN Path Protection Attributes table
            	**type**\:   :py:class:`OtnPpAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes>`
            
            .. attribute:: auto_mesh_attributes
            
            	Auto\-mesh Tunnel AttributeSets Table
            	**type**\:   :py:class:`AutoMeshAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes>`
            
            .. attribute:: xro_attributes
            
            	XRO Tunnel Attributes table
            	**type**\:   :py:class:`XroAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.AttributeSet, self).__init__()

                self.yang_name = "attribute-set"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"path-option-attributes" : ("path_option_attributes", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes), "p2mpte-attributes" : ("p2mpte_attributes", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes), "p2p-te-attributes" : ("p2p_te_attributes", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes), "auto-backup-attributes" : ("auto_backup_attributes", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes), "otn-pp-attributes" : ("otn_pp_attributes", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes), "auto-mesh-attributes" : ("auto_mesh_attributes", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes), "xro-attributes" : ("xro_attributes", MplsTe.GlobalAttributes.AttributeSet.XroAttributes)}
                self._child_list_classes = {}

                self.path_option_attributes = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes()
                self.path_option_attributes.parent = self
                self._children_name_map["path_option_attributes"] = "path-option-attributes"
                self._children_yang_names.add("path-option-attributes")

                self.p2mpte_attributes = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes()
                self.p2mpte_attributes.parent = self
                self._children_name_map["p2mpte_attributes"] = "p2mpte-attributes"
                self._children_yang_names.add("p2mpte-attributes")

                self.p2p_te_attributes = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes()
                self.p2p_te_attributes.parent = self
                self._children_name_map["p2p_te_attributes"] = "p2p-te-attributes"
                self._children_yang_names.add("p2p-te-attributes")

                self.auto_backup_attributes = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes()
                self.auto_backup_attributes.parent = self
                self._children_name_map["auto_backup_attributes"] = "auto-backup-attributes"
                self._children_yang_names.add("auto-backup-attributes")

                self.otn_pp_attributes = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes()
                self.otn_pp_attributes.parent = self
                self._children_name_map["otn_pp_attributes"] = "otn-pp-attributes"
                self._children_yang_names.add("otn-pp-attributes")

                self.auto_mesh_attributes = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes()
                self.auto_mesh_attributes.parent = self
                self._children_name_map["auto_mesh_attributes"] = "auto-mesh-attributes"
                self._children_yang_names.add("auto-mesh-attributes")

                self.xro_attributes = MplsTe.GlobalAttributes.AttributeSet.XroAttributes()
                self.xro_attributes.parent = self
                self._children_name_map["xro_attributes"] = "xro-attributes"
                self._children_yang_names.add("xro-attributes")
                self._segment_path = lambda: "attribute-set"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()


            class PathOptionAttributes(Entity):
                """
                Path Option Attribute\-Set Table
                
                .. attribute:: path_option_attribute
                
                	Path Option Attribute
                	**type**\: list of    :py:class:`PathOptionAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes, self).__init__()

                    self.yang_name = "path-option-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"path-option-attribute" : ("path_option_attribute", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute)}

                    self.path_option_attribute = YList(self)
                    self._segment_path = lambda: "path-option-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes, [], name, value)


                class PathOptionAttribute(Entity):
                    """
                    Path Option Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: bfd_reverse_path
                    
                    	Configure BFD reverse path
                    	**type**\:   :py:class:`BfdReversePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: att_path_option_path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`AttPathOptionPathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection>`
                    
                    .. attribute:: pce
                    
                    	Configure pce properties
                    	**type**\:   :py:class:`Pce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\:   :py:class:`AffinityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: new_style_affinity_affinity_types
                    
                    	Tunnel new style affinity attributes table
                    	**type**\:   :py:class:`NewStyleAffinityAffinityTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute, self).__init__()

                        self.yang_name = "path-option-attribute"
                        self.yang_parent_name = "path-option-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"bfd-reverse-path" : ("bfd_reverse_path", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath), "att-path-option-path-selection" : ("att_path_option_path_selection", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection), "pce" : ("pce", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce), "affinity-mask" : ("affinity_mask", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask), "bandwidth" : ("bandwidth", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth), "new-style-affinity-affinity-types" : ("new_style_affinity_affinity_types", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.bfd_reverse_path = None
                        self._children_name_map["bfd_reverse_path"] = "bfd-reverse-path"
                        self._children_yang_names.add("bfd-reverse-path")

                        self.att_path_option_path_selection = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection()
                        self.att_path_option_path_selection.parent = self
                        self._children_name_map["att_path_option_path_selection"] = "att-path-option-path-selection"
                        self._children_yang_names.add("att-path-option-path-selection")

                        self.pce = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce()
                        self.pce.parent = self
                        self._children_name_map["pce"] = "pce"
                        self._children_yang_names.add("pce")

                        self.affinity_mask = None
                        self._children_name_map["affinity_mask"] = "affinity-mask"
                        self._children_yang_names.add("affinity-mask")

                        self.bandwidth = None
                        self._children_name_map["bandwidth"] = "bandwidth"
                        self._children_yang_names.add("bandwidth")

                        self.new_style_affinity_affinity_types = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes()
                        self.new_style_affinity_affinity_types.parent = self
                        self._children_name_map["new_style_affinity_affinity_types"] = "new-style-affinity-affinity-types"
                        self._children_yang_names.add("new-style-affinity-affinity-types")
                        self._segment_path = lambda: "path-option-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/path-option-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute, ['attribute_set_name', 'enable'], name, value)


                    class BfdReversePath(Entity):
                        """
                        Configure BFD reverse path
                        
                        .. attribute:: bfd_reverse_path_type
                        
                        	BFD reverse path type
                        	**type**\:   :py:class:`BfdReversePath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.BfdReversePath>`
                        
                        .. attribute:: binding_label
                        
                        	BFD reverse path binding label
                        	**type**\:  int
                        
                        	**range:** 0..1048575
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath, self).__init__()

                            self.yang_name = "bfd-reverse-path"
                            self.yang_parent_name = "path-option-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bfd_reverse_path_type = YLeaf(YType.enumeration, "bfd-reverse-path-type")

                            self.binding_label = YLeaf(YType.uint32, "binding-label")
                            self._segment_path = lambda: "bfd-reverse-path"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.BfdReversePath, ['bfd_reverse_path_type', 'binding_label'], name, value)


                    class AttPathOptionPathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: path_selection_exclude_list
                        
                        	Path selection exclude list name configuration
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: enable
                        
                        	Enter path selection configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: invalidation
                        
                        	Path invalidation configuration for this specific tunnel
                        	**type**\:   :py:class:`Invalidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: path_selection_cost_limit
                        
                        	Path selection cost limit configuration for this specific tunnel
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection, self).__init__()

                            self.yang_name = "att-path-option-path-selection"
                            self.yang_parent_name = "path-option-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"invalidation" : ("invalidation", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation)}
                            self._child_list_classes = {}

                            self.path_selection_exclude_list = YLeaf(YType.str, "path-selection-exclude-list")

                            self.enable = YLeaf(YType.empty, "enable")

                            self.path_selection_cost_limit = YLeaf(YType.uint32, "path-selection-cost-limit")

                            self.invalidation = None
                            self._children_name_map["invalidation"] = "invalidation"
                            self._children_yang_names.add("invalidation")
                            self._segment_path = lambda: "att-path-option-path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection, ['path_selection_exclude_list', 'enable', 'path_selection_cost_limit'], name, value)


                        class Invalidation(Entity):
                            """
                            Path invalidation configuration for this
                            specific tunnel
                            
                            .. attribute:: path_invalidation_timeout
                            
                            	Path Invalidation Timeout
                            	**type**\:  int
                            
                            	**range:** 0..60000
                            
                            .. attribute:: path_invalidation_action
                            
                            	Path Invalidation Action
                            	**type**\:   :py:class:`PathInvalidationAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.PathInvalidationAction>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation, self).__init__()

                                self.yang_name = "invalidation"
                                self.yang_parent_name = "att-path-option-path-selection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.path_invalidation_timeout = YLeaf(YType.uint32, "path-invalidation-timeout")

                                self.path_invalidation_action = YLeaf(YType.enumeration, "path-invalidation-action")
                                self._segment_path = lambda: "invalidation"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AttPathOptionPathSelection.Invalidation, ['path_invalidation_timeout', 'path_invalidation_action'], name, value)


                    class Pce(Entity):
                        """
                        Configure pce properties
                        
                        .. attribute:: bidirectional
                        
                        	Bidirectional parameters
                        	**type**\:   :py:class:`Bidirectional <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: disjoint_path
                        
                        	Disjoint path parameters
                        	**type**\:   :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: enable
                        
                        	Always set to true
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce, self).__init__()

                            self.yang_name = "pce"
                            self.yang_parent_name = "path-option-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bidirectional" : ("bidirectional", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional), "disjoint-path" : ("disjoint_path", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

                            self.bidirectional = None
                            self._children_name_map["bidirectional"] = "bidirectional"
                            self._children_yang_names.add("bidirectional")

                            self.disjoint_path = None
                            self._children_name_map["disjoint_path"] = "disjoint-path"
                            self._children_yang_names.add("disjoint-path")
                            self._segment_path = lambda: "pce"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce, ['enable'], name, value)


                        class Bidirectional(Entity):
                            """
                            Bidirectional parameters
                            
                            .. attribute:: bd_source_address
                            
                            	Bidirectional Source IP Address
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: bd_group_id
                            
                            	Bidirectional Group ID
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional, self).__init__()

                                self.yang_name = "bidirectional"
                                self.yang_parent_name = "pce"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.bd_source_address = YLeaf(YType.str, "bd-source-address")

                                self.bd_group_id = YLeaf(YType.uint32, "bd-group-id")
                                self._segment_path = lambda: "bidirectional"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.Bidirectional, ['bd_source_address', 'bd_group_id'], name, value)


                        class DisjointPath(Entity):
                            """
                            Disjoint path parameters
                            
                            .. attribute:: dp_source_address
                            
                            	Disjoint Path Source IP Address
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: dp_type
                            
                            	Disjoint Path Type
                            	**type**\:  int
                            
                            	**range:** 1..3
                            
                            	**mandatory**\: True
                            
                            .. attribute:: dp_group_id
                            
                            	Disjoint Path Group ID
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath, self).__init__()

                                self.yang_name = "disjoint-path"
                                self.yang_parent_name = "pce"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.dp_source_address = YLeaf(YType.str, "dp-source-address")

                                self.dp_type = YLeaf(YType.uint32, "dp-type")

                                self.dp_group_id = YLeaf(YType.uint32, "dp-group-id")
                                self._segment_path = lambda: "disjoint-path"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Pce.DisjointPath, ['dp_source_address', 'dp_type', 'dp_group_id'], name, value)


                    class AffinityMask(Entity):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask, self).__init__()

                            self.yang_name = "affinity-mask"
                            self.yang_parent_name = "path-option-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.affinity = YLeaf(YType.str, "affinity")

                            self.mask = YLeaf(YType.str, "mask")
                            self._segment_path = lambda: "affinity-mask"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask, ['affinity', 'mask'], name, value)


                    class Bandwidth(Entity):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\:   :py:class:`MplsTeBandwidthDste <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDste>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwidth allocation
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**units**\: kbit/s
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth, self).__init__()

                            self.yang_name = "bandwidth"
                            self.yang_parent_name = "path-option-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.dste_type = YLeaf(YType.enumeration, "dste-type")

                            self.class_or_pool_type = YLeaf(YType.uint32, "class-or-pool-type")

                            self.bandwidth = YLeaf(YType.uint32, "bandwidth")
                            self._segment_path = lambda: "bandwidth"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth, ['dste_type', 'class_or_pool_type', 'bandwidth'], name, value)


                    class NewStyleAffinityAffinityTypes(Entity):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity_affinity_type
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes, self).__init__()

                            self.yang_name = "new-style-affinity-affinity-types"
                            self.yang_parent_name = "path-option-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"new-style-affinity-affinity-type" : ("new_style_affinity_affinity_type", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType), "new-style-affinity-affinity-type-affinity1" : ("new_style_affinity_affinity_type_affinity1", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1), "new-style-affinity-affinity-type-affinity1-affinity2" : ("new_style_affinity_affinity_type_affinity1_affinity2", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10", MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10)}

                            self.new_style_affinity_affinity_type = YList(self)
                            self.new_style_affinity_affinity_type_affinity1 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10 = YList(self)
                            self._segment_path = lambda: "new-style-affinity-affinity-types"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes, [], name, value)


                        class NewStyleAffinityAffinityType(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")
                                self._segment_path = lambda: "new-style-affinity-affinity-type" + "[affinity-type='" + self.affinity_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, ['affinity_type'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, ['affinity_type', 'affinity1'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, ['affinity_type', 'affinity1', 'affinity2'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, ['affinity_type', 'affinity1', 'affinity2', 'affinity3'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")

                                self.affinity10 = YLeaf(YType.str, "affinity10")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']" + "[affinity10='" + self.affinity10.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9', 'affinity10'], name, value)


            class P2MpteAttributes(Entity):
                """
                P2MP\-TE Tunnel AttributeSets Table
                
                .. attribute:: p2mpte_attribute
                
                	P2MP\-TE Tunnel Attribute
                	**type**\: list of    :py:class:`P2MpteAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes, self).__init__()

                    self.yang_name = "p2mpte-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"p2mpte-attribute" : ("p2mpte_attribute", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute)}

                    self.p2mpte_attribute = YList(self)
                    self._segment_path = lambda: "p2mpte-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes, [], name, value)


                class P2MpteAttribute(Entity):
                    """
                    P2MP\-TE Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interface_bandwidth
                    
                    	The bandwidth of the interface in kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\:   :py:class:`AffinityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection>`
                    
                    .. attribute:: new_style_affinity_affinity_types
                    
                    	Tunnel new style affinity attributes table
                    	**type**\:   :py:class:`NewStyleAffinityAffinityTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes>`
                    
                    .. attribute:: fast_reroute
                    
                    	Specify MPLS tunnel can be fast\-rerouted
                    	**type**\:   :py:class:`FastReroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: logging
                    
                    	Log tunnel LSP messages
                    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute, self).__init__()

                        self.yang_name = "p2mpte-attribute"
                        self.yang_parent_name = "p2mpte-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"priority" : ("priority", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority), "affinity-mask" : ("affinity_mask", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask), "bandwidth" : ("bandwidth", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth), "path-selection" : ("path_selection", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection), "new-style-affinity-affinity-types" : ("new_style_affinity_affinity_types", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes), "fast-reroute" : ("fast_reroute", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute), "logging" : ("logging", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.interface_bandwidth = YLeaf(YType.uint32, "interface-bandwidth")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.record_route = YLeaf(YType.empty, "record-route")

                        self.priority = None
                        self._children_name_map["priority"] = "priority"
                        self._children_yang_names.add("priority")

                        self.affinity_mask = None
                        self._children_name_map["affinity_mask"] = "affinity-mask"
                        self._children_yang_names.add("affinity-mask")

                        self.bandwidth = None
                        self._children_name_map["bandwidth"] = "bandwidth"
                        self._children_yang_names.add("bandwidth")

                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection()
                        self.path_selection.parent = self
                        self._children_name_map["path_selection"] = "path-selection"
                        self._children_yang_names.add("path-selection")

                        self.new_style_affinity_affinity_types = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes()
                        self.new_style_affinity_affinity_types.parent = self
                        self._children_name_map["new_style_affinity_affinity_types"] = "new-style-affinity-affinity-types"
                        self._children_yang_names.add("new-style-affinity-affinity-types")

                        self.fast_reroute = None
                        self._children_name_map["fast_reroute"] = "fast-reroute"
                        self._children_yang_names.add("fast-reroute")

                        self.logging = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging()
                        self.logging.parent = self
                        self._children_name_map["logging"] = "logging"
                        self._children_yang_names.add("logging")
                        self._segment_path = lambda: "p2mpte-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/p2mpte-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute, ['attribute_set_name', 'interface_bandwidth', 'enable', 'record_route'], name, value)


                    class Priority(Entity):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority, self).__init__()

                            self.yang_name = "priority"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.setup_priority = YLeaf(YType.uint32, "setup-priority")

                            self.hold_priority = YLeaf(YType.uint32, "hold-priority")
                            self._segment_path = lambda: "priority"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority, ['setup_priority', 'hold_priority'], name, value)


                    class AffinityMask(Entity):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask, self).__init__()

                            self.yang_name = "affinity-mask"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.affinity = YLeaf(YType.str, "affinity")

                            self.mask = YLeaf(YType.str, "mask")
                            self._segment_path = lambda: "affinity-mask"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask, ['affinity', 'mask'], name, value)


                    class Bandwidth(Entity):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\:   :py:class:`MplsTeBandwidthDste <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDste>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwidth allocation
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**units**\: kbit/s
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth, self).__init__()

                            self.yang_name = "bandwidth"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.dste_type = YLeaf(YType.enumeration, "dste-type")

                            self.class_or_pool_type = YLeaf(YType.uint32, "class-or-pool-type")

                            self.bandwidth = YLeaf(YType.uint32, "bandwidth")
                            self._segment_path = lambda: "bandwidth"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth, ['dste_type', 'class_or_pool_type', 'bandwidth'], name, value)


                    class PathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: enable
                        
                        	Enable path selection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection, self).__init__()

                            self.yang_name = "path-selection"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.PathSelection, ['enable'], name, value)


                    class NewStyleAffinityAffinityTypes(Entity):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity_affinity_type
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes, self).__init__()

                            self.yang_name = "new-style-affinity-affinity-types"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"new-style-affinity-affinity-type" : ("new_style_affinity_affinity_type", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType), "new-style-affinity-affinity-type-affinity1" : ("new_style_affinity_affinity_type_affinity1", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1), "new-style-affinity-affinity-type-affinity1-affinity2" : ("new_style_affinity_affinity_type_affinity1_affinity2", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10", MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10)}

                            self.new_style_affinity_affinity_type = YList(self)
                            self.new_style_affinity_affinity_type_affinity1 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10 = YList(self)
                            self._segment_path = lambda: "new-style-affinity-affinity-types"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes, [], name, value)


                        class NewStyleAffinityAffinityType(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")
                                self._segment_path = lambda: "new-style-affinity-affinity-type" + "[affinity-type='" + self.affinity_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, ['affinity_type'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, ['affinity_type', 'affinity1'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, ['affinity_type', 'affinity1', 'affinity2'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, ['affinity_type', 'affinity1', 'affinity2', 'affinity3'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")

                                self.affinity10 = YLeaf(YType.str, "affinity10")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']" + "[affinity10='" + self.affinity10.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9', 'affinity10'], name, value)


                    class FastReroute(Entity):
                        """
                        Specify MPLS tunnel can be fast\-rerouted
                        
                        .. attribute:: bandwidth_protection
                        
                        	Bandwidth Protection
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: node_protection
                        
                        	Node Protection
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute, self).__init__()

                            self.yang_name = "fast-reroute"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bandwidth_protection = YLeaf(YType.uint32, "bandwidth-protection")

                            self.node_protection = YLeaf(YType.uint32, "node-protection")
                            self._segment_path = lambda: "fast-reroute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute, ['bandwidth_protection', 'node_protection'], name, value)


                    class Logging(Entity):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel bandwidth change messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: all
                        
                        	Log all events for a tunnel
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: sub_lsp_state_message
                        
                        	Log all tunnel sub\-LSP state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging, self).__init__()

                            self.yang_name = "logging"
                            self.yang_parent_name = "p2mpte-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.insufficient_bw_message = YLeaf(YType.empty, "insufficient-bw-message")

                            self.reoptimized_message = YLeaf(YType.empty, "reoptimized-message")

                            self.bandwidth_change_message = YLeaf(YType.empty, "bandwidth-change-message")

                            self.all = YLeaf(YType.empty, "all")

                            self.pcalc_failure_message = YLeaf(YType.empty, "pcalc-failure-message")

                            self.state_message = YLeaf(YType.empty, "state-message")

                            self.reoptimize_attempts_message = YLeaf(YType.empty, "reoptimize-attempts-message")

                            self.sub_lsp_state_message = YLeaf(YType.empty, "sub-lsp-state-message")

                            self.reroute_messsage = YLeaf(YType.empty, "reroute-messsage")
                            self._segment_path = lambda: "logging"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging, ['insufficient_bw_message', 'reoptimized_message', 'bandwidth_change_message', 'all', 'pcalc_failure_message', 'state_message', 'reoptimize_attempts_message', 'sub_lsp_state_message', 'reroute_messsage'], name, value)


            class P2PTeAttributes(Entity):
                """
                P2P\-TE Tunnel AttributeSets Table
                
                .. attribute:: p2p_te_attribute
                
                	P2P\-TE Tunnel Attribute
                	**type**\: list of    :py:class:`P2PTeAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes, self).__init__()

                    self.yang_name = "p2p-te-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"p2p-te-attribute" : ("p2p_te_attribute", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute)}

                    self.p2p_te_attribute = YList(self)
                    self._segment_path = lambda: "p2p-te-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes, [], name, value)


                class P2PTeAttribute(Entity):
                    """
                    P2P\-TE Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection>`
                    
                    .. attribute:: pce
                    
                    	Configure pce properties
                    	**type**\:   :py:class:`Pce <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\:   :py:class:`AffinityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: logging
                    
                    	Log tunnel LSP messages
                    	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging>`
                    
                    .. attribute:: new_style_affinity_affinity_types
                    
                    	Tunnel new style affinity attributes table
                    	**type**\:   :py:class:`NewStyleAffinityAffinityTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute, self).__init__()

                        self.yang_name = "p2p-te-attribute"
                        self.yang_parent_name = "p2p-te-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"path-selection" : ("path_selection", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection), "pce" : ("pce", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce), "affinity-mask" : ("affinity_mask", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask), "logging" : ("logging", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging), "new-style-affinity-affinity-types" : ("new_style_affinity_affinity_types", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection()
                        self.path_selection.parent = self
                        self._children_name_map["path_selection"] = "path-selection"
                        self._children_yang_names.add("path-selection")

                        self.pce = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce()
                        self.pce.parent = self
                        self._children_name_map["pce"] = "pce"
                        self._children_yang_names.add("pce")

                        self.affinity_mask = None
                        self._children_name_map["affinity_mask"] = "affinity-mask"
                        self._children_yang_names.add("affinity-mask")

                        self.logging = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging()
                        self.logging.parent = self
                        self._children_name_map["logging"] = "logging"
                        self._children_yang_names.add("logging")

                        self.new_style_affinity_affinity_types = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes()
                        self.new_style_affinity_affinity_types.parent = self
                        self._children_name_map["new_style_affinity_affinity_types"] = "new-style-affinity-affinity-types"
                        self._children_yang_names.add("new-style-affinity-affinity-types")
                        self._segment_path = lambda: "p2p-te-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/p2p-te-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute, ['attribute_set_name', 'enable'], name, value)


                    class PathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: segment_routing_prepend
                        
                        	Path selection segment routing prepend configuration
                        	**type**\:   :py:class:`SegmentRoutingPrepend <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend>`
                        
                        .. attribute:: invalidation
                        
                        	Path selection invalidation configuration
                        	**type**\:   :py:class:`Invalidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation>`
                        
                        .. attribute:: path_selection_metric
                        
                        	Path selection metric to use in path calculation
                        	**type**\:   :py:class:`MplsTePathSelectionMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetric>`
                        
                        .. attribute:: path_selection_segment_routing_adjacency_protection
                        
                        	Segment routing adjacency protection type to use in path calculation
                        	**type**\:   :py:class:`MplsTePathSelectionSegmentRoutingAdjacencyProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionSegmentRoutingAdjacencyProtection>`
                        
                        .. attribute:: enable
                        
                        	Enter path selection configuration
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection, self).__init__()

                            self.yang_name = "path-selection"
                            self.yang_parent_name = "p2p-te-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"segment-routing-prepend" : ("segment_routing_prepend", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend), "invalidation" : ("invalidation", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation)}
                            self._child_list_classes = {}

                            self.path_selection_metric = YLeaf(YType.enumeration, "path-selection-metric")

                            self.path_selection_segment_routing_adjacency_protection = YLeaf(YType.enumeration, "path-selection-segment-routing-adjacency-protection")

                            self.enable = YLeaf(YType.empty, "enable")

                            self.segment_routing_prepend = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend()
                            self.segment_routing_prepend.parent = self
                            self._children_name_map["segment_routing_prepend"] = "segment-routing-prepend"
                            self._children_yang_names.add("segment-routing-prepend")

                            self.invalidation = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation()
                            self.invalidation.parent = self
                            self._children_name_map["invalidation"] = "invalidation"
                            self._children_yang_names.add("invalidation")
                            self._segment_path = lambda: "path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection, ['path_selection_metric', 'path_selection_segment_routing_adjacency_protection', 'enable'], name, value)


                        class SegmentRoutingPrepend(Entity):
                            """
                            Path selection segment routing prepend
                            configuration
                            
                            .. attribute:: indexes
                            
                            	Segment routing prepend index table
                            	**type**\:   :py:class:`Indexes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes>`
                            
                            .. attribute:: enable
                            
                            	Enter path selection segment routing prepend submode
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend, self).__init__()

                                self.yang_name = "segment-routing-prepend"
                                self.yang_parent_name = "path-selection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"indexes" : ("indexes", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes)}
                                self._child_list_classes = {}

                                self.enable = YLeaf(YType.empty, "enable")

                                self.indexes = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes()
                                self.indexes.parent = self
                                self._children_name_map["indexes"] = "indexes"
                                self._children_yang_names.add("indexes")
                                self._segment_path = lambda: "segment-routing-prepend"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend, ['enable'], name, value)


                            class Indexes(Entity):
                                """
                                Segment routing prepend index table
                                
                                .. attribute:: index
                                
                                	Prepend index information
                                	**type**\: list of    :py:class:`Index <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index>`
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes, self).__init__()

                                    self.yang_name = "indexes"
                                    self.yang_parent_name = "segment-routing-prepend"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"index" : ("index", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index)}

                                    self.index = YList(self)
                                    self._segment_path = lambda: "indexes"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes, [], name, value)


                                class Index(Entity):
                                    """
                                    Prepend index information
                                    
                                    .. attribute:: index_number  <key>
                                    
                                    	Index number
                                    	**type**\:  int
                                    
                                    	**range:** 1..10
                                    
                                    .. attribute:: prepend_type
                                    
                                    	Prepend type
                                    	**type**\:   :py:class:`SrPrepend <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.SrPrepend>`
                                    
                                    	**default value**\: none-type
                                    
                                    .. attribute:: mpls_label
                                    
                                    	MPLS Label
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    	**default value**\: 1048577
                                    
                                    

                                    """

                                    _prefix = 'mpls-te-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index, self).__init__()

                                        self.yang_name = "index"
                                        self.yang_parent_name = "indexes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.index_number = YLeaf(YType.uint32, "index-number")

                                        self.prepend_type = YLeaf(YType.enumeration, "prepend-type")

                                        self.mpls_label = YLeaf(YType.int32, "mpls-label")
                                        self._segment_path = lambda: "index" + "[index-number='" + self.index_number.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index, ['index_number', 'prepend_type', 'mpls_label'], name, value)


                        class Invalidation(Entity):
                            """
                            Path selection invalidation configuration
                            
                            .. attribute:: invalidation_timer
                            
                            	Path selection invalidation timer value (milliseconds)
                            	**type**\:  int
                            
                            	**range:** 0..60000
                            
                            	**units**\: millisecond
                            
                            .. attribute:: invalidation_timer_expire_type
                            
                            	Path selection invalidation timer expire type
                            	**type**\:   :py:class:`MplsTePathSelectionInvalidationTimerExpire <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionInvalidationTimerExpire>`
                            
                            	**default value**\: tunnel-action-tear
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation, self).__init__()

                                self.yang_name = "invalidation"
                                self.yang_parent_name = "path-selection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.invalidation_timer = YLeaf(YType.uint32, "invalidation-timer")

                                self.invalidation_timer_expire_type = YLeaf(YType.enumeration, "invalidation-timer-expire-type")
                                self._segment_path = lambda: "invalidation"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.Invalidation, ['invalidation_timer', 'invalidation_timer_expire_type'], name, value)


                    class Pce(Entity):
                        """
                        Configure pce properties
                        
                        .. attribute:: bidirectional
                        
                        	Bidirectional parameters
                        	**type**\:   :py:class:`Bidirectional <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: disjoint_path
                        
                        	Disjoint path parameters
                        	**type**\:   :py:class:`DisjointPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: enable
                        
                        	Always set to true
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce, self).__init__()

                            self.yang_name = "pce"
                            self.yang_parent_name = "p2p-te-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"bidirectional" : ("bidirectional", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional), "disjoint-path" : ("disjoint_path", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

                            self.bidirectional = None
                            self._children_name_map["bidirectional"] = "bidirectional"
                            self._children_yang_names.add("bidirectional")

                            self.disjoint_path = None
                            self._children_name_map["disjoint_path"] = "disjoint-path"
                            self._children_yang_names.add("disjoint-path")
                            self._segment_path = lambda: "pce"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce, ['enable'], name, value)


                        class Bidirectional(Entity):
                            """
                            Bidirectional parameters
                            
                            .. attribute:: bd_source_address
                            
                            	Bidirectional Source IP Address
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: bd_group_id
                            
                            	Bidirectional Group ID
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional, self).__init__()

                                self.yang_name = "bidirectional"
                                self.yang_parent_name = "pce"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.bd_source_address = YLeaf(YType.str, "bd-source-address")

                                self.bd_group_id = YLeaf(YType.uint32, "bd-group-id")
                                self._segment_path = lambda: "bidirectional"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.Bidirectional, ['bd_source_address', 'bd_group_id'], name, value)


                        class DisjointPath(Entity):
                            """
                            Disjoint path parameters
                            
                            .. attribute:: dp_source_address
                            
                            	Disjoint Path Source IP Address
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: dp_type
                            
                            	Disjoint Path Type
                            	**type**\:  int
                            
                            	**range:** 1..3
                            
                            	**mandatory**\: True
                            
                            .. attribute:: dp_group_id
                            
                            	Disjoint Path Group ID
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath, self).__init__()

                                self.yang_name = "disjoint-path"
                                self.yang_parent_name = "pce"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.dp_source_address = YLeaf(YType.str, "dp-source-address")

                                self.dp_type = YLeaf(YType.uint32, "dp-type")

                                self.dp_group_id = YLeaf(YType.uint32, "dp-group-id")
                                self._segment_path = lambda: "disjoint-path"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Pce.DisjointPath, ['dp_source_address', 'dp_type', 'dp_group_id'], name, value)


                    class AffinityMask(Entity):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask, self).__init__()

                            self.yang_name = "affinity-mask"
                            self.yang_parent_name = "p2p-te-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.affinity = YLeaf(YType.str, "affinity")

                            self.mask = YLeaf(YType.str, "mask")
                            self._segment_path = lambda: "affinity-mask"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask, ['affinity', 'mask'], name, value)


                    class Logging(Entity):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: lsp_switch_over_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: all
                        
                        	Log all events for a tunnel
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: record_route_messsage
                        
                        	Log tunnel record\-route messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bfd_state_message
                        
                        	Enable BFD session state change alarm
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging, self).__init__()

                            self.yang_name = "logging"
                            self.yang_parent_name = "p2p-te-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.lsp_switch_over_change_message = YLeaf(YType.empty, "lsp-switch-over-change-message")

                            self.all = YLeaf(YType.empty, "all")

                            self.record_route_messsage = YLeaf(YType.empty, "record-route-messsage")

                            self.bfd_state_message = YLeaf(YType.empty, "bfd-state-message")

                            self.bandwidth_change_message = YLeaf(YType.empty, "bandwidth-change-message")

                            self.reoptimize_attempts_message = YLeaf(YType.empty, "reoptimize-attempts-message")

                            self.reroute_messsage = YLeaf(YType.empty, "reroute-messsage")

                            self.state_message = YLeaf(YType.empty, "state-message")

                            self.insufficient_bw_message = YLeaf(YType.empty, "insufficient-bw-message")

                            self.reoptimized_message = YLeaf(YType.empty, "reoptimized-message")

                            self.pcalc_failure_message = YLeaf(YType.empty, "pcalc-failure-message")
                            self._segment_path = lambda: "logging"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging, ['lsp_switch_over_change_message', 'all', 'record_route_messsage', 'bfd_state_message', 'bandwidth_change_message', 'reoptimize_attempts_message', 'reroute_messsage', 'state_message', 'insufficient_bw_message', 'reoptimized_message', 'pcalc_failure_message'], name, value)


                    class NewStyleAffinityAffinityTypes(Entity):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity_affinity_type
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes, self).__init__()

                            self.yang_name = "new-style-affinity-affinity-types"
                            self.yang_parent_name = "p2p-te-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"new-style-affinity-affinity-type" : ("new_style_affinity_affinity_type", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType), "new-style-affinity-affinity-type-affinity1" : ("new_style_affinity_affinity_type_affinity1", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1), "new-style-affinity-affinity-type-affinity1-affinity2" : ("new_style_affinity_affinity_type_affinity1_affinity2", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10", MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10)}

                            self.new_style_affinity_affinity_type = YList(self)
                            self.new_style_affinity_affinity_type_affinity1 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10 = YList(self)
                            self._segment_path = lambda: "new-style-affinity-affinity-types"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes, [], name, value)


                        class NewStyleAffinityAffinityType(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")
                                self._segment_path = lambda: "new-style-affinity-affinity-type" + "[affinity-type='" + self.affinity_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, ['affinity_type'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, ['affinity_type', 'affinity1'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, ['affinity_type', 'affinity1', 'affinity2'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, ['affinity_type', 'affinity1', 'affinity2', 'affinity3'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")

                                self.affinity10 = YLeaf(YType.str, "affinity10")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']" + "[affinity10='" + self.affinity10.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9', 'affinity10'], name, value)


            class AutoBackupAttributes(Entity):
                """
                Auto\-backup Tunnel Attribute Table
                
                .. attribute:: auto_backup_attribute
                
                	Auto\-backup Tunnel Attribute
                	**type**\: list of    :py:class:`AutoBackupAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes, self).__init__()

                    self.yang_name = "auto-backup-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"auto-backup-attribute" : ("auto_backup_attribute", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute)}

                    self.auto_backup_attribute = YList(self)
                    self._segment_path = lambda: "auto-backup-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes, [], name, value)


                class AutoBackupAttribute(Entity):
                    """
                    Auto\-backup Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: signalled_name
                    
                    	Signalled name
                    	**type**\:   :py:class:`SignalledName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName>`
                    
                    .. attribute:: auto_backup_logging
                    
                    	Log tunnel LSP messages
                    	**type**\:   :py:class:`AutoBackupLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging>`
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\:   :py:class:`AffinityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection>`
                    
                    .. attribute:: policy_classes
                    
                    	Policy classes for PBTS
                    	**type**\:   :py:class:`PolicyClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses>`
                    
                    .. attribute:: new_style_affinity_affinity_types
                    
                    	Tunnel new style affinity attributes table
                    	**type**\:   :py:class:`NewStyleAffinityAffinityTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute, self).__init__()

                        self.yang_name = "auto-backup-attribute"
                        self.yang_parent_name = "auto-backup-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"signalled-name" : ("signalled_name", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName), "auto-backup-logging" : ("auto_backup_logging", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging), "priority" : ("priority", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority), "affinity-mask" : ("affinity_mask", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask), "path-selection" : ("path_selection", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection), "policy-classes" : ("policy_classes", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses), "new-style-affinity-affinity-types" : ("new_style_affinity_affinity_types", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.record_route = YLeaf(YType.empty, "record-route")

                        self.signalled_name = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName()
                        self.signalled_name.parent = self
                        self._children_name_map["signalled_name"] = "signalled-name"
                        self._children_yang_names.add("signalled-name")

                        self.auto_backup_logging = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging()
                        self.auto_backup_logging.parent = self
                        self._children_name_map["auto_backup_logging"] = "auto-backup-logging"
                        self._children_yang_names.add("auto-backup-logging")

                        self.priority = None
                        self._children_name_map["priority"] = "priority"
                        self._children_yang_names.add("priority")

                        self.affinity_mask = None
                        self._children_name_map["affinity_mask"] = "affinity-mask"
                        self._children_yang_names.add("affinity-mask")

                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection()
                        self.path_selection.parent = self
                        self._children_name_map["path_selection"] = "path-selection"
                        self._children_yang_names.add("path-selection")

                        self.policy_classes = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses()
                        self.policy_classes.parent = self
                        self._children_name_map["policy_classes"] = "policy-classes"
                        self._children_yang_names.add("policy-classes")

                        self.new_style_affinity_affinity_types = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes()
                        self.new_style_affinity_affinity_types.parent = self
                        self._children_name_map["new_style_affinity_affinity_types"] = "new-style-affinity-affinity-types"
                        self._children_yang_names.add("new-style-affinity-affinity-types")
                        self._segment_path = lambda: "auto-backup-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/auto-backup-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute, ['attribute_set_name', 'enable', 'record_route'], name, value)


                    class SignalledName(Entity):
                        """
                        Signalled name
                        
                        .. attribute:: name
                        
                        	Signalled name
                        	**type**\:  str
                        
                        .. attribute:: source_type
                        
                        	Source address or name
                        	**type**\:   :py:class:`MplsTeSigNameOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeSigNameOption>`
                        
                        .. attribute:: protected_interface_type
                        
                        	Protected\-interface address or name
                        	**type**\:   :py:class:`MplsTeSigNameOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeSigNameOption>`
                        
                        .. attribute:: mp_address
                        
                        	Set if merge\-point address is to be appended
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName, self).__init__()

                            self.yang_name = "signalled-name"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.name = YLeaf(YType.str, "name")

                            self.source_type = YLeaf(YType.enumeration, "source-type")

                            self.protected_interface_type = YLeaf(YType.enumeration, "protected-interface-type")

                            self.mp_address = YLeaf(YType.boolean, "mp-address")
                            self._segment_path = lambda: "signalled-name"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName, ['name', 'source_type', 'protected_interface_type', 'mp_address'], name, value)


                    class AutoBackupLogging(Entity):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging, self).__init__()

                            self.yang_name = "auto-backup-logging"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bandwidth_change_message = YLeaf(YType.empty, "bandwidth-change-message")

                            self.reoptimize_attempts_message = YLeaf(YType.empty, "reoptimize-attempts-message")

                            self.state_message = YLeaf(YType.empty, "state-message")

                            self.reoptimized_message = YLeaf(YType.empty, "reoptimized-message")
                            self._segment_path = lambda: "auto-backup-logging"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging, ['bandwidth_change_message', 'reoptimize_attempts_message', 'state_message', 'reoptimized_message'], name, value)


                    class Priority(Entity):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority, self).__init__()

                            self.yang_name = "priority"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.setup_priority = YLeaf(YType.uint32, "setup-priority")

                            self.hold_priority = YLeaf(YType.uint32, "hold-priority")
                            self._segment_path = lambda: "priority"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority, ['setup_priority', 'hold_priority'], name, value)


                    class AffinityMask(Entity):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask, self).__init__()

                            self.yang_name = "affinity-mask"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.affinity = YLeaf(YType.str, "affinity")

                            self.mask = YLeaf(YType.str, "mask")
                            self._segment_path = lambda: "affinity-mask"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask, ['affinity', 'mask'], name, value)


                    class PathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: enable
                        
                        	Enable path selection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection, self).__init__()

                            self.yang_name = "path-selection"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PathSelection, ['enable'], name, value)


                    class PolicyClasses(Entity):
                        """
                        Policy classes for PBTS
                        
                        .. attribute:: policy_class
                        
                        	Array of Policy class
                        	**type**\:  list of int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses, self).__init__()

                            self.yang_name = "policy-classes"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.policy_class = YLeafList(YType.uint32, "policy-class")
                            self._segment_path = lambda: "policy-classes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses, ['policy_class'], name, value)


                    class NewStyleAffinityAffinityTypes(Entity):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity_affinity_type
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes, self).__init__()

                            self.yang_name = "new-style-affinity-affinity-types"
                            self.yang_parent_name = "auto-backup-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"new-style-affinity-affinity-type" : ("new_style_affinity_affinity_type", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType), "new-style-affinity-affinity-type-affinity1" : ("new_style_affinity_affinity_type_affinity1", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1), "new-style-affinity-affinity-type-affinity1-affinity2" : ("new_style_affinity_affinity_type_affinity1_affinity2", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10", MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10)}

                            self.new_style_affinity_affinity_type = YList(self)
                            self.new_style_affinity_affinity_type_affinity1 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10 = YList(self)
                            self._segment_path = lambda: "new-style-affinity-affinity-types"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes, [], name, value)


                        class NewStyleAffinityAffinityType(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")
                                self._segment_path = lambda: "new-style-affinity-affinity-type" + "[affinity-type='" + self.affinity_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, ['affinity_type'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, ['affinity_type', 'affinity1'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, ['affinity_type', 'affinity1', 'affinity2'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, ['affinity_type', 'affinity1', 'affinity2', 'affinity3'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")

                                self.affinity10 = YLeaf(YType.str, "affinity10")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']" + "[affinity10='" + self.affinity10.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9', 'affinity10'], name, value)


            class OtnPpAttributes(Entity):
                """
                OTN Path Protection Attributes table
                
                .. attribute:: otn_pp_attribute
                
                	OTN Path Protection Attribute
                	**type**\: list of    :py:class:`OtnPpAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes, self).__init__()

                    self.yang_name = "otn-pp-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"otn-pp-attribute" : ("otn_pp_attribute", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute)}

                    self.otn_pp_attribute = YList(self)
                    self._segment_path = lambda: "otn-pp-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes, [], name, value)


                class OtnPpAttribute(Entity):
                    """
                    OTN Path Protection Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: revert_schedule_names
                    
                    	Specify APS revert schedule
                    	**type**\:   :py:class:`RevertScheduleNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames>`
                    
                    .. attribute:: sub_network_connection_mode
                    
                    	Sub\-network connection mode
                    	**type**\:   :py:class:`SubNetworkConnectionMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode>`
                    
                    .. attribute:: timers
                    
                    	Timers
                    	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers>`
                    
                    .. attribute:: aps_protection_mode
                    
                    	The APS protecion mode
                    	**type**\:   :py:class:`MplsTeOtnApsProtectionMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnApsProtectionMode>`
                    
                    .. attribute:: aps_restoration_style
                    
                    	The APS restoration style
                    	**type**\:   :py:class:`MplsTeOtnApsRestorationStyle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnApsRestorationStyle>`
                    
                    .. attribute:: aps_protection_type
                    
                    	The APS protecion type
                    	**type**\:   :py:class:`MplsTeOtnApsProtection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnApsProtection>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute, self).__init__()

                        self.yang_name = "otn-pp-attribute"
                        self.yang_parent_name = "otn-pp-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"revert-schedule-names" : ("revert_schedule_names", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames), "sub-network-connection-mode" : ("sub_network_connection_mode", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode), "timers" : ("timers", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers), "path-selection" : ("path_selection", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.aps_protection_mode = YLeaf(YType.enumeration, "aps-protection-mode")

                        self.aps_restoration_style = YLeaf(YType.enumeration, "aps-restoration-style")

                        self.aps_protection_type = YLeaf(YType.enumeration, "aps-protection-type")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.revert_schedule_names = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames()
                        self.revert_schedule_names.parent = self
                        self._children_name_map["revert_schedule_names"] = "revert-schedule-names"
                        self._children_yang_names.add("revert-schedule-names")

                        self.sub_network_connection_mode = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode()
                        self.sub_network_connection_mode.parent = self
                        self._children_name_map["sub_network_connection_mode"] = "sub-network-connection-mode"
                        self._children_yang_names.add("sub-network-connection-mode")

                        self.timers = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers()
                        self.timers.parent = self
                        self._children_name_map["timers"] = "timers"
                        self._children_yang_names.add("timers")

                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection()
                        self.path_selection.parent = self
                        self._children_name_map["path_selection"] = "path-selection"
                        self._children_yang_names.add("path-selection")
                        self._segment_path = lambda: "otn-pp-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/otn-pp-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute, ['attribute_set_name', 'aps_protection_mode', 'aps_restoration_style', 'aps_protection_type', 'enable'], name, value)


                    class RevertScheduleNames(Entity):
                        """
                        Specify APS revert schedule
                        
                        .. attribute:: revert_schedule_name
                        
                        	Name Identifier for revert schedule
                        	**type**\: list of    :py:class:`RevertScheduleName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames, self).__init__()

                            self.yang_name = "revert-schedule-names"
                            self.yang_parent_name = "otn-pp-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"revert-schedule-name" : ("revert_schedule_name", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName)}

                            self.revert_schedule_name = YList(self)
                            self._segment_path = lambda: "revert-schedule-names"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames, [], name, value)


                        class RevertScheduleName(Entity):
                            """
                            Name Identifier for revert schedule
                            
                            .. attribute:: schedule_name  <key>
                            
                            	Enter 64 characters for revert schedule name
                            	**type**\:  str
                            
                            	**length:** 1..254
                            
                            .. attribute:: schedule_duration
                            
                            	Set duration in format hh\:mm
                            	**type**\:   :py:class:`ScheduleDuration <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: schedule_date
                            
                            	Set date in format hh\:mm MMM DD YYYY
                            	**type**\:   :py:class:`ScheduleDate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: revert_schedule_max_tries
                            
                            	Revert Schedule Max tries
                            	**type**\:  int
                            
                            	**range:** 1..2016
                            
                            .. attribute:: sch_name_enable
                            
                            	Schedule name enable object
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: revert_schedule_frequency
                            
                            	Frequency set as Once, Daily, Weekly
                            	**type**\:  int
                            
                            	**range:** 1..3
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName, self).__init__()

                                self.yang_name = "revert-schedule-name"
                                self.yang_parent_name = "revert-schedule-names"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"schedule-duration" : ("schedule_duration", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration), "schedule-date" : ("schedule_date", MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate)}
                                self._child_list_classes = {}

                                self.schedule_name = YLeaf(YType.str, "schedule-name")

                                self.revert_schedule_max_tries = YLeaf(YType.uint32, "revert-schedule-max-tries")

                                self.sch_name_enable = YLeaf(YType.empty, "sch-name-enable")

                                self.revert_schedule_frequency = YLeaf(YType.uint32, "revert-schedule-frequency")

                                self.schedule_duration = None
                                self._children_name_map["schedule_duration"] = "schedule-duration"
                                self._children_yang_names.add("schedule-duration")

                                self.schedule_date = None
                                self._children_name_map["schedule_date"] = "schedule-date"
                                self._children_yang_names.add("schedule-date")
                                self._segment_path = lambda: "revert-schedule-name" + "[schedule-name='" + self.schedule_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName, ['schedule_name', 'revert_schedule_max_tries', 'sch_name_enable', 'revert_schedule_frequency'], name, value)


                            class ScheduleDuration(Entity):
                                """
                                Set duration in format hh\:mm
                                
                                .. attribute:: hour
                                
                                	Hour of day
                                	**type**\:  int
                                
                                	**range:** 0..167
                                
                                	**mandatory**\: True
                                
                                .. attribute:: minutes
                                
                                	Minute of the hour
                                	**type**\:  int
                                
                                	**range:** 0..59
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration, self).__init__()

                                    self.yang_name = "schedule-duration"
                                    self.yang_parent_name = "revert-schedule-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self.is_presence_container = True

                                    self.hour = YLeaf(YType.uint32, "hour")

                                    self.minutes = YLeaf(YType.uint32, "minutes")
                                    self._segment_path = lambda: "schedule-duration"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDuration, ['hour', 'minutes'], name, value)


                            class ScheduleDate(Entity):
                                """
                                Set date in format hh\:mm MMM DD YYYY
                                
                                .. attribute:: hour
                                
                                	Hour of day
                                	**type**\:  int
                                
                                	**range:** 0..23
                                
                                	**mandatory**\: True
                                
                                .. attribute:: minutes
                                
                                	Minute of the hour
                                	**type**\:  int
                                
                                	**range:** 0..59
                                
                                	**mandatory**\: True
                                
                                .. attribute:: month
                                
                                	Month of the year
                                	**type**\:  int
                                
                                	**range:** 0..11
                                
                                	**mandatory**\: True
                                
                                .. attribute:: day
                                
                                	Day of the month
                                	**type**\:  int
                                
                                	**range:** 1..31
                                
                                	**mandatory**\: True
                                
                                .. attribute:: year
                                
                                	Year
                                	**type**\:  int
                                
                                	**range:** 2015..2035
                                
                                	**mandatory**\: True
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate, self).__init__()

                                    self.yang_name = "schedule-date"
                                    self.yang_parent_name = "revert-schedule-name"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}
                                    self.is_presence_container = True

                                    self.hour = YLeaf(YType.uint32, "hour")

                                    self.minutes = YLeaf(YType.uint32, "minutes")

                                    self.month = YLeaf(YType.uint32, "month")

                                    self.day = YLeaf(YType.uint32, "day")

                                    self.year = YLeaf(YType.uint32, "year")
                                    self._segment_path = lambda: "schedule-date"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.RevertScheduleNames.RevertScheduleName.ScheduleDate, ['hour', 'minutes', 'month', 'day', 'year'], name, value)


                    class SubNetworkConnectionMode(Entity):
                        """
                        Sub\-network connection mode
                        
                        .. attribute:: connection_mode
                        
                        	The sub\-network connection mode
                        	**type**\:   :py:class:`MplsTeOtnSncMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnSncMode>`
                        
                        .. attribute:: connection_monitoring_mode
                        
                        	Tandem Connection Monitoring ID for the interface
                        	**type**\:  int
                        
                        	**range:** 1..6
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode, self).__init__()

                            self.yang_name = "sub-network-connection-mode"
                            self.yang_parent_name = "otn-pp-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.connection_mode = YLeaf(YType.enumeration, "connection-mode")

                            self.connection_monitoring_mode = YLeaf(YType.uint32, "connection-monitoring-mode")
                            self._segment_path = lambda: "sub-network-connection-mode"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode, ['connection_mode', 'connection_monitoring_mode'], name, value)


                    class Timers(Entity):
                        """
                        Timers
                        
                        .. attribute:: aps_wait_to_restore
                        
                        	G.709 OTN path protection wait to restore timer in seconds
                        	**type**\:  int
                        
                        	**range:** 0..720
                        
                        	**units**\: second
                        
                        .. attribute:: aps_hold_off
                        
                        	G.709 OTN path protection hold\-off timer in milliseconds
                        	**type**\:  int
                        
                        	**range:** 100..10000
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers, self).__init__()

                            self.yang_name = "timers"
                            self.yang_parent_name = "otn-pp-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.aps_wait_to_restore = YLeaf(YType.uint32, "aps-wait-to-restore")

                            self.aps_hold_off = YLeaf(YType.uint32, "aps-hold-off")
                            self._segment_path = lambda: "timers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers, ['aps_wait_to_restore', 'aps_hold_off'], name, value)


                    class PathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: enable
                        
                        	Enable path selection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection, self).__init__()

                            self.yang_name = "path-selection"
                            self.yang_parent_name = "otn-pp-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.PathSelection, ['enable'], name, value)


            class AutoMeshAttributes(Entity):
                """
                Auto\-mesh Tunnel AttributeSets Table
                
                .. attribute:: auto_mesh_attribute
                
                	Auto\-mesh Tunnel Attribute
                	**type**\: list of    :py:class:`AutoMeshAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes, self).__init__()

                    self.yang_name = "auto-mesh-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"auto-mesh-attribute" : ("auto_mesh_attribute", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute)}

                    self.auto_mesh_attribute = YList(self)
                    self._segment_path = lambda: "auto-mesh-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes, [], name, value)


                class AutoMeshAttribute(Entity):
                    """
                    Auto\-mesh Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_mesh_logging
                    
                    	Log tunnel LSP messages
                    	**type**\:   :py:class:`AutoMeshLogging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging>`
                    
                    .. attribute:: autoroute_announce
                    
                    	Enable autoroute announce
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: interface_bandwidth
                    
                    	The bandwidth of the interface in kbps
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: forward_class
                    
                    	Forward class value
                    	**type**\:  int
                    
                    	**range:** 1..7
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\:   :py:class:`Priority <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\:   :py:class:`AffinityMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection>`
                    
                    .. attribute:: collection_only
                    
                    	Enable bandwidth collection only, no auto\-bw adjustment
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: policy_classes
                    
                    	Policy classes for PBTS
                    	**type**\:   :py:class:`PolicyClasses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses>`
                    
                    .. attribute:: new_style_affinity_affinity_types
                    
                    	Tunnel new style affinity attributes table
                    	**type**\:   :py:class:`NewStyleAffinityAffinityTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enable the soft\-preemption feature on the tunnel
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: fast_reroute
                    
                    	Specify MPLS tunnel can be fast\-rerouted
                    	**type**\:   :py:class:`FastReroute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: load_share
                    
                    	Tunnel loadsharing metric
                    	**type**\:  int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute, self).__init__()

                        self.yang_name = "auto-mesh-attribute"
                        self.yang_parent_name = "auto-mesh-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"auto-mesh-logging" : ("auto_mesh_logging", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging), "priority" : ("priority", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority), "affinity-mask" : ("affinity_mask", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask), "bandwidth" : ("bandwidth", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth), "path-selection" : ("path_selection", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection), "policy-classes" : ("policy_classes", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses), "new-style-affinity-affinity-types" : ("new_style_affinity_affinity_types", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes), "fast-reroute" : ("fast_reroute", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.autoroute_announce = YLeaf(YType.empty, "autoroute-announce")

                        self.interface_bandwidth = YLeaf(YType.uint32, "interface-bandwidth")

                        self.forward_class = YLeaf(YType.uint32, "forward-class")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.record_route = YLeaf(YType.empty, "record-route")

                        self.collection_only = YLeaf(YType.empty, "collection-only")

                        self.soft_preemption = YLeaf(YType.empty, "soft-preemption")

                        self.load_share = YLeaf(YType.uint32, "load-share")

                        self.auto_mesh_logging = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging()
                        self.auto_mesh_logging.parent = self
                        self._children_name_map["auto_mesh_logging"] = "auto-mesh-logging"
                        self._children_yang_names.add("auto-mesh-logging")

                        self.priority = None
                        self._children_name_map["priority"] = "priority"
                        self._children_yang_names.add("priority")

                        self.affinity_mask = None
                        self._children_name_map["affinity_mask"] = "affinity-mask"
                        self._children_yang_names.add("affinity-mask")

                        self.bandwidth = None
                        self._children_name_map["bandwidth"] = "bandwidth"
                        self._children_yang_names.add("bandwidth")

                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection()
                        self.path_selection.parent = self
                        self._children_name_map["path_selection"] = "path-selection"
                        self._children_yang_names.add("path-selection")

                        self.policy_classes = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses()
                        self.policy_classes.parent = self
                        self._children_name_map["policy_classes"] = "policy-classes"
                        self._children_yang_names.add("policy-classes")

                        self.new_style_affinity_affinity_types = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes()
                        self.new_style_affinity_affinity_types.parent = self
                        self._children_name_map["new_style_affinity_affinity_types"] = "new-style-affinity-affinity-types"
                        self._children_yang_names.add("new-style-affinity-affinity-types")

                        self.fast_reroute = None
                        self._children_name_map["fast_reroute"] = "fast-reroute"
                        self._children_yang_names.add("fast-reroute")
                        self._segment_path = lambda: "auto-mesh-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/auto-mesh-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute, ['attribute_set_name', 'autoroute_announce', 'interface_bandwidth', 'forward_class', 'enable', 'record_route', 'collection_only', 'soft_preemption', 'load_share'], name, value)


                    class AutoMeshLogging(Entity):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging, self).__init__()

                            self.yang_name = "auto-mesh-logging"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.bandwidth_change_message = YLeaf(YType.empty, "bandwidth-change-message")

                            self.reoptimize_attempts_message = YLeaf(YType.empty, "reoptimize-attempts-message")

                            self.reroute_messsage = YLeaf(YType.empty, "reroute-messsage")

                            self.state_message = YLeaf(YType.empty, "state-message")

                            self.insufficient_bw_message = YLeaf(YType.empty, "insufficient-bw-message")

                            self.reoptimized_message = YLeaf(YType.empty, "reoptimized-message")

                            self.pcalc_failure_message = YLeaf(YType.empty, "pcalc-failure-message")
                            self._segment_path = lambda: "auto-mesh-logging"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging, ['bandwidth_change_message', 'reoptimize_attempts_message', 'reroute_messsage', 'state_message', 'insufficient_bw_message', 'reoptimized_message', 'pcalc_failure_message'], name, value)


                    class Priority(Entity):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority, self).__init__()

                            self.yang_name = "priority"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.setup_priority = YLeaf(YType.uint32, "setup-priority")

                            self.hold_priority = YLeaf(YType.uint32, "hold-priority")
                            self._segment_path = lambda: "priority"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority, ['setup_priority', 'hold_priority'], name, value)


                    class AffinityMask(Entity):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask, self).__init__()

                            self.yang_name = "affinity-mask"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.affinity = YLeaf(YType.str, "affinity")

                            self.mask = YLeaf(YType.str, "mask")
                            self._segment_path = lambda: "affinity-mask"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask, ['affinity', 'mask'], name, value)


                    class Bandwidth(Entity):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\:   :py:class:`MplsTeBandwidthDste <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDste>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwidth allocation
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**mandatory**\: True
                        
                        	**units**\: kbit/s
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth, self).__init__()

                            self.yang_name = "bandwidth"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.dste_type = YLeaf(YType.enumeration, "dste-type")

                            self.class_or_pool_type = YLeaf(YType.uint32, "class-or-pool-type")

                            self.bandwidth = YLeaf(YType.uint32, "bandwidth")
                            self._segment_path = lambda: "bandwidth"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth, ['dste_type', 'class_or_pool_type', 'bandwidth'], name, value)


                    class PathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: enable
                        
                        	Enable path selection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection, self).__init__()

                            self.yang_name = "path-selection"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PathSelection, ['enable'], name, value)


                    class PolicyClasses(Entity):
                        """
                        Policy classes for PBTS
                        
                        .. attribute:: policy_class
                        
                        	Array of Policy class
                        	**type**\:  list of int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses, self).__init__()

                            self.yang_name = "policy-classes"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.policy_class = YLeafList(YType.uint32, "policy-class")
                            self._segment_path = lambda: "policy-classes"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses, ['policy_class'], name, value)


                    class NewStyleAffinityAffinityTypes(Entity):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity_affinity_type
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9>`
                        
                        .. attribute:: new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of    :py:class:`NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes, self).__init__()

                            self.yang_name = "new-style-affinity-affinity-types"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"new-style-affinity-affinity-type" : ("new_style_affinity_affinity_type", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType), "new-style-affinity-affinity-type-affinity1" : ("new_style_affinity_affinity_type_affinity1", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1), "new-style-affinity-affinity-type-affinity1-affinity2" : ("new_style_affinity_affinity_type_affinity1_affinity2", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9), "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" : ("new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10", MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10)}

                            self.new_style_affinity_affinity_type = YList(self)
                            self.new_style_affinity_affinity_type_affinity1 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9 = YList(self)
                            self.new_style_affinity_affinity_type_affinity1_affinity2_affinity3_affinity4_affinity5_affinity6_affinity7_affinity8_affinity9_affinity10 = YList(self)
                            self._segment_path = lambda: "new-style-affinity-affinity-types"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes, [], name, value)


                        class NewStyleAffinityAffinityType(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")
                                self._segment_path = lambda: "new-style-affinity-affinity-type" + "[affinity-type='" + self.affinity_type.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityType, ['affinity_type'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1, ['affinity_type', 'affinity1'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2, ['affinity_type', 'affinity1', 'affinity2'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3, ['affinity_type', 'affinity1', 'affinity2', 'affinity3'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9'], name, value)


                        class NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10(Entity):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\:   :py:class:`MplsTeTunnelAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinity>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\:  str
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, self).__init__()

                                self.yang_name = "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10"
                                self.yang_parent_name = "new-style-affinity-affinity-types"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.affinity_type = YLeaf(YType.enumeration, "affinity-type")

                                self.affinity1 = YLeaf(YType.str, "affinity1")

                                self.affinity2 = YLeaf(YType.str, "affinity2")

                                self.affinity3 = YLeaf(YType.str, "affinity3")

                                self.affinity4 = YLeaf(YType.str, "affinity4")

                                self.affinity5 = YLeaf(YType.str, "affinity5")

                                self.affinity6 = YLeaf(YType.str, "affinity6")

                                self.affinity7 = YLeaf(YType.str, "affinity7")

                                self.affinity8 = YLeaf(YType.str, "affinity8")

                                self.affinity9 = YLeaf(YType.str, "affinity9")

                                self.affinity10 = YLeaf(YType.str, "affinity10")
                                self._segment_path = lambda: "new-style-affinity-affinity-type-affinity1-affinity2-affinity3-affinity4-affinity5-affinity6-affinity7-affinity8-affinity9-affinity10" + "[affinity-type='" + self.affinity_type.get() + "']" + "[affinity1='" + self.affinity1.get() + "']" + "[affinity2='" + self.affinity2.get() + "']" + "[affinity3='" + self.affinity3.get() + "']" + "[affinity4='" + self.affinity4.get() + "']" + "[affinity5='" + self.affinity5.get() + "']" + "[affinity6='" + self.affinity6.get() + "']" + "[affinity7='" + self.affinity7.get() + "']" + "[affinity8='" + self.affinity8.get() + "']" + "[affinity9='" + self.affinity9.get() + "']" + "[affinity10='" + self.affinity10.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinityAffinityTypes.NewStyleAffinityAffinityTypeAffinity1Affinity2Affinity3Affinity4Affinity5Affinity6Affinity7Affinity8Affinity9Affinity10, ['affinity_type', 'affinity1', 'affinity2', 'affinity3', 'affinity4', 'affinity5', 'affinity6', 'affinity7', 'affinity8', 'affinity9', 'affinity10'], name, value)


                    class FastReroute(Entity):
                        """
                        Specify MPLS tunnel can be fast\-rerouted
                        
                        .. attribute:: bandwidth_protection
                        
                        	Bandwidth Protection
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        .. attribute:: node_protection
                        
                        	Node Protection
                        	**type**\:  int
                        
                        	**range:** 0..1
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute, self).__init__()

                            self.yang_name = "fast-reroute"
                            self.yang_parent_name = "auto-mesh-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.bandwidth_protection = YLeaf(YType.uint32, "bandwidth-protection")

                            self.node_protection = YLeaf(YType.uint32, "node-protection")
                            self._segment_path = lambda: "fast-reroute"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute, ['bandwidth_protection', 'node_protection'], name, value)


            class XroAttributes(Entity):
                """
                XRO Tunnel Attributes table
                
                .. attribute:: xro_attribute
                
                	XRO Attribute
                	**type**\: list of    :py:class:`XroAttribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes, self).__init__()

                    self.yang_name = "xro-attributes"
                    self.yang_parent_name = "attribute-set"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"xro-attribute" : ("xro_attribute", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute)}

                    self.xro_attribute = YList(self)
                    self._segment_path = lambda: "xro-attributes"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes, [], name, value)


                class XroAttribute(Entity):
                    """
                    XRO Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: path_diversity
                    
                    	Path diversity
                    	**type**\:   :py:class:`PathDiversity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\:   :py:class:`PathSelection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute, self).__init__()

                        self.yang_name = "xro-attribute"
                        self.yang_parent_name = "xro-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"path-diversity" : ("path_diversity", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity), "path-selection" : ("path_selection", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection)}
                        self._child_list_classes = {}

                        self.attribute_set_name = YLeaf(YType.str, "attribute-set-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.path_diversity = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity()
                        self.path_diversity.parent = self
                        self._children_name_map["path_diversity"] = "path-diversity"
                        self._children_yang_names.add("path-diversity")

                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection()
                        self.path_selection.parent = self
                        self._children_name_map["path_selection"] = "path-selection"
                        self._children_yang_names.add("path-selection")
                        self._segment_path = lambda: "xro-attribute" + "[attribute-set-name='" + self.attribute_set_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/attribute-set/xro-attributes/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute, ['attribute_set_name', 'enable'], name, value)


                    class PathDiversity(Entity):
                        """
                        Path diversity
                        
                        .. attribute:: srlgs
                        
                        	SRLG\-based path diversity
                        	**type**\:   :py:class:`Srlgs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs>`
                        
                        .. attribute:: lsp
                        
                        	LSP\-based path diversity
                        	**type**\:   :py:class:`Lsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity, self).__init__()

                            self.yang_name = "path-diversity"
                            self.yang_parent_name = "xro-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"srlgs" : ("srlgs", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs), "lsp" : ("lsp", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp)}
                            self._child_list_classes = {}

                            self.srlgs = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs()
                            self.srlgs.parent = self
                            self._children_name_map["srlgs"] = "srlgs"
                            self._children_yang_names.add("srlgs")

                            self.lsp = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp()
                            self.lsp.parent = self
                            self._children_name_map["lsp"] = "lsp"
                            self._children_yang_names.add("lsp")
                            self._segment_path = lambda: "path-diversity"


                        class Srlgs(Entity):
                            """
                            SRLG\-based path diversity
                            
                            .. attribute:: srlg
                            
                            	SRLG\-based path\-diversity element
                            	**type**\: list of    :py:class:`Srlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs, self).__init__()

                                self.yang_name = "srlgs"
                                self.yang_parent_name = "path-diversity"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"srlg" : ("srlg", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg)}

                                self.srlg = YList(self)
                                self._segment_path = lambda: "srlgs"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs, [], name, value)


                            class Srlg(Entity):
                                """
                                SRLG\-based path\-diversity element
                                
                                .. attribute:: srlg  <key>
                                
                                	SRLG
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: conformance
                                
                                	The diversity conformance requirements
                                	**type**\:   :py:class:`MplsTePathDiversityConformance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathDiversityConformance>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg, self).__init__()

                                    self.yang_name = "srlg"
                                    self.yang_parent_name = "srlgs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.srlg = YLeaf(YType.uint32, "srlg")

                                    self.conformance = YLeaf(YType.enumeration, "conformance")
                                    self._segment_path = lambda: "srlg" + "[srlg='" + self.srlg.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg, ['srlg', 'conformance'], name, value)


                        class Lsp(Entity):
                            """
                            LSP\-based path diversity
                            
                            .. attribute:: fecs
                            
                            	FEC LSP\-based path diversity
                            	**type**\:   :py:class:`Fecs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp, self).__init__()

                                self.yang_name = "lsp"
                                self.yang_parent_name = "path-diversity"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"fecs" : ("fecs", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs)}
                                self._child_list_classes = {}

                                self.fecs = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs()
                                self.fecs.parent = self
                                self._children_name_map["fecs"] = "fecs"
                                self._children_yang_names.add("fecs")
                                self._segment_path = lambda: "lsp"


                            class Fecs(Entity):
                                """
                                FEC LSP\-based path diversity
                                
                                .. attribute:: fec
                                
                                	LSP\-based path\-diversity, referenced by FEC
                                	**type**\: list of    :py:class:`Fec <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec>`
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs, self).__init__()

                                    self.yang_name = "fecs"
                                    self.yang_parent_name = "lsp"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"fec" : ("fec", MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec)}

                                    self.fec = YList(self)
                                    self._segment_path = lambda: "fecs"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs, [], name, value)


                                class Fec(Entity):
                                    """
                                    LSP\-based path\-diversity, referenced by
                                    FEC
                                    
                                    .. attribute:: source  <key>
                                    
                                    	Source address
                                    	**type**\:  str
                                    
                                    .. attribute:: destination  <key>
                                    
                                    	Destination address
                                    	**type**\:  str
                                    
                                    .. attribute:: tunnel_id  <key>
                                    
                                    	Tunnel id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: extended_tunnel_id  <key>
                                    
                                    	Extended tunnel\-id
                                    	**type**\:  str
                                    
                                    .. attribute:: lsp_id  <key>
                                    
                                    	LSP id
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: conformance
                                    
                                    	The diversity conformance requirements
                                    	**type**\:   :py:class:`MplsTePathDiversityConformance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathDiversityConformance>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'mpls-te-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec, self).__init__()

                                        self.yang_name = "fec"
                                        self.yang_parent_name = "fecs"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.source = YLeaf(YType.str, "source")

                                        self.destination = YLeaf(YType.str, "destination")

                                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                                        self.extended_tunnel_id = YLeaf(YType.str, "extended-tunnel-id")

                                        self.lsp_id = YLeaf(YType.uint32, "lsp-id")

                                        self.conformance = YLeaf(YType.enumeration, "conformance")
                                        self._segment_path = lambda: "fec" + "[source='" + self.source.get() + "']" + "[destination='" + self.destination.get() + "']" + "[tunnel-id='" + self.tunnel_id.get() + "']" + "[extended-tunnel-id='" + self.extended_tunnel_id.get() + "']" + "[lsp-id='" + self.lsp_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec, ['source', 'destination', 'tunnel_id', 'extended_tunnel_id', 'lsp_id', 'conformance'], name, value)


                    class PathSelection(Entity):
                        """
                        Configure path selection properties
                        
                        .. attribute:: enable
                        
                        	Enable path selection
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection, self).__init__()

                            self.yang_name = "path-selection"
                            self.yang_parent_name = "xro-attribute"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")
                            self._segment_path = lambda: "path-selection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathSelection, ['enable'], name, value)


        class BfdOverLsp(Entity):
            """
            BFD over MPLS TE Global Configurations
            
            .. attribute:: tail
            
            	BFD over LSP Tail Global Configurations
            	**type**\:   :py:class:`Tail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BfdOverLsp.Tail>`
            
            .. attribute:: head
            
            	BFD over LSP Head Global Configurations
            	**type**\:   :py:class:`Head <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BfdOverLsp.Head>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.BfdOverLsp, self).__init__()

                self.yang_name = "bfd-over-lsp"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"tail" : ("tail", MplsTe.GlobalAttributes.BfdOverLsp.Tail), "head" : ("head", MplsTe.GlobalAttributes.BfdOverLsp.Head)}
                self._child_list_classes = {}

                self.tail = MplsTe.GlobalAttributes.BfdOverLsp.Tail()
                self.tail.parent = self
                self._children_name_map["tail"] = "tail"
                self._children_yang_names.add("tail")

                self.head = MplsTe.GlobalAttributes.BfdOverLsp.Head()
                self.head.parent = self
                self._children_name_map["head"] = "head"
                self._children_yang_names.add("head")
                self._segment_path = lambda: "bfd-over-lsp"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()


            class Tail(Entity):
                """
                BFD over LSP Tail Global Configurations
                
                .. attribute:: multiplier
                
                	Specify BFD over LSP tail multiplier
                	**type**\:  int
                
                	**range:** 3..10
                
                .. attribute:: minimum_interval
                
                	Specify BFD over LSP tail minimum interval
                	**type**\:  int
                
                	**range:** 50..30000
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.BfdOverLsp.Tail, self).__init__()

                    self.yang_name = "tail"
                    self.yang_parent_name = "bfd-over-lsp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.multiplier = YLeaf(YType.uint32, "multiplier")

                    self.minimum_interval = YLeaf(YType.uint32, "minimum-interval")
                    self._segment_path = lambda: "tail"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/bfd-over-lsp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.BfdOverLsp.Tail, ['multiplier', 'minimum_interval'], name, value)


            class Head(Entity):
                """
                BFD over LSP Head Global Configurations
                
                .. attribute:: reopt_timeout
                
                	BFD session down reopt timeout
                	**type**\:  int
                
                	**range:** 120..4294967295
                
                .. attribute:: down_action
                
                	Specify BFD session down action
                	**type**\:   :py:class:`MplsTeBfdSessionDownAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeBfdSessionDownAction>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.BfdOverLsp.Head, self).__init__()

                    self.yang_name = "head"
                    self.yang_parent_name = "bfd-over-lsp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.reopt_timeout = YLeaf(YType.uint32, "reopt-timeout")

                    self.down_action = YLeaf(YType.enumeration, "down-action")
                    self._segment_path = lambda: "head"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/bfd-over-lsp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.BfdOverLsp.Head, ['reopt_timeout', 'down_action'], name, value)


        class BandwidthAccounting(Entity):
            """
            Bandwidth accounting configuration data
            
            .. attribute:: application
            
            	Bandwidth accounting application configuration data
            	**type**\:   :py:class:`Application <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BandwidthAccounting.Application>`
            
            .. attribute:: account_flooding_threshold
            
            	This object sets the flooding threshold as percentage of total link bandwidth for bandwidth accounting. Default to 10%, 10%
            	**type**\:   :py:class:`AccountFloodingThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BandwidthAccounting.AccountFloodingThreshold>`
            
            .. attribute:: sampling_interval
            
            	This object sets the sampling interval in seconds for bandwidth accounting. Default to 60 seconds
            	**type**\:  int
            
            	**range:** 30..600
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: adjustment_factor
            
            	This object sets the percentage adjustment factor for the non RSVP\-TE bandwidth accounting.  Default is 100%
            	**type**\:  int
            
            	**range:** 0..200
            
            	**units**\: percentage
            
            	**default value**\: 100
            
            .. attribute:: collection_type_rsvp_te
            
            	This object enables the bandwidth accounting RSVP\-TE sample collection
            	**type**\:  bool
            
            	**default value**\: false
            
            .. attribute:: enable
            
            	This object controls whether BW accounting is enabled. This object must be set before setting any other objects  under the BandwidthAccounting class
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.BandwidthAccounting, self).__init__()

                self.yang_name = "bandwidth-accounting"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"application" : ("application", MplsTe.GlobalAttributes.BandwidthAccounting.Application), "account-flooding-threshold" : ("account_flooding_threshold", MplsTe.GlobalAttributes.BandwidthAccounting.AccountFloodingThreshold)}
                self._child_list_classes = {}

                self.sampling_interval = YLeaf(YType.uint32, "sampling-interval")

                self.adjustment_factor = YLeaf(YType.uint32, "adjustment-factor")

                self.collection_type_rsvp_te = YLeaf(YType.boolean, "collection-type-rsvp-te")

                self.enable = YLeaf(YType.empty, "enable")

                self.application = MplsTe.GlobalAttributes.BandwidthAccounting.Application()
                self.application.parent = self
                self._children_name_map["application"] = "application"
                self._children_yang_names.add("application")

                self.account_flooding_threshold = MplsTe.GlobalAttributes.BandwidthAccounting.AccountFloodingThreshold()
                self.account_flooding_threshold.parent = self
                self._children_name_map["account_flooding_threshold"] = "account-flooding-threshold"
                self._children_yang_names.add("account-flooding-threshold")
                self._segment_path = lambda: "bandwidth-accounting"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.BandwidthAccounting, ['sampling_interval', 'adjustment_factor', 'collection_type_rsvp_te', 'enable'], name, value)


            class Application(Entity):
                """
                Bandwidth accounting application configuration
                data
                
                .. attribute:: application_enforced
                
                	This object enables the application
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: application_interval
                
                	This object sets the application interval in seconds for bandwidth accounting. Default to 180 seconds
                	**type**\:  int
                
                	**range:** 90..1800
                
                	**units**\: second
                
                	**default value**\: 180
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.BandwidthAccounting.Application, self).__init__()

                    self.yang_name = "application"
                    self.yang_parent_name = "bandwidth-accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.application_enforced = YLeaf(YType.boolean, "application-enforced")

                    self.application_interval = YLeaf(YType.uint32, "application-interval")
                    self._segment_path = lambda: "application"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/bandwidth-accounting/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.BandwidthAccounting.Application, ['application_enforced', 'application_interval'], name, value)


            class AccountFloodingThreshold(Entity):
                """
                This object sets the flooding threshold as
                percentage of total link bandwidth for
                bandwidth accounting. Default to 10%, 10%
                
                .. attribute:: up_threshold
                
                	Upward flooding Threshold in percentages of total bandwidth
                	**type**\:  int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 10
                
                .. attribute:: down_threshold
                
                	Downward flooding Threshold in percentages of total bandwidth
                	**type**\:  int
                
                	**range:** 0..100
                
                	**units**\: percentage
                
                	**default value**\: 10
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.BandwidthAccounting.AccountFloodingThreshold, self).__init__()

                    self.yang_name = "account-flooding-threshold"
                    self.yang_parent_name = "bandwidth-accounting"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.up_threshold = YLeaf(YType.uint32, "up-threshold")

                    self.down_threshold = YLeaf(YType.uint32, "down-threshold")
                    self._segment_path = lambda: "account-flooding-threshold"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/bandwidth-accounting/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.BandwidthAccounting.AccountFloodingThreshold, ['up_threshold', 'down_threshold'], name, value)


        class PceAttributes(Entity):
            """
            Configuration MPLS TE PCE attributes
            
            .. attribute:: pce_stateful
            
            	PCE Stateful
            	**type**\:   :py:class:`PceStateful <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.PceStateful>`
            
            .. attribute:: timer
            
            	Configure PCE (Path Computation Element) timers
            	**type**\:   :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Timer>`
            
            .. attribute:: peers
            
            	Configure PCE peers
            	**type**\:   :py:class:`Peers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Peers>`
            
            .. attribute:: logging
            
            	Configure PCE (Path Computation Element) logging feature
            	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Logging>`
            
            .. attribute:: request_timeout
            
            	Request timeout value in seconds
            	**type**\:  int
            
            	**range:** 5..100
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: reoptimize_period
            
            	PCE reoptimization period for PCE\-based paths
            	**type**\:  int
            
            	**range:** 60..604800
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: address
            
            	Address of this PCE
            	**type**\:  str
            
            .. attribute:: deadtimer
            
            	Deadtimer interval in seconds
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: second
            
            	**default value**\: 120
            
            .. attribute:: keepalive
            
            	Keepalive interval in seconds
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: second
            
            	**default value**\: 30
            
            .. attribute:: keepalive_tolerance
            
            	Keepalive interval tolerance in seconds
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: second
            
            	**default value**\: 10
            
            .. attribute:: peer_source_addr
            
            	PCE Peer Source Address
            	**type**\:  str
            
            .. attribute:: speaker_entity_id
            
            	PCE speaker entity identifier
            	**type**\:  str
            
            	**length:** 1..256
            
            .. attribute:: segment_routing
            
            	PCE segment routing capability
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: password
            
            	MD5 password
            	**type**\:  str
            
            .. attribute:: keychain
            
            	Keychain based authentication
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: precedence
            
            	Precedence order
            	**type**\:  int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.PceAttributes, self).__init__()

                self.yang_name = "pce-attributes"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"pce-stateful" : ("pce_stateful", MplsTe.GlobalAttributes.PceAttributes.PceStateful), "timer" : ("timer", MplsTe.GlobalAttributes.PceAttributes.Timer), "peers" : ("peers", MplsTe.GlobalAttributes.PceAttributes.Peers), "logging" : ("logging", MplsTe.GlobalAttributes.PceAttributes.Logging)}
                self._child_list_classes = {}

                self.request_timeout = YLeaf(YType.uint32, "request-timeout")

                self.reoptimize_period = YLeaf(YType.uint32, "reoptimize-period")

                self.address = YLeaf(YType.str, "address")

                self.deadtimer = YLeaf(YType.uint32, "deadtimer")

                self.keepalive = YLeaf(YType.uint32, "keepalive")

                self.keepalive_tolerance = YLeaf(YType.uint32, "keepalive-tolerance")

                self.peer_source_addr = YLeaf(YType.str, "peer-source-addr")

                self.speaker_entity_id = YLeaf(YType.str, "speaker-entity-id")

                self.segment_routing = YLeaf(YType.empty, "segment-routing")

                self.password = YLeaf(YType.str, "password")

                self.keychain = YLeaf(YType.str, "keychain")

                self.precedence = YLeaf(YType.uint32, "precedence")

                self.pce_stateful = MplsTe.GlobalAttributes.PceAttributes.PceStateful()
                self.pce_stateful.parent = self
                self._children_name_map["pce_stateful"] = "pce-stateful"
                self._children_yang_names.add("pce-stateful")

                self.timer = MplsTe.GlobalAttributes.PceAttributes.Timer()
                self.timer.parent = self
                self._children_name_map["timer"] = "timer"
                self._children_yang_names.add("timer")

                self.peers = MplsTe.GlobalAttributes.PceAttributes.Peers()
                self.peers.parent = self
                self._children_name_map["peers"] = "peers"
                self._children_yang_names.add("peers")

                self.logging = MplsTe.GlobalAttributes.PceAttributes.Logging()
                self.logging.parent = self
                self._children_name_map["logging"] = "logging"
                self._children_yang_names.add("logging")
                self._segment_path = lambda: "pce-attributes"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.PceAttributes, ['request_timeout', 'reoptimize_period', 'address', 'deadtimer', 'keepalive', 'keepalive_tolerance', 'peer_source_addr', 'speaker_entity_id', 'segment_routing', 'password', 'keychain', 'precedence'], name, value)


            class PceStateful(Entity):
                """
                PCE Stateful
                
                .. attribute:: stateful_timers
                
                	Configure Stateful PCE (Path Computation Element) timers
                	**type**\:   :py:class:`StatefulTimers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers>`
                
                .. attribute:: fast_repair
                
                	Enable reoptimization by PCC after path failures
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: instantiation
                
                	PCE stateful instantiation capability
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: cisco_extension
                
                	Enable processing of PCEP Cisco extension
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: delegation
                
                	Delegate all statically configured tunnels
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: report
                
                	Report all statically configured tunnels
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	PCE stateful capability
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PceAttributes.PceStateful, self).__init__()

                    self.yang_name = "pce-stateful"
                    self.yang_parent_name = "pce-attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"stateful-timers" : ("stateful_timers", MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers)}
                    self._child_list_classes = {}

                    self.fast_repair = YLeaf(YType.empty, "fast-repair")

                    self.instantiation = YLeaf(YType.empty, "instantiation")

                    self.cisco_extension = YLeaf(YType.empty, "cisco-extension")

                    self.delegation = YLeaf(YType.empty, "delegation")

                    self.report = YLeaf(YType.empty, "report")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.stateful_timers = MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers()
                    self.stateful_timers.parent = self
                    self._children_name_map["stateful_timers"] = "stateful-timers"
                    self._children_yang_names.add("stateful-timers")
                    self._segment_path = lambda: "pce-stateful"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.PceAttributes.PceStateful, ['fast_repair', 'instantiation', 'cisco_extension', 'delegation', 'report', 'enable'], name, value)


                class StatefulTimers(Entity):
                    """
                    Configure Stateful PCE (Path Computation
                    Element) timers
                    
                    .. attribute:: redelegation_timeout
                    
                    	Timer for static tunnel redelegation in seconds, default is 180 seconds
                    	**type**\:  int
                    
                    	**range:** 0..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 180
                    
                    .. attribute:: state_timeout
                    
                    	State timeout for LSPs without delegation in seconds, zero means immediate removal, default is 180 seconds
                    	**type**\:  int
                    
                    	**range:** 0..3600
                    
                    	**units**\: second
                    
                    	**default value**\: 180
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers, self).__init__()

                        self.yang_name = "stateful-timers"
                        self.yang_parent_name = "pce-stateful"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.redelegation_timeout = YLeaf(YType.uint32, "redelegation-timeout")

                        self.state_timeout = YLeaf(YType.uint32, "state-timeout")
                        self._segment_path = lambda: "stateful-timers"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/pce-stateful/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers, ['redelegation_timeout', 'state_timeout'], name, value)


            class Timer(Entity):
                """
                Configure PCE (Path Computation Element)
                timers
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PceAttributes.Timer, self).__init__()

                    self.yang_name = "timer"
                    self.yang_parent_name = "pce-attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self._segment_path = lambda: "timer"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/%s" % self._segment_path()


            class Peers(Entity):
                """
                Configure PCE peers
                
                .. attribute:: peer
                
                	PCE peer
                	**type**\: list of    :py:class:`Peer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Peers.Peer>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PceAttributes.Peers, self).__init__()

                    self.yang_name = "peers"
                    self.yang_parent_name = "pce-attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"peer" : ("peer", MplsTe.GlobalAttributes.PceAttributes.Peers.Peer)}

                    self.peer = YList(self)
                    self._segment_path = lambda: "peers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.PceAttributes.Peers, [], name, value)


                class Peer(Entity):
                    """
                    PCE peer
                    
                    .. attribute:: pce_peer_address  <key>
                    
                    	Address of PCE Peer
                    	**type**\:  str
                    
                    .. attribute:: enable
                    
                    	Enabled PCE peer (default source address uses local)
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: password
                    
                    	MD5 password
                    	**type**\:  str
                    
                    .. attribute:: keychain
                    
                    	Keychain based authentication
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: precedence
                    
                    	Precedence order
                    	**type**\:  int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.PceAttributes.Peers.Peer, self).__init__()

                        self.yang_name = "peer"
                        self.yang_parent_name = "peers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.pce_peer_address = YLeaf(YType.str, "pce-peer-address")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.password = YLeaf(YType.str, "password")

                        self.keychain = YLeaf(YType.str, "keychain")

                        self.precedence = YLeaf(YType.uint32, "precedence")
                        self._segment_path = lambda: "peer" + "[pce-peer-address='" + self.pce_peer_address.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/peers/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.PceAttributes.Peers.Peer, ['pce_peer_address', 'enable', 'password', 'keychain', 'precedence'], name, value)


            class Logging(Entity):
                """
                Configure PCE (Path Computation Element)
                logging feature
                
                .. attribute:: events
                
                	Configure logging events
                	**type**\:   :py:class:`Events <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Logging.Events>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PceAttributes.Logging, self).__init__()

                    self.yang_name = "logging"
                    self.yang_parent_name = "pce-attributes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"events" : ("events", MplsTe.GlobalAttributes.PceAttributes.Logging.Events)}
                    self._child_list_classes = {}

                    self.events = MplsTe.GlobalAttributes.PceAttributes.Logging.Events()
                    self.events.parent = self
                    self._children_name_map["events"] = "events"
                    self._children_yang_names.add("events")
                    self._segment_path = lambda: "logging"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/%s" % self._segment_path()


                class Events(Entity):
                    """
                    Configure logging events
                    
                    .. attribute:: peer_status
                    
                    	Peer status changes logging
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.PceAttributes.Logging.Events, self).__init__()

                        self.yang_name = "events"
                        self.yang_parent_name = "logging"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.peer_status = YLeaf(YType.empty, "peer-status")
                        self._segment_path = lambda: "events"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/pce-attributes/logging/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.PceAttributes.Logging.Events, ['peer_status'], name, value)


        class LspOutOfResource(Entity):
            """
            Configure LSP OOR attributes in MPLS\-TE
            
            .. attribute:: lsp_oor_red_state
            
            	Configuration for LSP OOR Red/Major State
            	**type**\:   :py:class:`LspOorRedState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState>`
            
            .. attribute:: lsp_oor_yellow_state
            
            	Configuration for LSP OOR Yellow/Minor State
            	**type**\:   :py:class:`LspOorYellowState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.LspOutOfResource, self).__init__()

                self.yang_name = "lsp-out-of-resource"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"lsp-oor-red-state" : ("lsp_oor_red_state", MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState), "lsp-oor-yellow-state" : ("lsp_oor_yellow_state", MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState)}
                self._child_list_classes = {}

                self.lsp_oor_red_state = MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState()
                self.lsp_oor_red_state.parent = self
                self._children_name_map["lsp_oor_red_state"] = "lsp-oor-red-state"
                self._children_yang_names.add("lsp-oor-red-state")

                self.lsp_oor_yellow_state = MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState()
                self.lsp_oor_yellow_state.parent = self
                self._children_name_map["lsp_oor_yellow_state"] = "lsp-oor-yellow-state"
                self._children_yang_names.add("lsp-oor-yellow-state")
                self._segment_path = lambda: "lsp-out-of-resource"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()


            class LspOorRedState(Entity):
                """
                Configuration for LSP OOR Red/Major State
                
                .. attribute:: all_transit_lsp_threshold
                
                	Threshold for all transit LSPs
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: unprotected_transit_lsp_threshold
                
                	Threshold for unprotected transit LSPs
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState, self).__init__()

                    self.yang_name = "lsp-oor-red-state"
                    self.yang_parent_name = "lsp-out-of-resource"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.all_transit_lsp_threshold = YLeaf(YType.int32, "all-transit-lsp-threshold")

                    self.unprotected_transit_lsp_threshold = YLeaf(YType.int32, "unprotected-transit-lsp-threshold")
                    self._segment_path = lambda: "lsp-oor-red-state"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/lsp-out-of-resource/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.LspOutOfResource.LspOorRedState, ['all_transit_lsp_threshold', 'unprotected_transit_lsp_threshold'], name, value)


            class LspOorYellowState(Entity):
                """
                Configuration for LSP OOR Yellow/Minor State
                
                .. attribute:: all_transit_lsp_threshold
                
                	Threshold for all transit LSPs
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                .. attribute:: unprotected_transit_lsp_threshold
                
                	Threshold for unprotected transit LSPs
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState, self).__init__()

                    self.yang_name = "lsp-oor-yellow-state"
                    self.yang_parent_name = "lsp-out-of-resource"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.all_transit_lsp_threshold = YLeaf(YType.int32, "all-transit-lsp-threshold")

                    self.unprotected_transit_lsp_threshold = YLeaf(YType.int32, "unprotected-transit-lsp-threshold")
                    self._segment_path = lambda: "lsp-oor-yellow-state"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/lsp-out-of-resource/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.LspOutOfResource.LspOorYellowState, ['all_transit_lsp_threshold', 'unprotected_transit_lsp_threshold'], name, value)


        class SoftPreemption(Entity):
            """
            Soft preemption configuration data
            
            .. attribute:: timeout
            
            	This object sets the timeout in seconds before hard preemption is triggered
            	**type**\:  int
            
            	**range:** 1..300
            
            	**units**\: second
            
            	**default value**\: 60
            
            .. attribute:: frr_rewrite
            
            	This object controls whether FRR rewrite during soft preemption is enabled
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: enable
            
            	This object controls whether soft preemption is enabled. This object must be set before setting any other objects under the SoftPreemption class
            	**type**\:  bool
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.SoftPreemption, self).__init__()

                self.yang_name = "soft-preemption"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.timeout = YLeaf(YType.uint32, "timeout")

                self.frr_rewrite = YLeaf(YType.empty, "frr-rewrite")

                self.enable = YLeaf(YType.boolean, "enable")
                self._segment_path = lambda: "soft-preemption"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.SoftPreemption, ['timeout', 'frr_rewrite', 'enable'], name, value)


        class FastReroute(Entity):
            """
            Configure fast reroute attributes
            
            .. attribute:: timers
            
            	Configure fast reroute timers
            	**type**\:   :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.FastReroute.Timers>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.FastReroute, self).__init__()

                self.yang_name = "fast-reroute"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"timers" : ("timers", MplsTe.GlobalAttributes.FastReroute.Timers)}
                self._child_list_classes = {}

                self.timers = MplsTe.GlobalAttributes.FastReroute.Timers()
                self.timers.parent = self
                self._children_name_map["timers"] = "timers"
                self._children_yang_names.add("timers")
                self._segment_path = lambda: "fast-reroute"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()


            class Timers(Entity):
                """
                Configure fast reroute timers
                
                .. attribute:: hold_backup
                
                	Seconds before backup declared UP (0 disables hold\-timer)
                	**type**\:  int
                
                	**range:** 0..604800
                
                	**units**\: second
                
                .. attribute:: promotion
                
                	The value of the promotion timer in seconds
                	**type**\:  int
                
                	**range:** 0..604800
                
                	**units**\: second
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.FastReroute.Timers, self).__init__()

                    self.yang_name = "timers"
                    self.yang_parent_name = "fast-reroute"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.hold_backup = YLeaf(YType.uint32, "hold-backup")

                    self.promotion = YLeaf(YType.uint32, "promotion")
                    self._segment_path = lambda: "timers"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/fast-reroute/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.FastReroute.Timers, ['hold_backup', 'promotion'], name, value)


        class PathSelection(Entity):
            """
            Path selection configuration
            
            .. attribute:: loose_metrics
            
            	Path selection Loose ERO Metric Class configuration
            	**type**\:   :py:class:`LooseMetrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection.LooseMetrics>`
            
            .. attribute:: invalidation
            
            	Path invalidation configuration for all tunnels
            	**type**\:   :py:class:`Invalidation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection.Invalidation>`
            
            .. attribute:: ignore_overload_role
            
            	Path selection to ignore overload node during CSPF
            	**type**\:   :py:class:`IgnoreOverloadRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole>`
            
            .. attribute:: loose_affinities
            
            	Path selection Loose ERO Affinity Class configuration
            	**type**\:   :py:class:`LooseAffinities <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection.LooseAffinities>`
            
            .. attribute:: cost_limit
            
            	Path selection cost limit configuration for all tunnels
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: tiebreaker
            
            	CSPF tiebreaker to use in path calculation
            	**type**\:   :py:class:`MplsTePathSelectionTiebreaker <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionTiebreaker>`
            
            .. attribute:: metric
            
            	Metric to use in path calculation
            	**type**\:   :py:class:`MplsTePathSelectionMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetric>`
            
            .. attribute:: loose_domain_match
            
            	Use only the IGP instance of the incoming interface
            	**type**\:  bool
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.PathSelection, self).__init__()

                self.yang_name = "path-selection"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"loose-metrics" : ("loose_metrics", MplsTe.GlobalAttributes.PathSelection.LooseMetrics), "invalidation" : ("invalidation", MplsTe.GlobalAttributes.PathSelection.Invalidation), "ignore-overload-role" : ("ignore_overload_role", MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole), "loose-affinities" : ("loose_affinities", MplsTe.GlobalAttributes.PathSelection.LooseAffinities)}
                self._child_list_classes = {}

                self.cost_limit = YLeaf(YType.uint32, "cost-limit")

                self.tiebreaker = YLeaf(YType.enumeration, "tiebreaker")

                self.metric = YLeaf(YType.enumeration, "metric")

                self.loose_domain_match = YLeaf(YType.boolean, "loose-domain-match")

                self.loose_metrics = MplsTe.GlobalAttributes.PathSelection.LooseMetrics()
                self.loose_metrics.parent = self
                self._children_name_map["loose_metrics"] = "loose-metrics"
                self._children_yang_names.add("loose-metrics")

                self.invalidation = MplsTe.GlobalAttributes.PathSelection.Invalidation()
                self.invalidation.parent = self
                self._children_name_map["invalidation"] = "invalidation"
                self._children_yang_names.add("invalidation")

                self.ignore_overload_role = MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole()
                self.ignore_overload_role.parent = self
                self._children_name_map["ignore_overload_role"] = "ignore-overload-role"
                self._children_yang_names.add("ignore-overload-role")

                self.loose_affinities = MplsTe.GlobalAttributes.PathSelection.LooseAffinities()
                self.loose_affinities.parent = self
                self._children_name_map["loose_affinities"] = "loose-affinities"
                self._children_yang_names.add("loose-affinities")
                self._segment_path = lambda: "path-selection"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.PathSelection, ['cost_limit', 'tiebreaker', 'metric', 'loose_domain_match'], name, value)


            class LooseMetrics(Entity):
                """
                Path selection Loose ERO Metric Class
                configuration
                
                .. attribute:: loose_metric
                
                	Path selection Loose ERO Metric configuration
                	**type**\: list of    :py:class:`LooseMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PathSelection.LooseMetrics, self).__init__()

                    self.yang_name = "loose-metrics"
                    self.yang_parent_name = "path-selection"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"loose-metric" : ("loose_metric", MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric)}

                    self.loose_metric = YList(self)
                    self._segment_path = lambda: "loose-metrics"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/path-selection/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.PathSelection.LooseMetrics, [], name, value)


                class LooseMetric(Entity):
                    """
                    Path selection Loose ERO Metric configuration
                    
                    .. attribute:: class_type  <key>
                    
                    	Path Selection class Type
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: metric_type
                    
                    	Metric to use for ERO Expansion
                    	**type**\:   :py:class:`MplsTePathSelectionMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetric>`
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric, self).__init__()

                        self.yang_name = "loose-metric"
                        self.yang_parent_name = "loose-metrics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.class_type = YLeaf(YType.uint32, "class-type")

                        self.metric_type = YLeaf(YType.enumeration, "metric-type")
                        self._segment_path = lambda: "loose-metric" + "[class-type='" + self.class_type.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/path-selection/loose-metrics/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.PathSelection.LooseMetrics.LooseMetric, ['class_type', 'metric_type'], name, value)


            class Invalidation(Entity):
                """
                Path invalidation configuration for all
                tunnels
                
                .. attribute:: path_invalidation_timeout
                
                	Path Invalidation Timeout
                	**type**\:  int
                
                	**range:** 0..60000
                
                .. attribute:: path_invalidation_action
                
                	Path Invalidation Action
                	**type**\:   :py:class:`PathInvalidationAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.PathInvalidationAction>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PathSelection.Invalidation, self).__init__()

                    self.yang_name = "invalidation"
                    self.yang_parent_name = "path-selection"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.path_invalidation_timeout = YLeaf(YType.uint32, "path-invalidation-timeout")

                    self.path_invalidation_action = YLeaf(YType.enumeration, "path-invalidation-action")
                    self._segment_path = lambda: "invalidation"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/path-selection/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.PathSelection.Invalidation, ['path_invalidation_timeout', 'path_invalidation_action'], name, value)


            class IgnoreOverloadRole(Entity):
                """
                Path selection to ignore overload node during
                CSPF
                
                .. attribute:: head
                
                	Set if the OL\-bit is to be applied to tunnel heads
                	**type**\:  bool
                
                .. attribute:: mid
                
                	Set if the OL\-bit is to be applied to tunnel midpoints
                	**type**\:  bool
                
                .. attribute:: tail
                
                	Set if the OL\-bit is to be applied to tunnel tails
                	**type**\:  bool
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole, self).__init__()

                    self.yang_name = "ignore-overload-role"
                    self.yang_parent_name = "path-selection"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.head = YLeaf(YType.boolean, "head")

                    self.mid = YLeaf(YType.boolean, "mid")

                    self.tail = YLeaf(YType.boolean, "tail")
                    self._segment_path = lambda: "ignore-overload-role"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/path-selection/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.PathSelection.IgnoreOverloadRole, ['head', 'mid', 'tail'], name, value)


            class LooseAffinities(Entity):
                """
                Path selection Loose ERO Affinity Class
                configuration
                
                .. attribute:: loose_affinity
                
                	Path selection Loose ERO Affinity configuration
                	**type**\: list of    :py:class:`LooseAffinity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.PathSelection.LooseAffinities, self).__init__()

                    self.yang_name = "loose-affinities"
                    self.yang_parent_name = "path-selection"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"loose-affinity" : ("loose_affinity", MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity)}

                    self.loose_affinity = YList(self)
                    self._segment_path = lambda: "loose-affinities"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/path-selection/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.PathSelection.LooseAffinities, [], name, value)


                class LooseAffinity(Entity):
                    """
                    Path selection Loose ERO Affinity
                    configuration
                    
                    .. attribute:: class_type  <key>
                    
                    	Path Selection class Type
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: affinity
                    
                    	Affinity flags
                    	**type**\:  str
                    
                    .. attribute:: mask
                    
                    	Affinity mask
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity, self).__init__()

                        self.yang_name = "loose-affinity"
                        self.yang_parent_name = "loose-affinities"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.class_type = YLeaf(YType.uint32, "class-type")

                        self.affinity = YLeaf(YType.str, "affinity")

                        self.mask = YLeaf(YType.str, "mask")
                        self._segment_path = lambda: "loose-affinity" + "[class-type='" + self.class_type.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/path-selection/loose-affinities/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GlobalAttributes.PathSelection.LooseAffinities.LooseAffinity, ['class_type', 'affinity', 'mask'], name, value)


        class AffinityMappings(Entity):
            """
            Affinity Mapping Table configuration
            
            .. attribute:: affinity_mapping
            
            	Affinity Mapping configuration
            	**type**\: list of    :py:class:`AffinityMapping <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GlobalAttributes.AffinityMappings, self).__init__()

                self.yang_name = "affinity-mappings"
                self.yang_parent_name = "global-attributes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"affinity-mapping" : ("affinity_mapping", MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping)}

                self.affinity_mapping = YList(self)
                self._segment_path = lambda: "affinity-mappings"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GlobalAttributes.AffinityMappings, [], name, value)


            class AffinityMapping(Entity):
                """
                Affinity Mapping configuration
                
                .. attribute:: affinity_name  <key>
                
                	Affinity Name
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: value_type
                
                	Affinity value type
                	**type**\:   :py:class:`MplsTeAffinityValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeAffinityValue>`
                
                .. attribute:: value
                
                	Affinity Value in Hex number or by Bit position
                	**type**\:  str
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping, self).__init__()

                    self.yang_name = "affinity-mapping"
                    self.yang_parent_name = "affinity-mappings"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.affinity_name = YLeaf(YType.str, "affinity-name")

                    self.value_type = YLeaf(YType.enumeration, "value-type")

                    self.value = YLeaf(YType.str, "value")
                    self._segment_path = lambda: "affinity-mapping" + "[affinity-name='" + self.affinity_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes/affinity-mappings/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping, ['affinity_name', 'value_type', 'value'], name, value)


    class TransportProfile(Entity):
        """
        MPLS transport profile configuration data
        
        .. attribute:: fault
        
        	Fault management
        	**type**\:   :py:class:`Fault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault>`
        
        .. attribute:: alarm
        
        	Alarm management
        	**type**\:   :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Alarm>`
        
        .. attribute:: bfd
        
        	Configure BFD parameters
        	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Bfd>`
        
        .. attribute:: midpoints
        
        	MPLS\-TP tunnel mid\-point table
        	**type**\:   :py:class:`Midpoints <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints>`
        
        .. attribute:: global_id
        
        	Transport profile global identifier
        	**type**\:  int
        
        	**range:** 1..65535
        
        .. attribute:: node_id
        
        	Node identifier in IPv4 address format
        	**type**\:  str
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.TransportProfile, self).__init__()

            self.yang_name = "transport-profile"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"fault" : ("fault", MplsTe.TransportProfile.Fault), "alarm" : ("alarm", MplsTe.TransportProfile.Alarm), "bfd" : ("bfd", MplsTe.TransportProfile.Bfd), "midpoints" : ("midpoints", MplsTe.TransportProfile.Midpoints)}
            self._child_list_classes = {}

            self.global_id = YLeaf(YType.uint32, "global-id")

            self.node_id = YLeaf(YType.str, "node-id")

            self.fault = MplsTe.TransportProfile.Fault()
            self.fault.parent = self
            self._children_name_map["fault"] = "fault"
            self._children_yang_names.add("fault")

            self.alarm = MplsTe.TransportProfile.Alarm()
            self.alarm.parent = self
            self._children_name_map["alarm"] = "alarm"
            self._children_yang_names.add("alarm")

            self.bfd = MplsTe.TransportProfile.Bfd()
            self.bfd.parent = self
            self._children_name_map["bfd"] = "bfd"
            self._children_yang_names.add("bfd")

            self.midpoints = MplsTe.TransportProfile.Midpoints()
            self.midpoints.parent = self
            self._children_name_map["midpoints"] = "midpoints"
            self._children_yang_names.add("midpoints")
            self._segment_path = lambda: "transport-profile"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.TransportProfile, ['global_id', 'node_id'], name, value)


        class Fault(Entity):
            """
            Fault management
            
            .. attribute:: protection_trigger
            
            	OAM events that trigger protection switching
            	**type**\:   :py:class:`ProtectionTrigger <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault.ProtectionTrigger>`
            
            .. attribute:: wait_to_restore_interval
            
            	Waiting time before restoring working LSP
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: second
            
            	**default value**\: 0
            
            .. attribute:: refresh_interval
            
            	Periodic refresh interval for fault OAM messages
            	**type**\:  int
            
            	**range:** 1..20
            
            	**units**\: second
            
            	**default value**\: 20
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.TransportProfile.Fault, self).__init__()

                self.yang_name = "fault"
                self.yang_parent_name = "transport-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"protection-trigger" : ("protection_trigger", MplsTe.TransportProfile.Fault.ProtectionTrigger)}
                self._child_list_classes = {}

                self.wait_to_restore_interval = YLeaf(YType.uint32, "wait-to-restore-interval")

                self.refresh_interval = YLeaf(YType.uint32, "refresh-interval")

                self.protection_trigger = MplsTe.TransportProfile.Fault.ProtectionTrigger()
                self.protection_trigger.parent = self
                self._children_name_map["protection_trigger"] = "protection-trigger"
                self._children_yang_names.add("protection-trigger")
                self._segment_path = lambda: "fault"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.TransportProfile.Fault, ['wait_to_restore_interval', 'refresh_interval'], name, value)


            class ProtectionTrigger(Entity):
                """
                OAM events that trigger protection switching
                
                .. attribute:: ldi
                
                	Protection switching due to LDI event
                	**type**\:   :py:class:`Ldi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi>`
                
                .. attribute:: lkr
                
                	Protection switching due to LKR event
                	**type**\:   :py:class:`Lkr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr>`
                
                .. attribute:: ais
                
                	Enable protection switching due to AIS event
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.TransportProfile.Fault.ProtectionTrigger, self).__init__()

                    self.yang_name = "protection-trigger"
                    self.yang_parent_name = "fault"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"ldi" : ("ldi", MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi), "lkr" : ("lkr", MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr)}
                    self._child_list_classes = {}

                    self.ais = YLeaf(YType.empty, "ais")

                    self.ldi = MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi()
                    self.ldi.parent = self
                    self._children_name_map["ldi"] = "ldi"
                    self._children_yang_names.add("ldi")

                    self.lkr = MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr()
                    self.lkr.parent = self
                    self._children_name_map["lkr"] = "lkr"
                    self._children_yang_names.add("lkr")
                    self._segment_path = lambda: "protection-trigger"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/fault/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.TransportProfile.Fault.ProtectionTrigger, ['ais'], name, value)


                class Ldi(Entity):
                    """
                    Protection switching due to LDI event
                    
                    .. attribute:: disable
                    
                    	Disable protection switching due to LDI event
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi, self).__init__()

                        self.yang_name = "ldi"
                        self.yang_parent_name = "protection-trigger"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.disable = YLeaf(YType.empty, "disable")
                        self._segment_path = lambda: "ldi"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/fault/protection-trigger/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi, ['disable'], name, value)


                class Lkr(Entity):
                    """
                    Protection switching due to LKR event
                    
                    .. attribute:: disable
                    
                    	Disable protection switching due to LKR event
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr, self).__init__()

                        self.yang_name = "lkr"
                        self.yang_parent_name = "protection-trigger"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.disable = YLeaf(YType.empty, "disable")
                        self._segment_path = lambda: "lkr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/fault/protection-trigger/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr, ['disable'], name, value)


        class Alarm(Entity):
            """
            Alarm management
            
            .. attribute:: suppress_event
            
            	Suppress all tunnel/LSP alarms
            	**type**\:   :py:class:`SuppressEvent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Alarm.SuppressEvent>`
            
            .. attribute:: soak_time
            
            	Duration of soaking alarms
            	**type**\:  int
            
            	**range:** 0..10
            
            	**units**\: second
            
            	**default value**\: 3
            
            .. attribute:: enable_alarm
            
            	Enable Transport Profile Alarm
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.TransportProfile.Alarm, self).__init__()

                self.yang_name = "alarm"
                self.yang_parent_name = "transport-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"suppress-event" : ("suppress_event", MplsTe.TransportProfile.Alarm.SuppressEvent)}
                self._child_list_classes = {}

                self.soak_time = YLeaf(YType.uint32, "soak-time")

                self.enable_alarm = YLeaf(YType.empty, "enable-alarm")

                self.suppress_event = MplsTe.TransportProfile.Alarm.SuppressEvent()
                self.suppress_event.parent = self
                self._children_name_map["suppress_event"] = "suppress-event"
                self._children_yang_names.add("suppress-event")
                self._segment_path = lambda: "alarm"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.TransportProfile.Alarm, ['soak_time', 'enable_alarm'], name, value)


            class SuppressEvent(Entity):
                """
                Suppress all tunnel/LSP alarms
                
                .. attribute:: disable
                
                	Disable alarm suppression
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.TransportProfile.Alarm.SuppressEvent, self).__init__()

                    self.yang_name = "suppress-event"
                    self.yang_parent_name = "alarm"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.disable = YLeaf(YType.empty, "disable")
                    self._segment_path = lambda: "suppress-event"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/alarm/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.TransportProfile.Alarm.SuppressEvent, ['disable'], name, value)


        class Bfd(Entity):
            """
            Configure BFD parameters
            
            .. attribute:: min_interval_standby
            
            	Hello interval for standby transport profile LSPs, either in milli\-seconds or in micro\-seconds
            	**type**\:   :py:class:`MinIntervalStandby <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Bfd.MinIntervalStandby>`
            
            .. attribute:: min_interval
            
            	Hello interval, either in milli\-seconds or in micro\-seconds
            	**type**\:   :py:class:`MinInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Bfd.MinInterval>`
            
            .. attribute:: detection_multiplier_standby
            
            	Detect multiplier for standby transport profile LSP
            	**type**\:  int
            
            	**range:** 2..10
            
            .. attribute:: detection_multiplier
            
            	Detect multiplier
            	**type**\:  int
            
            	**range:** 2..10
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.TransportProfile.Bfd, self).__init__()

                self.yang_name = "bfd"
                self.yang_parent_name = "transport-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"min-interval-standby" : ("min_interval_standby", MplsTe.TransportProfile.Bfd.MinIntervalStandby), "min-interval" : ("min_interval", MplsTe.TransportProfile.Bfd.MinInterval)}
                self._child_list_classes = {}

                self.detection_multiplier_standby = YLeaf(YType.uint32, "detection-multiplier-standby")

                self.detection_multiplier = YLeaf(YType.uint32, "detection-multiplier")

                self.min_interval_standby = MplsTe.TransportProfile.Bfd.MinIntervalStandby()
                self.min_interval_standby.parent = self
                self._children_name_map["min_interval_standby"] = "min-interval-standby"
                self._children_yang_names.add("min-interval-standby")

                self.min_interval = MplsTe.TransportProfile.Bfd.MinInterval()
                self.min_interval.parent = self
                self._children_name_map["min_interval"] = "min-interval"
                self._children_yang_names.add("min-interval")
                self._segment_path = lambda: "bfd"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.TransportProfile.Bfd, ['detection_multiplier_standby', 'detection_multiplier'], name, value)


            class MinIntervalStandby(Entity):
                """
                Hello interval for standby transport profile
                LSPs, either in milli\-seconds or in
                micro\-seconds
                
                .. attribute:: interval_standby_ms
                
                	Hello interval in milli\-seconds
                	**type**\:  int
                
                	**range:** 3..5000
                
                	**units**\: millisecond
                
                .. attribute:: interval_standby_us
                
                	Hello interval in micro\-seconds
                	**type**\:  int
                
                	**range:** 3000..5000000
                
                	**units**\: microsecond
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.TransportProfile.Bfd.MinIntervalStandby, self).__init__()

                    self.yang_name = "min-interval-standby"
                    self.yang_parent_name = "bfd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interval_standby_ms = YLeaf(YType.uint32, "interval-standby-ms")

                    self.interval_standby_us = YLeaf(YType.uint32, "interval-standby-us")
                    self._segment_path = lambda: "min-interval-standby"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/bfd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.TransportProfile.Bfd.MinIntervalStandby, ['interval_standby_ms', 'interval_standby_us'], name, value)


            class MinInterval(Entity):
                """
                Hello interval, either in milli\-seconds or in
                micro\-seconds
                
                .. attribute:: interval_ms
                
                	Hello interval in milli\-seconds
                	**type**\:  int
                
                	**range:** 3..5000
                
                	**units**\: millisecond
                
                .. attribute:: interval_us
                
                	Hello interval in micro\-seconds
                	**type**\:  int
                
                	**range:** 3000..5000000
                
                	**units**\: microsecond
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.TransportProfile.Bfd.MinInterval, self).__init__()

                    self.yang_name = "min-interval"
                    self.yang_parent_name = "bfd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.interval_ms = YLeaf(YType.uint32, "interval-ms")

                    self.interval_us = YLeaf(YType.uint32, "interval-us")
                    self._segment_path = lambda: "min-interval"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/bfd/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.TransportProfile.Bfd.MinInterval, ['interval_ms', 'interval_us'], name, value)


        class Midpoints(Entity):
            """
            MPLS\-TP tunnel mid\-point table
            
            .. attribute:: midpoint
            
            	Transport profile mid\-point identifier
            	**type**\: list of    :py:class:`Midpoint <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.TransportProfile.Midpoints, self).__init__()

                self.yang_name = "midpoints"
                self.yang_parent_name = "transport-profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"midpoint" : ("midpoint", MplsTe.TransportProfile.Midpoints.Midpoint)}

                self.midpoint = YList(self)
                self._segment_path = lambda: "midpoints"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.TransportProfile.Midpoints, [], name, value)


            class Midpoint(Entity):
                """
                Transport profile mid\-point identifier
                
                .. attribute:: midpoint_name  <key>
                
                	Name of mid\-point
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: source
                
                	Node identifier, tunnel identifier and optional global identifier of the source of the LSP
                	**type**\:   :py:class:`Source <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.Source>`
                
                	**presence node**\: True
                
                .. attribute:: destination
                
                	Node identifier, tunnel identifier and optional global identifier of the destination of the LSP
                	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.Destination>`
                
                	**presence node**\: True
                
                .. attribute:: forward_lsp
                
                	Forward transport profile LSP
                	**type**\:   :py:class:`ForwardLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp>`
                
                .. attribute:: reverse_lsp
                
                	none
                	**type**\:   :py:class:`ReverseLsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp>`
                
                .. attribute:: tunnel_name
                
                	Tunnel Name
                	**type**\:  str
                
                .. attribute:: lsp_protect
                
                	Enable LSP protection
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: lsp_id
                
                	Numeric identifier
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.TransportProfile.Midpoints.Midpoint, self).__init__()

                    self.yang_name = "midpoint"
                    self.yang_parent_name = "midpoints"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"source" : ("source", MplsTe.TransportProfile.Midpoints.Midpoint.Source), "destination" : ("destination", MplsTe.TransportProfile.Midpoints.Midpoint.Destination), "forward-lsp" : ("forward_lsp", MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp), "reverse-lsp" : ("reverse_lsp", MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp)}
                    self._child_list_classes = {}

                    self.midpoint_name = YLeaf(YType.str, "midpoint-name")

                    self.tunnel_name = YLeaf(YType.str, "tunnel-name")

                    self.lsp_protect = YLeaf(YType.empty, "lsp-protect")

                    self.lsp_id = YLeaf(YType.uint32, "lsp-id")

                    self.source = None
                    self._children_name_map["source"] = "source"
                    self._children_yang_names.add("source")

                    self.destination = None
                    self._children_name_map["destination"] = "destination"
                    self._children_yang_names.add("destination")

                    self.forward_lsp = MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp()
                    self.forward_lsp.parent = self
                    self._children_name_map["forward_lsp"] = "forward-lsp"
                    self._children_yang_names.add("forward-lsp")

                    self.reverse_lsp = MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp()
                    self.reverse_lsp.parent = self
                    self._children_name_map["reverse_lsp"] = "reverse-lsp"
                    self._children_yang_names.add("reverse-lsp")
                    self._segment_path = lambda: "midpoint" + "[midpoint-name='" + self.midpoint_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/transport-profile/midpoints/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint, ['midpoint_name', 'tunnel_name', 'lsp_protect', 'lsp_id'], name, value)


                class Source(Entity):
                    """
                    Node identifier, tunnel identifier and
                    optional global identifier of the source of
                    the LSP
                    
                    .. attribute:: node_id
                    
                    	Node identifier in IPv4 address format
                    	**type**\:  str
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel identifier in numeric value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: global_id
                    
                    	Global identifier in numeric value
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.TransportProfile.Midpoints.Midpoint.Source, self).__init__()

                        self.yang_name = "source"
                        self.yang_parent_name = "midpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.node_id = YLeaf(YType.str, "node-id")

                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                        self.global_id = YLeaf(YType.uint32, "global-id")
                        self._segment_path = lambda: "source"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint.Source, ['node_id', 'tunnel_id', 'global_id'], name, value)


                class Destination(Entity):
                    """
                    Node identifier, tunnel identifier and
                    optional global identifier of the destination
                    of the LSP
                    
                    .. attribute:: node_id
                    
                    	Node identifier in IPv4 address format
                    	**type**\:  str
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel identifier in numeric value
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: global_id
                    
                    	Global identifier in numeric value
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.TransportProfile.Midpoints.Midpoint.Destination, self).__init__()

                        self.yang_name = "destination"
                        self.yang_parent_name = "midpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.node_id = YLeaf(YType.str, "node-id")

                        self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                        self.global_id = YLeaf(YType.uint32, "global-id")
                        self._segment_path = lambda: "destination"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint.Destination, ['node_id', 'tunnel_id', 'global_id'], name, value)


                class ForwardLsp(Entity):
                    """
                    Forward transport profile LSP
                    
                    .. attribute:: forward_io_map
                    
                    	Label cross\-connect of forward transport profile LSP
                    	**type**\:   :py:class:`ForwardIoMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: forward_bandwidth
                    
                    	Bandwidth of forward transport profile LSP
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp, self).__init__()

                        self.yang_name = "forward-lsp"
                        self.yang_parent_name = "midpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"forward-io-map" : ("forward_io_map", MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap)}
                        self._child_list_classes = {}

                        self.forward_bandwidth = YLeaf(YType.uint32, "forward-bandwidth")

                        self.forward_io_map = None
                        self._children_name_map["forward_io_map"] = "forward-io-map"
                        self._children_yang_names.add("forward-io-map")
                        self._segment_path = lambda: "forward-lsp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp, ['forward_bandwidth'], name, value)


                    class ForwardIoMap(Entity):
                        """
                        Label cross\-connect of forward transport
                        profile LSP
                        
                        .. attribute:: in_label
                        
                        	MPLS label
                        	**type**\:  int
                        
                        	**range:** 16..4015
                        
                        .. attribute:: out_label
                        
                        	Outgoing MPLS label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        	**mandatory**\: True
                        
                        .. attribute:: out_link
                        
                        	Transport profile identifier of outgoing link
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap, self).__init__()

                            self.yang_name = "forward-io-map"
                            self.yang_parent_name = "forward-lsp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.in_label = YLeaf(YType.uint32, "in-label")

                            self.out_label = YLeaf(YType.uint32, "out-label")

                            self.out_link = YLeaf(YType.uint32, "out-link")
                            self._segment_path = lambda: "forward-io-map"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap, ['in_label', 'out_label', 'out_link'], name, value)


                class ReverseLsp(Entity):
                    """
                    none
                    
                    .. attribute:: reverse_io_map
                    
                    	Label cross\-connect of reverse transport profile LSP
                    	**type**\:   :py:class:`ReverseIoMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: reverse_bandwidth
                    
                    	Bandwidth of reverse transport profile LSP
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: kbit/s
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp, self).__init__()

                        self.yang_name = "reverse-lsp"
                        self.yang_parent_name = "midpoint"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"reverse-io-map" : ("reverse_io_map", MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap)}
                        self._child_list_classes = {}

                        self.reverse_bandwidth = YLeaf(YType.uint32, "reverse-bandwidth")

                        self.reverse_io_map = None
                        self._children_name_map["reverse_io_map"] = "reverse-io-map"
                        self._children_yang_names.add("reverse-io-map")
                        self._segment_path = lambda: "reverse-lsp"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp, ['reverse_bandwidth'], name, value)


                    class ReverseIoMap(Entity):
                        """
                        Label cross\-connect of reverse transport
                        profile LSP
                        
                        .. attribute:: in_label
                        
                        	MPLS label
                        	**type**\:  int
                        
                        	**range:** 16..4015
                        
                        .. attribute:: out_label
                        
                        	Outgoing MPLS label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        	**mandatory**\: True
                        
                        .. attribute:: out_link
                        
                        	Transport profile identifier of outgoing link
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap, self).__init__()

                            self.yang_name = "reverse-io-map"
                            self.yang_parent_name = "reverse-lsp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}
                            self.is_presence_container = True

                            self.in_label = YLeaf(YType.uint32, "in-label")

                            self.out_label = YLeaf(YType.uint32, "out-label")

                            self.out_link = YLeaf(YType.uint32, "out-link")
                            self._segment_path = lambda: "reverse-io-map"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap, ['in_label', 'out_label', 'out_link'], name, value)


    class Interfaces(Entity):
        """
        Configure MPLS TE interfaces
        
        .. attribute:: interface
        
        	Configure an MPLS TE interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", MplsTe.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.Interfaces, [], name, value)


        class Interface(Entity):
            """
            Configure an MPLS TE interface
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            .. attribute:: transport_profile_link
            
            	MPLS transport profile capable link
            	**type**\:   :py:class:`TransportProfileLink <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.TransportProfileLink>`
            
            .. attribute:: lcac
            
            	LCAC specific MPLS interface configuration
            	**type**\:   :py:class:`Lcac <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac>`
            
            .. attribute:: global_attributes
            
            	MPLS TE global interface configuration
            	**type**\:   :py:class:`GlobalAttributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"transport-profile-link" : ("transport_profile_link", MplsTe.Interfaces.Interface.TransportProfileLink), "lcac" : ("lcac", MplsTe.Interfaces.Interface.Lcac), "global-attributes" : ("global_attributes", MplsTe.Interfaces.Interface.GlobalAttributes)}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.transport_profile_link = MplsTe.Interfaces.Interface.TransportProfileLink()
                self.transport_profile_link.parent = self
                self._children_name_map["transport_profile_link"] = "transport-profile-link"
                self._children_yang_names.add("transport-profile-link")

                self.lcac = MplsTe.Interfaces.Interface.Lcac()
                self.lcac.parent = self
                self._children_name_map["lcac"] = "lcac"
                self._children_yang_names.add("lcac")

                self.global_attributes = MplsTe.Interfaces.Interface.GlobalAttributes()
                self.global_attributes.parent = self
                self._children_name_map["global_attributes"] = "global-attributes"
                self._children_yang_names.add("global-attributes")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.Interfaces.Interface, ['interface_name'], name, value)


            class TransportProfileLink(Entity):
                """
                MPLS transport profile capable link
                
                .. attribute:: links
                
                	Transport profile link table
                	**type**\:   :py:class:`Links <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.TransportProfileLink.Links>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.Interfaces.Interface.TransportProfileLink, self).__init__()

                    self.yang_name = "transport-profile-link"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"links" : ("links", MplsTe.Interfaces.Interface.TransportProfileLink.Links)}
                    self._child_list_classes = {}

                    self.links = MplsTe.Interfaces.Interface.TransportProfileLink.Links()
                    self.links.parent = self
                    self._children_name_map["links"] = "links"
                    self._children_yang_names.add("links")
                    self._segment_path = lambda: "transport-profile-link"


                class Links(Entity):
                    """
                    Transport profile link table
                    
                    .. attribute:: link
                    
                    	Transport profile link
                    	**type**\: list of    :py:class:`Link <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.TransportProfileLink.Links, self).__init__()

                        self.yang_name = "links"
                        self.yang_parent_name = "transport-profile-link"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"link" : ("link", MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link)}

                        self.link = YList(self)
                        self._segment_path = lambda: "links"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.TransportProfileLink.Links, [], name, value)


                    class Link(Entity):
                        """
                        Transport profile link
                        
                        .. attribute:: link_id  <key>
                        
                        	Numeric link identifier
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\:   :py:class:`LinkNextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.LinkNextHop>`
                        
                        	**default value**\: ipv4-address
                        
                        .. attribute:: next_hop_address
                        
                        	Next\-hop address in IPv4 format
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link, self).__init__()

                            self.yang_name = "link"
                            self.yang_parent_name = "links"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.link_id = YLeaf(YType.uint32, "link-id")

                            self.next_hop_type = YLeaf(YType.enumeration, "next-hop-type")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")
                            self._segment_path = lambda: "link" + "[link-id='" + self.link_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link, ['link_id', 'next_hop_type', 'next_hop_address'], name, value)


            class Lcac(Entity):
                """
                LCAC specific MPLS interface configuration
                
                .. attribute:: switchings
                
                	Set the te\-link switching attributes
                	**type**\:   :py:class:`Switchings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Switchings>`
                
                .. attribute:: flood_area
                
                	Set the IGP instance into which this interface is to be flooded (GMPLS only)
                	**type**\:   :py:class:`FloodArea <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.FloodArea>`
                
                .. attribute:: attribute_name_xr
                
                	Set the interface attribute names
                	**type**\:   :py:class:`AttributeNameXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.AttributeNameXr>`
                
                .. attribute:: attribute_names
                
                	Attribute name table
                	**type**\:   :py:class:`AttributeNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.AttributeNames>`
                
                .. attribute:: srlgs
                
                	Configure SRLG membership for the interface
                	**type**\:   :py:class:`Srlgs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Srlgs>`
                
                .. attribute:: up_thresholds
                
                	Set thresholds for increased resource availability in %
                	**type**\:   :py:class:`UpThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.UpThresholds>`
                
                .. attribute:: down_thresholds
                
                	Set thresholds for decreased resource availability in %
                	**type**\:   :py:class:`DownThresholds <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.DownThresholds>`
                
                .. attribute:: bfd
                
                	Enable use of Bidirectional Forwarding Detection
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: fault_oam_lockout
                
                	Lockout protection on the interface for Flex LSP
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: attribute_flags
                
                	Set user defined interface attribute flags
                	**type**\:  str
                
                .. attribute:: enable
                
                	Enable MPLS\-TE on the link
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: admin_weight
                
                	Set administrative weight for the interface
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.Interfaces.Interface.Lcac, self).__init__()

                    self.yang_name = "lcac"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"switchings" : ("switchings", MplsTe.Interfaces.Interface.Lcac.Switchings), "flood-area" : ("flood_area", MplsTe.Interfaces.Interface.Lcac.FloodArea), "attribute-name-xr" : ("attribute_name_xr", MplsTe.Interfaces.Interface.Lcac.AttributeNameXr), "attribute-names" : ("attribute_names", MplsTe.Interfaces.Interface.Lcac.AttributeNames), "srlgs" : ("srlgs", MplsTe.Interfaces.Interface.Lcac.Srlgs), "up-thresholds" : ("up_thresholds", MplsTe.Interfaces.Interface.Lcac.UpThresholds), "down-thresholds" : ("down_thresholds", MplsTe.Interfaces.Interface.Lcac.DownThresholds)}
                    self._child_list_classes = {}

                    self.bfd = YLeaf(YType.empty, "bfd")

                    self.fault_oam_lockout = YLeaf(YType.empty, "fault-oam-lockout")

                    self.attribute_flags = YLeaf(YType.str, "attribute-flags")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.admin_weight = YLeaf(YType.int32, "admin-weight")

                    self.switchings = MplsTe.Interfaces.Interface.Lcac.Switchings()
                    self.switchings.parent = self
                    self._children_name_map["switchings"] = "switchings"
                    self._children_yang_names.add("switchings")

                    self.flood_area = MplsTe.Interfaces.Interface.Lcac.FloodArea()
                    self.flood_area.parent = self
                    self._children_name_map["flood_area"] = "flood-area"
                    self._children_yang_names.add("flood-area")

                    self.attribute_name_xr = MplsTe.Interfaces.Interface.Lcac.AttributeNameXr()
                    self.attribute_name_xr.parent = self
                    self._children_name_map["attribute_name_xr"] = "attribute-name-xr"
                    self._children_yang_names.add("attribute-name-xr")

                    self.attribute_names = MplsTe.Interfaces.Interface.Lcac.AttributeNames()
                    self.attribute_names.parent = self
                    self._children_name_map["attribute_names"] = "attribute-names"
                    self._children_yang_names.add("attribute-names")

                    self.srlgs = MplsTe.Interfaces.Interface.Lcac.Srlgs()
                    self.srlgs.parent = self
                    self._children_name_map["srlgs"] = "srlgs"
                    self._children_yang_names.add("srlgs")

                    self.up_thresholds = MplsTe.Interfaces.Interface.Lcac.UpThresholds()
                    self.up_thresholds.parent = self
                    self._children_name_map["up_thresholds"] = "up-thresholds"
                    self._children_yang_names.add("up-thresholds")

                    self.down_thresholds = MplsTe.Interfaces.Interface.Lcac.DownThresholds()
                    self.down_thresholds.parent = self
                    self._children_name_map["down_thresholds"] = "down-thresholds"
                    self._children_yang_names.add("down-thresholds")
                    self._segment_path = lambda: "lcac"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.Interfaces.Interface.Lcac, ['bfd', 'fault_oam_lockout', 'attribute_flags', 'enable', 'admin_weight'], name, value)


                class Switchings(Entity):
                    """
                    Set the te\-link switching attributes
                    
                    .. attribute:: switching
                    
                    	The te\-link switching attributes
                    	**type**\: list of    :py:class:`Switching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Switchings.Switching>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.Switchings, self).__init__()

                        self.yang_name = "switchings"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"switching" : ("switching", MplsTe.Interfaces.Interface.Lcac.Switchings.Switching)}

                        self.switching = YList(self)
                        self._segment_path = lambda: "switchings"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.Switchings, [], name, value)


                    class Switching(Entity):
                        """
                        The te\-link switching attributes
                        
                        .. attribute:: switching_id  <key>
                        
                        	Switching index
                        	**type**\: one of the below types:
                        
                        	**type**\:   :py:class:`MplsTeSwitchingIndex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeSwitchingIndex>`
                        
                        
                        ----
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        
                        ----
                        .. attribute:: encoding
                        
                        	Set the local encoding type
                        	**type**\:   :py:class:`MplsTeSwitchingEncoding <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeSwitchingEncoding>`
                        
                        .. attribute:: capability
                        
                        	Set the local switching capability
                        	**type**\:   :py:class:`MplsTeSwitchingCap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeSwitchingCap>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.Lcac.Switchings.Switching, self).__init__()

                            self.yang_name = "switching"
                            self.yang_parent_name = "switchings"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.switching_id = YLeaf(YType.str, "switching-id")

                            self.encoding = YLeaf(YType.enumeration, "encoding")

                            self.capability = YLeaf(YType.enumeration, "capability")
                            self._segment_path = lambda: "switching" + "[switching-id='" + self.switching_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.Switchings.Switching, ['switching_id', 'encoding', 'capability'], name, value)


                class FloodArea(Entity):
                    """
                    Set the IGP instance into which this
                    interface is to be flooded (GMPLS only)
                    
                    .. attribute:: igp_type
                    
                    	IGP type
                    	**type**\:   :py:class:`MplsLcacFloodingIgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsLcacFloodingIgp>`
                    
                    .. attribute:: process_name
                    
                    	Process name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: area_id
                    
                    	Area ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.FloodArea, self).__init__()

                        self.yang_name = "flood-area"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.igp_type = YLeaf(YType.enumeration, "igp-type")

                        self.process_name = YLeaf(YType.str, "process-name")

                        self.area_id = YLeaf(YType.int32, "area-id")
                        self._segment_path = lambda: "flood-area"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.FloodArea, ['igp_type', 'process_name', 'area_id'], name, value)


                class AttributeNameXr(Entity):
                    """
                    Set the interface attribute names
                    
                    .. attribute:: attribute_name
                    
                    	Array of Attribute Names
                    	**type**\:  list of str
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.AttributeNameXr, self).__init__()

                        self.yang_name = "attribute-name-xr"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.attribute_name = YLeafList(YType.str, "attribute-name")
                        self._segment_path = lambda: "attribute-name-xr"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.AttributeNameXr, ['attribute_name'], name, value)


                class AttributeNames(Entity):
                    """
                    Attribute name table
                    
                    .. attribute:: attribute_name
                    
                    	Set the interface attribute names
                    	**type**\: list of    :py:class:`AttributeName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.AttributeNames, self).__init__()

                        self.yang_name = "attribute-names"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"attribute-name" : ("attribute_name", MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName)}

                        self.attribute_name = YList(self)
                        self._segment_path = lambda: "attribute-names"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.AttributeNames, [], name, value)


                    class AttributeName(Entity):
                        """
                        Set the interface attribute names
                        
                        .. attribute:: affinity_index  <key>
                        
                        	Specify the entry index
                        	**type**\:  int
                        
                        	**range:** 1..9
                        
                        .. attribute:: value
                        
                        	Array of Attribute Names
                        	**type**\:  list of str
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName, self).__init__()

                            self.yang_name = "attribute-name"
                            self.yang_parent_name = "attribute-names"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.affinity_index = YLeaf(YType.uint32, "affinity-index")

                            self.value = YLeafList(YType.str, "value")
                            self._segment_path = lambda: "attribute-name" + "[affinity-index='" + self.affinity_index.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName, ['affinity_index', 'value'], name, value)


                class Srlgs(Entity):
                    """
                    Configure SRLG membership for the interface
                    
                    .. attribute:: srlg
                    
                    	SRLG membership number
                    	**type**\: list of    :py:class:`Srlg <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.Srlgs, self).__init__()

                        self.yang_name = "srlgs"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"srlg" : ("srlg", MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg)}

                        self.srlg = YList(self)
                        self._segment_path = lambda: "srlgs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.Srlgs, [], name, value)


                    class Srlg(Entity):
                        """
                        SRLG membership number
                        
                        .. attribute:: srlg_number  <key>
                        
                        	SRLG membership number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg, self).__init__()

                            self.yang_name = "srlg"
                            self.yang_parent_name = "srlgs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.srlg_number = YLeaf(YType.uint32, "srlg-number")
                            self._segment_path = lambda: "srlg" + "[srlg-number='" + self.srlg_number.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg, ['srlg_number'], name, value)


                class UpThresholds(Entity):
                    """
                    Set thresholds for increased resource
                    availability in %
                    
                    .. attribute:: up_threshold
                    
                    	Array of up threshold percentage
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    	**units**\: percentage
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.UpThresholds, self).__init__()

                        self.yang_name = "up-thresholds"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.up_threshold = YLeafList(YType.uint32, "up-threshold")
                        self._segment_path = lambda: "up-thresholds"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.UpThresholds, ['up_threshold'], name, value)


                class DownThresholds(Entity):
                    """
                    Set thresholds for decreased resource
                    availability in %
                    
                    .. attribute:: down_threshold
                    
                    	Array of down threshold percentage
                    	**type**\:  list of int
                    
                    	**range:** 0..100
                    
                    	**units**\: percentage
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.Lcac.DownThresholds, self).__init__()

                        self.yang_name = "down-thresholds"
                        self.yang_parent_name = "lcac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.down_threshold = YLeafList(YType.uint32, "down-threshold")
                        self._segment_path = lambda: "down-thresholds"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.Lcac.DownThresholds, ['down_threshold'], name, value)


            class GlobalAttributes(Entity):
                """
                MPLS TE global interface configuration
                
                .. attribute:: backup_tunnels
                
                	Configure MPLS TE backup tunnels for this interface
                	**type**\:   :py:class:`BackupTunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels>`
                
                .. attribute:: auto_tunnel
                
                	Auto tunnel configuration
                	**type**\:   :py:class:`AutoTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel>`
                
                .. attribute:: backup_paths
                
                	Configure MPLS TE backup tunnels for this interface
                	**type**\:   :py:class:`BackupPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.Interfaces.Interface.GlobalAttributes, self).__init__()

                    self.yang_name = "global-attributes"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"backup-tunnels" : ("backup_tunnels", MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels), "auto-tunnel" : ("auto_tunnel", MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel), "backup-paths" : ("backup_paths", MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths)}
                    self._child_list_classes = {}

                    self.backup_tunnels = MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels()
                    self.backup_tunnels.parent = self
                    self._children_name_map["backup_tunnels"] = "backup-tunnels"
                    self._children_yang_names.add("backup-tunnels")

                    self.auto_tunnel = MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel()
                    self.auto_tunnel.parent = self
                    self._children_name_map["auto_tunnel"] = "auto-tunnel"
                    self._children_yang_names.add("auto-tunnel")

                    self.backup_paths = MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths()
                    self.backup_paths.parent = self
                    self._children_name_map["backup_paths"] = "backup-paths"
                    self._children_yang_names.add("backup-paths")
                    self._segment_path = lambda: "global-attributes"


                class BackupTunnels(Entity):
                    """
                    Configure MPLS TE backup tunnels for this
                    interface
                    
                    .. attribute:: backup_tunnel
                    
                    	Tunnel name
                    	**type**\: list of    :py:class:`BackupTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels, self).__init__()

                        self.yang_name = "backup-tunnels"
                        self.yang_parent_name = "global-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"backup-tunnel" : ("backup_tunnel", MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel)}

                        self.backup_tunnel = YList(self)
                        self._segment_path = lambda: "backup-tunnels"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels, [], name, value)


                    class BackupTunnel(Entity):
                        """
                        Tunnel name
                        
                        .. attribute:: tunnel_name  <key>
                        
                        	Tunnel name
                        	**type**\:  str
                        
                        	**length:** 1..59
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel, self).__init__()

                            self.yang_name = "backup-tunnel"
                            self.yang_parent_name = "backup-tunnels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.tunnel_name = YLeaf(YType.str, "tunnel-name")
                            self._segment_path = lambda: "backup-tunnel" + "[tunnel-name='" + self.tunnel_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.GlobalAttributes.BackupTunnels.BackupTunnel, ['tunnel_name'], name, value)


                class AutoTunnel(Entity):
                    """
                    Auto tunnel configuration
                    
                    .. attribute:: backup
                    
                    	Auto tunnel backup configuration
                    	**type**\:   :py:class:`Backup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel, self).__init__()

                        self.yang_name = "auto-tunnel"
                        self.yang_parent_name = "global-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"backup" : ("backup", MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup)}
                        self._child_list_classes = {}

                        self.backup = MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup()
                        self.backup.parent = self
                        self._children_name_map["backup"] = "backup"
                        self._children_yang_names.add("backup")
                        self._segment_path = lambda: "auto-tunnel"


                    class Backup(Entity):
                        """
                        Auto tunnel backup configuration
                        
                        .. attribute:: exclude
                        
                        	Auto\-tunnel backup exclusion criteria
                        	**type**\:   :py:class:`Exclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude>`
                        
                        .. attribute:: enable
                        
                        	Enable auto\-tunnel backup on this TE link
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: attribute_set
                        
                        	The name of attribute set to be applied to this auto backup lsp
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: next_hop_only
                        
                        	Enable NHOP\-only mode for auto\-tunnel backup on this TE link
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup, self).__init__()

                            self.yang_name = "backup"
                            self.yang_parent_name = "auto-tunnel"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"exclude" : ("exclude", MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude)}
                            self._child_list_classes = {}

                            self.enable = YLeaf(YType.empty, "enable")

                            self.attribute_set = YLeaf(YType.str, "attribute-set")

                            self.next_hop_only = YLeaf(YType.empty, "next-hop-only")

                            self.exclude = MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude()
                            self.exclude.parent = self
                            self._children_name_map["exclude"] = "exclude"
                            self._children_yang_names.add("exclude")
                            self._segment_path = lambda: "backup"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup, ['enable', 'attribute_set', 'next_hop_only'], name, value)


                        class Exclude(Entity):
                            """
                            Auto\-tunnel backup exclusion criteria
                            
                            .. attribute:: srlg_mode
                            
                            	Set exclude SRLG mode for auto\-tunnel backup on this TE link
                            	**type**\:   :py:class:`MplsTesrlgExclude <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTesrlgExclude>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude, self).__init__()

                                self.yang_name = "exclude"
                                self.yang_parent_name = "backup"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.srlg_mode = YLeaf(YType.enumeration, "srlg-mode")
                                self._segment_path = lambda: "exclude"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude, ['srlg_mode'], name, value)


                class BackupPaths(Entity):
                    """
                    Configure MPLS TE backup tunnels for this
                    interface
                    
                    .. attribute:: backup_path
                    
                    	Tunnel interface number
                    	**type**\: list of    :py:class:`BackupPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths, self).__init__()

                        self.yang_name = "backup-paths"
                        self.yang_parent_name = "global-attributes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"backup-path" : ("backup_path", MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath)}

                        self.backup_path = YList(self)
                        self._segment_path = lambda: "backup-paths"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths, [], name, value)


                    class BackupPath(Entity):
                        """
                        Tunnel interface number
                        
                        .. attribute:: tunnel_number  <key>
                        
                        	Tunnel interface number
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath, self).__init__()

                            self.yang_name = "backup-path"
                            self.yang_parent_name = "backup-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.tunnel_number = YLeaf(YType.uint32, "tunnel-number")
                            self._segment_path = lambda: "backup-path" + "[tunnel-number='" + self.tunnel_number.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath, ['tunnel_number'], name, value)


    class GmplsNni(Entity):
        """
        GMPLS\-NNI configuration
        
        .. attribute:: topology_instances
        
        	GMPLS\-NNI topology instance table
        	**type**\:   :py:class:`TopologyInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances>`
        
        .. attribute:: tunnel_heads
        
        	GMPLS\-NNI tunnel\-head table
        	**type**\:   :py:class:`TunnelHeads <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads>`
        
        .. attribute:: path_selection_metric
        
        	Path selection configuration for all gmpls nni tunnels
        	**type**\:   :py:class:`MplsTePathSelectionMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetric>`
        
        .. attribute:: enable_gmpls_nni
        
        	Enable MPLS Traffic Engineering GMPLS\-NNI
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.GmplsNni, self).__init__()

            self.yang_name = "gmpls-nni"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"topology-instances" : ("topology_instances", MplsTe.GmplsNni.TopologyInstances), "tunnel-heads" : ("tunnel_heads", MplsTe.GmplsNni.TunnelHeads)}
            self._child_list_classes = {}

            self.path_selection_metric = YLeaf(YType.enumeration, "path-selection-metric")

            self.enable_gmpls_nni = YLeaf(YType.empty, "enable-gmpls-nni")

            self.topology_instances = MplsTe.GmplsNni.TopologyInstances()
            self.topology_instances.parent = self
            self._children_name_map["topology_instances"] = "topology-instances"
            self._children_yang_names.add("topology-instances")

            self.tunnel_heads = MplsTe.GmplsNni.TunnelHeads()
            self.tunnel_heads.parent = self
            self._children_name_map["tunnel_heads"] = "tunnel-heads"
            self._children_yang_names.add("tunnel-heads")
            self._segment_path = lambda: "gmpls-nni"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.GmplsNni, ['path_selection_metric', 'enable_gmpls_nni'], name, value)


        class TopologyInstances(Entity):
            """
            GMPLS\-NNI topology instance table
            
            .. attribute:: topology_instance
            
            	GMPLS\-NNI topology instance configuration
            	**type**\: list of    :py:class:`TopologyInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GmplsNni.TopologyInstances, self).__init__()

                self.yang_name = "topology-instances"
                self.yang_parent_name = "gmpls-nni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"topology-instance" : ("topology_instance", MplsTe.GmplsNni.TopologyInstances.TopologyInstance)}

                self.topology_instance = YList(self)
                self._segment_path = lambda: "topology-instances"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-nni/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GmplsNni.TopologyInstances, [], name, value)


            class TopologyInstance(Entity):
                """
                GMPLS\-NNI topology instance configuration
                
                .. attribute:: ospf_area_type  <key>
                
                	OSPF area format
                	**type**\:   :py:class:`OspfAreaMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OspfAreaMode>`
                
                .. attribute:: igp_instance_name  <key>
                
                	Name of IGP instance
                	**type**\:  str
                
                	**length:** 1..40
                
                .. attribute:: igp_type  <key>
                
                	IGP type
                	**type**\:   :py:class:`MplsTeIgpProtocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTeIgpProtocol>`
                
                .. attribute:: ospf_int
                
                	ospf int
                	**type**\: list of    :py:class:`OspfInt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt>`
                
                .. attribute:: ospfip_addr
                
                	ospfip addr
                	**type**\: list of    :py:class:`OspfipAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance, self).__init__()

                    self.yang_name = "topology-instance"
                    self.yang_parent_name = "topology-instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ospf-int" : ("ospf_int", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt), "ospfip-addr" : ("ospfip_addr", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr)}

                    self.ospf_area_type = YLeaf(YType.enumeration, "ospf-area-type")

                    self.igp_instance_name = YLeaf(YType.str, "igp-instance-name")

                    self.igp_type = YLeaf(YType.enumeration, "igp-type")

                    self.ospf_int = YList(self)
                    self.ospfip_addr = YList(self)
                    self._segment_path = lambda: "topology-instance" + "[ospf-area-type='" + self.ospf_area_type.get() + "']" + "[igp-instance-name='" + self.igp_instance_name.get() + "']" + "[igp-type='" + self.igp_type.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-nni/topology-instances/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance, ['ospf_area_type', 'igp_instance_name', 'igp_type'], name, value)


                class OspfInt(Entity):
                    """
                    ospf int
                    
                    .. attribute:: igp_area  <key>
                    
                    	IGP area
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: controllers
                    
                    	GMPLS\-NNI controllers
                    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt, self).__init__()

                        self.yang_name = "ospf-int"
                        self.yang_parent_name = "topology-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"controllers" : ("controllers", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers)}
                        self._child_list_classes = {}

                        self.igp_area = YLeaf(YType.int32, "igp-area")

                        self.controllers = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers()
                        self.controllers.parent = self
                        self._children_name_map["controllers"] = "controllers"
                        self._children_yang_names.add("controllers")
                        self._segment_path = lambda: "ospf-int" + "[igp-area='" + self.igp_area.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt, ['igp_area'], name, value)


                    class Controllers(Entity):
                        """
                        GMPLS\-NNI controllers
                        
                        .. attribute:: controller
                        
                        	Configure a GMPLS NNI controller
                        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers, self).__init__()

                            self.yang_name = "controllers"
                            self.yang_parent_name = "ospf-int"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"controller" : ("controller", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller)}

                            self.controller = YList(self)
                            self._segment_path = lambda: "controllers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers, [], name, value)


                        class Controller(Entity):
                            """
                            Configure a GMPLS NNI controller
                            
                            .. attribute:: controller_name  <key>
                            
                            	Controller name
                            	**type**\:  str
                            
                            .. attribute:: tti_mode
                            
                            	Set tandem connection monitoring for the interface
                            	**type**\:   :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode>`
                            
                            .. attribute:: admin_weight
                            
                            	Set administrative weight for the interface
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: enable
                            
                            	Enable GMPLS\-NNI on the link
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: delay
                            
                            	Set link delay for the interface
                            	**type**\:  int
                            
                            	**range:** 1..16777215
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller, self).__init__()

                                self.yang_name = "controller"
                                self.yang_parent_name = "controllers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"tti-mode" : ("tti_mode", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode)}
                                self._child_list_classes = {}

                                self.controller_name = YLeaf(YType.str, "controller-name")

                                self.admin_weight = YLeaf(YType.uint32, "admin-weight")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.delay = YLeaf(YType.uint32, "delay")

                                self.tti_mode = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode()
                                self.tti_mode.parent = self
                                self._children_name_map["tti_mode"] = "tti-mode"
                                self._children_yang_names.add("tti-mode")
                                self._segment_path = lambda: "controller" + "[controller-name='" + self.controller_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller, ['controller_name', 'admin_weight', 'enable', 'delay'], name, value)


                            class TtiMode(Entity):
                                """
                                Set tandem connection monitoring for the
                                interface
                                
                                .. attribute:: tti_mode_type
                                
                                	Type of Trail Trace Identifier
                                	**type**\:   :py:class:`GmplsttiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.GmplsttiMode>`
                                
                                .. attribute:: tcmid
                                
                                	Tandem Connection Monitoring ID for the interface
                                	**type**\:  int
                                
                                	**range:** 1..6
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode, self).__init__()

                                    self.yang_name = "tti-mode"
                                    self.yang_parent_name = "controller"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.tti_mode_type = YLeaf(YType.enumeration, "tti-mode-type")

                                    self.tcmid = YLeaf(YType.uint32, "tcmid")
                                    self._segment_path = lambda: "tti-mode"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode, ['tti_mode_type', 'tcmid'], name, value)


                class OspfipAddr(Entity):
                    """
                    ospfip addr
                    
                    .. attribute:: address  <key>
                    
                    	Area ID if in IP address format
                    	**type**\:  str
                    
                    .. attribute:: controllers
                    
                    	GMPLS\-NNI controllers
                    	**type**\:   :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr, self).__init__()

                        self.yang_name = "ospfip-addr"
                        self.yang_parent_name = "topology-instance"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"controllers" : ("controllers", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers)}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.controllers = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers()
                        self.controllers.parent = self
                        self._children_name_map["controllers"] = "controllers"
                        self._children_yang_names.add("controllers")
                        self._segment_path = lambda: "ospfip-addr" + "[address='" + self.address.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr, ['address'], name, value)


                    class Controllers(Entity):
                        """
                        GMPLS\-NNI controllers
                        
                        .. attribute:: controller
                        
                        	Configure a GMPLS NNI controller
                        	**type**\: list of    :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers, self).__init__()

                            self.yang_name = "controllers"
                            self.yang_parent_name = "ospfip-addr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"controller" : ("controller", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller)}

                            self.controller = YList(self)
                            self._segment_path = lambda: "controllers"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers, [], name, value)


                        class Controller(Entity):
                            """
                            Configure a GMPLS NNI controller
                            
                            .. attribute:: controller_name  <key>
                            
                            	Controller name
                            	**type**\:  str
                            
                            .. attribute:: tti_mode
                            
                            	Set tandem connection monitoring for the interface
                            	**type**\:   :py:class:`TtiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode>`
                            
                            .. attribute:: admin_weight
                            
                            	Set administrative weight for the interface
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: enable
                            
                            	Enable GMPLS\-NNI on the link
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: delay
                            
                            	Set link delay for the interface
                            	**type**\:  int
                            
                            	**range:** 1..16777215
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller, self).__init__()

                                self.yang_name = "controller"
                                self.yang_parent_name = "controllers"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"tti-mode" : ("tti_mode", MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode)}
                                self._child_list_classes = {}

                                self.controller_name = YLeaf(YType.str, "controller-name")

                                self.admin_weight = YLeaf(YType.uint32, "admin-weight")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.delay = YLeaf(YType.uint32, "delay")

                                self.tti_mode = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode()
                                self.tti_mode.parent = self
                                self._children_name_map["tti_mode"] = "tti-mode"
                                self._children_yang_names.add("tti-mode")
                                self._segment_path = lambda: "controller" + "[controller-name='" + self.controller_name.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller, ['controller_name', 'admin_weight', 'enable', 'delay'], name, value)


                            class TtiMode(Entity):
                                """
                                Set tandem connection monitoring for the
                                interface
                                
                                .. attribute:: tti_mode_type
                                
                                	Type of Trail Trace Identifier
                                	**type**\:   :py:class:`GmplsttiMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.GmplsttiMode>`
                                
                                .. attribute:: tcmid
                                
                                	Tandem Connection Monitoring ID for the interface
                                	**type**\:  int
                                
                                	**range:** 1..6
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode, self).__init__()

                                    self.yang_name = "tti-mode"
                                    self.yang_parent_name = "controller"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.tti_mode_type = YLeaf(YType.enumeration, "tti-mode-type")

                                    self.tcmid = YLeaf(YType.uint32, "tcmid")
                                    self._segment_path = lambda: "tti-mode"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode, ['tti_mode_type', 'tcmid'], name, value)


        class TunnelHeads(Entity):
            """
            GMPLS\-NNI tunnel\-head table
            
            .. attribute:: tunnel_head
            
            	The configuration for a GMPLS NNI tunnel head\-end
            	**type**\: list of    :py:class:`TunnelHead <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.GmplsNni.TunnelHeads, self).__init__()

                self.yang_name = "tunnel-heads"
                self.yang_parent_name = "gmpls-nni"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"tunnel-head" : ("tunnel_head", MplsTe.GmplsNni.TunnelHeads.TunnelHead)}

                self.tunnel_head = YList(self)
                self._segment_path = lambda: "tunnel-heads"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-nni/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.GmplsNni.TunnelHeads, [], name, value)


            class TunnelHead(Entity):
                """
                The configuration for a GMPLS NNI tunnel
                head\-end
                
                .. attribute:: tunnel_id  <key>
                
                	Tunnel ID
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: signalled_bandwidth
                
                	The existence of this configuration indicates the signalled bandwidth has been set for the tunnel
                	**type**\:   :py:class:`SignalledBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth>`
                
                .. attribute:: destination
                
                	The existence of this configuration indicates the destination has been set for the tunnel
                	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination>`
                
                .. attribute:: protection_switching
                
                	The configuration for a GMPLS NNI tunnel protection switch
                	**type**\:   :py:class:`ProtectionSwitching <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching>`
                
                .. attribute:: logging
                
                	Tunnel event logging
                	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging>`
                
                .. attribute:: path_options
                
                	GMPLS NNI path options
                	**type**\:   :py:class:`PathOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions>`
                
                .. attribute:: static_uni
                
                	The existence of this configuration indicates the static UNI endpoints have been set for the tunnel
                	**type**\:   :py:class:`StaticUni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni>`
                
                .. attribute:: enable
                
                	The existence of this configuration indicates the a new GMPLS NNI tunnel has been enabled
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: restore_lsp_shutdown
                
                	The existence of this configuration indicates the restore LSP of tunnel is shutdown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: current_lsp_shutdown
                
                	The existence of this configuration indicates the current/working LSP of tunnel is shutdown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: path_selection_metric
                
                	Path selection configuration for this specific tunnel
                	**type**\:   :py:class:`MplsTePathSelectionMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetric>`
                
                .. attribute:: payload
                
                	The existence of this configuration indicates the Payload type have been set for the tunnel
                	**type**\:   :py:class:`OtnPayload <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnPayload>`
                
                .. attribute:: standby_lsp_shutdown
                
                	The existence of this configuration indicates the standby/protect LSP of tunnel is shutdown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: shutdown
                
                	The existence of this configuration indicates the tunnel is shutdown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: path_protection_attribute_set_profile
                
                	The name of the path\-protection profile to be included in signalling messages
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: record_route
                
                	Record the route used by the tunnel
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: signalled_name
                
                	The name of the tunnel to be included in signalling messages
                	**type**\:  str
                
                	**length:** 1..254
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsTe.GmplsNni.TunnelHeads.TunnelHead, self).__init__()

                    self.yang_name = "tunnel-head"
                    self.yang_parent_name = "tunnel-heads"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"signalled-bandwidth" : ("signalled_bandwidth", MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth), "destination" : ("destination", MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination), "protection-switching" : ("protection_switching", MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching), "logging" : ("logging", MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging), "path-options" : ("path_options", MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions), "static-uni" : ("static_uni", MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni)}
                    self._child_list_classes = {}

                    self.tunnel_id = YLeaf(YType.uint32, "tunnel-id")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.restore_lsp_shutdown = YLeaf(YType.empty, "restore-lsp-shutdown")

                    self.current_lsp_shutdown = YLeaf(YType.empty, "current-lsp-shutdown")

                    self.path_selection_metric = YLeaf(YType.enumeration, "path-selection-metric")

                    self.payload = YLeaf(YType.enumeration, "payload")

                    self.standby_lsp_shutdown = YLeaf(YType.empty, "standby-lsp-shutdown")

                    self.shutdown = YLeaf(YType.empty, "shutdown")

                    self.path_protection_attribute_set_profile = YLeaf(YType.str, "path-protection-attribute-set-profile")

                    self.record_route = YLeaf(YType.empty, "record-route")

                    self.signalled_name = YLeaf(YType.str, "signalled-name")

                    self.signalled_bandwidth = MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth()
                    self.signalled_bandwidth.parent = self
                    self._children_name_map["signalled_bandwidth"] = "signalled-bandwidth"
                    self._children_yang_names.add("signalled-bandwidth")

                    self.destination = MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination()
                    self.destination.parent = self
                    self._children_name_map["destination"] = "destination"
                    self._children_yang_names.add("destination")

                    self.protection_switching = MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching()
                    self.protection_switching.parent = self
                    self._children_name_map["protection_switching"] = "protection-switching"
                    self._children_yang_names.add("protection-switching")

                    self.logging = MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging()
                    self.logging.parent = self
                    self._children_name_map["logging"] = "logging"
                    self._children_yang_names.add("logging")

                    self.path_options = MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions()
                    self.path_options.parent = self
                    self._children_name_map["path_options"] = "path-options"
                    self._children_yang_names.add("path-options")

                    self.static_uni = MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni()
                    self.static_uni.parent = self
                    self._children_name_map["static_uni"] = "static-uni"
                    self._children_yang_names.add("static-uni")
                    self._segment_path = lambda: "tunnel-head" + "[tunnel-id='" + self.tunnel_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/gmpls-nni/tunnel-heads/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead, ['tunnel_id', 'enable', 'restore_lsp_shutdown', 'current_lsp_shutdown', 'path_selection_metric', 'payload', 'standby_lsp_shutdown', 'shutdown', 'path_protection_attribute_set_profile', 'record_route', 'signalled_name'], name, value)


                class SignalledBandwidth(Entity):
                    """
                    The existence of this configuration indicates
                    the signalled bandwidth has been set for the
                    tunnel
                    
                    .. attribute:: signalled_bandwidth_type
                    
                    	The g.709 signal type requested
                    	**type**\:   :py:class:`OtnSignaledBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnSignaledBandwidth>`
                    
                    .. attribute:: bitrate
                    
                    	Bitrate value in Kbps for ODUflex framing type
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    	**units**\: kbit/s
                    
                    .. attribute:: od_uflex_framing_type
                    
                    	Framing type in case of ODUflex signal type
                    	**type**\:   :py:class:`OtnSignaledBandwidthFlexFraming <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnSignaledBandwidthFlexFraming>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth, self).__init__()

                        self.yang_name = "signalled-bandwidth"
                        self.yang_parent_name = "tunnel-head"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.signalled_bandwidth_type = YLeaf(YType.enumeration, "signalled-bandwidth-type")

                        self.bitrate = YLeaf(YType.int32, "bitrate")

                        self.od_uflex_framing_type = YLeaf(YType.enumeration, "od-uflex-framing-type")
                        self._segment_path = lambda: "signalled-bandwidth"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth, ['signalled_bandwidth_type', 'bitrate', 'od_uflex_framing_type'], name, value)


                class Destination(Entity):
                    """
                    The existence of this configuration indicates
                    the destination has been set for the tunnel
                    
                    .. attribute:: destination
                    
                    	IPV4 tunnel destination
                    	**type**\:  str
                    
                    .. attribute:: destination_type
                    
                    	Destination type whether it is unicast or unnumbered
                    	**type**\:   :py:class:`OtnDestination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnDestination>`
                    
                    .. attribute:: interface_if_index
                    
                    	Interface index of port
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination, self).__init__()

                        self.yang_name = "destination"
                        self.yang_parent_name = "tunnel-head"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.destination = YLeaf(YType.str, "destination")

                        self.destination_type = YLeaf(YType.enumeration, "destination-type")

                        self.interface_if_index = YLeaf(YType.int32, "interface-if-index")
                        self._segment_path = lambda: "destination"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination, ['destination', 'destination_type', 'interface_if_index'], name, value)


                class ProtectionSwitching(Entity):
                    """
                    The configuration for a GMPLS NNI tunnel
                    protection switch
                    
                    .. attribute:: lockout
                    
                    	The configuration is used to prevent switch over for a particular path type in tunnel
                    	**type**\:   :py:class:`OtnProtectionSwitchLockout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnProtectionSwitchLockout>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching, self).__init__()

                        self.yang_name = "protection-switching"
                        self.yang_parent_name = "tunnel-head"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.lockout = YLeaf(YType.enumeration, "lockout")
                        self._segment_path = lambda: "protection-switching"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.ProtectionSwitching, ['lockout'], name, value)


                class Logging(Entity):
                    """
                    Tunnel event logging
                    
                    .. attribute:: active_lsp_message
                    
                    	Log all tunnel messages for changes in Active LSP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: homepath_state_message
                    
                    	Log all messages for changes in state of Homepath of Working LSP
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: signalling_state_message
                    
                    	Log all tunnel sub\-LSP state messages
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: path_change_message
                    
                    	Log all tunnel messages for changes in path\-change
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: static_cross_connect_message
                    
                    	Log all tunnel messages for static cross\-connect messages
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: tunnel_state_message
                    
                    	Log all tunnel messages for changes in tunnel\-state
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: insufficient_bw_message
                    
                    	Log tunnel messages for insufficient bandwidth
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging, self).__init__()

                        self.yang_name = "logging"
                        self.yang_parent_name = "tunnel-head"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.active_lsp_message = YLeaf(YType.empty, "active-lsp-message")

                        self.homepath_state_message = YLeaf(YType.empty, "homepath-state-message")

                        self.signalling_state_message = YLeaf(YType.empty, "signalling-state-message")

                        self.path_change_message = YLeaf(YType.empty, "path-change-message")

                        self.static_cross_connect_message = YLeaf(YType.empty, "static-cross-connect-message")

                        self.tunnel_state_message = YLeaf(YType.empty, "tunnel-state-message")

                        self.insufficient_bw_message = YLeaf(YType.empty, "insufficient-bw-message")
                        self._segment_path = lambda: "logging"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging, ['active_lsp_message', 'homepath_state_message', 'signalling_state_message', 'path_change_message', 'static_cross_connect_message', 'tunnel_state_message', 'insufficient_bw_message'], name, value)


                class PathOptions(Entity):
                    """
                    GMPLS NNI path options
                    
                    .. attribute:: path_option
                    
                    	The existence of this configuration indicates the path options have been set for the tunnel
                    	**type**\: list of    :py:class:`PathOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions, self).__init__()

                        self.yang_name = "path-options"
                        self.yang_parent_name = "tunnel-head"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"path-option" : ("path_option", MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption)}

                        self.path_option = YList(self)
                        self._segment_path = lambda: "path-options"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions, [], name, value)


                    class PathOption(Entity):
                        """
                        The existence of this configuration
                        indicates the path options have been set for
                        the tunnel
                        
                        .. attribute:: preference_level  <key>
                        
                        	Preference level for this path option
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        .. attribute:: path_type
                        
                        	The type of the path option
                        	**type**\:   :py:class:`MplsTePathOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOption>`
                        
                        .. attribute:: path_id
                        
                        	The ID of the IP explicit path associated with this option
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: path_name
                        
                        	The name of the IP explicit path associated with this option
                        	**type**\:  str
                        
                        .. attribute:: protected_by_preference_level
                        
                        	Preference level of the protecting explicit path. 
                        	**type**\:  int
                        
                        	**range:** 1..1001
                        
                        .. attribute:: restore_by_preference_level
                        
                        	Preference level of the restore path. 
                        	**type**\:  int
                        
                        	**range:** 1..1000
                        
                        .. attribute:: xro_type
                        
                        	The route\-exclusion type
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: xro_attribute_set_name
                        
                        	The name of the XRO attribute set to be used for this path\-option
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: lockdown
                        
                        	Lockdown properties
                        	**type**\:   :py:class:`MplsTePathOptionProperty <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionProperty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption, self).__init__()

                            self.yang_name = "path-option"
                            self.yang_parent_name = "path-options"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.preference_level = YLeaf(YType.uint32, "preference-level")

                            self.path_type = YLeaf(YType.enumeration, "path-type")

                            self.path_id = YLeaf(YType.uint32, "path-id")

                            self.path_name = YLeaf(YType.str, "path-name")

                            self.protected_by_preference_level = YLeaf(YType.uint32, "protected-by-preference-level")

                            self.restore_by_preference_level = YLeaf(YType.uint32, "restore-by-preference-level")

                            self.xro_type = YLeaf(YType.empty, "xro-type")

                            self.xro_attribute_set_name = YLeaf(YType.str, "xro-attribute-set-name")

                            self.lockdown = YLeaf(YType.enumeration, "lockdown")
                            self._segment_path = lambda: "path-option" + "[preference-level='" + self.preference_level.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption, ['preference_level', 'path_type', 'path_id', 'path_name', 'protected_by_preference_level', 'restore_by_preference_level', 'xro_type', 'xro_attribute_set_name', 'lockdown'], name, value)


                class StaticUni(Entity):
                    """
                    The existence of this configuration indicates
                    the static UNI endpoints have been set for
                    the tunnel
                    
                    .. attribute:: ingress_controller_name
                    
                    	Name of  ingress controller
                    	**type**\:  str
                    
                    	**length:** 1..255
                    
                    .. attribute:: egress_controller_if_index
                    
                    	Interface index of Egress controller
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ingress_type
                    
                    	Ingress type whether it is xconnect or terminated
                    	**type**\:   :py:class:`OtnStaticUni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnStaticUni>`
                    
                    .. attribute:: egress_type
                    
                    	Egress type whether it is xconnect or terminated
                    	**type**\:   :py:class:`OtnStaticUni <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.OtnStaticUni>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni, self).__init__()

                        self.yang_name = "static-uni"
                        self.yang_parent_name = "tunnel-head"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.ingress_controller_name = YLeaf(YType.str, "ingress-controller-name")

                        self.egress_controller_if_index = YLeaf(YType.int32, "egress-controller-if-index")

                        self.ingress_type = YLeaf(YType.enumeration, "ingress-type")

                        self.egress_type = YLeaf(YType.enumeration, "egress-type")
                        self._segment_path = lambda: "static-uni"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni, ['ingress_controller_name', 'egress_controller_if_index', 'ingress_type', 'egress_type'], name, value)


    class Lcac(Entity):
        """
        LCAC specific MPLS global configuration
        
        .. attribute:: bfd
        
        	BFD configuration
        	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Lcac.Bfd>`
        
        .. attribute:: flooding_threshold
        
        	Configure flooding threshold as percentage of total link bandwidth
        	**type**\:   :py:class:`FloodingThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Lcac.FloodingThreshold>`
        
        .. attribute:: bandwidth_hold_timer
        
        	Bandwidth hold timer value (seconds)
        	**type**\:  int
        
        	**range:** 1..300
        
        	**units**\: second
        
        .. attribute:: delay_preempt_bundle_capacity_timer
        
        	Bundle capacity preemption timer value (seconds)
        	**type**\:  int
        
        	**range:** 0..300
        
        	**units**\: second
        
        .. attribute:: periodic_flooding_timer
        
        	Periodic flooding value (seconds)
        	**type**\:  int
        
        	**range:** 0..3600
        
        	**units**\: second
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsTe.Lcac, self).__init__()

            self.yang_name = "lcac"
            self.yang_parent_name = "mpls-te"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"bfd" : ("bfd", MplsTe.Lcac.Bfd), "flooding-threshold" : ("flooding_threshold", MplsTe.Lcac.FloodingThreshold)}
            self._child_list_classes = {}

            self.bandwidth_hold_timer = YLeaf(YType.uint32, "bandwidth-hold-timer")

            self.delay_preempt_bundle_capacity_timer = YLeaf(YType.uint32, "delay-preempt-bundle-capacity-timer")

            self.periodic_flooding_timer = YLeaf(YType.uint32, "periodic-flooding-timer")

            self.bfd = MplsTe.Lcac.Bfd()
            self.bfd.parent = self
            self._children_name_map["bfd"] = "bfd"
            self._children_yang_names.add("bfd")

            self.flooding_threshold = MplsTe.Lcac.FloodingThreshold()
            self.flooding_threshold.parent = self
            self._children_name_map["flooding_threshold"] = "flooding-threshold"
            self._children_yang_names.add("flooding-threshold")
            self._segment_path = lambda: "lcac"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsTe.Lcac, ['bandwidth_hold_timer', 'delay_preempt_bundle_capacity_timer', 'periodic_flooding_timer'], name, value)


        class Bfd(Entity):
            """
            BFD configuration
            
            .. attribute:: interval
            
            	Hello interval for BFD sessions created by TE
            	**type**\:  int
            
            	**range:** 15..200
            
            	**units**\: millisecond
            
            .. attribute:: detection_multiplier
            
            	Detection multiplier for BFD sessions created by TE
            	**type**\:  int
            
            	**range:** 2..10
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.Lcac.Bfd, self).__init__()

                self.yang_name = "bfd"
                self.yang_parent_name = "lcac"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interval = YLeaf(YType.uint32, "interval")

                self.detection_multiplier = YLeaf(YType.uint32, "detection-multiplier")
                self._segment_path = lambda: "bfd"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/lcac/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.Lcac.Bfd, ['interval', 'detection_multiplier'], name, value)


        class FloodingThreshold(Entity):
            """
            Configure flooding threshold as percentage of
            total link bandwidth.
            
            .. attribute:: up_stream
            
            	Upward flooding Threshold in percentages of total bandwidth
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percentage
            
            .. attribute:: down_stream
            
            	Downward flooding Threshold in percentages of total bandwidth
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percentage
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsTe.Lcac.FloodingThreshold, self).__init__()

                self.yang_name = "flooding-threshold"
                self.yang_parent_name = "lcac"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.up_stream = YLeaf(YType.uint32, "up-stream")

                self.down_stream = YLeaf(YType.uint32, "down-stream")
                self._segment_path = lambda: "flooding-threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-te-cfg:mpls-te/lcac/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsTe.Lcac.FloodingThreshold, ['up_stream', 'down_stream'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsTe()
        return self._top_entity

