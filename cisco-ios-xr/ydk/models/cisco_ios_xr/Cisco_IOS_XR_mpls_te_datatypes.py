""" Cisco_IOS_XR_mpls_te_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BfdReversePathEnum(Enum):
    """
    BfdReversePathEnum

    Bfd reverse path

    .. data:: bfd_reverse_path_binding_label = 1

    	BindingLabel

    """

    bfd_reverse_path_binding_label = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['BfdReversePathEnum']


class CtypeEnum(Enum):
    """
    CtypeEnum

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

    ctype_null = 0

    ctype_ipv4 = 1

    ctype_ipv4_p2p_tunnel = 7

    ctype_ipv6_p2p_tunnel = 8

    ctype_ipv4_uni = 9

    ctype_ipv4_p2mp_tunnel = 13

    ctype_ipv6_p2mp_tunnel = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['CtypeEnum']


class MplsTeAffinityValueEnum(Enum):
    """
    MplsTeAffinityValueEnum

    Mpls te affinity value

    .. data:: hex_value = 1

    	Affinity value in Hex number

    .. data:: bit_position = 2

    	Affinity value by Bit-Position

    """

    hex_value = 1

    bit_position = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAffinityValueEnum']


class MplsTeAttrSetEnum(Enum):
    """
    MplsTeAttrSetEnum

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

    not_used = 0

    static = 1

    lsp = 2

    unassigned = 3

    auto_backup = 4

    auto_mesh = 5

    xro = 6

    p2mp_te = 7

    otn_pp = 8

    p2p_te = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAttrSetEnum']


class MplsTeAutorouteMetricEnum(Enum):
    """
    MplsTeAutorouteMetricEnum

    Mpls te autoroute metric

    .. data:: relative = 1

    	Relative

    .. data:: absolute = 2

    	Absolute

    .. data:: constant = 3

    	Constant

    """

    relative = 1

    absolute = 2

    constant = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAutorouteMetricEnum']


class MplsTeBackupBandwidthClassEnum(Enum):
    """
    MplsTeBackupBandwidthClassEnum

    Mpls te backup bandwidth class

    .. data:: class0 = 0

    	Class 0

    .. data:: class1 = 1

    	Class 1

    .. data:: any_class = 9

    	Any Class

    """

    class0 = 0

    class1 = 1

    any_class = 9


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBackupBandwidthClassEnum']


class MplsTeBackupBandwidthPoolEnum(Enum):
    """
    MplsTeBackupBandwidthPoolEnum

    Mpls te backup bandwidth pool

    .. data:: any_pool = 1

    	Any Pool

    .. data:: global_pool = 2

    	Global Pool

    .. data:: sub_pool = 4

    	Sub Pool

    """

    any_pool = 1

    global_pool = 2

    sub_pool = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBackupBandwidthPoolEnum']


class MplsTeBandwidthDsteEnum(Enum):
    """
    MplsTeBandwidthDsteEnum

    Mpls te bandwidth dste

    .. data:: standard_dste = 0

    	IETF-Standard DSTE

    .. data:: pre_standard_dste = 1

    	Pre-Standard DSTE

    """

    standard_dste = 0

    pre_standard_dste = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthDsteEnum']


class MplsTeBandwidthLimitEnum(Enum):
    """
    MplsTeBandwidthLimitEnum

    Mpls te bandwidth limit

    .. data:: unlimited = 64

    	Unlimited

    .. data:: limited = 128

    	Limited

    """

    unlimited = 64

    limited = 128


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthLimitEnum']


class MplsTeBandwidthPoolEnum(Enum):
    """
    MplsTeBandwidthPoolEnum

    Mpls te bandwidth pool

    .. data:: any_pool = 0

    	Any Pool

    .. data:: sub_pool = 1

    	Sub Pool

    """

    any_pool = 0

    sub_pool = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthPoolEnum']


class MplsTeBfdSessionDownActionEnum(Enum):
    """
    MplsTeBfdSessionDownActionEnum

    Mpls te bfd session down action

    .. data:: re_setup = 1

    	Tear down and resetup

    """

    re_setup = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBfdSessionDownActionEnum']


class MplsTeIgpProtocolEnum(Enum):
    """
    MplsTeIgpProtocolEnum

    Mpls te igp protocol

    .. data:: none = 0

    	Not set

    .. data:: isis = 1

    	IS IS

    .. data:: ospf = 2

    	OSPF

    """

    none = 0

    isis = 1

    ospf = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeIgpProtocolEnum']


class MplsTeLogFrrProtectionEnum(Enum):
    """
    MplsTeLogFrrProtectionEnum

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

    frr_active_primary = 1

    backup = 256

    frr_ready_primary = 512

    primary = 513

    all = 769


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeLogFrrProtectionEnum']


class MplsTeOtnApsProtectionEnum(Enum):
    """
    MplsTeOtnApsProtectionEnum

    Mpls te otn aps protection

    .. data:: Y_1plus1_unidir_no_aps = 4

    	1PLUS1 UNIDIR NO APS

    .. data:: Y_1plus1_unidir_aps = 8

    	1PLUS1 UNIDIR APS

    .. data:: Y_1plus1_bdir_aps = 16

    	1PLUS1 BIDIR APS

    """

    Y_1plus1_unidir_no_aps = 4

    Y_1plus1_unidir_aps = 8

    Y_1plus1_bdir_aps = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsProtectionEnum']


class MplsTeOtnApsProtectionModeEnum(Enum):
    """
    MplsTeOtnApsProtectionModeEnum

    Mpls te otn aps protection mode

    .. data:: revertive = 1

    	Revertive

    .. data:: non_revertive = 2

    	Non Revertive

    """

    revertive = 1

    non_revertive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsProtectionModeEnum']


