""" Cisco_IOS_XR_mpls_te_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ctype_Enum(Enum):
    """
    Ctype_Enum

    Ctype

    """

    """

    CTYPE NULL

    """
    CTYPE_NULL = 0

    """

    CTYPE IPV4

    """
    CTYPE_IPV4 = 1

    """

    CTYPE IPV4 P2P TUNNEL

    """
    CTYPE_IPV4_P2P_TUNNEL = 7

    """

    CTYPE IPV6 P2P TUNNEL

    """
    CTYPE_IPV6_P2P_TUNNEL = 8

    """

    CTYPE IPV4 UNI

    """
    CTYPE_IPV4_UNI = 9

    """

    CTYPE IPV4 P2MP TUNNEL

    """
    CTYPE_IPV4_P2MP_TUNNEL = 13

    """

    CTYPE IPV6 P2MP TUNNEL

    """
    CTYPE_IPV6_P2MP_TUNNEL = 14


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['Ctype_Enum']


class MplsTeAffinityValue_Enum(Enum):
    """
    MplsTeAffinityValue_Enum

    Mpls te affinity value

    """

    """

    Affinity value in Hex number

    """
    HEX_VALUE = 1

    """

    Affinity value by Bit\-Position

    """
    BIT_POSITION = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAffinityValue_Enum']


class MplsTeAttrSet_Enum(Enum):
    """
    MplsTeAttrSet_Enum

    Mpls te attr set

    """

    """

    Not used

    """
    NOT_USED = 0

    """

    Static

    """
    STATIC = 1

    """

    LSP

    """
    LSP = 2

    """

    Unassigned

    """
    UNASSIGNED = 3

    """

    Auto backup

    """
    AUTO_BACKUP = 4

    """

    Auto mesh

    """
    AUTO_MESH = 5

    """

    XRO

    """
    XRO = 6

    """

    P2MP TE

    """
    P2MP_TE = 7

    """

    OTN Path Protection

    """
    OTN_PP = 8

    """

    P2P TE

    """
    P2P_TE = 9


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAttrSet_Enum']


class MplsTeAutorouteMetric_Enum(Enum):
    """
    MplsTeAutorouteMetric_Enum

    Mpls te autoroute metric

    """

    """

    Relative

    """
    RELATIVE = 1

    """

    Absolute

    """
    ABSOLUTE = 2

    """

    Constant

    """
    CONSTANT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAutorouteMetric_Enum']


class MplsTeBackupBandwidthClass_Enum(Enum):
    """
    MplsTeBackupBandwidthClass_Enum

    Mpls te backup bandwidth class

    """

    """

    Class 0

    """
    CLASS0 = 0

    """

    Class 1

    """
    CLASS1 = 1

    """

    Any Class

    """
    ANY_CLASS = 9


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBackupBandwidthClass_Enum']


class MplsTeBackupBandwidthPool_Enum(Enum):
    """
    MplsTeBackupBandwidthPool_Enum

    Mpls te backup bandwidth pool

    """

    """

    Any Pool

    """
    ANY_POOL = 1

    """

    Global Pool

    """
    GLOBAL_POOL = 2

    """

    Sub Pool

    """
    SUB_POOL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBackupBandwidthPool_Enum']


class MplsTeBandwidthDste_Enum(Enum):
    """
    MplsTeBandwidthDste_Enum

    Mpls te bandwidth dste

    """

    """

    IETF\-Standard DSTE

    """
    STANDARD_DSTE = 0

    """

    Pre\-Standard DSTE

    """
    PRE_STANDARD_DSTE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthDste_Enum']


class MplsTeBandwidthLimit_Enum(Enum):
    """
    MplsTeBandwidthLimit_Enum

    Mpls te bandwidth limit

    """

    """

    Unlimited

    """
    UNLIMITED = 64

    """

    Limited

    """
    LIMITED = 128


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthLimit_Enum']


class MplsTeBandwidthPool_Enum(Enum):
    """
    MplsTeBandwidthPool_Enum

    Mpls te bandwidth pool

    """

    """

    Any Pool

    """
    ANY_POOL = 0

    """

    Sub Pool

    """
    SUB_POOL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthPool_Enum']


class MplsTeBfdSessionDownAction_Enum(Enum):
    """
    MplsTeBfdSessionDownAction_Enum

    Mpls te bfd session down action

    """

    """

    Tear down and resetup

    """
    RE_SETUP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBfdSessionDownAction_Enum']


class MplsTeIgpProtocol_Enum(Enum):
    """
    MplsTeIgpProtocol_Enum

    Mpls te igp protocol

    """

    """

    Not set

    """
    NONE = 0

    """

    IS IS

    """
    ISIS = 1

    """

    OSPF

    """
    OSPF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeIgpProtocol_Enum']


class MplsTeLogFrrProtection_Enum(Enum):
    """
    MplsTeLogFrrProtection_Enum

    Mpls te log frr protection

    """

    """

    Track only FRR active on primary LSP

    """
    FRR_ACTIVE_PRIMARY = 1

    """

    backup tunnel

    """
    BACKUP = 256

    """

    Track only FRR ready on primary LSP

    """
    FRR_READY_PRIMARY = 512

    """

    primary LSP

    """
    PRIMARY = 513

    """

    all

    """
    ALL = 769


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeLogFrrProtection_Enum']


class MplsTeOtnApsProtectionMode_Enum(Enum):
    """
    MplsTeOtnApsProtectionMode_Enum

    Mpls te otn aps protection mode

    """

    """

    Revertive

    """
    REVERTIVE = 1

    """

    Non Revertive

    """
    NON_REVERTIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsProtectionMode_Enum']


class MplsTeOtnApsProtection_Enum(Enum):
    """
    MplsTeOtnApsProtection_Enum

    Mpls te otn aps protection

    """

    """

    1PLUS1 UNIDIR NO APS

    """
    Y_1PLUS1_UNIDIR_NO_APS = 4

    """

    1PLUS1 UNIDIR APS

    """
    Y_1PLUS1_UNIDIR_APS = 8

    """

    1PLUS1 BIDIR APS

    """
    Y_1PLUS1_BDIR_APS = 16

    """

    1PLUS1PLUS R BIDIR APS

    """
    Y_1PLUS1PLUS_R_BIDIR_APS = 32


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsProtection_Enum']


class MplsTeOtnSncMode_Enum(Enum):
    """
    MplsTeOtnSncMode_Enum

    Mpls te otn snc mode

    """

    """

    SNC N

    """
    SNC_N = 1

    """

    SNC I

    """
    SNC_I = 2

    """

    SNC S

    """
    SNC_S = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnSncMode_Enum']


class MplsTePathDiversityConformance_Enum(Enum):
    """
    MplsTePathDiversityConformance_Enum

    Mpls te path diversity conformance

    """

    """

    Strict

    """
    STRICT = 0

    """

    Best effort

    """
    BEST_EFFORT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathDiversityConformance_Enum']


class MplsTePathOptionProperty_Enum(Enum):
    """
    MplsTePathOptionProperty_Enum

    Mpls te path option property

    """

    """

    No property

    """
    NONE = 0

    """

    Path is not a canditate forreoptimization

    """
    LOCKDOWN = 1

    """

    Explicit path does not require topology
    database

    """
    VERBATIM = 4

    """

    Dynamic path found by PCE server

    """
    PCE = 8

    """

    Segment Routing path

    """
    SEGMENT_ROUTING = 16


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionProperty_Enum']


class MplsTePathOptionProtection_Enum(Enum):
    """
    MplsTePathOptionProtection_Enum

    Mpls te path option protection

    """

    """

    Active path

    """
    ACTIVE = 0

    """

    Protecting Path

    """
    PROTECTING = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionProtection_Enum']


class MplsTePathOption_Enum(Enum):
    """
    MplsTePathOption_Enum

    Mpls te path option

    """

    """

    Not Set

    """
    NOT_SET = 0

    """

    Dynamic

    """
    DYNAMIC = 1

    """

    Explicit, identified by name

    """
    EXPLICIT_NAME = 3

    """

    Explicit, identified by number

    """
    EXPLICIT_NUMBER = 4

    """

    No ERO

    """
    NO_ERO = 5

    """

    Segment routing

    """
    SR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOption_Enum']


class MplsTePathSelectionInvalidationTimerExpire_Enum(Enum):
    """
    MplsTePathSelectionInvalidationTimerExpire_Enum

    Mpls te path selection invalidation timer expire

    """

    """

    Tear down tunnel.

    """
    TUNNEL_ACTION_TEAR = 1

    """

    Drop tunnel traffic.

    """
    TUNNEL_ACTION_DROP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionInvalidationTimerExpire_Enum']


class MplsTePathSelectionMetric_Enum(Enum):
    """
    MplsTePathSelectionMetric_Enum

    Mpls te path selection metric

    """

    """

    IGP Metric

    """
    IGP = 1

    """

    TE Metric

    """
    TE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionMetric_Enum']


class MplsTePathSelectionSegmentRoutingAdjacencyProtection_Enum(Enum):
    """
    MplsTePathSelectionSegmentRoutingAdjacencyProtection_Enum

    Mpls te path selection segment routing adjacency
    protection

    """

    """

    Any segment can be used in a path.

    """
    NOT_SET = 0

    """

    Only unprotected adjacency segments can be used
    in a path.

    """
    ADJ_UNPROTECTED = 1

    """

    Only protected adjacency segments can be used
    in a path.

    """
    ADJ_PROTECTED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionSegmentRoutingAdjacencyProtection_Enum']


class MplsTePathSelectionTiebreaker_Enum(Enum):
    """
    MplsTePathSelectionTiebreaker_Enum

    Mpls te path selection tiebreaker

    """

    """

    Prefer the path with the least\-utilized links

    """
    MIN_FILL = 1

    """

    Prefer the path with the most\-utilized links

    """
    MAX_FILL = 2

    """

    Prefer a path with links utilized randomly

    """
    RANDOM = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionTiebreaker_Enum']


class MplsTeSigNameOption_Enum(Enum):
    """
    MplsTeSigNameOption_Enum

    Mpls te sig name option

    """

    """

    None

    """
    NONE = 0

    """

    Address

    """
    ADDRESS = 1

    """

    Name

    """
    NAME = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeSigNameOption_Enum']


class MplsTeSwitchingCap_Enum(Enum):
    """
    MplsTeSwitchingCap_Enum

    Mpls te switching cap

    """

    """

    PSC1

    """
    PSC1 = 1

    """

    LSC

    """
    LSC = 150

    """

    FSC

    """
    FSC = 200


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeSwitchingCap_Enum']


class MplsTeTunnelAffinity_Enum(Enum):
    """
    MplsTeTunnelAffinity_Enum

    Mpls te tunnel affinity

    """

    """

    Include Affinity

    """
    INCLUDE = 1

    """

    Strictly Include Affinity

    """
    INCLUDE_STRICT = 2

    """

    Exclude Affinity

    """
    EXCLUDE = 3

    """

    Exclude All Affinities

    """
    EXCLUDE_ALL = 4

    """

    Ignore Affinity

    """
    IGNORE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeTunnelAffinity_Enum']


class MplsTesrlgExclude_Enum(Enum):
    """
    MplsTesrlgExclude_Enum

    Mpls tesrlg exclude

    """

    """

    SRLG Mandatory Exclude

    """
    MANDATORY = 1

    """

    SRLG Preferred Exclude

    """
    PREFERRED = 2

    """

    SRLG Weighted Exclude

    """
    WEIGHTED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTesrlgExclude_Enum']


class PathInvalidationAction_Enum(Enum):
    """
    PathInvalidationAction_Enum

    Path invalidation action

    """

    """

    Tear

    """
    TEAR = 1

    """

    Drop

    """
    DROP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['PathInvalidationAction_Enum']


class SrPrepend_Enum(Enum):
    """
    SrPrepend_Enum

    Sr prepend

    """

    """

    NoneType

    """
    NONE_TYPE = 0

    """

    Next Label

    """
    NEXT_LABEL = 1

    """

    BGP NHOP

    """
    BGP_N_HOP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['SrPrepend_Enum']



