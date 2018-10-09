""" Cisco_IOS_XR_mpls_te_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BfdReversePath(Enum):
    """
    BfdReversePath (Enum Class)

    Bfd reverse path

    .. data:: bfd_reverse_path_binding_label = 1

    	BindingLabel

    """

    bfd_reverse_path_binding_label = Enum.YLeaf(1, "bfd-reverse-path-binding-label")


class Ctype(Enum):
    """
    Ctype (Enum Class)

    Ctype

    .. data:: ctype_null = 0

    	CTYPE NULL

    .. data:: ctype_ipv4 = 1

    	CTYPE IPV4

    .. data:: ctype_ipv4_p2p_tunnel = 7

    	CTYPE IPV4 P2P TUNNEL

    .. data:: ctype_ipv6_p2p_tunnel = 8

    	CTYPE IPV6 P2P TUNNEL

    .. data:: ctype_ipv4_uni = 9

    	CTYPE IPV4 UNI

    .. data:: ctype_ipv4_p2mp_tunnel = 13

    	CTYPE IPV4 P2MP TUNNEL

    .. data:: ctype_ipv6_p2mp_tunnel = 14

    	CTYPE IPV6 P2MP TUNNEL

    """

    ctype_null = Enum.YLeaf(0, "ctype-null")

    ctype_ipv4 = Enum.YLeaf(1, "ctype-ipv4")

    ctype_ipv4_p2p_tunnel = Enum.YLeaf(7, "ctype-ipv4-p2p-tunnel")

    ctype_ipv6_p2p_tunnel = Enum.YLeaf(8, "ctype-ipv6-p2p-tunnel")

    ctype_ipv4_uni = Enum.YLeaf(9, "ctype-ipv4-uni")

    ctype_ipv4_p2mp_tunnel = Enum.YLeaf(13, "ctype-ipv4-p2mp-tunnel")

    ctype_ipv6_p2mp_tunnel = Enum.YLeaf(14, "ctype-ipv6-p2mp-tunnel")


class MplsTeAffinityValue(Enum):
    """
    MplsTeAffinityValue (Enum Class)

    Mpls te affinity value

    .. data:: hex_value = 1

    	Affinity value in Hex number

    .. data:: bit_position = 2

    	Affinity value by Bit-Position

    """

    hex_value = Enum.YLeaf(1, "hex-value")

    bit_position = Enum.YLeaf(2, "bit-position")


class MplsTeAttrSet(Enum):
    """
    MplsTeAttrSet (Enum Class)

    Mpls te attr set

    .. data:: not_used = 0

    	Not used

    .. data:: static = 1

    	Static

    .. data:: lsp = 2

    	LSP

    .. data:: unassigned = 3

    	Unassigned

    .. data:: auto_backup = 4

    	Auto backup

    .. data:: auto_mesh = 5

    	Auto mesh

    .. data:: xro = 6

    	XRO

    .. data:: p2mp_te = 7

    	P2MP TE

    .. data:: otn_pp = 8

    	OTN Path Protection

    .. data:: p2p_te = 9

    	P2P TE

    """

    not_used = Enum.YLeaf(0, "not-used")

    static = Enum.YLeaf(1, "static")

    lsp = Enum.YLeaf(2, "lsp")

    unassigned = Enum.YLeaf(3, "unassigned")

    auto_backup = Enum.YLeaf(4, "auto-backup")

    auto_mesh = Enum.YLeaf(5, "auto-mesh")

    xro = Enum.YLeaf(6, "xro")

    p2mp_te = Enum.YLeaf(7, "p2mp-te")

    otn_pp = Enum.YLeaf(8, "otn-pp")

    p2p_te = Enum.YLeaf(9, "p2p-te")


class MplsTeAutorouteMetric(Enum):
    """
    MplsTeAutorouteMetric (Enum Class)

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
    MplsTeBackupBandwidthClass (Enum Class)

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
    MplsTeBackupBandwidthPool (Enum Class)

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
    MplsTeBandwidthDste (Enum Class)

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
    MplsTeBandwidthLimit (Enum Class)

    Mpls te bandwidth limit

    .. data:: unlimited = 64

    	Unlimited

    .. data:: limited = 128

    	Limited

    """

    unlimited = Enum.YLeaf(64, "unlimited")

    limited = Enum.YLeaf(128, "limited")


class MplsTeBandwidthPool(Enum):
    """
    MplsTeBandwidthPool (Enum Class)

    Mpls te bandwidth pool

    .. data:: any_pool = 0

    	Any Pool

    .. data:: sub_pool = 1

    	Sub Pool

    """

    any_pool = Enum.YLeaf(0, "any-pool")

    sub_pool = Enum.YLeaf(1, "sub-pool")


class MplsTeBfdSessionDownAction(Enum):
    """
    MplsTeBfdSessionDownAction (Enum Class)

    Mpls te bfd session down action

    .. data:: re_setup = 1

    	Tear down and resetup

    """

    re_setup = Enum.YLeaf(1, "re-setup")


class MplsTeIgpProtocol(Enum):
    """
    MplsTeIgpProtocol (Enum Class)

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
    MplsTeLogFrrProtection (Enum Class)

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
    MplsTeOtnApsProtection (Enum Class)

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
    MplsTeOtnApsProtectionMode (Enum Class)

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
    MplsTeOtnApsRestorationStyle (Enum Class)

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
    MplsTeOtnSncMode (Enum Class)

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


class MplsTePathDiversityConformance(Enum):
    """
    MplsTePathDiversityConformance (Enum Class)

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
    MplsTePathOption (Enum Class)

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

    	Deprecated

    """

    not_set = Enum.YLeaf(0, "not-set")

    dynamic = Enum.YLeaf(1, "dynamic")

    explicit_name = Enum.YLeaf(3, "explicit-name")

    explicit_number = Enum.YLeaf(4, "explicit-number")

    no_ero = Enum.YLeaf(5, "no-ero")

    sr = Enum.YLeaf(6, "sr")


class MplsTePathOptionProperty(Enum):
    """
    MplsTePathOptionProperty (Enum Class)

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
    MplsTePathOptionProtection (Enum Class)

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
    MplsTePathSelectionInvalidationTimerExpire (Enum Class)

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
    MplsTePathSelectionMetric (Enum Class)

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
    MplsTePathSelectionSegmentRoutingAdjacencyProtection (Enum Class)

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
    MplsTePathSelectionTiebreaker (Enum Class)

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
    MplsTeSigNameOption (Enum Class)

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


class MplsTeSwitchingCap(Enum):
    """
    MplsTeSwitchingCap (Enum Class)

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


class MplsTeTunnelAffinity(Enum):
    """
    MplsTeTunnelAffinity (Enum Class)

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


class MplsTesrlgExclude(Enum):
    """
    MplsTesrlgExclude (Enum Class)

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


class PathInvalidationAction(Enum):
    """
    PathInvalidationAction (Enum Class)

    Path invalidation action

    .. data:: tear = 1

    	Tear

    .. data:: drop = 2

    	Drop

    """

    tear = Enum.YLeaf(1, "tear")

    drop = Enum.YLeaf(2, "drop")


class SrPrepend(Enum):
    """
    SrPrepend (Enum Class)

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