class MplsTeOtnApsRestorationStyleEnum(Enum):
    """
    MplsTeOtnApsRestorationStyleEnum

    Mpls te otn aps restoration style

    .. data:: keep_failed_lsp = 1

    	Keep Failed Lsp

    .. data:: delete_failed_lsp = 2

    	Delete Failed Lsp

    """

    keep_failed_lsp = 1

    delete_failed_lsp = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsRestorationStyleEnum']


class MplsTeOtnSncModeEnum(Enum):
    """
    MplsTeOtnSncModeEnum

    Mpls te otn snc mode

    .. data:: snc_n = 1

    	SNC N

    .. data:: snc_i = 2

    	SNC I

    .. data:: snc_s = 3

    	SNC S

    """

    snc_n = 1

    snc_i = 2

    snc_s = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnSncModeEnum']


class MplsTePathDiversityConformanceEnum(Enum):
    """
    MplsTePathDiversityConformanceEnum

    Mpls te path diversity conformance

    .. data:: strict = 0

    	Strict

    .. data:: best_effort = 1

    	Best effort

    """

    strict = 0

    best_effort = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathDiversityConformanceEnum']


class MplsTePathOptionEnum(Enum):
    """
    MplsTePathOptionEnum

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

    not_set = 0

    dynamic = 1

    explicit_name = 3

    explicit_number = 4

    no_ero = 5

    sr = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionEnum']


class MplsTePathOptionPropertyEnum(Enum):
    """
    MplsTePathOptionPropertyEnum

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

    none = 0

    lockdown = 1

    verbatim = 4

    pce = 8

    segment_routing = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionPropertyEnum']


class MplsTePathOptionProtectionEnum(Enum):
    """
    MplsTePathOptionProtectionEnum

    Mpls te path option protection

    .. data:: active = 0

    	Active path

    .. data:: protecting = 1

    	Protecting Path

    """

    active = 0

    protecting = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionProtectionEnum']


class MplsTePathSelectionInvalidationTimerExpireEnum(Enum):
    """
    MplsTePathSelectionInvalidationTimerExpireEnum

    Mpls te path selection invalidation timer expire

    .. data:: tunnel_action_tear = 1

    	Tear down tunnel.

    .. data:: tunnel_action_drop = 2

    	Drop tunnel traffic.

    """

    tunnel_action_tear = 1

    tunnel_action_drop = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionInvalidationTimerExpireEnum']


class MplsTePathSelectionMetricEnum(Enum):
    """
    MplsTePathSelectionMetricEnum

    Mpls te path selection metric

    .. data:: igp = 1

    	IGP Metric

    .. data:: te = 2

    	TE Metric

    .. data:: delay = 4

    	DELAY Metric

    """

    igp = 1

    te = 2

    delay = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionMetricEnum']


class MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum(Enum):
    """
    MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum

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

    not_set = 0

    adj_unprotected = 1

    adj_protected = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum']


class MplsTePathSelectionTiebreakerEnum(Enum):
    """
    MplsTePathSelectionTiebreakerEnum

    Mpls te path selection tiebreaker

    .. data:: min_fill = 1

    	Prefer the path with the least-utilized links

    .. data:: max_fill = 2

    	Prefer the path with the most-utilized links

    .. data:: random = 3

    	Prefer a path with links utilized randomly

    """

    min_fill = 1

    max_fill = 2

    random = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionTiebreakerEnum']


class MplsTeSigNameOptionEnum(Enum):
    """
    MplsTeSigNameOptionEnum

    Mpls te sig name option

    .. data:: none = 0

    	None

    .. data:: address = 1

    	Address

    .. data:: name = 2

    	Name

    """

    none = 0

    address = 1

    name = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeSigNameOptionEnum']


class MplsTeSwitchingCapEnum(Enum):
    """
    MplsTeSwitchingCapEnum

    Mpls te switching cap

    .. data:: psc1 = 1

    	PSC1

    .. data:: lsc = 150

    	LSC

    .. data:: fsc = 200

    	FSC

    """

    psc1 = 1

    lsc = 150

    fsc = 200


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeSwitchingCapEnum']


class MplsTeTunnelAffinityEnum(Enum):
    """
    MplsTeTunnelAffinityEnum

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

    include = 1

    include_strict = 2

    exclude = 3

    exclude_all = 4

    ignore = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeTunnelAffinityEnum']


class MplsTesrlgExcludeEnum(Enum):
    """
    MplsTesrlgExcludeEnum

    Mpls tesrlg exclude

    .. data:: mandatory = 1

    	SRLG Mandatory Exclude

    .. data:: preferred = 2

    	SRLG Preferred Exclude

    .. data:: weighted = 3

    	SRLG Weighted Exclude

    """

    mandatory = 1

    preferred = 2

    weighted = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTesrlgExcludeEnum']


class PathInvalidationActionEnum(Enum):
    """
    PathInvalidationActionEnum

    Path invalidation action

    .. data:: tear = 1

    	Tear

    .. data:: drop = 2

    	Drop

    """

    tear = 1

    drop = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['PathInvalidationActionEnum']


class SrPrependEnum(Enum):
    """
    SrPrependEnum

    Sr prepend

    .. data:: none_type = 0

    	NoneType

    .. data:: next_label = 1

    	Next Label

    .. data:: bgp_n_hop = 2

    	BGP NHOP

    """

    none_type = 0

    next_label = 1

    bgp_n_hop = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['SrPrependEnum']



