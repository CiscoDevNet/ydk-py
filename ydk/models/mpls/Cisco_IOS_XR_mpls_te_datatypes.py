""" Cisco_IOS_XR_mpls_te_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CtypeEnum(Enum):
    """
    CtypeEnum

    Ctype

    .. data:: CTYPE_NULL = 0

    	CTYPE NULL

    .. data:: CTYPE_IPV4 = 1

    	CTYPE IPV4

    .. data:: CTYPE_IPV4_P2P_TUNNEL = 7

    	CTYPE IPV4 P2P TUNNEL

    .. data:: CTYPE_IPV6_P2P_TUNNEL = 8

    	CTYPE IPV6 P2P TUNNEL

    .. data:: CTYPE_IPV4_UNI = 9

    	CTYPE IPV4 UNI

    .. data:: CTYPE_IPV4_P2MP_TUNNEL = 13

    	CTYPE IPV4 P2MP TUNNEL

    .. data:: CTYPE_IPV6_P2MP_TUNNEL = 14

    	CTYPE IPV6 P2MP TUNNEL

    """

    CTYPE_NULL = 0

    CTYPE_IPV4 = 1

    CTYPE_IPV4_P2P_TUNNEL = 7

    CTYPE_IPV6_P2P_TUNNEL = 8

    CTYPE_IPV4_UNI = 9

    CTYPE_IPV4_P2MP_TUNNEL = 13

    CTYPE_IPV6_P2MP_TUNNEL = 14


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['CtypeEnum']


class MplsTeAffinityValueEnum(Enum):
    """
    MplsTeAffinityValueEnum

    Mpls te affinity value

    .. data:: HEX_VALUE = 1

    	Affinity value in Hex number

    .. data:: BIT_POSITION = 2

    	Affinity value by Bit-Position

    """

    HEX_VALUE = 1

    BIT_POSITION = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAffinityValueEnum']


class MplsTeAttrSetEnum(Enum):
    """
    MplsTeAttrSetEnum

    Mpls te attr set

    .. data:: NOT_USED = 0

    	Not used

    .. data:: STATIC = 1

    	Static

    .. data:: LSP = 2

    	LSP

    .. data:: UNASSIGNED = 3

    	Unassigned

    .. data:: AUTO_BACKUP = 4

    	Auto backup

    .. data:: AUTO_MESH = 5

    	Auto mesh

    .. data:: XRO = 6

    	XRO

    .. data:: P2MP_TE = 7

    	P2MP TE

    .. data:: OTN_PP = 8

    	OTN Path Protection

    .. data:: P2P_TE = 9

    	P2P TE

    """

    NOT_USED = 0

    STATIC = 1

    LSP = 2

    UNASSIGNED = 3

    AUTO_BACKUP = 4

    AUTO_MESH = 5

    XRO = 6

    P2MP_TE = 7

    OTN_PP = 8

    P2P_TE = 9


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAttrSetEnum']


class MplsTeAutorouteMetricEnum(Enum):
    """
    MplsTeAutorouteMetricEnum

    Mpls te autoroute metric

    .. data:: RELATIVE = 1

    	Relative

    .. data:: ABSOLUTE = 2

    	Absolute

    .. data:: CONSTANT = 3

    	Constant

    """

    RELATIVE = 1

    ABSOLUTE = 2

    CONSTANT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeAutorouteMetricEnum']


class MplsTeBackupBandwidthClassEnum(Enum):
    """
    MplsTeBackupBandwidthClassEnum

    Mpls te backup bandwidth class

    .. data:: CLASS0 = 0

    	Class 0

    .. data:: CLASS1 = 1

    	Class 1

    .. data:: ANY_CLASS = 9

    	Any Class

    """

    CLASS0 = 0

    CLASS1 = 1

    ANY_CLASS = 9


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBackupBandwidthClassEnum']


class MplsTeBackupBandwidthPoolEnum(Enum):
    """
    MplsTeBackupBandwidthPoolEnum

    Mpls te backup bandwidth pool

    .. data:: ANY_POOL = 1

    	Any Pool

    .. data:: GLOBAL_POOL = 2

    	Global Pool

    .. data:: SUB_POOL = 4

    	Sub Pool

    """

    ANY_POOL = 1

    GLOBAL_POOL = 2

    SUB_POOL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBackupBandwidthPoolEnum']


class MplsTeBandwidthDsteEnum(Enum):
    """
    MplsTeBandwidthDsteEnum

    Mpls te bandwidth dste

    .. data:: STANDARD_DSTE = 0

    	IETF-Standard DSTE

    .. data:: PRE_STANDARD_DSTE = 1

    	Pre-Standard DSTE

    """

    STANDARD_DSTE = 0

    PRE_STANDARD_DSTE = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthDsteEnum']


class MplsTeBandwidthLimitEnum(Enum):
    """
    MplsTeBandwidthLimitEnum

    Mpls te bandwidth limit

    .. data:: UNLIMITED = 64

    	Unlimited

    .. data:: LIMITED = 128

    	Limited

    """

    UNLIMITED = 64

    LIMITED = 128


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthLimitEnum']


class MplsTeBandwidthPoolEnum(Enum):
    """
    MplsTeBandwidthPoolEnum

    Mpls te bandwidth pool

    .. data:: ANY_POOL = 0

    	Any Pool

    .. data:: SUB_POOL = 1

    	Sub Pool

    """

    ANY_POOL = 0

    SUB_POOL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBandwidthPoolEnum']


class MplsTeBfdSessionDownActionEnum(Enum):
    """
    MplsTeBfdSessionDownActionEnum

    Mpls te bfd session down action

    .. data:: RE_SETUP = 1

    	Tear down and resetup

    """

    RE_SETUP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeBfdSessionDownActionEnum']


class MplsTeIgpProtocolEnum(Enum):
    """
    MplsTeIgpProtocolEnum

    Mpls te igp protocol

    .. data:: NONE = 0

    	Not set

    .. data:: ISIS = 1

    	IS IS

    .. data:: OSPF = 2

    	OSPF

    """

    NONE = 0

    ISIS = 1

    OSPF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeIgpProtocolEnum']


class MplsTeLogFrrProtectionEnum(Enum):
    """
    MplsTeLogFrrProtectionEnum

    Mpls te log frr protection

    .. data:: FRR_ACTIVE_PRIMARY = 1

    	Track only FRR active on primary LSP

    .. data:: BACKUP = 256

    	backup tunnel

    .. data:: FRR_READY_PRIMARY = 512

    	Track only FRR ready on primary LSP

    .. data:: PRIMARY = 513

    	primary LSP

    .. data:: ALL = 769

    	all

    """

    FRR_ACTIVE_PRIMARY = 1

    BACKUP = 256

    FRR_READY_PRIMARY = 512

    PRIMARY = 513

    ALL = 769


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeLogFrrProtectionEnum']


class MplsTeOtnApsProtectionEnum(Enum):
    """
    MplsTeOtnApsProtectionEnum

    Mpls te otn aps protection

    .. data:: Y_1PLUS1_UNIDIR_NO_APS = 4

    	1PLUS1 UNIDIR NO APS

    .. data:: Y_1PLUS1_UNIDIR_APS = 8

    	1PLUS1 UNIDIR APS

    .. data:: Y_1PLUS1_BDIR_APS = 16

    	1PLUS1 BIDIR APS

    .. data:: Y_1PLUS1PLUS_R_BIDIR_APS = 32

    	1PLUS1PLUS R BIDIR APS

    """

    Y_1PLUS1_UNIDIR_NO_APS = 4

    Y_1PLUS1_UNIDIR_APS = 8

    Y_1PLUS1_BDIR_APS = 16

    Y_1PLUS1PLUS_R_BIDIR_APS = 32


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsProtectionEnum']


class MplsTeOtnApsProtectionModeEnum(Enum):
    """
    MplsTeOtnApsProtectionModeEnum

    Mpls te otn aps protection mode

    .. data:: REVERTIVE = 1

    	Revertive

    .. data:: NON_REVERTIVE = 2

    	Non Revertive

    """

    REVERTIVE = 1

    NON_REVERTIVE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnApsProtectionModeEnum']


class MplsTeOtnSncModeEnum(Enum):
    """
    MplsTeOtnSncModeEnum

    Mpls te otn snc mode

    .. data:: SNC_N = 1

    	SNC N

    .. data:: SNC_I = 2

    	SNC I

    .. data:: SNC_S = 3

    	SNC S

    """

    SNC_N = 1

    SNC_I = 2

    SNC_S = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeOtnSncModeEnum']


class MplsTePathDiversityConformanceEnum(Enum):
    """
    MplsTePathDiversityConformanceEnum

    Mpls te path diversity conformance

    .. data:: STRICT = 0

    	Strict

    .. data:: BEST_EFFORT = 1

    	Best effort

    """

    STRICT = 0

    BEST_EFFORT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathDiversityConformanceEnum']


class MplsTePathOptionEnum(Enum):
    """
    MplsTePathOptionEnum

    Mpls te path option

    .. data:: NOT_SET = 0

    	Not Set

    .. data:: DYNAMIC = 1

    	Dynamic

    .. data:: EXPLICIT_NAME = 3

    	Explicit, identified by name

    .. data:: EXPLICIT_NUMBER = 4

    	Explicit, identified by number

    .. data:: NO_ERO = 5

    	No ERO

    .. data:: SR = 6

    	Segment routing

    """

    NOT_SET = 0

    DYNAMIC = 1

    EXPLICIT_NAME = 3

    EXPLICIT_NUMBER = 4

    NO_ERO = 5

    SR = 6


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionEnum']


class MplsTePathOptionPropertyEnum(Enum):
    """
    MplsTePathOptionPropertyEnum

    Mpls te path option property

    .. data:: NONE = 0

    	No property

    .. data:: LOCKDOWN = 1

    	Path is not a canditate forreoptimization

    .. data:: VERBATIM = 4

    	Explicit path does not require topology

    	database

    .. data:: PCE = 8

    	Dynamic path found by PCE server

    .. data:: SEGMENT_ROUTING = 16

    	Segment Routing path

    """

    NONE = 0

    LOCKDOWN = 1

    VERBATIM = 4

    PCE = 8

    SEGMENT_ROUTING = 16


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionPropertyEnum']


class MplsTePathOptionProtectionEnum(Enum):
    """
    MplsTePathOptionProtectionEnum

    Mpls te path option protection

    .. data:: ACTIVE = 0

    	Active path

    .. data:: PROTECTING = 1

    	Protecting Path

    """

    ACTIVE = 0

    PROTECTING = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathOptionProtectionEnum']


class MplsTePathSelectionInvalidationTimerExpireEnum(Enum):
    """
    MplsTePathSelectionInvalidationTimerExpireEnum

    Mpls te path selection invalidation timer expire

    .. data:: TUNNEL_ACTION_TEAR = 1

    	Tear down tunnel.

    .. data:: TUNNEL_ACTION_DROP = 2

    	Drop tunnel traffic.

    """

    TUNNEL_ACTION_TEAR = 1

    TUNNEL_ACTION_DROP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionInvalidationTimerExpireEnum']


class MplsTePathSelectionMetricEnum(Enum):
    """
    MplsTePathSelectionMetricEnum

    Mpls te path selection metric

    .. data:: IGP = 1

    	IGP Metric

    .. data:: TE = 2

    	TE Metric

    """

    IGP = 1

    TE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionMetricEnum']


class MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum(Enum):
    """
    MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum

    Mpls te path selection segment routing adjacency

    protection

    .. data:: NOT_SET = 0

    	Any segment can be used in a path.

    .. data:: ADJ_UNPROTECTED = 1

    	Only unprotected adjacency segments can be used

    	in a path.

    .. data:: ADJ_PROTECTED = 2

    	Only protected adjacency segments can be used

    	in a path.

    """

    NOT_SET = 0

    ADJ_UNPROTECTED = 1

    ADJ_PROTECTED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum']


class MplsTePathSelectionTiebreakerEnum(Enum):
    """
    MplsTePathSelectionTiebreakerEnum

    Mpls te path selection tiebreaker

    .. data:: MIN_FILL = 1

    	Prefer the path with the least-utilized links

    .. data:: MAX_FILL = 2

    	Prefer the path with the most-utilized links

    .. data:: RANDOM = 3

    	Prefer a path with links utilized randomly

    """

    MIN_FILL = 1

    MAX_FILL = 2

    RANDOM = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTePathSelectionTiebreakerEnum']


class MplsTeSigNameOptionEnum(Enum):
    """
    MplsTeSigNameOptionEnum

    Mpls te sig name option

    .. data:: NONE = 0

    	None

    .. data:: ADDRESS = 1

    	Address

    .. data:: NAME = 2

    	Name

    """

    NONE = 0

    ADDRESS = 1

    NAME = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeSigNameOptionEnum']


class MplsTeSwitchingCapEnum(Enum):
    """
    MplsTeSwitchingCapEnum

    Mpls te switching cap

    .. data:: PSC1 = 1

    	PSC1

    .. data:: LSC = 150

    	LSC

    .. data:: FSC = 200

    	FSC

    """

    PSC1 = 1

    LSC = 150

    FSC = 200


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeSwitchingCapEnum']


class MplsTeTunnelAffinityEnum(Enum):
    """
    MplsTeTunnelAffinityEnum

    Mpls te tunnel affinity

    .. data:: INCLUDE = 1

    	Include Affinity

    .. data:: INCLUDE_STRICT = 2

    	Strictly Include Affinity

    .. data:: EXCLUDE = 3

    	Exclude Affinity

    .. data:: EXCLUDE_ALL = 4

    	Exclude All Affinities

    .. data:: IGNORE = 5

    	Ignore Affinity

    """

    INCLUDE = 1

    INCLUDE_STRICT = 2

    EXCLUDE = 3

    EXCLUDE_ALL = 4

    IGNORE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTeTunnelAffinityEnum']


class MplsTesrlgExcludeEnum(Enum):
    """
    MplsTesrlgExcludeEnum

    Mpls tesrlg exclude

    .. data:: MANDATORY = 1

    	SRLG Mandatory Exclude

    .. data:: PREFERRED = 2

    	SRLG Preferred Exclude

    .. data:: WEIGHTED = 3

    	SRLG Weighted Exclude

    """

    MANDATORY = 1

    PREFERRED = 2

    WEIGHTED = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['MplsTesrlgExcludeEnum']


class PathInvalidationActionEnum(Enum):
    """
    PathInvalidationActionEnum

    Path invalidation action

    .. data:: TEAR = 1

    	Tear

    .. data:: DROP = 2

    	Drop

    """

    TEAR = 1

    DROP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['PathInvalidationActionEnum']


class SrPrependEnum(Enum):
    """
    SrPrependEnum

    Sr prepend

    .. data:: NONE_TYPE = 0

    	NoneType

    .. data:: NEXT_LABEL = 1

    	Next Label

    .. data:: BGP_N_HOP = 2

    	BGP NHOP

    """

    NONE_TYPE = 0

    NEXT_LABEL = 1

    BGP_N_HOP = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_datatypes as meta
        return meta._meta_table['SrPrependEnum']



