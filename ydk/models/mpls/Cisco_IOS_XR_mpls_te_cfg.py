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

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BandwidthConstraintEnum(Enum):
    """
    BandwidthConstraintEnum

    Bandwidth constraint

    .. data:: BANDWIDTH_CONSTRAINT_MAXIMUM_ALLOCATION_MODEL = 1

    	Maximum Allocation Bandwidth Constaints Model

    """

    BANDWIDTH_CONSTRAINT_MAXIMUM_ALLOCATION_MODEL = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['BandwidthConstraintEnum']


class BindingSegmentIdEnum(Enum):
    """
    BindingSegmentIdEnum

    Binding segment id

    .. data:: ANY_LABEL = 1

    	AnyLabel

    .. data:: SPECIFIED_LABEL = 2

    	SpecifiedLabel

    """

    ANY_LABEL = 1

    SPECIFIED_LABEL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['BindingSegmentIdEnum']


class GmplsttiModeEnum(Enum):
    """
    GmplsttiModeEnum

    Gmplstti mode

    .. data:: SM = 1

    	Section Monitoring

    .. data:: PM = 2

    	Path Monitoring

    .. data:: TCM = 3

    	Tandem Connection

    """

    SM = 1

    PM = 2

    TCM = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['GmplsttiModeEnum']


class IetfModeEnum(Enum):
    """
    IetfModeEnum

    Ietf mode

    .. data:: STANDARD = 3

    	IETF Standard

    """

    STANDARD = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['IetfModeEnum']


class LinkNextHopEnum(Enum):
    """
    LinkNextHopEnum

    Link next hop

    .. data:: NONE = 1

    	No next hop

    .. data:: IPV4_ADDRESS = 2

    	IPv4 next-hop address

    """

    NONE = 1

    IPV4_ADDRESS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['LinkNextHopEnum']


class MplsLcacFloodingIgpEnum(Enum):
    """
    MplsLcacFloodingIgpEnum

    Mpls lcac flooding igp

    .. data:: OSPF = 0

    	OSPF

    """

    OSPF = 0


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsLcacFloodingIgpEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeAffinityValueEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeBandwidthLimitEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeSigNameOptionEnum']


class MplsTeSignaledLabelEnum(Enum):
    """
    MplsTeSignaledLabelEnum

    Mpls te signaled label

    .. data:: NOT_SET = 0

    	Not Set

    .. data:: DWDM = 1

    	DWDM Label (RFC 6205), 50GHz channel spacing

    """

    NOT_SET = 0

    DWDM = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeSignaledLabelEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeSwitchingCapEnum']


class MplsTeSwitchingEncodeEnum(Enum):
    """
    MplsTeSwitchingEncodeEnum

    Mpls te switching encode

    .. data:: NONE = 0

    	None

    .. data:: PACKET = 1

    	Packet

    .. data:: ETHERNET = 2

    	Ethernet

    .. data:: SONDET_SDH = 5

    	SONET SDH

    """

    NONE = 0

    PACKET = 1

    ETHERNET = 2

    SONDET_SDH = 5


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeSwitchingEncodeEnum']


class MplsTeSwitchingEncodingEnum(Enum):
    """
    MplsTeSwitchingEncodingEnum

    Mpls te switching encoding

    .. data:: PACKET = 1

    	Packet

    .. data:: ETHERNET = 2

    	Ethernet

    .. data:: SONDET_SDH = 5

    	SONET SDH

    """

    PACKET = 1

    ETHERNET = 2

    SONDET_SDH = 5


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeSwitchingEncodingEnum']


class MplsTeSwitchingIndexEnum(Enum):
    """
    MplsTeSwitchingIndexEnum

    Mpls te switching index

    .. data:: LINK = 255

    	Link

    """

    LINK = 255


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTeSwitchingIndexEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTesrlgExcludeEnum']


class OspfAreaModeEnum(Enum):
    """
    OspfAreaModeEnum

    Ospf area mode

    .. data:: OSPF_INT = 0

    	OSPF area in integer format

    .. data:: OSPFIP_ADDR = 1

    	OSPF area in IP address format

    """

    OSPF_INT = 0

    OSPFIP_ADDR = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['OspfAreaModeEnum']


class OtnDestinationEnum(Enum):
    """
    OtnDestinationEnum

    Otn destination

    .. data:: UN_NUMBER_ED = 1

    	UNICAST=0

    """

    UN_NUMBER_ED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['OtnDestinationEnum']


class OtnPayloadEnum(Enum):
    """
    OtnPayloadEnum

    Otn payload

    .. data:: UNKNOWN = 0

    	Payload unknown

    .. data:: BMP = 50

    	Bmp Payload

    .. data:: GFP_F = 54

    	Gfp_F Payload

    .. data:: GMP = 55

    	GMP Payload

    .. data:: GFP_F_EXT = 70

    	Gfp_F_EXT Payload

    """

    UNKNOWN = 0

    BMP = 50

    GFP_F = 54

    GMP = 55

    GFP_F_EXT = 70


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['OtnPayloadEnum']


class OtnSignaledBandwidthEnum(Enum):
    """
    OtnSignaledBandwidthEnum

    Otn signaled bandwidth

    .. data:: ODU1 = 1

    	Signalled BW for ODU1

    .. data:: ODU2 = 2

    	Signalled BW for ODU2

    .. data:: ODU3 = 3

    	Signalled BW for ODU3

    .. data:: ODU4 = 4

    	Signalled BW for ODU4

    .. data:: ODU0 = 10

    	Signalled BW for ODU0

    .. data:: ODU2E = 11

    	Signalled BW for ODU2e

    .. data:: OD_UFLEX_CBR = 20

    	Signalled BW for ODUflex CBR

    .. data:: OD_UFLEX_GFP_RESIZE = 21

    	Signalled BW for ODUflex GFP Resizable

    .. data:: OD_UFLEX_GFP_NOT_RESIZE = 22

    	Signalled BW for ODUflex GFP not Resizable

    .. data:: ODU1E = 23

    	Signalled BW for ODU1e

    .. data:: ODU1F = 24

    	Signalled BW for ODU1f

    .. data:: ODU2F = 25

    	Signalled BW for ODU2f

    .. data:: ODU3E1 = 26

    	Signalled BW for ODU3e1

    .. data:: ODU3E2 = 27

    	Signalled BW for ODU3e2

    """

    ODU1 = 1

    ODU2 = 2

    ODU3 = 3

    ODU4 = 4

    ODU0 = 10

    ODU2E = 11

    OD_UFLEX_CBR = 20

    OD_UFLEX_GFP_RESIZE = 21

    OD_UFLEX_GFP_NOT_RESIZE = 22

    ODU1E = 23

    ODU1F = 24

    ODU2F = 25

    ODU3E1 = 26

    ODU3E2 = 27


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['OtnSignaledBandwidthEnum']


class OtnSignaledBandwidthFlexFramingEnum(Enum):
    """
    OtnSignaledBandwidthFlexFramingEnum

    Otn signaled bandwidth flex framing

    .. data:: CBR = 20

    	CBR

    .. data:: FRAMED_GFP_FIXED = 21

    	GFP fixed framing type

    .. data:: FRAMED_GFP_RESIZE = 22

    	GFP resizeable framing type

    """

    CBR = 20

    FRAMED_GFP_FIXED = 21

    FRAMED_GFP_RESIZE = 22


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['OtnSignaledBandwidthFlexFramingEnum']


class OtnStaticUniEnum(Enum):
    """
    OtnStaticUniEnum

    Otn static uni

    .. data:: UNKNOWN = 0

    	Uni-Type None

    .. data:: XC = 1

    	Uni-Type XC

    .. data:: TERMINATION = 2

    	Uni-Type Termination

    """

    UNKNOWN = 0

    XC = 1

    TERMINATION = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['OtnStaticUniEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['PathInvalidationActionEnum']


class RoutePriorityRoleEnum(Enum):
    """
    RoutePriorityRoleEnum

    Route priority role

    .. data:: ROUTE_PRIORITY_ROLE_HEAD_BACK_UP = 0

    	TE Route Priority Role Head Backup

    .. data:: ROUTE_PRIORITY_ROLE_HEAD_PRIMARY = 1

    	TE Route Priority Role Head Primary

    .. data:: ROUTE_PRIORITY_ROLE_MIDDLE = 2

    	TE Route Priority Role Middle

    """

    ROUTE_PRIORITY_ROLE_HEAD_BACK_UP = 0

    ROUTE_PRIORITY_ROLE_HEAD_PRIMARY = 1

    ROUTE_PRIORITY_ROLE_MIDDLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['RoutePriorityRoleEnum']


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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['SrPrependEnum']



class MplsTe(object):
    """
    The root of MPLS TE configuration
    
    .. attribute:: diff_serv_traffic_engineering
    
    	Configure Diff\-Serv Traffic\-Engineering
    	**type**\: :py:class:`DiffServTrafficEngineering <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.DiffServTrafficEngineering>`
    
    .. attribute:: gmpls_uni
    
    	GMPLS\-UNI configuration
    	**type**\: :py:class:`GmplsUni <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni>`
    
    .. attribute:: global_attributes
    
    	Configure MPLS TE global attributes
    	**type**\: :py:class:`GlobalAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes>`
    
    .. attribute:: transport_profile
    
    	MPLS transport profile configuration data
    	**type**\: :py:class:`TransportProfile <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile>`
    
    .. attribute:: interfaces
    
    	Configure MPLS TE interfaces
    	**type**\: :py:class:`Interfaces <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces>`
    
    .. attribute:: gmpls_nni
    
    	GMPLS\-NNI configuration
    	**type**\: :py:class:`GmplsNni <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni>`
    
    .. attribute:: lcac
    
    	LCAC specific MPLS global configuration
    	**type**\: :py:class:`Lcac <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Lcac>`
    
    .. attribute:: enable_traffic_engineering
    
    	Enable MPLS Traffic Engineering
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    

    """

    _prefix = 'mpls-te-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.diff_serv_traffic_engineering = MplsTe.DiffServTrafficEngineering()
        self.diff_serv_traffic_engineering.parent = self
        self.gmpls_uni = MplsTe.GmplsUni()
        self.gmpls_uni.parent = self
        self.global_attributes = MplsTe.GlobalAttributes()
        self.global_attributes.parent = self
        self.transport_profile = MplsTe.TransportProfile()
        self.transport_profile.parent = self
        self.interfaces = MplsTe.Interfaces()
        self.interfaces.parent = self
        self.gmpls_nni = MplsTe.GmplsNni()
        self.gmpls_nni.parent = self
        self.lcac = MplsTe.Lcac()
        self.lcac.parent = self
        self.enable_traffic_engineering = None


    class DiffServTrafficEngineering(object):
        """
        Configure Diff\-Serv Traffic\-Engineering
        
        .. attribute:: classes
        
        	Configure Diff\-Serv Traffic\-Engineering Classes
        	**type**\: :py:class:`Classes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.DiffServTrafficEngineering.Classes>`
        
        .. attribute:: bandwidth_constraint_model
        
        	Diff\-Serv Traffic\-Engineering Bandwidth Constraint Model
        	**type**\: :py:class:`BandwidthConstraintEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.BandwidthConstraintEnum>`
        
        .. attribute:: mode_ietf
        
        	Diff\-Serv Traffic\-Engineering IETF mode
        	**type**\: :py:class:`IetfModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.IetfModeEnum>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.classes = MplsTe.DiffServTrafficEngineering.Classes()
            self.classes.parent = self
            self.bandwidth_constraint_model = None
            self.mode_ietf = None


        class Classes(object):
            """
            Configure Diff\-Serv Traffic\-Engineering Classes
            
            .. attribute:: class_
            
            	DSTE class number
            	**type**\: list of :py:class:`Class <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.DiffServTrafficEngineering.Classes.Class>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.class_ = YList()
                self.class_.parent = self
                self.class_.name = 'class_'


            class Class(object):
                """
                DSTE class number
                
                .. attribute:: class_number  <key>
                
                	DS\-TE class number
                	**type**\: int
                
                	**range:** 0..7
                
                .. attribute:: class_type
                
                	Class type number
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: class_priority
                
                	Class\-type priority
                	**type**\: int
                
                	**range:** 0..7
                
                .. attribute:: unused
                
                	TRUE to skip classtype and class priority provisioning FALSE to provision them
                	**type**\: bool
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.class_number = None
                    self.class_type = None
                    self.class_priority = None
                    self.unused = None

                @property
                def _common_path(self):
                    if self.class_number is None:
                        raise YPYDataValidationError('Key property class_number is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:diff-serv-traffic-engineering/Cisco-IOS-XR-mpls-te-cfg:classes/Cisco-IOS-XR-mpls-te-cfg:class[Cisco-IOS-XR-mpls-te-cfg:class-number = ' + str(self.class_number) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.class_number is not None:
                        return True

                    if self.class_type is not None:
                        return True

                    if self.class_priority is not None:
                        return True

                    if self.unused is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.DiffServTrafficEngineering.Classes.Class']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:diff-serv-traffic-engineering/Cisco-IOS-XR-mpls-te-cfg:classes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.class_ is not None:
                    for child_ref in self.class_:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.DiffServTrafficEngineering.Classes']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:diff-serv-traffic-engineering'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.classes is not None and self.classes._has_data():
                return True

            if self.bandwidth_constraint_model is not None:
                return True

            if self.mode_ietf is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.DiffServTrafficEngineering']['meta_info']


    class GmplsUni(object):
        """
        GMPLS\-UNI configuration
        
        .. attribute:: timers
        
        	GMPLS\-UNI timer configuration
        	**type**\: :py:class:`Timers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Timers>`
        
        .. attribute:: controllers
        
        	GMPLS\-UNI controllers
        	**type**\: :py:class:`Controllers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.timers = MplsTe.GmplsUni.Timers()
            self.timers.parent = self
            self.controllers = MplsTe.GmplsUni.Controllers()
            self.controllers.parent = self


        class Timers(object):
            """
            GMPLS\-UNI timer configuration
            
            .. attribute:: path_option_timers
            
            	GMPLS\-UNI path\-option timer configuration
            	**type**\: :py:class:`PathOptionTimers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Timers.PathOptionTimers>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path_option_timers = MplsTe.GmplsUni.Timers.PathOptionTimers()
                self.path_option_timers.parent = self


            class PathOptionTimers(object):
                """
                GMPLS\-UNI path\-option timer configuration
                
                .. attribute:: holddown
                
                	GMPLS\-UNI path\-option holddown timer configuration
                	**type**\: :py:class:`Holddown <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.holddown = MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown()
                    self.holddown.parent = self


                class Holddown(object):
                    """
                    GMPLS\-UNI path\-option holddown timer
                    configuration
                    
                    .. attribute:: minimum
                    
                    	Minimum holddown (seconds)
                    	**type**\: int
                    
                    	**range:** 5..3600
                    
                    .. attribute:: maximum
                    
                    	Maximum holddown (seconds)
                    	**type**\: int
                    
                    	**range:** 5..3600
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.minimum = None
                        self.maximum = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-uni/Cisco-IOS-XR-mpls-te-cfg:timers/Cisco-IOS-XR-mpls-te-cfg:path-option-timers/Cisco-IOS-XR-mpls-te-cfg:holddown'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.minimum is not None:
                            return True

                        if self.maximum is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsUni.Timers.PathOptionTimers.Holddown']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-uni/Cisco-IOS-XR-mpls-te-cfg:timers/Cisco-IOS-XR-mpls-te-cfg:path-option-timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.holddown is not None and self.holddown._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GmplsUni.Timers.PathOptionTimers']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-uni/Cisco-IOS-XR-mpls-te-cfg:timers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.path_option_timers is not None and self.path_option_timers._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GmplsUni.Timers']['meta_info']


        class Controllers(object):
            """
            GMPLS\-UNI controllers
            
            .. attribute:: controller
            
            	Configure a GMPLS controller
            	**type**\: list of :py:class:`Controller <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.controller = YList()
                self.controller.parent = self
                self.controller.name = 'controller'


            class Controller(object):
                """
                Configure a GMPLS controller
                
                .. attribute:: controller_name  <key>
                
                	Controller name
                	**type**\: str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: announce
                
                	Announce discovered tunnel properties to system
                	**type**\: :py:class:`Announce <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.Announce>`
                
                .. attribute:: controller_logging
                
                	Controller logging
                	**type**\: :py:class:`ControllerLogging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.ControllerLogging>`
                
                .. attribute:: gmpls_unitunnel_head
                
                	GMPLS\-UNI tunnel\-head properties
                	**type**\: :py:class:`GmplsUnitunnelHead <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead>`
                
                .. attribute:: enable
                
                	Enable GMPLS\-UNI on the link
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.controller_name = None
                    self.announce = MplsTe.GmplsUni.Controllers.Controller.Announce()
                    self.announce.parent = self
                    self.controller_logging = MplsTe.GmplsUni.Controllers.Controller.ControllerLogging()
                    self.controller_logging.parent = self
                    self.gmpls_unitunnel_head = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead()
                    self.gmpls_unitunnel_head.parent = self
                    self.enable = None


                class Announce(object):
                    """
                    Announce discovered tunnel properties to
                    system
                    
                    .. attribute:: srl_gs
                    
                    	Enable announcement of discovered SRLGs
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.srl_gs = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:announce'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.srl_gs is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.Announce']['meta_info']


                class ControllerLogging(object):
                    """
                    Controller logging
                    
                    .. attribute:: discovered_srlg_change_logging
                    
                    	Enable logging of changes to of discovered SRLGs
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.discovered_srlg_change_logging = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:controller-logging'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.discovered_srlg_change_logging is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.ControllerLogging']['meta_info']


                class GmplsUnitunnelHead(object):
                    """
                    GMPLS\-UNI tunnel\-head properties
                    
                    .. attribute:: path_options
                    
                    	Path\-option configuration
                    	**type**\: :py:class:`PathOptions <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions>`
                    
                    .. attribute:: recording
                    
                    	Tunnel property recording
                    	**type**\: :py:class:`Recording <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording>`
                    
                    .. attribute:: logging
                    
                    	Tunnel event logging
                    	**type**\: :py:class:`Logging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging>`
                    
                    .. attribute:: tunnel_id
                    
                    	GMPLS\-UNI head tunnel\-id
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: enable
                    
                    	Set link as a GMPLS tunnel head
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: destination
                    
                    	Set the destination of the tunnel
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\: :py:class:`Priority <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: signalled_name
                    
                    	The name of the tunnel to be included in signalling messages
                    	**type**\: str
                    
                    	**range:** 0..254
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.path_options = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions()
                        self.path_options.parent = self
                        self.recording = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording()
                        self.recording.parent = self
                        self.logging = MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging()
                        self.logging.parent = self
                        self.tunnel_id = None
                        self.enable = None
                        self.destination = None
                        self.priority = None
                        self.record_route = None
                        self.signalled_name = None


                    class PathOptions(object):
                        """
                        Path\-option configuration
                        
                        .. attribute:: path_option
                        
                        	A Path\-option
                        	**type**\: list of :py:class:`PathOption <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path_option = YList()
                            self.path_option.parent = self
                            self.path_option.name = 'path_option'


                        class PathOption(object):
                            """
                            A Path\-option
                            
                            .. attribute:: preference_level  <key>
                            
                            	Preference level for this path option
                            	**type**\: int
                            
                            	**range:** 1..1000
                            
                            .. attribute:: path_type
                            
                            	The type of the path option
                            	**type**\: :py:class:`MplsTePathOptionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionEnum>`
                            
                            .. attribute:: path_id
                            
                            	The ID of the explicit path associated with this option
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: path_name
                            
                            	The name of the explicit path associated with this option
                            	**type**\: str
                            
                            .. attribute:: xro_type
                            
                            	The route\-exclusion type
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: xro_attribute_set_name
                            
                            	The name of the XRO attribute set to be used for this path\-option
                            	**type**\: str
                            
                            	**range:** 0..64
                            
                            .. attribute:: lockdown
                            
                            	Path option properties\: must be Lockdown
                            	**type**\: :py:class:`MplsTePathOptionPropertyEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionPropertyEnum>`
                            
                            .. attribute:: verbatim
                            
                            	Path option properties\: must be verbatim if set
                            	**type**\: :py:class:`MplsTePathOptionPropertyEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionPropertyEnum>`
                            
                            .. attribute:: signaled_label
                            
                            	Signaled label type
                            	**type**\: :py:class:`MplsTeSignaledLabelEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeSignaledLabelEnum>`
                            
                            .. attribute:: dwdm_channel
                            
                            	DWDM channel number
                            	**type**\: int
                            
                            	**range:** 1..89
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.preference_level = None
                                self.path_type = None
                                self.path_id = None
                                self.path_name = None
                                self.xro_type = None
                                self.xro_attribute_set_name = None
                                self.lockdown = None
                                self.verbatim = None
                                self.signaled_label = None
                                self.dwdm_channel = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.preference_level is None:
                                    raise YPYDataValidationError('Key property preference_level is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-option[Cisco-IOS-XR-mpls-te-cfg:preference-level = ' + str(self.preference_level) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.preference_level is not None:
                                    return True

                                if self.path_type is not None:
                                    return True

                                if self.path_id is not None:
                                    return True

                                if self.path_name is not None:
                                    return True

                                if self.xro_type is not None:
                                    return True

                                if self.xro_attribute_set_name is not None:
                                    return True

                                if self.lockdown is not None:
                                    return True

                                if self.verbatim is not None:
                                    return True

                                if self.signaled_label is not None:
                                    return True

                                if self.dwdm_channel is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions.PathOption']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.path_option is not None:
                                for child_ref in self.path_option:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.PathOptions']['meta_info']


                    class Recording(object):
                        """
                        Tunnel property recording
                        
                        .. attribute:: srlg
                        
                        	Enable SRLG\-recording during signaling
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.srlg = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:recording'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.srlg is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Recording']['meta_info']


                    class Logging(object):
                        """
                        Tunnel event logging
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.state_message = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:logging'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.state_message is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Logging']['meta_info']


                    class Priority(object):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.setup_priority = None
                            self.hold_priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:priority'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.setup_priority is not None:
                                return True

                            if self.hold_priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead.Priority']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:gmpls-unitunnel-head'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.path_options is not None and self.path_options._has_data():
                            return True

                        if self.recording is not None and self.recording._has_data():
                            return True

                        if self.logging is not None and self.logging._has_data():
                            return True

                        if self.tunnel_id is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.destination is not None:
                            return True

                        if self.priority is not None and self.priority._has_data():
                            return True

                        if self.record_route is not None:
                            return True

                        if self.signalled_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller.GmplsUnitunnelHead']['meta_info']

                @property
                def _common_path(self):
                    if self.controller_name is None:
                        raise YPYDataValidationError('Key property controller_name is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-uni/Cisco-IOS-XR-mpls-te-cfg:controllers/Cisco-IOS-XR-mpls-te-cfg:controller[Cisco-IOS-XR-mpls-te-cfg:controller-name = ' + str(self.controller_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.controller_name is not None:
                        return True

                    if self.announce is not None and self.announce._has_data():
                        return True

                    if self.controller_logging is not None and self.controller_logging._has_data():
                        return True

                    if self.gmpls_unitunnel_head is not None and self.gmpls_unitunnel_head._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GmplsUni.Controllers.Controller']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-uni/Cisco-IOS-XR-mpls-te-cfg:controllers'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.controller is not None:
                    for child_ref in self.controller:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GmplsUni.Controllers']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-uni'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.timers is not None and self.timers._has_data():
                return True

            if self.controllers is not None and self.controllers._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.GmplsUni']['meta_info']


    class GlobalAttributes(object):
        """
        Configure MPLS TE global attributes
        
        .. attribute:: path_selection_loose_affinities
        
        	Path selection Loose ERO Affinity Class configuration
        	**type**\: :py:class:`PathSelectionLooseAffinities <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelectionLooseAffinities>`
        
        .. attribute:: auto_tunnel
        
        	Configure auto\-tunnels feature
        	**type**\: :py:class:`AutoTunnel <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel>`
        
        .. attribute:: secondary_router_ids
        
        	Configure MPLS TE Secondary Router ID
        	**type**\: :py:class:`SecondaryRouterIds <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.SecondaryRouterIds>`
        
        .. attribute:: srlg
        
        	Configure SRLG values and MPLS\-TE properties
        	**type**\: :py:class:`Srlg <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg>`
        
        .. attribute:: queues
        
        	Configure MPLS TE route priority
        	**type**\: :py:class:`Queues <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Queues>`
        
        .. attribute:: path_selection_loose_metrics
        
        	Path selection Loose ERO Metric Class configuration
        	**type**\: :py:class:`PathSelectionLooseMetrics <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelectionLooseMetrics>`
        
        .. attribute:: mib
        
        	MPLS\-TE MIB properties
        	**type**\: :py:class:`Mib <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Mib>`
        
        .. attribute:: attribute_set
        
        	Attribute AttributeSets
        	**type**\: :py:class:`AttributeSet <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet>`
        
        .. attribute:: bfd_over_lsp
        
        	BFD over MPLS TE Global Configurations
        	**type**\: :py:class:`BfdOverLsp <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BfdOverLsp>`
        
        .. attribute:: pce_attributes
        
        	Configuration MPLS TE PCE attributes
        	**type**\: :py:class:`PceAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes>`
        
        .. attribute:: soft_preemption
        
        	Soft preemption configuration data
        	**type**\: :py:class:`SoftPreemption <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.SoftPreemption>`
        
        .. attribute:: path_invalidation
        
        	Path invalidation configuration for all tunnels
        	**type**\: :py:class:`PathInvalidation <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathInvalidation>`
        
        .. attribute:: fast_reroute
        
        	Configure fast reroute attributes
        	**type**\: :py:class:`FastReroute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.FastReroute>`
        
        .. attribute:: path_selection_ignore_overload_role
        
        	Path selection to ignore overload node during CSPF
        	**type**\: :py:class:`PathSelectionIgnoreOverloadRole <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole>`
        
        .. attribute:: affinity_mappings
        
        	Affinity Mapping Table configuration
        	**type**\: :py:class:`AffinityMappings <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AffinityMappings>`
        
        .. attribute:: log_nsr_status
        
        	Log NSR status messages
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: path_selection_tiebreaker
        
        	CSPF tiebreaker to use in path calculation
        	**type**\: :py:class:`MplsTePathSelectionTiebreakerEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionTiebreakerEnum>`
        
        .. attribute:: log_issu_status
        
        	Log ISSU status messages
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: reoptimize_link_up
        
        	Enable reoptimization based on link\-up events
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: reoptimize_delay_cleanup_timer
        
        	Reoptimization Delay Cleanup Value (seconds)
        	**type**\: int
        
        	**range:** 0..300
        
        .. attribute:: disable_reoptimize_affinity_failure
        
        	Disable reoptimization after affinity failures
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: maximum_tunnels
        
        	The maximum number of tunnel heads that will be allowed
        	**type**\: int
        
        	**range:** 1..65536
        
        .. attribute:: link_holddown_timer
        
        	Holddown time for links which had Path Errors in seconds
        	**type**\: int
        
        	**range:** 0..300
        
        .. attribute:: path_selection_metric
        
        	Metric to use in path calculation
        	**type**\: :py:class:`MplsTePathSelectionMetricEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetricEnum>`
        
        .. attribute:: fault_oam
        
        	Enable Fault\-OAM functionality for bidirectional tunnels
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: enable_unequal_load_balancing
        
        	Enable unequal load\-balancing over tunnels to the same destination
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: log_tail
        
        	Log all tail tunnel events
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: reoptimize_delay_after_frr_timer
        
        	Reoptimization Delay After FRR Value (seconds)
        	**type**\: int
        
        	**range:** 0..120
        
        .. attribute:: auto_bandwidth_collect_frequency
        
        	Auto\-bandwidth global collection frequency in minutes
        	**type**\: int
        
        	**range:** 1..10080
        
        .. attribute:: reopt_delay_path_protect_switchover_timer
        
        	Seconds between path protect switchover and tunnel re\-optimization. Set to 0 to disable
        	**type**\: int
        
        	**range:** 0..604800
        
        .. attribute:: log_all
        
        	Always set to true
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: loose_path_retry_period
        
        	Signalling retry for tunnels terminating outside the headend area
        	**type**\: int
        
        	**range:** 30..600
        
        .. attribute:: reoptimize_load_balancing
        
        	Load balance bandwidth during reoptimization
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: log_head
        
        	Log all head tunnel events
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: path_selection_ignore_overload
        
        	Deprecated \- do not use
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: graceful_preemption_on_bandwidth_reduction
        
        	Enable graceful preemption when there is a bandwidth reduction
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: advertise_explicit_nulls
        
        	Enable explicit\-null advertising to PHOP
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: reoptimize_delay_install_timer
        
        	Reoptimization Delay Install Value (seconds)
        	**type**\: int
        
        	**range:** 0..3600
        
        .. attribute:: reoptimize_delay_after_affinity_failure_timer
        
        	Delay reoptimizing current LSP after affinity failures
        	**type**\: int
        
        	**range:** 1..604800
        
        .. attribute:: log_frr_protection
        
        	Log FRR Protection messages
        	**type**\: :py:class:`MplsTeLogFrrProtectionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeLogFrrProtectionEnum>`
        
        .. attribute:: reoptimize_timer_frequency
        
        	Reoptimize timers period in seconds
        	**type**\: int
        
        	**range:** 0..604800
        
        .. attribute:: log_mid
        
        	Log all mid tunnel events
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: log_preemption
        
        	Log tunnel preemption messages
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        .. attribute:: path_selection_cost_limit
        
        	Path selection cost limit configuration for all tunnels
        	**type**\: int
        
        	**range:** 1..4294967295
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.path_selection_loose_affinities = MplsTe.GlobalAttributes.PathSelectionLooseAffinities()
            self.path_selection_loose_affinities.parent = self
            self.auto_tunnel = MplsTe.GlobalAttributes.AutoTunnel()
            self.auto_tunnel.parent = self
            self.secondary_router_ids = MplsTe.GlobalAttributes.SecondaryRouterIds()
            self.secondary_router_ids.parent = self
            self.srlg = MplsTe.GlobalAttributes.Srlg()
            self.srlg.parent = self
            self.queues = MplsTe.GlobalAttributes.Queues()
            self.queues.parent = self
            self.path_selection_loose_metrics = MplsTe.GlobalAttributes.PathSelectionLooseMetrics()
            self.path_selection_loose_metrics.parent = self
            self.mib = MplsTe.GlobalAttributes.Mib()
            self.mib.parent = self
            self.attribute_set = MplsTe.GlobalAttributes.AttributeSet()
            self.attribute_set.parent = self
            self.bfd_over_lsp = MplsTe.GlobalAttributes.BfdOverLsp()
            self.bfd_over_lsp.parent = self
            self.pce_attributes = MplsTe.GlobalAttributes.PceAttributes()
            self.pce_attributes.parent = self
            self.soft_preemption = MplsTe.GlobalAttributes.SoftPreemption()
            self.soft_preemption.parent = self
            self.path_invalidation = MplsTe.GlobalAttributes.PathInvalidation()
            self.path_invalidation.parent = self
            self.fast_reroute = MplsTe.GlobalAttributes.FastReroute()
            self.fast_reroute.parent = self
            self.path_selection_ignore_overload_role = MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole()
            self.path_selection_ignore_overload_role.parent = self
            self.affinity_mappings = MplsTe.GlobalAttributes.AffinityMappings()
            self.affinity_mappings.parent = self
            self.log_nsr_status = None
            self.path_selection_tiebreaker = None
            self.log_issu_status = None
            self.reoptimize_link_up = None
            self.reoptimize_delay_cleanup_timer = None
            self.disable_reoptimize_affinity_failure = None
            self.maximum_tunnels = None
            self.link_holddown_timer = None
            self.path_selection_metric = None
            self.fault_oam = None
            self.enable_unequal_load_balancing = None
            self.log_tail = None
            self.reoptimize_delay_after_frr_timer = None
            self.auto_bandwidth_collect_frequency = None
            self.reopt_delay_path_protect_switchover_timer = None
            self.log_all = None
            self.loose_path_retry_period = None
            self.reoptimize_load_balancing = None
            self.log_head = None
            self.path_selection_ignore_overload = None
            self.graceful_preemption_on_bandwidth_reduction = None
            self.advertise_explicit_nulls = None
            self.reoptimize_delay_install_timer = None
            self.reoptimize_delay_after_affinity_failure_timer = None
            self.log_frr_protection = None
            self.reoptimize_timer_frequency = None
            self.log_mid = None
            self.log_preemption = None
            self.path_selection_cost_limit = None


        class PathSelectionLooseAffinities(object):
            """
            Path selection Loose ERO Affinity Class
            configuration
            
            .. attribute:: path_selection_loose_affinity
            
            	Path selection Loose ERO Affinity configuration
            	**type**\: list of :py:class:`PathSelectionLooseAffinity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelectionLooseAffinities.PathSelectionLooseAffinity>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path_selection_loose_affinity = YList()
                self.path_selection_loose_affinity.parent = self
                self.path_selection_loose_affinity.name = 'path_selection_loose_affinity'


            class PathSelectionLooseAffinity(object):
                """
                Path selection Loose ERO Affinity
                configuration
                
                .. attribute:: class_type  <key>
                
                	Path Selection class Type
                	**type**\: int
                
                	**range:** 0..7
                
                .. attribute:: affinity
                
                	Affinity flags
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: mask
                
                	Affinity mask
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.class_type = None
                    self.affinity = None
                    self.mask = None

                @property
                def _common_path(self):
                    if self.class_type is None:
                        raise YPYDataValidationError('Key property class_type is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:path-selection-loose-affinities/Cisco-IOS-XR-mpls-te-cfg:path-selection-loose-affinity[Cisco-IOS-XR-mpls-te-cfg:class-type = ' + str(self.class_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.class_type is not None:
                        return True

                    if self.affinity is not None:
                        return True

                    if self.mask is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.PathSelectionLooseAffinities.PathSelectionLooseAffinity']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:path-selection-loose-affinities'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.path_selection_loose_affinity is not None:
                    for child_ref in self.path_selection_loose_affinity:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.PathSelectionLooseAffinities']['meta_info']


        class AutoTunnel(object):
            """
            Configure auto\-tunnels feature
            
            .. attribute:: pcc
            
            	Configure auto\-tunnel PCC (Path Computation Client) feature
            	**type**\: :py:class:`Pcc <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Pcc>`
            
            .. attribute:: p2p_auto_tunnel
            
            	Configure P2P auto\-tunnel feature
            	**type**\: :py:class:`P2PAutoTunnel <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel>`
            
            .. attribute:: backup
            
            	Configure auto\-tunnel backup feature
            	**type**\: :py:class:`Backup <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup>`
            
            .. attribute:: mesh
            
            	Configure auto\-tunnel mesh feature
            	**type**\: :py:class:`Mesh <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh>`
            
            .. attribute:: p2mp_auto_tunnel
            
            	Configure P2MP auto\-tunnel feature
            	**type**\: :py:class:`P2MpAutoTunnel <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.pcc = MplsTe.GlobalAttributes.AutoTunnel.Pcc()
                self.pcc.parent = self
                self.p2p_auto_tunnel = MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel()
                self.p2p_auto_tunnel.parent = self
                self.backup = MplsTe.GlobalAttributes.AutoTunnel.Backup()
                self.backup.parent = self
                self.mesh = MplsTe.GlobalAttributes.AutoTunnel.Mesh()
                self.mesh.parent = self
                self.p2mp_auto_tunnel = MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel()
                self.p2mp_auto_tunnel.parent = self


            class Pcc(object):
                """
                Configure auto\-tunnel PCC (Path Computation
                Client) feature
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\: :py:class:`TunnelRange <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange()
                    self.tunnel_range.parent = self


                class TunnelRange(object):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.min_tunnel_id = None
                        self.max_tunnel_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:pcc/Cisco-IOS-XR-mpls-te-cfg:tunnel-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.min_tunnel_id is not None:
                            return True

                        if self.max_tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Pcc.TunnelRange']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:pcc'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tunnel_range is not None and self.tunnel_range._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Pcc']['meta_info']


            class P2PAutoTunnel(object):
                """
                Configure P2P auto\-tunnel feature
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\: :py:class:`TunnelRange <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange()
                    self.tunnel_range.parent = self


                class TunnelRange(object):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.min_tunnel_id = None
                        self.max_tunnel_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:p2p-auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:tunnel-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.min_tunnel_id is not None:
                            return True

                        if self.max_tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel.TunnelRange']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:p2p-auto-tunnel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tunnel_range is not None and self.tunnel_range._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2PAutoTunnel']['meta_info']


            class Backup(object):
                """
                Configure auto\-tunnel backup feature
                
                .. attribute:: affinity_ignore
                
                	Ignore affinity during CSPF for auto backup tunnels
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: timers
                
                	Configure auto\-tunnel backup timers value
                	**type**\: :py:class:`Timers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers>`
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\: :py:class:`TunnelRange <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.affinity_ignore = None
                    self.timers = MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers()
                    self.timers.parent = self
                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange()
                    self.tunnel_range.parent = self


                class Timers(object):
                    """
                    Configure auto\-tunnel backup timers value
                    
                    .. attribute:: removal
                    
                    	Configure auto\-tunnel backup removal timers value
                    	**type**\: :py:class:`Removal <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.removal = MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal()
                        self.removal.parent = self


                    class Removal(object):
                        """
                        Configure auto\-tunnel backup removal timers
                        value
                        
                        .. attribute:: unused
                        
                        	Auto\-tunnel backup unused timeout in minutes (0=never timeout)
                        	**type**\: int
                        
                        	**range:** 0..10080
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.unused = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:backup/Cisco-IOS-XR-mpls-te-cfg:timers/Cisco-IOS-XR-mpls-te-cfg:removal'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.unused is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers.Removal']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:backup/Cisco-IOS-XR-mpls-te-cfg:timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.removal is not None and self.removal._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.Timers']['meta_info']


                class TunnelRange(object):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.min_tunnel_id = None
                        self.max_tunnel_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:backup/Cisco-IOS-XR-mpls-te-cfg:tunnel-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.min_tunnel_id is not None:
                            return True

                        if self.max_tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup.TunnelRange']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:backup'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.affinity_ignore is not None:
                        return True

                    if self.timers is not None and self.timers._has_data():
                        return True

                    if self.tunnel_range is not None and self.tunnel_range._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Backup']['meta_info']


            class Mesh(object):
                """
                Configure auto\-tunnel mesh feature
                
                .. attribute:: mesh_groups
                
                	Configure auto\-tunnel mesh group
                	**type**\: :py:class:`MeshGroups <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups>`
                
                .. attribute:: timers
                
                	Configure auto\-tunnel backup timers value
                	**type**\: :py:class:`Timers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers>`
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\: :py:class:`TunnelRange <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.mesh_groups = MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups()
                    self.mesh_groups.parent = self
                    self.timers = MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers()
                    self.timers.parent = self
                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange()
                    self.tunnel_range.parent = self


                class MeshGroups(object):
                    """
                    Configure auto\-tunnel mesh group
                    
                    .. attribute:: mesh_group
                    
                    	Auto\-mesh group identifier
                    	**type**\: list of :py:class:`MeshGroup <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.mesh_group = YList()
                        self.mesh_group.parent = self
                        self.mesh_group.name = 'mesh_group'


                    class MeshGroup(object):
                        """
                        Auto\-mesh group identifier
                        
                        .. attribute:: mesh_group_id  <key>
                        
                        	Mesh group ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: destination_list
                        
                        	The name of prefix\-list to be applied to this destination\-list
                        	**type**\: str
                        
                        	**range:** 0..32
                        
                        .. attribute:: disable
                        
                        	Disables mesh group
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: attribute_set
                        
                        	The name of auto\-mesh attribute set to be applied to this group
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: create
                        
                        	Auto\-mesh group enable object that controls whether this group is configured or not .This object must be set before other configuration supplied for this group
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: one_hop
                        
                        	Automatically create tunnel to all next\-hops
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.mesh_group_id = None
                            self.destination_list = None
                            self.disable = None
                            self.attribute_set = None
                            self.create = None
                            self.one_hop = None

                        @property
                        def _common_path(self):
                            if self.mesh_group_id is None:
                                raise YPYDataValidationError('Key property mesh_group_id is None')

                            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:mesh/Cisco-IOS-XR-mpls-te-cfg:mesh-groups/Cisco-IOS-XR-mpls-te-cfg:mesh-group[Cisco-IOS-XR-mpls-te-cfg:mesh-group-id = ' + str(self.mesh_group_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.mesh_group_id is not None:
                                return True

                            if self.destination_list is not None:
                                return True

                            if self.disable is not None:
                                return True

                            if self.attribute_set is not None:
                                return True

                            if self.create is not None:
                                return True

                            if self.one_hop is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups.MeshGroup']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:mesh/Cisco-IOS-XR-mpls-te-cfg:mesh-groups'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.mesh_group is not None:
                            for child_ref in self.mesh_group:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.MeshGroups']['meta_info']


                class Timers(object):
                    """
                    Configure auto\-tunnel backup timers value
                    
                    .. attribute:: removal
                    
                    	Configure auto\-tunnel backup removal timers value
                    	**type**\: :py:class:`Removal <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.removal = MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal()
                        self.removal.parent = self


                    class Removal(object):
                        """
                        Configure auto\-tunnel backup removal timers
                        value
                        
                        .. attribute:: unused
                        
                        	Auto\-tunnel backup unused timeout in minutes (0=never timeout)
                        	**type**\: int
                        
                        	**range:** 0..10080
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.unused = None

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:mesh/Cisco-IOS-XR-mpls-te-cfg:timers/Cisco-IOS-XR-mpls-te-cfg:removal'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.unused is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers.Removal']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:mesh/Cisco-IOS-XR-mpls-te-cfg:timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.removal is not None and self.removal._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.Timers']['meta_info']


                class TunnelRange(object):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.min_tunnel_id = None
                        self.max_tunnel_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:mesh/Cisco-IOS-XR-mpls-te-cfg:tunnel-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.min_tunnel_id is not None:
                            return True

                        if self.max_tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh.TunnelRange']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:mesh'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.mesh_groups is not None and self.mesh_groups._has_data():
                        return True

                    if self.timers is not None and self.timers._has_data():
                        return True

                    if self.tunnel_range is not None and self.tunnel_range._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.Mesh']['meta_info']


            class P2MpAutoTunnel(object):
                """
                Configure P2MP auto\-tunnel feature
                
                .. attribute:: tunnel_range
                
                	Configure tunnel ID range for auto\-tunnel features
                	**type**\: :py:class:`TunnelRange <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tunnel_range = MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange()
                    self.tunnel_range.parent = self


                class TunnelRange(object):
                    """
                    Configure tunnel ID range for auto\-tunnel
                    features
                    
                    .. attribute:: min_tunnel_id
                    
                    	Minimum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: max_tunnel_id
                    
                    	Maximum tunnel ID for auto\-tunnels
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.min_tunnel_id = None
                        self.max_tunnel_id = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:p2mp-auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:tunnel-range'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.min_tunnel_id is not None:
                            return True

                        if self.max_tunnel_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel.TunnelRange']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel/Cisco-IOS-XR-mpls-te-cfg:p2mp-auto-tunnel'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tunnel_range is not None and self.tunnel_range._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel.P2MpAutoTunnel']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.pcc is not None and self.pcc._has_data():
                    return True

                if self.p2p_auto_tunnel is not None and self.p2p_auto_tunnel._has_data():
                    return True

                if self.backup is not None and self.backup._has_data():
                    return True

                if self.mesh is not None and self.mesh._has_data():
                    return True

                if self.p2mp_auto_tunnel is not None and self.p2mp_auto_tunnel._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.AutoTunnel']['meta_info']


        class SecondaryRouterIds(object):
            """
            Configure MPLS TE Secondary Router ID
            
            .. attribute:: secondary_router_id
            
            	Secondary Router ID
            	**type**\: list of :py:class:`SecondaryRouterId <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.secondary_router_id = YList()
                self.secondary_router_id.parent = self
                self.secondary_router_id.name = 'secondary_router_id'


            class SecondaryRouterId(object):
                """
                Secondary Router ID
                
                .. attribute:: secondary_router_id_value  <key>
                
                	Secondary TE Router ID
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.secondary_router_id_value = None

                @property
                def _common_path(self):
                    if self.secondary_router_id_value is None:
                        raise YPYDataValidationError('Key property secondary_router_id_value is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:secondary-router-ids/Cisco-IOS-XR-mpls-te-cfg:secondary-router-id[Cisco-IOS-XR-mpls-te-cfg:secondary-router-id-value = ' + str(self.secondary_router_id_value) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.secondary_router_id_value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds.SecondaryRouterId']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:secondary-router-ids'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.secondary_router_id is not None:
                    for child_ref in self.secondary_router_id:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.SecondaryRouterIds']['meta_info']


        class Srlg(object):
            """
            Configure SRLG values and MPLS\-TE properties
            
            .. attribute:: names
            
            	Configure SRLG identified by names
            	**type**\: :py:class:`Names <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Names>`
            
            .. attribute:: values
            
            	Configure SRLG values and MPLS\-TE properties
            	**type**\: :py:class:`Values <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Values>`
            
            .. attribute:: default_admin_weight
            
            	Default Admin weight any SRLG value that does not have one
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: enable
            
            	Enter SRLG property configuration
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.names = MplsTe.GlobalAttributes.Srlg.Names()
                self.names.parent = self
                self.values = MplsTe.GlobalAttributes.Srlg.Values()
                self.values.parent = self
                self.default_admin_weight = None
                self.enable = None


            class Names(object):
                """
                Configure SRLG identified by names
                
                .. attribute:: name
                
                	SRLG name and its MPLS\-TE properties
                	**type**\: list of :py:class:`Name <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Names.Name>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = YList()
                    self.name.parent = self
                    self.name.name = 'name'


                class Name(object):
                    """
                    SRLG name and its MPLS\-TE properties
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG membership name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: admin_weight
                    
                    	Administrative weight for the SRLG value
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.srlg_name = None
                        self.admin_weight = None

                    @property
                    def _common_path(self):
                        if self.srlg_name is None:
                            raise YPYDataValidationError('Key property srlg_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:srlg/Cisco-IOS-XR-mpls-te-cfg:names/Cisco-IOS-XR-mpls-te-cfg:name[Cisco-IOS-XR-mpls-te-cfg:srlg-name = ' + str(self.srlg_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.srlg_name is not None:
                            return True

                        if self.admin_weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.Srlg.Names.Name']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:srlg/Cisco-IOS-XR-mpls-te-cfg:names'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.name is not None:
                        for child_ref in self.name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.Srlg.Names']['meta_info']


            class Values(object):
                """
                Configure SRLG values and MPLS\-TE properties
                
                .. attribute:: value
                
                	SRLG value and its MPLS\-TE properties
                	**type**\: list of :py:class:`Value <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Values.Value>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.value = YList()
                    self.value.parent = self
                    self.value.name = 'value'


                class Value(object):
                    """
                    SRLG value and its MPLS\-TE properties
                    
                    .. attribute:: srlg_number  <key>
                    
                    	SRLG membership number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_address_maps
                    
                    	Configure outgoing and remote link addresses for a given SRLG value
                    	**type**\: :py:class:`Ipv4AddressMaps <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps>`
                    
                    .. attribute:: admin_weight
                    
                    	Administrative weight for the SRLG value
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.srlg_number = None
                        self.ipv4_address_maps = MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps()
                        self.ipv4_address_maps.parent = self
                        self.admin_weight = None


                    class Ipv4AddressMaps(object):
                        """
                        Configure outgoing and remote link addresses
                        for a given SRLG value
                        
                        .. attribute:: ipv4_address_map
                        
                        	A mapping of the remote and local addresses of a link to an SRLG value
                        	**type**\: list of :py:class:`Ipv4AddressMap <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.ipv4_address_map = YList()
                            self.ipv4_address_map.parent = self
                            self.ipv4_address_map.name = 'ipv4_address_map'


                        class Ipv4AddressMap(object):
                            """
                            A mapping of the remote and local addresses
                            of a link to an SRLG value
                            
                            .. attribute:: outgoing_ipv4_address  <key>
                            
                            	Outgoing v4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: remote_ipv4_address  <key>
                            
                            	Remote v4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.outgoing_ipv4_address = None
                                self.remote_ipv4_address = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.outgoing_ipv4_address is None:
                                    raise YPYDataValidationError('Key property outgoing_ipv4_address is None')
                                if self.remote_ipv4_address is None:
                                    raise YPYDataValidationError('Key property remote_ipv4_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:ipv4-address-map[Cisco-IOS-XR-mpls-te-cfg:outgoing-ipv4-address = ' + str(self.outgoing_ipv4_address) + '][Cisco-IOS-XR-mpls-te-cfg:remote-ipv4-address = ' + str(self.remote_ipv4_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.outgoing_ipv4_address is not None:
                                    return True

                                if self.remote_ipv4_address is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps.Ipv4AddressMap']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:ipv4-address-maps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.ipv4_address_map is not None:
                                for child_ref in self.ipv4_address_map:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value.Ipv4AddressMaps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.srlg_number is None:
                            raise YPYDataValidationError('Key property srlg_number is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:srlg/Cisco-IOS-XR-mpls-te-cfg:values/Cisco-IOS-XR-mpls-te-cfg:value[Cisco-IOS-XR-mpls-te-cfg:srlg-number = ' + str(self.srlg_number) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.srlg_number is not None:
                            return True

                        if self.ipv4_address_maps is not None and self.ipv4_address_maps._has_data():
                            return True

                        if self.admin_weight is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.Srlg.Values.Value']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:srlg/Cisco-IOS-XR-mpls-te-cfg:values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.value is not None:
                        for child_ref in self.value:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.Srlg.Values']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:srlg'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.names is not None and self.names._has_data():
                    return True

                if self.values is not None and self.values._has_data():
                    return True

                if self.default_admin_weight is not None:
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.Srlg']['meta_info']


        class Queues(object):
            """
            Configure MPLS TE route priority
            
            .. attribute:: queue
            
            	Configure route priority queue value
            	**type**\: list of :py:class:`Queue <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.Queues.Queue>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.queue = YList()
                self.queue.parent = self
                self.queue.name = 'queue'


            class Queue(object):
                """
                Configure route priority queue value
                
                .. attribute:: role  <key>
                
                	Route Priority Tunnel Role
                	**type**\: :py:class:`RoutePriorityRoleEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.RoutePriorityRoleEnum>`
                
                .. attribute:: value
                
                	Route priority queue value
                	**type**\: int
                
                	**range:** 0..12
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.role = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.role is None:
                        raise YPYDataValidationError('Key property role is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:queues/Cisco-IOS-XR-mpls-te-cfg:queue[Cisco-IOS-XR-mpls-te-cfg:role = ' + str(self.role) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.role is not None:
                        return True

                    if self.value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.Queues.Queue']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:queues'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.queue is not None:
                    for child_ref in self.queue:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.Queues']['meta_info']


        class PathSelectionLooseMetrics(object):
            """
            Path selection Loose ERO Metric Class
            configuration
            
            .. attribute:: path_selection_loose_metric
            
            	Path selection Loose ERO Metric configuration
            	**type**\: list of :py:class:`PathSelectionLooseMetric <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PathSelectionLooseMetrics.PathSelectionLooseMetric>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path_selection_loose_metric = YList()
                self.path_selection_loose_metric.parent = self
                self.path_selection_loose_metric.name = 'path_selection_loose_metric'


            class PathSelectionLooseMetric(object):
                """
                Path selection Loose ERO Metric configuration
                
                .. attribute:: class_type  <key>
                
                	Path Selection class Type
                	**type**\: int
                
                	**range:** 0..7
                
                .. attribute:: metric_type
                
                	Metric to use for ERO Expansion
                	**type**\: :py:class:`MplsTePathSelectionMetricEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetricEnum>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.class_type = None
                    self.metric_type = None

                @property
                def _common_path(self):
                    if self.class_type is None:
                        raise YPYDataValidationError('Key property class_type is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:path-selection-loose-metrics/Cisco-IOS-XR-mpls-te-cfg:path-selection-loose-metric[Cisco-IOS-XR-mpls-te-cfg:class-type = ' + str(self.class_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.class_type is not None:
                        return True

                    if self.metric_type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.PathSelectionLooseMetrics.PathSelectionLooseMetric']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:path-selection-loose-metrics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.path_selection_loose_metric is not None:
                    for child_ref in self.path_selection_loose_metric:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.PathSelectionLooseMetrics']['meta_info']


        class Mib(object):
            """
            MPLS\-TE MIB properties
            
            .. attribute:: midpoint_lsp_stats_collection_disable
            
            	Disables mib midpoint LSP traffic stats collection
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.midpoint_lsp_stats_collection_disable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:mib'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.midpoint_lsp_stats_collection_disable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.Mib']['meta_info']


        class AttributeSet(object):
            """
            Attribute AttributeSets
            
            .. attribute:: path_option_attributes
            
            	Path Option Attribute\-Set Table
            	**type**\: :py:class:`PathOptionAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes>`
            
            .. attribute:: p2mpte_attributes
            
            	P2MP\-TE Tunnel AttributeSets Table
            	**type**\: :py:class:`P2MpteAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes>`
            
            .. attribute:: p2p_te_attributes
            
            	P2P\-TE Tunnel AttributeSets Table
            	**type**\: :py:class:`P2PTeAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes>`
            
            .. attribute:: auto_backup_attributes
            
            	Auto\-backup Tunnel Attribute Table
            	**type**\: :py:class:`AutoBackupAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes>`
            
            .. attribute:: otn_pp_attributes
            
            	OTN Path Protection Attributes table
            	**type**\: :py:class:`OtnPpAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes>`
            
            .. attribute:: auto_mesh_attributes
            
            	Auto\-mesh Tunnel AttributeSets Table
            	**type**\: :py:class:`AutoMeshAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes>`
            
            .. attribute:: xro_attributes
            
            	XRO Tunnel Attributes table
            	**type**\: :py:class:`XroAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path_option_attributes = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes()
                self.path_option_attributes.parent = self
                self.p2mpte_attributes = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes()
                self.p2mpte_attributes.parent = self
                self.p2p_te_attributes = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes()
                self.p2p_te_attributes.parent = self
                self.auto_backup_attributes = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes()
                self.auto_backup_attributes.parent = self
                self.otn_pp_attributes = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes()
                self.otn_pp_attributes.parent = self
                self.auto_mesh_attributes = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes()
                self.auto_mesh_attributes.parent = self
                self.xro_attributes = MplsTe.GlobalAttributes.AttributeSet.XroAttributes()
                self.xro_attributes.parent = self


            class PathOptionAttributes(object):
                """
                Path Option Attribute\-Set Table
                
                .. attribute:: path_option_attribute
                
                	Path Option Attribute
                	**type**\: list of :py:class:`PathOptionAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.path_option_attribute = YList()
                    self.path_option_attribute.parent = self
                    self.path_option_attribute.name = 'path_option_attribute'


                class PathOptionAttribute(object):
                    """
                    Path Option Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: path_selection_exclude_list
                    
                    	Path selection exclude list name configuration
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\: :py:class:`AffinityMask <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask>`
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\: :py:class:`Bandwidth <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth>`
                    
                    .. attribute:: path_selection_cost_limit
                    
                    	Path selection cost limit configuration for this specific tunnel
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    .. attribute:: new_style_affinities
                    
                    	Tunnel new style affinity attributes table
                    	**type**\: :py:class:`NewStyleAffinities <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities>`
                    
                    .. attribute:: path_invalidation
                    
                    	Path invalidation configuration for this specific tunnel
                    	**type**\: :py:class:`PathInvalidation <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.path_selection_exclude_list = None
                        self.enable = None
                        self.affinity_mask = None
                        self.bandwidth = None
                        self.path_selection_cost_limit = None
                        self.new_style_affinities = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities()
                        self.new_style_affinities.parent = self
                        self.path_invalidation = MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation()
                        self.path_invalidation.parent = self


                    class AffinityMask(object):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.affinity = None
                            self.mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:affinity-mask'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.affinity is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.AffinityMask']['meta_info']


                    class Bandwidth(object):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\: :py:class:`MplsTeBandwidthDsteEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDsteEnum>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwith allocation
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dste_type = None
                            self.class_or_pool_type = None
                            self.bandwidth = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:bandwidth'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.dste_type is not None:
                                return True

                            if self.class_or_pool_type is not None:
                                return True

                            if self.bandwidth is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.Bandwidth']['meta_info']


                    class NewStyleAffinities(object):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of :py:class:`NewStyleAffinity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities.NewStyleAffinity>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.new_style_affinity = YList()
                            self.new_style_affinity.parent = self
                            self.new_style_affinity.name = 'new_style_affinity'


                        class NewStyleAffinity(object):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\: :py:class:`MplsTeTunnelAffinityEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinityEnum>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.affinity_type = None
                                self.affinity1 = None
                                self.affinity2 = None
                                self.affinity3 = None
                                self.affinity4 = None
                                self.affinity5 = None
                                self.affinity6 = None
                                self.affinity7 = None
                                self.affinity8 = None
                                self.affinity9 = None
                                self.affinity10 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.affinity_type is None:
                                    raise YPYDataValidationError('Key property affinity_type is None')
                                if self.affinity1 is None:
                                    raise YPYDataValidationError('Key property affinity1 is None')
                                if self.affinity2 is None:
                                    raise YPYDataValidationError('Key property affinity2 is None')
                                if self.affinity3 is None:
                                    raise YPYDataValidationError('Key property affinity3 is None')
                                if self.affinity4 is None:
                                    raise YPYDataValidationError('Key property affinity4 is None')
                                if self.affinity5 is None:
                                    raise YPYDataValidationError('Key property affinity5 is None')
                                if self.affinity6 is None:
                                    raise YPYDataValidationError('Key property affinity6 is None')
                                if self.affinity7 is None:
                                    raise YPYDataValidationError('Key property affinity7 is None')
                                if self.affinity8 is None:
                                    raise YPYDataValidationError('Key property affinity8 is None')
                                if self.affinity9 is None:
                                    raise YPYDataValidationError('Key property affinity9 is None')
                                if self.affinity10 is None:
                                    raise YPYDataValidationError('Key property affinity10 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinity[Cisco-IOS-XR-mpls-te-cfg:affinity-type = ' + str(self.affinity_type) + '][Cisco-IOS-XR-mpls-te-cfg:affinity1 = ' + str(self.affinity1) + '][Cisco-IOS-XR-mpls-te-cfg:affinity2 = ' + str(self.affinity2) + '][Cisco-IOS-XR-mpls-te-cfg:affinity3 = ' + str(self.affinity3) + '][Cisco-IOS-XR-mpls-te-cfg:affinity4 = ' + str(self.affinity4) + '][Cisco-IOS-XR-mpls-te-cfg:affinity5 = ' + str(self.affinity5) + '][Cisco-IOS-XR-mpls-te-cfg:affinity6 = ' + str(self.affinity6) + '][Cisco-IOS-XR-mpls-te-cfg:affinity7 = ' + str(self.affinity7) + '][Cisco-IOS-XR-mpls-te-cfg:affinity8 = ' + str(self.affinity8) + '][Cisco-IOS-XR-mpls-te-cfg:affinity9 = ' + str(self.affinity9) + '][Cisco-IOS-XR-mpls-te-cfg:affinity10 = ' + str(self.affinity10) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.affinity_type is not None:
                                    return True

                                if self.affinity1 is not None:
                                    return True

                                if self.affinity2 is not None:
                                    return True

                                if self.affinity3 is not None:
                                    return True

                                if self.affinity4 is not None:
                                    return True

                                if self.affinity5 is not None:
                                    return True

                                if self.affinity6 is not None:
                                    return True

                                if self.affinity7 is not None:
                                    return True

                                if self.affinity8 is not None:
                                    return True

                                if self.affinity9 is not None:
                                    return True

                                if self.affinity10 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.new_style_affinity is not None:
                                for child_ref in self.new_style_affinity:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.NewStyleAffinities']['meta_info']


                    class PathInvalidation(object):
                        """
                        Path invalidation configuration for this
                        specific tunnel
                        
                        .. attribute:: path_invalidation_timeout
                        
                        	Path Invalidation Timeout
                        	**type**\: int
                        
                        	**range:** 0..60000
                        
                        .. attribute:: path_invalidation_action
                        
                        	Path Invalidation Action
                        	**type**\: :py:class:`PathInvalidationActionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.PathInvalidationActionEnum>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path_invalidation_timeout = None
                            self.path_invalidation_action = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-invalidation'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.path_invalidation_timeout is not None:
                                return True

                            if self.path_invalidation_action is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute.PathInvalidation']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:path-option-attributes/Cisco-IOS-XR-mpls-te-cfg:path-option-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.path_selection_exclude_list is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.affinity_mask is not None and self.affinity_mask._has_data():
                            return True

                        if self.bandwidth is not None and self.bandwidth._has_data():
                            return True

                        if self.path_selection_cost_limit is not None:
                            return True

                        if self.new_style_affinities is not None and self.new_style_affinities._has_data():
                            return True

                        if self.path_invalidation is not None and self.path_invalidation._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes.PathOptionAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:path-option-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.path_option_attribute is not None:
                        for child_ref in self.path_option_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.PathOptionAttributes']['meta_info']


            class P2MpteAttributes(object):
                """
                P2MP\-TE Tunnel AttributeSets Table
                
                .. attribute:: p2mpte_attribute
                
                	P2MP\-TE Tunnel Attribute
                	**type**\: list of :py:class:`P2MpteAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.p2mpte_attribute = YList()
                    self.p2mpte_attribute.parent = self
                    self.p2mpte_attribute.name = 'p2mpte_attribute'


                class P2MpteAttribute(object):
                    """
                    P2MP\-TE Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: interface_bandwidth
                    
                    	The bandwidth of the interface in kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\: :py:class:`Priority <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\: :py:class:`AffinityMask <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask>`
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\: :py:class:`Bandwidth <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth>`
                    
                    .. attribute:: new_style_affinities
                    
                    	Tunnel new style affinity attributes table
                    	**type**\: :py:class:`NewStyleAffinities <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities>`
                    
                    .. attribute:: fast_reroute
                    
                    	Specify MPLS tunnel can be fast\-rerouted
                    	**type**\: :py:class:`FastReroute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute>`
                    
                    .. attribute:: logging
                    
                    	Log tunnel LSP messages
                    	**type**\: :py:class:`Logging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.interface_bandwidth = None
                        self.priority = None
                        self.enable = None
                        self.record_route = None
                        self.affinity_mask = None
                        self.bandwidth = None
                        self.new_style_affinities = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities()
                        self.new_style_affinities.parent = self
                        self.fast_reroute = None
                        self.logging = MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging()
                        self.logging.parent = self


                    class Priority(object):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.setup_priority = None
                            self.hold_priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:priority'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.setup_priority is not None:
                                return True

                            if self.hold_priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Priority']['meta_info']


                    class AffinityMask(object):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.affinity = None
                            self.mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:affinity-mask'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.affinity is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.AffinityMask']['meta_info']


                    class Bandwidth(object):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\: :py:class:`MplsTeBandwidthDsteEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDsteEnum>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwith allocation
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dste_type = None
                            self.class_or_pool_type = None
                            self.bandwidth = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:bandwidth'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.dste_type is not None:
                                return True

                            if self.class_or_pool_type is not None:
                                return True

                            if self.bandwidth is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Bandwidth']['meta_info']


                    class NewStyleAffinities(object):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of :py:class:`NewStyleAffinity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities.NewStyleAffinity>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.new_style_affinity = YList()
                            self.new_style_affinity.parent = self
                            self.new_style_affinity.name = 'new_style_affinity'


                        class NewStyleAffinity(object):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\: :py:class:`MplsTeTunnelAffinityEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinityEnum>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.affinity_type = None
                                self.affinity1 = None
                                self.affinity2 = None
                                self.affinity3 = None
                                self.affinity4 = None
                                self.affinity5 = None
                                self.affinity6 = None
                                self.affinity7 = None
                                self.affinity8 = None
                                self.affinity9 = None
                                self.affinity10 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.affinity_type is None:
                                    raise YPYDataValidationError('Key property affinity_type is None')
                                if self.affinity1 is None:
                                    raise YPYDataValidationError('Key property affinity1 is None')
                                if self.affinity2 is None:
                                    raise YPYDataValidationError('Key property affinity2 is None')
                                if self.affinity3 is None:
                                    raise YPYDataValidationError('Key property affinity3 is None')
                                if self.affinity4 is None:
                                    raise YPYDataValidationError('Key property affinity4 is None')
                                if self.affinity5 is None:
                                    raise YPYDataValidationError('Key property affinity5 is None')
                                if self.affinity6 is None:
                                    raise YPYDataValidationError('Key property affinity6 is None')
                                if self.affinity7 is None:
                                    raise YPYDataValidationError('Key property affinity7 is None')
                                if self.affinity8 is None:
                                    raise YPYDataValidationError('Key property affinity8 is None')
                                if self.affinity9 is None:
                                    raise YPYDataValidationError('Key property affinity9 is None')
                                if self.affinity10 is None:
                                    raise YPYDataValidationError('Key property affinity10 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinity[Cisco-IOS-XR-mpls-te-cfg:affinity-type = ' + str(self.affinity_type) + '][Cisco-IOS-XR-mpls-te-cfg:affinity1 = ' + str(self.affinity1) + '][Cisco-IOS-XR-mpls-te-cfg:affinity2 = ' + str(self.affinity2) + '][Cisco-IOS-XR-mpls-te-cfg:affinity3 = ' + str(self.affinity3) + '][Cisco-IOS-XR-mpls-te-cfg:affinity4 = ' + str(self.affinity4) + '][Cisco-IOS-XR-mpls-te-cfg:affinity5 = ' + str(self.affinity5) + '][Cisco-IOS-XR-mpls-te-cfg:affinity6 = ' + str(self.affinity6) + '][Cisco-IOS-XR-mpls-te-cfg:affinity7 = ' + str(self.affinity7) + '][Cisco-IOS-XR-mpls-te-cfg:affinity8 = ' + str(self.affinity8) + '][Cisco-IOS-XR-mpls-te-cfg:affinity9 = ' + str(self.affinity9) + '][Cisco-IOS-XR-mpls-te-cfg:affinity10 = ' + str(self.affinity10) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.affinity_type is not None:
                                    return True

                                if self.affinity1 is not None:
                                    return True

                                if self.affinity2 is not None:
                                    return True

                                if self.affinity3 is not None:
                                    return True

                                if self.affinity4 is not None:
                                    return True

                                if self.affinity5 is not None:
                                    return True

                                if self.affinity6 is not None:
                                    return True

                                if self.affinity7 is not None:
                                    return True

                                if self.affinity8 is not None:
                                    return True

                                if self.affinity9 is not None:
                                    return True

                                if self.affinity10 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.new_style_affinity is not None:
                                for child_ref in self.new_style_affinity:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.NewStyleAffinities']['meta_info']


                    class FastReroute(object):
                        """
                        Specify MPLS tunnel can be fast\-rerouted
                        
                        .. attribute:: bandwidth_protection
                        
                        	Bandwidth Protection
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: node_protection
                        
                        	Node Protection
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bandwidth_protection = None
                            self.node_protection = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:fast-reroute'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.bandwidth_protection is not None:
                                return True

                            if self.node_protection is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.FastReroute']['meta_info']


                    class Logging(object):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel bandwidth change messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: all
                        
                        	Log all events for a tunnel
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: sub_lsp_state_message
                        
                        	Log all tunnel sub\-LSP state messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.insufficient_bw_message = None
                            self.reoptimized_message = None
                            self.bandwidth_change_message = None
                            self.all = None
                            self.pcalc_failure_message = None
                            self.state_message = None
                            self.reoptimize_attempts_message = None
                            self.sub_lsp_state_message = None
                            self.reroute_messsage = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:logging'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.insufficient_bw_message is not None:
                                return True

                            if self.reoptimized_message is not None:
                                return True

                            if self.bandwidth_change_message is not None:
                                return True

                            if self.all is not None:
                                return True

                            if self.pcalc_failure_message is not None:
                                return True

                            if self.state_message is not None:
                                return True

                            if self.reoptimize_attempts_message is not None:
                                return True

                            if self.sub_lsp_state_message is not None:
                                return True

                            if self.reroute_messsage is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute.Logging']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:p2mpte-attributes/Cisco-IOS-XR-mpls-te-cfg:p2mpte-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.interface_bandwidth is not None:
                            return True

                        if self.priority is not None and self.priority._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.record_route is not None:
                            return True

                        if self.affinity_mask is not None and self.affinity_mask._has_data():
                            return True

                        if self.bandwidth is not None and self.bandwidth._has_data():
                            return True

                        if self.new_style_affinities is not None and self.new_style_affinities._has_data():
                            return True

                        if self.fast_reroute is not None and self.fast_reroute._has_data():
                            return True

                        if self.logging is not None and self.logging._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes.P2MpteAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:p2mpte-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.p2mpte_attribute is not None:
                        for child_ref in self.p2mpte_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2MpteAttributes']['meta_info']


            class P2PTeAttributes(object):
                """
                P2P\-TE Tunnel AttributeSets Table
                
                .. attribute:: p2p_te_attribute
                
                	P2P\-TE Tunnel Attribute
                	**type**\: list of :py:class:`P2PTeAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.p2p_te_attribute = YList()
                    self.p2p_te_attribute.parent = self
                    self.p2p_te_attribute.name = 'p2p_te_attribute'


                class P2PTeAttribute(object):
                    """
                    P2P\-TE Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: path_selection
                    
                    	Configure path selection properties
                    	**type**\: :py:class:`PathSelection <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection>`
                    
                    .. attribute:: logging
                    
                    	Log tunnel LSP messages
                    	**type**\: :py:class:`Logging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\: :py:class:`AffinityMask <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask>`
                    
                    .. attribute:: new_style_affinities
                    
                    	Tunnel new style affinity attributes table
                    	**type**\: :py:class:`NewStyleAffinities <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.path_selection = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection()
                        self.path_selection.parent = self
                        self.logging = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging()
                        self.logging.parent = self
                        self.enable = None
                        self.affinity_mask = None
                        self.new_style_affinities = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities()
                        self.new_style_affinities.parent = self


                    class PathSelection(object):
                        """
                        Configure path selection properties
                        
                        .. attribute:: segment_routing_prepend
                        
                        	Path selection segment routing prepend configuration
                        	**type**\: :py:class:`SegmentRoutingPrepend <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend>`
                        
                        .. attribute:: path_selection_invalidation
                        
                        	Path selection invalidation configuration
                        	**type**\: :py:class:`PathSelectionInvalidation <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation>`
                        
                        .. attribute:: enable
                        
                        	Enter path selection configuration
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: path_selection_metric
                        
                        	Path selection metric to use in path calculation
                        	**type**\: :py:class:`MplsTePathSelectionMetricEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionMetricEnum>`
                        
                        .. attribute:: path_selection_segment_routing_adjacency_protection
                        
                        	Segment routing adjacency protection type to use in path calculation
                        	**type**\: :py:class:`MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionSegmentRoutingAdjacencyProtectionEnum>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.segment_routing_prepend = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend()
                            self.segment_routing_prepend.parent = self
                            self.path_selection_invalidation = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation()
                            self.path_selection_invalidation.parent = self
                            self.enable = None
                            self.path_selection_metric = None
                            self.path_selection_segment_routing_adjacency_protection = None


                        class SegmentRoutingPrepend(object):
                            """
                            Path selection segment routing prepend
                            configuration
                            
                            .. attribute:: indexes
                            
                            	Segment routing prepend index table
                            	**type**\: :py:class:`Indexes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes>`
                            
                            .. attribute:: enable
                            
                            	Enter path selection segment routing prepend submode
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.indexes = MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes()
                                self.indexes.parent = self
                                self.enable = None


                            class Indexes(object):
                                """
                                Segment routing prepend index table
                                
                                .. attribute:: index
                                
                                	Prepend index information
                                	**type**\: list of :py:class:`Index <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index>`
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.index = YList()
                                    self.index.parent = self
                                    self.index.name = 'index'


                                class Index(object):
                                    """
                                    Prepend index information
                                    
                                    .. attribute:: index_number  <key>
                                    
                                    	Index number
                                    	**type**\: int
                                    
                                    	**range:** 1..10
                                    
                                    .. attribute:: prepend_type
                                    
                                    	Prepend type
                                    	**type**\: :py:class:`SrPrependEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.SrPrependEnum>`
                                    
                                    .. attribute:: mpls_label
                                    
                                    	MPLS Label
                                    	**type**\: int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'mpls-te-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.index_number = None
                                        self.prepend_type = None
                                        self.mpls_label = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.index_number is None:
                                            raise YPYDataValidationError('Key property index_number is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:index[Cisco-IOS-XR-mpls-te-cfg:index-number = ' + str(self.index_number) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.index_number is not None:
                                            return True

                                        if self.prepend_type is not None:
                                            return True

                                        if self.mpls_label is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes.Index']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:indexes'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.index is not None:
                                        for child_ref in self.index:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend.Indexes']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:segment-routing-prepend'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.indexes is not None and self.indexes._has_data():
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.SegmentRoutingPrepend']['meta_info']


                        class PathSelectionInvalidation(object):
                            """
                            Path selection invalidation configuration
                            
                            .. attribute:: invalidation_timer
                            
                            	Path selection invalidation timer value (milliseconds)
                            	**type**\: int
                            
                            	**range:** 0..60000
                            
                            .. attribute:: invalidation_timer_expire_type
                            
                            	Path selection invalidation timer expire type
                            	**type**\: :py:class:`MplsTePathSelectionInvalidationTimerExpireEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathSelectionInvalidationTimerExpireEnum>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.invalidation_timer = None
                                self.invalidation_timer_expire_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-selection-invalidation'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.invalidation_timer is not None:
                                    return True

                                if self.invalidation_timer_expire_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection.PathSelectionInvalidation']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-selection'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.segment_routing_prepend is not None and self.segment_routing_prepend._has_data():
                                return True

                            if self.path_selection_invalidation is not None and self.path_selection_invalidation._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.path_selection_metric is not None:
                                return True

                            if self.path_selection_segment_routing_adjacency_protection is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.PathSelection']['meta_info']


                    class Logging(object):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: lsp_switch_over_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: all
                        
                        	Log all events for a tunnel
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: record_route_messsage
                        
                        	Log tunnel record\-route messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: bfd_state_message
                        
                        	Enable BFD session state change alarm
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.lsp_switch_over_change_message = None
                            self.all = None
                            self.record_route_messsage = None
                            self.bfd_state_message = None
                            self.bandwidth_change_message = None
                            self.reoptimize_attempts_message = None
                            self.reroute_messsage = None
                            self.state_message = None
                            self.insufficient_bw_message = None
                            self.reoptimized_message = None
                            self.pcalc_failure_message = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:logging'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.lsp_switch_over_change_message is not None:
                                return True

                            if self.all is not None:
                                return True

                            if self.record_route_messsage is not None:
                                return True

                            if self.bfd_state_message is not None:
                                return True

                            if self.bandwidth_change_message is not None:
                                return True

                            if self.reoptimize_attempts_message is not None:
                                return True

                            if self.reroute_messsage is not None:
                                return True

                            if self.state_message is not None:
                                return True

                            if self.insufficient_bw_message is not None:
                                return True

                            if self.reoptimized_message is not None:
                                return True

                            if self.pcalc_failure_message is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.Logging']['meta_info']


                    class AffinityMask(object):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.affinity = None
                            self.mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:affinity-mask'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.affinity is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.AffinityMask']['meta_info']


                    class NewStyleAffinities(object):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of :py:class:`NewStyleAffinity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities.NewStyleAffinity>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.new_style_affinity = YList()
                            self.new_style_affinity.parent = self
                            self.new_style_affinity.name = 'new_style_affinity'


                        class NewStyleAffinity(object):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\: :py:class:`MplsTeTunnelAffinityEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinityEnum>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.affinity_type = None
                                self.affinity1 = None
                                self.affinity2 = None
                                self.affinity3 = None
                                self.affinity4 = None
                                self.affinity5 = None
                                self.affinity6 = None
                                self.affinity7 = None
                                self.affinity8 = None
                                self.affinity9 = None
                                self.affinity10 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.affinity_type is None:
                                    raise YPYDataValidationError('Key property affinity_type is None')
                                if self.affinity1 is None:
                                    raise YPYDataValidationError('Key property affinity1 is None')
                                if self.affinity2 is None:
                                    raise YPYDataValidationError('Key property affinity2 is None')
                                if self.affinity3 is None:
                                    raise YPYDataValidationError('Key property affinity3 is None')
                                if self.affinity4 is None:
                                    raise YPYDataValidationError('Key property affinity4 is None')
                                if self.affinity5 is None:
                                    raise YPYDataValidationError('Key property affinity5 is None')
                                if self.affinity6 is None:
                                    raise YPYDataValidationError('Key property affinity6 is None')
                                if self.affinity7 is None:
                                    raise YPYDataValidationError('Key property affinity7 is None')
                                if self.affinity8 is None:
                                    raise YPYDataValidationError('Key property affinity8 is None')
                                if self.affinity9 is None:
                                    raise YPYDataValidationError('Key property affinity9 is None')
                                if self.affinity10 is None:
                                    raise YPYDataValidationError('Key property affinity10 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinity[Cisco-IOS-XR-mpls-te-cfg:affinity-type = ' + str(self.affinity_type) + '][Cisco-IOS-XR-mpls-te-cfg:affinity1 = ' + str(self.affinity1) + '][Cisco-IOS-XR-mpls-te-cfg:affinity2 = ' + str(self.affinity2) + '][Cisco-IOS-XR-mpls-te-cfg:affinity3 = ' + str(self.affinity3) + '][Cisco-IOS-XR-mpls-te-cfg:affinity4 = ' + str(self.affinity4) + '][Cisco-IOS-XR-mpls-te-cfg:affinity5 = ' + str(self.affinity5) + '][Cisco-IOS-XR-mpls-te-cfg:affinity6 = ' + str(self.affinity6) + '][Cisco-IOS-XR-mpls-te-cfg:affinity7 = ' + str(self.affinity7) + '][Cisco-IOS-XR-mpls-te-cfg:affinity8 = ' + str(self.affinity8) + '][Cisco-IOS-XR-mpls-te-cfg:affinity9 = ' + str(self.affinity9) + '][Cisco-IOS-XR-mpls-te-cfg:affinity10 = ' + str(self.affinity10) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.affinity_type is not None:
                                    return True

                                if self.affinity1 is not None:
                                    return True

                                if self.affinity2 is not None:
                                    return True

                                if self.affinity3 is not None:
                                    return True

                                if self.affinity4 is not None:
                                    return True

                                if self.affinity5 is not None:
                                    return True

                                if self.affinity6 is not None:
                                    return True

                                if self.affinity7 is not None:
                                    return True

                                if self.affinity8 is not None:
                                    return True

                                if self.affinity9 is not None:
                                    return True

                                if self.affinity10 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.new_style_affinity is not None:
                                for child_ref in self.new_style_affinity:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute.NewStyleAffinities']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:p2p-te-attributes/Cisco-IOS-XR-mpls-te-cfg:p2p-te-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.path_selection is not None and self.path_selection._has_data():
                            return True

                        if self.logging is not None and self.logging._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.affinity_mask is not None and self.affinity_mask._has_data():
                            return True

                        if self.new_style_affinities is not None and self.new_style_affinities._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes.P2PTeAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:p2p-te-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.p2p_te_attribute is not None:
                        for child_ref in self.p2p_te_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.P2PTeAttributes']['meta_info']


            class AutoBackupAttributes(object):
                """
                Auto\-backup Tunnel Attribute Table
                
                .. attribute:: auto_backup_attribute
                
                	Auto\-backup Tunnel Attribute
                	**type**\: list of :py:class:`AutoBackupAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.auto_backup_attribute = YList()
                    self.auto_backup_attribute.parent = self
                    self.auto_backup_attribute.name = 'auto_backup_attribute'


                class AutoBackupAttribute(object):
                    """
                    Auto\-backup Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: signalled_name
                    
                    	Signalled name
                    	**type**\: :py:class:`SignalledName <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName>`
                    
                    .. attribute:: auto_backup_logging
                    
                    	Log tunnel LSP messages
                    	**type**\: :py:class:`AutoBackupLogging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging>`
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\: :py:class:`Priority <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\: :py:class:`AffinityMask <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask>`
                    
                    .. attribute:: policy_classes
                    
                    	Policy classes for PBTS
                    	**type**\: :py:class:`PolicyClasses <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses>`
                    
                    .. attribute:: new_style_affinities
                    
                    	Tunnel new style affinity attributes table
                    	**type**\: :py:class:`NewStyleAffinities <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.signalled_name = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName()
                        self.signalled_name.parent = self
                        self.auto_backup_logging = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging()
                        self.auto_backup_logging.parent = self
                        self.priority = None
                        self.enable = None
                        self.record_route = None
                        self.affinity_mask = None
                        self.policy_classes = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses()
                        self.policy_classes.parent = self
                        self.new_style_affinities = MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities()
                        self.new_style_affinities.parent = self


                    class SignalledName(object):
                        """
                        Signalled name
                        
                        .. attribute:: name
                        
                        	Signalled name
                        	**type**\: str
                        
                        .. attribute:: source_type
                        
                        	Source address or name
                        	**type**\: :py:class:`MplsTeSigNameOptionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeSigNameOptionEnum>`
                        
                        .. attribute:: protected_interface_type
                        
                        	Protected\-interface address or name
                        	**type**\: :py:class:`MplsTeSigNameOptionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeSigNameOptionEnum>`
                        
                        .. attribute:: mp_address
                        
                        	Set if merge\-point address is to be appended
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.name = None
                            self.source_type = None
                            self.protected_interface_type = None
                            self.mp_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:signalled-name'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.name is not None:
                                return True

                            if self.source_type is not None:
                                return True

                            if self.protected_interface_type is not None:
                                return True

                            if self.mp_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.SignalledName']['meta_info']


                    class AutoBackupLogging(object):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bandwidth_change_message = None
                            self.reoptimize_attempts_message = None
                            self.state_message = None
                            self.reoptimized_message = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:auto-backup-logging'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.bandwidth_change_message is not None:
                                return True

                            if self.reoptimize_attempts_message is not None:
                                return True

                            if self.state_message is not None:
                                return True

                            if self.reoptimized_message is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AutoBackupLogging']['meta_info']


                    class Priority(object):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.setup_priority = None
                            self.hold_priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:priority'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.setup_priority is not None:
                                return True

                            if self.hold_priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.Priority']['meta_info']


                    class AffinityMask(object):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.affinity = None
                            self.mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:affinity-mask'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.affinity is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.AffinityMask']['meta_info']


                    class PolicyClasses(object):
                        """
                        Policy classes for PBTS
                        
                        .. attribute:: policy_class
                        
                        	Array of Policy class
                        	**type**\: list of int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.policy_class = YLeafList()
                            self.policy_class.parent = self
                            self.policy_class.name = 'policy_class'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:policy-classes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.policy_class is not None:
                                for child in self.policy_class:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.PolicyClasses']['meta_info']


                    class NewStyleAffinities(object):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of :py:class:`NewStyleAffinity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities.NewStyleAffinity>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.new_style_affinity = YList()
                            self.new_style_affinity.parent = self
                            self.new_style_affinity.name = 'new_style_affinity'


                        class NewStyleAffinity(object):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\: :py:class:`MplsTeTunnelAffinityEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinityEnum>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.affinity_type = None
                                self.affinity1 = None
                                self.affinity2 = None
                                self.affinity3 = None
                                self.affinity4 = None
                                self.affinity5 = None
                                self.affinity6 = None
                                self.affinity7 = None
                                self.affinity8 = None
                                self.affinity9 = None
                                self.affinity10 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.affinity_type is None:
                                    raise YPYDataValidationError('Key property affinity_type is None')
                                if self.affinity1 is None:
                                    raise YPYDataValidationError('Key property affinity1 is None')
                                if self.affinity2 is None:
                                    raise YPYDataValidationError('Key property affinity2 is None')
                                if self.affinity3 is None:
                                    raise YPYDataValidationError('Key property affinity3 is None')
                                if self.affinity4 is None:
                                    raise YPYDataValidationError('Key property affinity4 is None')
                                if self.affinity5 is None:
                                    raise YPYDataValidationError('Key property affinity5 is None')
                                if self.affinity6 is None:
                                    raise YPYDataValidationError('Key property affinity6 is None')
                                if self.affinity7 is None:
                                    raise YPYDataValidationError('Key property affinity7 is None')
                                if self.affinity8 is None:
                                    raise YPYDataValidationError('Key property affinity8 is None')
                                if self.affinity9 is None:
                                    raise YPYDataValidationError('Key property affinity9 is None')
                                if self.affinity10 is None:
                                    raise YPYDataValidationError('Key property affinity10 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinity[Cisco-IOS-XR-mpls-te-cfg:affinity-type = ' + str(self.affinity_type) + '][Cisco-IOS-XR-mpls-te-cfg:affinity1 = ' + str(self.affinity1) + '][Cisco-IOS-XR-mpls-te-cfg:affinity2 = ' + str(self.affinity2) + '][Cisco-IOS-XR-mpls-te-cfg:affinity3 = ' + str(self.affinity3) + '][Cisco-IOS-XR-mpls-te-cfg:affinity4 = ' + str(self.affinity4) + '][Cisco-IOS-XR-mpls-te-cfg:affinity5 = ' + str(self.affinity5) + '][Cisco-IOS-XR-mpls-te-cfg:affinity6 = ' + str(self.affinity6) + '][Cisco-IOS-XR-mpls-te-cfg:affinity7 = ' + str(self.affinity7) + '][Cisco-IOS-XR-mpls-te-cfg:affinity8 = ' + str(self.affinity8) + '][Cisco-IOS-XR-mpls-te-cfg:affinity9 = ' + str(self.affinity9) + '][Cisco-IOS-XR-mpls-te-cfg:affinity10 = ' + str(self.affinity10) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.affinity_type is not None:
                                    return True

                                if self.affinity1 is not None:
                                    return True

                                if self.affinity2 is not None:
                                    return True

                                if self.affinity3 is not None:
                                    return True

                                if self.affinity4 is not None:
                                    return True

                                if self.affinity5 is not None:
                                    return True

                                if self.affinity6 is not None:
                                    return True

                                if self.affinity7 is not None:
                                    return True

                                if self.affinity8 is not None:
                                    return True

                                if self.affinity9 is not None:
                                    return True

                                if self.affinity10 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.new_style_affinity is not None:
                                for child_ref in self.new_style_affinity:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute.NewStyleAffinities']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:auto-backup-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-backup-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.signalled_name is not None and self.signalled_name._has_data():
                            return True

                        if self.auto_backup_logging is not None and self.auto_backup_logging._has_data():
                            return True

                        if self.priority is not None and self.priority._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.record_route is not None:
                            return True

                        if self.affinity_mask is not None and self.affinity_mask._has_data():
                            return True

                        if self.policy_classes is not None and self.policy_classes._has_data():
                            return True

                        if self.new_style_affinities is not None and self.new_style_affinities._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes.AutoBackupAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:auto-backup-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.auto_backup_attribute is not None:
                        for child_ref in self.auto_backup_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoBackupAttributes']['meta_info']


            class OtnPpAttributes(object):
                """
                OTN Path Protection Attributes table
                
                .. attribute:: otn_pp_attribute
                
                	OTN Path Protection Attribute
                	**type**\: list of :py:class:`OtnPpAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.otn_pp_attribute = YList()
                    self.otn_pp_attribute.parent = self
                    self.otn_pp_attribute.name = 'otn_pp_attribute'


                class OtnPpAttribute(object):
                    """
                    OTN Path Protection Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: sub_network_connection_mode
                    
                    	Sub\-network connection mode
                    	**type**\: :py:class:`SubNetworkConnectionMode <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode>`
                    
                    .. attribute:: timers
                    
                    	Timers
                    	**type**\: :py:class:`Timers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers>`
                    
                    .. attribute:: aps_protection_mode
                    
                    	The APS protecion mode
                    	**type**\: :py:class:`MplsTeOtnApsProtectionModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnApsProtectionModeEnum>`
                    
                    .. attribute:: aps_protection_type
                    
                    	The APS protecion type
                    	**type**\: :py:class:`MplsTeOtnApsProtectionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnApsProtectionEnum>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.sub_network_connection_mode = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode()
                        self.sub_network_connection_mode.parent = self
                        self.timers = MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers()
                        self.timers.parent = self
                        self.aps_protection_mode = None
                        self.aps_protection_type = None
                        self.enable = None


                    class SubNetworkConnectionMode(object):
                        """
                        Sub\-network connection mode
                        
                        .. attribute:: connection_mode
                        
                        	The sub\-network connection mode
                        	**type**\: :py:class:`MplsTeOtnSncModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeOtnSncModeEnum>`
                        
                        .. attribute:: connection_monitoring_mode
                        
                        	Tandem Connection Monitoring ID for the interface
                        	**type**\: int
                        
                        	**range:** 1..6
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.connection_mode = None
                            self.connection_monitoring_mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:sub-network-connection-mode'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.connection_mode is not None:
                                return True

                            if self.connection_monitoring_mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.SubNetworkConnectionMode']['meta_info']


                    class Timers(object):
                        """
                        Timers
                        
                        .. attribute:: aps_wait_to_restore
                        
                        	G.709 OTN path protection wait to restore timer in seconds
                        	**type**\: int
                        
                        	**range:** 0..720
                        
                        .. attribute:: aps_hold_off
                        
                        	G.709 OTN path protection hold\-off timer in milliseconds
                        	**type**\: int
                        
                        	**range:** 100..10000
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.aps_wait_to_restore = None
                            self.aps_hold_off = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:timers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.aps_wait_to_restore is not None:
                                return True

                            if self.aps_hold_off is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute.Timers']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:otn-pp-attributes/Cisco-IOS-XR-mpls-te-cfg:otn-pp-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.sub_network_connection_mode is not None and self.sub_network_connection_mode._has_data():
                            return True

                        if self.timers is not None and self.timers._has_data():
                            return True

                        if self.aps_protection_mode is not None:
                            return True

                        if self.aps_protection_type is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes.OtnPpAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:otn-pp-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.otn_pp_attribute is not None:
                        for child_ref in self.otn_pp_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.OtnPpAttributes']['meta_info']


            class AutoMeshAttributes(object):
                """
                Auto\-mesh Tunnel AttributeSets Table
                
                .. attribute:: auto_mesh_attribute
                
                	Auto\-mesh Tunnel Attribute
                	**type**\: list of :py:class:`AutoMeshAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.auto_mesh_attribute = YList()
                    self.auto_mesh_attribute.parent = self
                    self.auto_mesh_attribute.name = 'auto_mesh_attribute'


                class AutoMeshAttribute(object):
                    """
                    Auto\-mesh Tunnel Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: auto_mesh_logging
                    
                    	Log tunnel LSP messages
                    	**type**\: :py:class:`AutoMeshLogging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging>`
                    
                    .. attribute:: autoroute_announce
                    
                    	Enable autoroute announce
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: interface_bandwidth
                    
                    	The bandwidth of the interface in kbps
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forward_class
                    
                    	Forward class value
                    	**type**\: int
                    
                    	**range:** 1..7
                    
                    .. attribute:: priority
                    
                    	Tunnel Setup and Hold Priorities
                    	**type**\: :py:class:`Priority <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: record_route
                    
                    	Record the route used by the tunnel
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: affinity_mask
                    
                    	Set the affinity flags and mask
                    	**type**\: :py:class:`AffinityMask <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask>`
                    
                    .. attribute:: bandwidth
                    
                    	Tunnel bandwidth requirement
                    	**type**\: :py:class:`Bandwidth <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth>`
                    
                    .. attribute:: collection_only
                    
                    	Enable bandwidth collection only, no auto\-bw adjustment
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: policy_classes
                    
                    	Policy classes for PBTS
                    	**type**\: :py:class:`PolicyClasses <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses>`
                    
                    .. attribute:: new_style_affinities
                    
                    	Tunnel new style affinity attributes table
                    	**type**\: :py:class:`NewStyleAffinities <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities>`
                    
                    .. attribute:: soft_preemption
                    
                    	Enable the soft\-preemption feature on the tunnel
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: fast_reroute
                    
                    	Specify MPLS tunnel can be fast\-rerouted
                    	**type**\: :py:class:`FastReroute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute>`
                    
                    .. attribute:: load_share
                    
                    	Tunnel loadsharing metric
                    	**type**\: int
                    
                    	**range:** 1..4294967295
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.auto_mesh_logging = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging()
                        self.auto_mesh_logging.parent = self
                        self.autoroute_announce = None
                        self.interface_bandwidth = None
                        self.forward_class = None
                        self.priority = None
                        self.enable = None
                        self.record_route = None
                        self.affinity_mask = None
                        self.bandwidth = None
                        self.collection_only = None
                        self.policy_classes = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses()
                        self.policy_classes.parent = self
                        self.new_style_affinities = MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities()
                        self.new_style_affinities.parent = self
                        self.soft_preemption = None
                        self.fast_reroute = None
                        self.load_share = None


                    class AutoMeshLogging(object):
                        """
                        Log tunnel LSP messages
                        
                        .. attribute:: bandwidth_change_message
                        
                        	Log tunnel messages for bandwidth change
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimize_attempts_message
                        
                        	Log tunnel reoptimization attempts messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reroute_messsage
                        
                        	Log tunnel rereoute messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: state_message
                        
                        	Log tunnel state messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: insufficient_bw_message
                        
                        	Log tunnel messages for insufficient bandwidth
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: reoptimized_message
                        
                        	Log tunnel reoptimized messages
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: pcalc_failure_message
                        
                        	Enable logging for path\-calculation failures
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bandwidth_change_message = None
                            self.reoptimize_attempts_message = None
                            self.reroute_messsage = None
                            self.state_message = None
                            self.insufficient_bw_message = None
                            self.reoptimized_message = None
                            self.pcalc_failure_message = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:auto-mesh-logging'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.bandwidth_change_message is not None:
                                return True

                            if self.reoptimize_attempts_message is not None:
                                return True

                            if self.reroute_messsage is not None:
                                return True

                            if self.state_message is not None:
                                return True

                            if self.insufficient_bw_message is not None:
                                return True

                            if self.reoptimized_message is not None:
                                return True

                            if self.pcalc_failure_message is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AutoMeshLogging']['meta_info']


                    class Priority(object):
                        """
                        Tunnel Setup and Hold Priorities
                        
                        .. attribute:: setup_priority
                        
                        	Setup Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: hold_priority
                        
                        	Hold Priority
                        	**type**\: int
                        
                        	**range:** 0..7
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.setup_priority = None
                            self.hold_priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:priority'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.setup_priority is not None:
                                return True

                            if self.hold_priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Priority']['meta_info']


                    class AffinityMask(object):
                        """
                        Set the affinity flags and mask
                        
                        .. attribute:: affinity
                        
                        	Affinity flags
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: mask
                        
                        	Affinity mask
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.affinity = None
                            self.mask = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:affinity-mask'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.affinity is not None:
                                return True

                            if self.mask is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.AffinityMask']['meta_info']


                    class Bandwidth(object):
                        """
                        Tunnel bandwidth requirement
                        
                        .. attribute:: dste_type
                        
                        	DSTE\-standard flag
                        	**type**\: :py:class:`MplsTeBandwidthDsteEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeBandwidthDsteEnum>`
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: class_or_pool_type
                        
                        	Class type for the bandwith allocation
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: bandwidth
                        
                        	The value of the bandwidth reserved by this tunnel in kbps
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.dste_type = None
                            self.class_or_pool_type = None
                            self.bandwidth = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:bandwidth'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.dste_type is not None:
                                return True

                            if self.class_or_pool_type is not None:
                                return True

                            if self.bandwidth is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.Bandwidth']['meta_info']


                    class PolicyClasses(object):
                        """
                        Policy classes for PBTS
                        
                        .. attribute:: policy_class
                        
                        	Array of Policy class
                        	**type**\: list of int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.policy_class = YLeafList()
                            self.policy_class.parent = self
                            self.policy_class.name = 'policy_class'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:policy-classes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.policy_class is not None:
                                for child in self.policy_class:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.PolicyClasses']['meta_info']


                    class NewStyleAffinities(object):
                        """
                        Tunnel new style affinity attributes table
                        
                        .. attribute:: new_style_affinity
                        
                        	Tunnel new style affinity attribute
                        	**type**\: list of :py:class:`NewStyleAffinity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities.NewStyleAffinity>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.new_style_affinity = YList()
                            self.new_style_affinity.parent = self
                            self.new_style_affinity.name = 'new_style_affinity'


                        class NewStyleAffinity(object):
                            """
                            Tunnel new style affinity attribute
                            
                            .. attribute:: affinity_type  <key>
                            
                            	The type of the affinity entry
                            	**type**\: :py:class:`MplsTeTunnelAffinityEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeTunnelAffinityEnum>`
                            
                            .. attribute:: affinity1  <key>
                            
                            	The name of the first affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity2  <key>
                            
                            	The name of the second affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity3  <key>
                            
                            	The name of the third affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity4  <key>
                            
                            	The name of the fourth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity5  <key>
                            
                            	The name of the fifth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity6  <key>
                            
                            	The name of the sixth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity7  <key>
                            
                            	The name of the seventh affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity8  <key>
                            
                            	The name of the eighth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity9  <key>
                            
                            	The name of the nineth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: affinity10  <key>
                            
                            	The name of the tenth affinity
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.affinity_type = None
                                self.affinity1 = None
                                self.affinity2 = None
                                self.affinity3 = None
                                self.affinity4 = None
                                self.affinity5 = None
                                self.affinity6 = None
                                self.affinity7 = None
                                self.affinity8 = None
                                self.affinity9 = None
                                self.affinity10 = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.affinity_type is None:
                                    raise YPYDataValidationError('Key property affinity_type is None')
                                if self.affinity1 is None:
                                    raise YPYDataValidationError('Key property affinity1 is None')
                                if self.affinity2 is None:
                                    raise YPYDataValidationError('Key property affinity2 is None')
                                if self.affinity3 is None:
                                    raise YPYDataValidationError('Key property affinity3 is None')
                                if self.affinity4 is None:
                                    raise YPYDataValidationError('Key property affinity4 is None')
                                if self.affinity5 is None:
                                    raise YPYDataValidationError('Key property affinity5 is None')
                                if self.affinity6 is None:
                                    raise YPYDataValidationError('Key property affinity6 is None')
                                if self.affinity7 is None:
                                    raise YPYDataValidationError('Key property affinity7 is None')
                                if self.affinity8 is None:
                                    raise YPYDataValidationError('Key property affinity8 is None')
                                if self.affinity9 is None:
                                    raise YPYDataValidationError('Key property affinity9 is None')
                                if self.affinity10 is None:
                                    raise YPYDataValidationError('Key property affinity10 is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinity[Cisco-IOS-XR-mpls-te-cfg:affinity-type = ' + str(self.affinity_type) + '][Cisco-IOS-XR-mpls-te-cfg:affinity1 = ' + str(self.affinity1) + '][Cisco-IOS-XR-mpls-te-cfg:affinity2 = ' + str(self.affinity2) + '][Cisco-IOS-XR-mpls-te-cfg:affinity3 = ' + str(self.affinity3) + '][Cisco-IOS-XR-mpls-te-cfg:affinity4 = ' + str(self.affinity4) + '][Cisco-IOS-XR-mpls-te-cfg:affinity5 = ' + str(self.affinity5) + '][Cisco-IOS-XR-mpls-te-cfg:affinity6 = ' + str(self.affinity6) + '][Cisco-IOS-XR-mpls-te-cfg:affinity7 = ' + str(self.affinity7) + '][Cisco-IOS-XR-mpls-te-cfg:affinity8 = ' + str(self.affinity8) + '][Cisco-IOS-XR-mpls-te-cfg:affinity9 = ' + str(self.affinity9) + '][Cisco-IOS-XR-mpls-te-cfg:affinity10 = ' + str(self.affinity10) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.affinity_type is not None:
                                    return True

                                if self.affinity1 is not None:
                                    return True

                                if self.affinity2 is not None:
                                    return True

                                if self.affinity3 is not None:
                                    return True

                                if self.affinity4 is not None:
                                    return True

                                if self.affinity5 is not None:
                                    return True

                                if self.affinity6 is not None:
                                    return True

                                if self.affinity7 is not None:
                                    return True

                                if self.affinity8 is not None:
                                    return True

                                if self.affinity9 is not None:
                                    return True

                                if self.affinity10 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities.NewStyleAffinity']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:new-style-affinities'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.new_style_affinity is not None:
                                for child_ref in self.new_style_affinity:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.NewStyleAffinities']['meta_info']


                    class FastReroute(object):
                        """
                        Specify MPLS tunnel can be fast\-rerouted
                        
                        .. attribute:: bandwidth_protection
                        
                        	Bandwidth Protection
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: node_protection
                        
                        	Node Protection
                        	**type**\: int
                        
                        	**range:** 0..1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.bandwidth_protection = None
                            self.node_protection = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:fast-reroute'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.bandwidth_protection is not None:
                                return True

                            if self.node_protection is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute.FastReroute']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:auto-mesh-attributes/Cisco-IOS-XR-mpls-te-cfg:auto-mesh-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.auto_mesh_logging is not None and self.auto_mesh_logging._has_data():
                            return True

                        if self.autoroute_announce is not None:
                            return True

                        if self.interface_bandwidth is not None:
                            return True

                        if self.forward_class is not None:
                            return True

                        if self.priority is not None and self.priority._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.record_route is not None:
                            return True

                        if self.affinity_mask is not None and self.affinity_mask._has_data():
                            return True

                        if self.bandwidth is not None and self.bandwidth._has_data():
                            return True

                        if self.collection_only is not None:
                            return True

                        if self.policy_classes is not None and self.policy_classes._has_data():
                            return True

                        if self.new_style_affinities is not None and self.new_style_affinities._has_data():
                            return True

                        if self.soft_preemption is not None:
                            return True

                        if self.fast_reroute is not None and self.fast_reroute._has_data():
                            return True

                        if self.load_share is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes.AutoMeshAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:auto-mesh-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.auto_mesh_attribute is not None:
                        for child_ref in self.auto_mesh_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.AutoMeshAttributes']['meta_info']


            class XroAttributes(object):
                """
                XRO Tunnel Attributes table
                
                .. attribute:: xro_attribute
                
                	XRO Attribute
                	**type**\: list of :py:class:`XroAttribute <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.xro_attribute = YList()
                    self.xro_attribute.parent = self
                    self.xro_attribute.name = 'xro_attribute'


                class XroAttribute(object):
                    """
                    XRO Attribute
                    
                    .. attribute:: attribute_set_name  <key>
                    
                    	Attribute Set Name
                    	**type**\: str
                    
                    	**range:** 0..64
                    
                    .. attribute:: path_diversity
                    
                    	Path diversity
                    	**type**\: :py:class:`PathDiversity <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity>`
                    
                    .. attribute:: enable
                    
                    	Attribute\-set enable object that controls whether this attribute\-set is configured or not .This object must be set before other configuration supplied for this attribute\-set
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_set_name = None
                        self.path_diversity = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity()
                        self.path_diversity.parent = self
                        self.enable = None


                    class PathDiversity(object):
                        """
                        Path diversity
                        
                        .. attribute:: srlgs
                        
                        	SRLG\-based path diversity
                        	**type**\: :py:class:`Srlgs <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs>`
                        
                        .. attribute:: lsp
                        
                        	LSP\-based path diversity
                        	**type**\: :py:class:`Lsp <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.srlgs = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs()
                            self.srlgs.parent = self
                            self.lsp = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp()
                            self.lsp.parent = self


                        class Srlgs(object):
                            """
                            SRLG\-based path diversity
                            
                            .. attribute:: srlg
                            
                            	SRLG\-based path\-diversity element
                            	**type**\: list of :py:class:`Srlg <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.srlg = YList()
                                self.srlg.parent = self
                                self.srlg.name = 'srlg'


                            class Srlg(object):
                                """
                                SRLG\-based path\-diversity element
                                
                                .. attribute:: srlg  <key>
                                
                                	SRLG
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: conformance
                                
                                	The diversity conformance requirements
                                	**type**\: :py:class:`MplsTePathDiversityConformanceEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathDiversityConformanceEnum>`
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.srlg = None
                                    self.conformance = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.srlg is None:
                                        raise YPYDataValidationError('Key property srlg is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:srlg[Cisco-IOS-XR-mpls-te-cfg:srlg = ' + str(self.srlg) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.srlg is not None:
                                        return True

                                    if self.conformance is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs.Srlg']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:srlgs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.srlg is not None:
                                    for child_ref in self.srlg:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Srlgs']['meta_info']


                        class Lsp(object):
                            """
                            LSP\-based path diversity
                            
                            .. attribute:: fecs
                            
                            	FEC LSP\-based path diversity
                            	**type**\: :py:class:`Fecs <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.fecs = MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs()
                                self.fecs.parent = self


                            class Fecs(object):
                                """
                                FEC LSP\-based path diversity
                                
                                .. attribute:: fec
                                
                                	LSP\-based path\-diversity, referenced by FEC
                                	**type**\: list of :py:class:`Fec <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec>`
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.fec = YList()
                                    self.fec.parent = self
                                    self.fec.name = 'fec'


                                class Fec(object):
                                    """
                                    LSP\-based path\-diversity, referenced by
                                    FEC
                                    
                                    .. attribute:: source  <key>
                                    
                                    	Source address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: destination  <key>
                                    
                                    	Destination address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: tunnel_id  <key>
                                    
                                    	Tunnel id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: extended_tunnel_id  <key>
                                    
                                    	Extended tunnel\-id
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: lsp_id  <key>
                                    
                                    	LSP id
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: conformance
                                    
                                    	The diversity conformance requirements
                                    	**type**\: :py:class:`MplsTePathDiversityConformanceEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathDiversityConformanceEnum>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-te-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.source = None
                                        self.destination = None
                                        self.tunnel_id = None
                                        self.extended_tunnel_id = None
                                        self.lsp_id = None
                                        self.conformance = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.source is None:
                                            raise YPYDataValidationError('Key property source is None')
                                        if self.destination is None:
                                            raise YPYDataValidationError('Key property destination is None')
                                        if self.tunnel_id is None:
                                            raise YPYDataValidationError('Key property tunnel_id is None')
                                        if self.extended_tunnel_id is None:
                                            raise YPYDataValidationError('Key property extended_tunnel_id is None')
                                        if self.lsp_id is None:
                                            raise YPYDataValidationError('Key property lsp_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:fec[Cisco-IOS-XR-mpls-te-cfg:source = ' + str(self.source) + '][Cisco-IOS-XR-mpls-te-cfg:destination = ' + str(self.destination) + '][Cisco-IOS-XR-mpls-te-cfg:tunnel-id = ' + str(self.tunnel_id) + '][Cisco-IOS-XR-mpls-te-cfg:extended-tunnel-id = ' + str(self.extended_tunnel_id) + '][Cisco-IOS-XR-mpls-te-cfg:lsp-id = ' + str(self.lsp_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.source is not None:
                                            return True

                                        if self.destination is not None:
                                            return True

                                        if self.tunnel_id is not None:
                                            return True

                                        if self.extended_tunnel_id is not None:
                                            return True

                                        if self.lsp_id is not None:
                                            return True

                                        if self.conformance is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs.Fec']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:fecs'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.fec is not None:
                                        for child_ref in self.fec:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp.Fecs']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:lsp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.fecs is not None and self.fecs._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity.Lsp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-diversity'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.srlgs is not None and self.srlgs._has_data():
                                return True

                            if self.lsp is not None and self.lsp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute.PathDiversity']['meta_info']

                    @property
                    def _common_path(self):
                        if self.attribute_set_name is None:
                            raise YPYDataValidationError('Key property attribute_set_name is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:xro-attributes/Cisco-IOS-XR-mpls-te-cfg:xro-attribute[Cisco-IOS-XR-mpls-te-cfg:attribute-set-name = ' + str(self.attribute_set_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_set_name is not None:
                            return True

                        if self.path_diversity is not None and self.path_diversity._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes.XroAttribute']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set/Cisco-IOS-XR-mpls-te-cfg:xro-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.xro_attribute is not None:
                        for child_ref in self.xro_attribute:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet.XroAttributes']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:attribute-set'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.path_option_attributes is not None and self.path_option_attributes._has_data():
                    return True

                if self.p2mpte_attributes is not None and self.p2mpte_attributes._has_data():
                    return True

                if self.p2p_te_attributes is not None and self.p2p_te_attributes._has_data():
                    return True

                if self.auto_backup_attributes is not None and self.auto_backup_attributes._has_data():
                    return True

                if self.otn_pp_attributes is not None and self.otn_pp_attributes._has_data():
                    return True

                if self.auto_mesh_attributes is not None and self.auto_mesh_attributes._has_data():
                    return True

                if self.xro_attributes is not None and self.xro_attributes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.AttributeSet']['meta_info']


        class BfdOverLsp(object):
            """
            BFD over MPLS TE Global Configurations
            
            .. attribute:: tail
            
            	BFD over LSP Tail Global Configurations
            	**type**\: :py:class:`Tail <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BfdOverLsp.Tail>`
            
            .. attribute:: head
            
            	BFD over LSP Head Global Configurations
            	**type**\: :py:class:`Head <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.BfdOverLsp.Head>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.tail = MplsTe.GlobalAttributes.BfdOverLsp.Tail()
                self.tail.parent = self
                self.head = MplsTe.GlobalAttributes.BfdOverLsp.Head()
                self.head.parent = self


            class Tail(object):
                """
                BFD over LSP Tail Global Configurations
                
                .. attribute:: multiplier
                
                	Specify BFD over LSP tail multiplier
                	**type**\: int
                
                	**range:** 3..10
                
                .. attribute:: minimum_interval
                
                	Specify BFD over LSP tail minimum interval
                	**type**\: int
                
                	**range:** 100..30000
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.multiplier = None
                    self.minimum_interval = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:bfd-over-lsp/Cisco-IOS-XR-mpls-te-cfg:tail'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.multiplier is not None:
                        return True

                    if self.minimum_interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.BfdOverLsp.Tail']['meta_info']


            class Head(object):
                """
                BFD over LSP Head Global Configurations
                
                .. attribute:: reopt_timeout
                
                	BFD session down reopt timeout
                	**type**\: int
                
                	**range:** 120..4294967295
                
                .. attribute:: down_action
                
                	Specify BFD session down action
                	**type**\: :py:class:`MplsTeBfdSessionDownActionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeBfdSessionDownActionEnum>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.reopt_timeout = None
                    self.down_action = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:bfd-over-lsp/Cisco-IOS-XR-mpls-te-cfg:head'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.reopt_timeout is not None:
                        return True

                    if self.down_action is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.BfdOverLsp.Head']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:bfd-over-lsp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.tail is not None and self.tail._has_data():
                    return True

                if self.head is not None and self.head._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.BfdOverLsp']['meta_info']


        class PceAttributes(object):
            """
            Configuration MPLS TE PCE attributes
            
            .. attribute:: pce_stateful
            
            	PCE Stateful
            	**type**\: :py:class:`PceStateful <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.PceStateful>`
            
            .. attribute:: timer
            
            	Configure PCE (Path Computation Element) timers
            	**type**\: :py:class:`Timer <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Timer>`
            
            .. attribute:: peers
            
            	Configure PCE peers
            	**type**\: :py:class:`Peers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Peers>`
            
            .. attribute:: logging
            
            	Configure PCE (Path Computation Element) logging feature
            	**type**\: :py:class:`Logging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Logging>`
            
            .. attribute:: request_timeout
            
            	Request timeout value in seconds
            	**type**\: int
            
            	**range:** 5..100
            
            .. attribute:: reoptimize_period
            
            	PCE reoptimization period for PCE\-based paths
            	**type**\: int
            
            	**range:** 60..604800
            
            .. attribute:: address
            
            	Address of this PCE
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: deadtimer
            
            	Deadtimer interval in seconds
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: keepalive
            
            	Keepalive interval in seconds
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: keepalive_tolerance
            
            	Keepalive interval tolerance in seconds
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: peer_source_addr
            
            	PCE Peer Source Address
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: speaker_entity_id
            
            	PCE speaker entity identifier
            	**type**\: str
            
            	**range:** 0..256
            
            .. attribute:: password
            
            	MD5 password
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            .. attribute:: keychain
            
            	Keychain based authentication
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: precedence
            
            	Precedence order
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.pce_stateful = MplsTe.GlobalAttributes.PceAttributes.PceStateful()
                self.pce_stateful.parent = self
                self.timer = MplsTe.GlobalAttributes.PceAttributes.Timer()
                self.timer.parent = self
                self.peers = MplsTe.GlobalAttributes.PceAttributes.Peers()
                self.peers.parent = self
                self.logging = MplsTe.GlobalAttributes.PceAttributes.Logging()
                self.logging.parent = self
                self.request_timeout = None
                self.reoptimize_period = None
                self.address = None
                self.deadtimer = None
                self.keepalive = None
                self.keepalive_tolerance = None
                self.peer_source_addr = None
                self.speaker_entity_id = None
                self.password = None
                self.keychain = None
                self.precedence = None


            class PceStateful(object):
                """
                PCE Stateful
                
                .. attribute:: stateful_timers
                
                	Configure Stateful PCE (Path Computation Element) timers
                	**type**\: :py:class:`StatefulTimers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers>`
                
                .. attribute:: fast_repair
                
                	Enable reoptimization by PCC after path failures
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: instantiation
                
                	PCE stateful instantiation capability
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: cisco_extension
                
                	Enable processing of PCEP Cisco extension
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: delegation
                
                	Delegate all statically configured tunnels
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: report
                
                	Report all statically configured tunnels
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: enable
                
                	PCE stateful capability
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.stateful_timers = MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers()
                    self.stateful_timers.parent = self
                    self.fast_repair = None
                    self.instantiation = None
                    self.cisco_extension = None
                    self.delegation = None
                    self.report = None
                    self.enable = None


                class StatefulTimers(object):
                    """
                    Configure Stateful PCE (Path Computation
                    Element) timers
                    
                    .. attribute:: redelegation_timeout
                    
                    	Timer for static tunnel redelegation in seconds, default is 180 seconds
                    	**type**\: int
                    
                    	**range:** 0..3600
                    
                    .. attribute:: state_timeout
                    
                    	State timeout for LSPs without delegation in seconds, zero means immediate removal, default is 180 seconds
                    	**type**\: int
                    
                    	**range:** 0..3600
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.redelegation_timeout = None
                        self.state_timeout = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-stateful/Cisco-IOS-XR-mpls-te-cfg:stateful-timers'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.redelegation_timeout is not None:
                            return True

                        if self.state_timeout is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.PceStateful.StatefulTimers']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-stateful'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.stateful_timers is not None and self.stateful_timers._has_data():
                        return True

                    if self.fast_repair is not None:
                        return True

                    if self.instantiation is not None:
                        return True

                    if self.cisco_extension is not None:
                        return True

                    if self.delegation is not None:
                        return True

                    if self.report is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.PceStateful']['meta_info']


            class Timer(object):
                """
                Configure PCE (Path Computation Element)
                timers
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:timer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.Timer']['meta_info']


            class Peers(object):
                """
                Configure PCE peers
                
                .. attribute:: peer
                
                	PCE peer
                	**type**\: list of :py:class:`Peer <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Peers.Peer>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.peer = YList()
                    self.peer.parent = self
                    self.peer.name = 'peer'


                class Peer(object):
                    """
                    PCE peer
                    
                    .. attribute:: pce_peer_address  <key>
                    
                    	Address of PCE Peer
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: enable
                    
                    	Enabled PCE peer (default source address uses local)
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: password
                    
                    	MD5 password
                    	**type**\: str
                    
                    	**pattern:** (!.+)\|([^!].+)
                    
                    .. attribute:: keychain
                    
                    	Keychain based authentication
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: precedence
                    
                    	Precedence order
                    	**type**\: int
                    
                    	**range:** 0..255
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pce_peer_address = None
                        self.enable = None
                        self.password = None
                        self.keychain = None
                        self.precedence = None

                    @property
                    def _common_path(self):
                        if self.pce_peer_address is None:
                            raise YPYDataValidationError('Key property pce_peer_address is None')

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:peers/Cisco-IOS-XR-mpls-te-cfg:peer[Cisco-IOS-XR-mpls-te-cfg:pce-peer-address = ' + str(self.pce_peer_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.pce_peer_address is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.password is not None:
                            return True

                        if self.keychain is not None:
                            return True

                        if self.precedence is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.Peers.Peer']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:peers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.peer is not None:
                        for child_ref in self.peer:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.Peers']['meta_info']


            class Logging(object):
                """
                Configure PCE (Path Computation Element)
                logging feature
                
                .. attribute:: events
                
                	Configure logging events
                	**type**\: :py:class:`Events <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.PceAttributes.Logging.Events>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.events = MplsTe.GlobalAttributes.PceAttributes.Logging.Events()
                    self.events.parent = self


                class Events(object):
                    """
                    Configure logging events
                    
                    .. attribute:: peer_status
                    
                    	Peer status changes logging
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.peer_status = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:logging/Cisco-IOS-XR-mpls-te-cfg:events'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.peer_status is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.Logging.Events']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes/Cisco-IOS-XR-mpls-te-cfg:logging'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.events is not None and self.events._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes.Logging']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:pce-attributes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.pce_stateful is not None and self.pce_stateful._has_data():
                    return True

                if self.timer is not None and self.timer._has_data():
                    return True

                if self.peers is not None and self.peers._has_data():
                    return True

                if self.logging is not None and self.logging._has_data():
                    return True

                if self.request_timeout is not None:
                    return True

                if self.reoptimize_period is not None:
                    return True

                if self.address is not None:
                    return True

                if self.deadtimer is not None:
                    return True

                if self.keepalive is not None:
                    return True

                if self.keepalive_tolerance is not None:
                    return True

                if self.peer_source_addr is not None:
                    return True

                if self.speaker_entity_id is not None:
                    return True

                if self.password is not None:
                    return True

                if self.keychain is not None:
                    return True

                if self.precedence is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.PceAttributes']['meta_info']


        class SoftPreemption(object):
            """
            Soft preemption configuration data
            
            .. attribute:: timeout
            
            	This object sets the timeout in seconds before hard preemption is triggered
            	**type**\: int
            
            	**range:** 1..300
            
            .. attribute:: frr_rewrite
            
            	This object controls whether FRR rewrite during soft preemption is enabled
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: enable
            
            	This object controls whether soft preemption is enabled. This object must be set before setting any other objects under the SoftPreemption class
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.timeout = None
                self.frr_rewrite = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:soft-preemption'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.timeout is not None:
                    return True

                if self.frr_rewrite is not None:
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.SoftPreemption']['meta_info']


        class PathInvalidation(object):
            """
            Path invalidation configuration for all tunnels
            
            .. attribute:: path_invalidation_timeout
            
            	Path Invalidation Timeout
            	**type**\: int
            
            	**range:** 0..60000
            
            .. attribute:: path_invalidation_action
            
            	Path Invalidation Action
            	**type**\: :py:class:`PathInvalidationActionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.PathInvalidationActionEnum>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.path_invalidation_timeout = None
                self.path_invalidation_action = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:path-invalidation'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.path_invalidation_timeout is not None:
                    return True

                if self.path_invalidation_action is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.PathInvalidation']['meta_info']


        class FastReroute(object):
            """
            Configure fast reroute attributes
            
            .. attribute:: timers
            
            	Configure fast reroute timers
            	**type**\: :py:class:`Timers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.FastReroute.Timers>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.timers = MplsTe.GlobalAttributes.FastReroute.Timers()
                self.timers.parent = self


            class Timers(object):
                """
                Configure fast reroute timers
                
                .. attribute:: hold_backup
                
                	Seconds before backup declared UP (0 disables hold\-timer)
                	**type**\: int
                
                	**range:** 0..604800
                
                .. attribute:: promotion
                
                	The value of the promotion timer in seconds
                	**type**\: int
                
                	**range:** 0..604800
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.hold_backup = None
                    self.promotion = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:fast-reroute/Cisco-IOS-XR-mpls-te-cfg:timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.hold_backup is not None:
                        return True

                    if self.promotion is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.FastReroute.Timers']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:fast-reroute'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.timers is not None and self.timers._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.FastReroute']['meta_info']


        class PathSelectionIgnoreOverloadRole(object):
            """
            Path selection to ignore overload node during
            CSPF
            
            .. attribute:: head
            
            	Set if the OL\-bit is to be applied to tunnel heads
            	**type**\: bool
            
            .. attribute:: mid
            
            	Set if the OL\-bit is to be applied to tunnel midpoints
            	**type**\: bool
            
            .. attribute:: tail
            
            	Set if the OL\-bit is to be applied to tunnel tails
            	**type**\: bool
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.head = None
                self.mid = None
                self.tail = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:path-selection-ignore-overload-role'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.head is not None:
                    return True

                if self.mid is not None:
                    return True

                if self.tail is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.PathSelectionIgnoreOverloadRole']['meta_info']


        class AffinityMappings(object):
            """
            Affinity Mapping Table configuration
            
            .. attribute:: affinity_mapping
            
            	Affinity Mapping configuration
            	**type**\: list of :py:class:`AffinityMapping <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.affinity_mapping = YList()
                self.affinity_mapping.parent = self
                self.affinity_mapping.name = 'affinity_mapping'


            class AffinityMapping(object):
                """
                Affinity Mapping configuration
                
                .. attribute:: affinity_name  <key>
                
                	Affinity Name
                	**type**\: str
                
                	**range:** 0..32
                
                .. attribute:: value_type
                
                	Affinity value type
                	**type**\: :py:class:`MplsTeAffinityValueEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeAffinityValueEnum>`
                
                .. attribute:: value
                
                	Affinity Value in Hex number or by Bit position
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.affinity_name = None
                    self.value_type = None
                    self.value = None

                @property
                def _common_path(self):
                    if self.affinity_name is None:
                        raise YPYDataValidationError('Key property affinity_name is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:affinity-mappings/Cisco-IOS-XR-mpls-te-cfg:affinity-mapping[Cisco-IOS-XR-mpls-te-cfg:affinity-name = ' + str(self.affinity_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.affinity_name is not None:
                        return True

                    if self.value_type is not None:
                        return True

                    if self.value is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GlobalAttributes.AffinityMappings.AffinityMapping']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes/Cisco-IOS-XR-mpls-te-cfg:affinity-mappings'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.affinity_mapping is not None:
                    for child_ref in self.affinity_mapping:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GlobalAttributes.AffinityMappings']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:global-attributes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.path_selection_loose_affinities is not None and self.path_selection_loose_affinities._has_data():
                return True

            if self.auto_tunnel is not None and self.auto_tunnel._has_data():
                return True

            if self.secondary_router_ids is not None and self.secondary_router_ids._has_data():
                return True

            if self.srlg is not None and self.srlg._has_data():
                return True

            if self.queues is not None and self.queues._has_data():
                return True

            if self.path_selection_loose_metrics is not None and self.path_selection_loose_metrics._has_data():
                return True

            if self.mib is not None and self.mib._has_data():
                return True

            if self.attribute_set is not None and self.attribute_set._has_data():
                return True

            if self.bfd_over_lsp is not None and self.bfd_over_lsp._has_data():
                return True

            if self.pce_attributes is not None and self.pce_attributes._has_data():
                return True

            if self.soft_preemption is not None and self.soft_preemption._has_data():
                return True

            if self.path_invalidation is not None and self.path_invalidation._has_data():
                return True

            if self.fast_reroute is not None and self.fast_reroute._has_data():
                return True

            if self.path_selection_ignore_overload_role is not None and self.path_selection_ignore_overload_role._has_data():
                return True

            if self.affinity_mappings is not None and self.affinity_mappings._has_data():
                return True

            if self.log_nsr_status is not None:
                return True

            if self.path_selection_tiebreaker is not None:
                return True

            if self.log_issu_status is not None:
                return True

            if self.reoptimize_link_up is not None:
                return True

            if self.reoptimize_delay_cleanup_timer is not None:
                return True

            if self.disable_reoptimize_affinity_failure is not None:
                return True

            if self.maximum_tunnels is not None:
                return True

            if self.link_holddown_timer is not None:
                return True

            if self.path_selection_metric is not None:
                return True

            if self.fault_oam is not None:
                return True

            if self.enable_unequal_load_balancing is not None:
                return True

            if self.log_tail is not None:
                return True

            if self.reoptimize_delay_after_frr_timer is not None:
                return True

            if self.auto_bandwidth_collect_frequency is not None:
                return True

            if self.reopt_delay_path_protect_switchover_timer is not None:
                return True

            if self.log_all is not None:
                return True

            if self.loose_path_retry_period is not None:
                return True

            if self.reoptimize_load_balancing is not None:
                return True

            if self.log_head is not None:
                return True

            if self.path_selection_ignore_overload is not None:
                return True

            if self.graceful_preemption_on_bandwidth_reduction is not None:
                return True

            if self.advertise_explicit_nulls is not None:
                return True

            if self.reoptimize_delay_install_timer is not None:
                return True

            if self.reoptimize_delay_after_affinity_failure_timer is not None:
                return True

            if self.log_frr_protection is not None:
                return True

            if self.reoptimize_timer_frequency is not None:
                return True

            if self.log_mid is not None:
                return True

            if self.log_preemption is not None:
                return True

            if self.path_selection_cost_limit is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.GlobalAttributes']['meta_info']


    class TransportProfile(object):
        """
        MPLS transport profile configuration data
        
        .. attribute:: fault
        
        	Fault management
        	**type**\: :py:class:`Fault <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault>`
        
        .. attribute:: alarm
        
        	Alarm management
        	**type**\: :py:class:`Alarm <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Alarm>`
        
        .. attribute:: bfd
        
        	Configure BFD parameters
        	**type**\: :py:class:`Bfd <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Bfd>`
        
        .. attribute:: midpoints
        
        	MPLS\-TP tunnel mid\-point table
        	**type**\: :py:class:`Midpoints <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints>`
        
        .. attribute:: global_id
        
        	Transport profile global identifier
        	**type**\: int
        
        	**range:** 1..65535
        
        .. attribute:: node_id
        
        	Node identifier in IPv4 address format
        	**type**\: str
        
        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.fault = MplsTe.TransportProfile.Fault()
            self.fault.parent = self
            self.alarm = MplsTe.TransportProfile.Alarm()
            self.alarm.parent = self
            self.bfd = MplsTe.TransportProfile.Bfd()
            self.bfd.parent = self
            self.midpoints = MplsTe.TransportProfile.Midpoints()
            self.midpoints.parent = self
            self.global_id = None
            self.node_id = None


        class Fault(object):
            """
            Fault management
            
            .. attribute:: protection_trigger
            
            	OAM events that trigger protection switching
            	**type**\: :py:class:`ProtectionTrigger <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault.ProtectionTrigger>`
            
            .. attribute:: wait_to_restore_interval
            
            	Waiting time before restoring working LSP
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: refresh_interval
            
            	Periodic refresh interval for fault OAM messages
            	**type**\: int
            
            	**range:** 1..20
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.protection_trigger = MplsTe.TransportProfile.Fault.ProtectionTrigger()
                self.protection_trigger.parent = self
                self.wait_to_restore_interval = None
                self.refresh_interval = None


            class ProtectionTrigger(object):
                """
                OAM events that trigger protection switching
                
                .. attribute:: ldi
                
                	Protection switching due to LDI event
                	**type**\: :py:class:`Ldi <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi>`
                
                .. attribute:: lkr
                
                	Protection switching due to LKR event
                	**type**\: :py:class:`Lkr <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr>`
                
                .. attribute:: ais
                
                	Enable protection switching due to AIS event
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ldi = MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi()
                    self.ldi.parent = self
                    self.lkr = MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr()
                    self.lkr.parent = self
                    self.ais = None


                class Ldi(object):
                    """
                    Protection switching due to LDI event
                    
                    .. attribute:: disable
                    
                    	Disable protection switching due to LDI event
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.disable = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:fault/Cisco-IOS-XR-mpls-te-cfg:protection-trigger/Cisco-IOS-XR-mpls-te-cfg:ldi'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.disable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger.Ldi']['meta_info']


                class Lkr(object):
                    """
                    Protection switching due to LKR event
                    
                    .. attribute:: disable
                    
                    	Disable protection switching due to LKR event
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.disable = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:fault/Cisco-IOS-XR-mpls-te-cfg:protection-trigger/Cisco-IOS-XR-mpls-te-cfg:lkr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.disable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger.Lkr']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:fault/Cisco-IOS-XR-mpls-te-cfg:protection-trigger'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.ldi is not None and self.ldi._has_data():
                        return True

                    if self.lkr is not None and self.lkr._has_data():
                        return True

                    if self.ais is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.TransportProfile.Fault.ProtectionTrigger']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:fault'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.protection_trigger is not None and self.protection_trigger._has_data():
                    return True

                if self.wait_to_restore_interval is not None:
                    return True

                if self.refresh_interval is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.TransportProfile.Fault']['meta_info']


        class Alarm(object):
            """
            Alarm management
            
            .. attribute:: suppress_event
            
            	Suppress all tunnel/LSP alarms
            	**type**\: :py:class:`SuppressEvent <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Alarm.SuppressEvent>`
            
            .. attribute:: soak_time
            
            	Duration of soaking alarms
            	**type**\: int
            
            	**range:** 0..10
            
            .. attribute:: enable_alarm
            
            	Enable Transport Profile Alarm
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.suppress_event = MplsTe.TransportProfile.Alarm.SuppressEvent()
                self.suppress_event.parent = self
                self.soak_time = None
                self.enable_alarm = None


            class SuppressEvent(object):
                """
                Suppress all tunnel/LSP alarms
                
                .. attribute:: disable
                
                	Disable alarm suppression
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.disable = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:alarm/Cisco-IOS-XR-mpls-te-cfg:suppress-event'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.disable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.TransportProfile.Alarm.SuppressEvent']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:alarm'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.suppress_event is not None and self.suppress_event._has_data():
                    return True

                if self.soak_time is not None:
                    return True

                if self.enable_alarm is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.TransportProfile.Alarm']['meta_info']


        class Bfd(object):
            """
            Configure BFD parameters
            
            .. attribute:: min_interval_standby
            
            	Hello interval for standby transport profile LSPs, either in milli\-seconds or in micro\-seconds
            	**type**\: :py:class:`MinIntervalStandby <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Bfd.MinIntervalStandby>`
            
            .. attribute:: min_interval
            
            	Hello interval, either in milli\-seconds or in micro\-seconds
            	**type**\: :py:class:`MinInterval <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Bfd.MinInterval>`
            
            .. attribute:: detection_multiplier_standby
            
            	Detect multiplier for standby transport profile LSP
            	**type**\: int
            
            	**range:** 2..10
            
            .. attribute:: detection_multiplier
            
            	Detect multiplier
            	**type**\: int
            
            	**range:** 2..10
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.min_interval_standby = MplsTe.TransportProfile.Bfd.MinIntervalStandby()
                self.min_interval_standby.parent = self
                self.min_interval = MplsTe.TransportProfile.Bfd.MinInterval()
                self.min_interval.parent = self
                self.detection_multiplier_standby = None
                self.detection_multiplier = None


            class MinIntervalStandby(object):
                """
                Hello interval for standby transport profile
                LSPs, either in milli\-seconds or in
                micro\-seconds
                
                .. attribute:: interval_standby_ms
                
                	Hello interval in milli\-seconds
                	**type**\: int
                
                	**range:** 3..5000
                
                .. attribute:: interval_standby_us
                
                	Hello interval in micro\-seconds
                	**type**\: int
                
                	**range:** 3000..5000000
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interval_standby_ms = None
                    self.interval_standby_us = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:bfd/Cisco-IOS-XR-mpls-te-cfg:min-interval-standby'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interval_standby_ms is not None:
                        return True

                    if self.interval_standby_us is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.TransportProfile.Bfd.MinIntervalStandby']['meta_info']


            class MinInterval(object):
                """
                Hello interval, either in milli\-seconds or in
                micro\-seconds
                
                .. attribute:: interval_ms
                
                	Hello interval in milli\-seconds
                	**type**\: int
                
                	**range:** 3..5000
                
                .. attribute:: interval_us
                
                	Hello interval in micro\-seconds
                	**type**\: int
                
                	**range:** 3000..5000000
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interval_ms = None
                    self.interval_us = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:bfd/Cisco-IOS-XR-mpls-te-cfg:min-interval'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.interval_ms is not None:
                        return True

                    if self.interval_us is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.TransportProfile.Bfd.MinInterval']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:bfd'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.min_interval_standby is not None and self.min_interval_standby._has_data():
                    return True

                if self.min_interval is not None and self.min_interval._has_data():
                    return True

                if self.detection_multiplier_standby is not None:
                    return True

                if self.detection_multiplier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.TransportProfile.Bfd']['meta_info']


        class Midpoints(object):
            """
            MPLS\-TP tunnel mid\-point table
            
            .. attribute:: midpoint
            
            	Transport profile mid\-point identifier
            	**type**\: list of :py:class:`Midpoint <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.midpoint = YList()
                self.midpoint.parent = self
                self.midpoint.name = 'midpoint'


            class Midpoint(object):
                """
                Transport profile mid\-point identifier
                
                .. attribute:: midpoint_name  <key>
                
                	Name of mid\-point
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: source
                
                	Node identifier, tunnel identifier and optional global identifier of the source of the LSP
                	**type**\: :py:class:`Source <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.Source>`
                
                .. attribute:: destination
                
                	Node identifier, tunnel identifier and optional global identifier of the destination of the LSP
                	**type**\: :py:class:`Destination <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.Destination>`
                
                .. attribute:: forward_lsp
                
                	Forward transport profile LSP
                	**type**\: :py:class:`ForwardLsp <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp>`
                
                .. attribute:: reverse_lsp
                
                	none
                	**type**\: :py:class:`ReverseLsp <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp>`
                
                .. attribute:: tunnel_name
                
                	Tunnel Name
                	**type**\: str
                
                .. attribute:: lsp_protect
                
                	Enable LSP protection
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: lsp_id
                
                	Numeric identifier
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.midpoint_name = None
                    self.source = None
                    self.destination = None
                    self.forward_lsp = MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp()
                    self.forward_lsp.parent = self
                    self.reverse_lsp = MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp()
                    self.reverse_lsp.parent = self
                    self.tunnel_name = None
                    self.lsp_protect = None
                    self.lsp_id = None


                class Source(object):
                    """
                    Node identifier, tunnel identifier and
                    optional global identifier of the source of
                    the LSP
                    
                    .. attribute:: node_id
                    
                    	Node identifier in IPv4 address format
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel identifier in numeric value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: global_id
                    
                    	Global identifier in numeric value
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_id = None
                        self.tunnel_id = None
                        self.global_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:source'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.node_id is not None:
                            return True

                        if self.tunnel_id is not None:
                            return True

                        if self.global_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.Source']['meta_info']


                class Destination(object):
                    """
                    Node identifier, tunnel identifier and
                    optional global identifier of the destination
                    of the LSP
                    
                    .. attribute:: node_id
                    
                    	Node identifier in IPv4 address format
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: tunnel_id
                    
                    	Tunnel identifier in numeric value
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    .. attribute:: global_id
                    
                    	Global identifier in numeric value
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node_id = None
                        self.tunnel_id = None
                        self.global_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:destination'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.node_id is not None:
                            return True

                        if self.tunnel_id is not None:
                            return True

                        if self.global_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.Destination']['meta_info']


                class ForwardLsp(object):
                    """
                    Forward transport profile LSP
                    
                    .. attribute:: forward_io_map
                    
                    	Label cross\-connect of forward transport profile LSP
                    	**type**\: :py:class:`ForwardIoMap <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap>`
                    
                    .. attribute:: forward_bandwidth
                    
                    	Bandwidth of forward transport profile LSP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.forward_io_map = None
                        self.forward_bandwidth = None


                    class ForwardIoMap(object):
                        """
                        Label cross\-connect of forward transport
                        profile LSP
                        
                        .. attribute:: in_label
                        
                        	MPLS label
                        	**type**\: int
                        
                        	**range:** 16..4015
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: out_label
                        
                        	Outgoing MPLS label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: out_link
                        
                        	Transport profile identifier of outgoing link
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.in_label = None
                            self.out_label = None
                            self.out_link = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:forward-io-map'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.in_label is not None:
                                return True

                            if self.out_label is not None:
                                return True

                            if self.out_link is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp.ForwardIoMap']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:forward-lsp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.forward_io_map is not None and self.forward_io_map._has_data():
                            return True

                        if self.forward_bandwidth is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ForwardLsp']['meta_info']


                class ReverseLsp(object):
                    """
                    none
                    
                    .. attribute:: reverse_io_map
                    
                    	Label cross\-connect of reverse transport profile LSP
                    	**type**\: :py:class:`ReverseIoMap <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap>`
                    
                    .. attribute:: reverse_bandwidth
                    
                    	Bandwidth of reverse transport profile LSP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.reverse_io_map = None
                        self.reverse_bandwidth = None


                    class ReverseIoMap(object):
                        """
                        Label cross\-connect of reverse transport
                        profile LSP
                        
                        .. attribute:: in_label
                        
                        	MPLS label
                        	**type**\: int
                        
                        	**range:** 16..4015
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: out_label
                        
                        	Outgoing MPLS label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        .. attribute:: out_link
                        
                        	Transport profile identifier of outgoing link
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.in_label = None
                            self.out_label = None
                            self.out_link = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:reverse-io-map'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.in_label is not None:
                                return True

                            if self.out_label is not None:
                                return True

                            if self.out_link is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp.ReverseIoMap']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:reverse-lsp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.reverse_io_map is not None and self.reverse_io_map._has_data():
                            return True

                        if self.reverse_bandwidth is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint.ReverseLsp']['meta_info']

                @property
                def _common_path(self):
                    if self.midpoint_name is None:
                        raise YPYDataValidationError('Key property midpoint_name is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:midpoints/Cisco-IOS-XR-mpls-te-cfg:midpoint[Cisco-IOS-XR-mpls-te-cfg:midpoint-name = ' + str(self.midpoint_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.midpoint_name is not None:
                        return True

                    if self.source is not None and self.source._has_data():
                        return True

                    if self.destination is not None and self.destination._has_data():
                        return True

                    if self.forward_lsp is not None and self.forward_lsp._has_data():
                        return True

                    if self.reverse_lsp is not None and self.reverse_lsp._has_data():
                        return True

                    if self.tunnel_name is not None:
                        return True

                    if self.lsp_protect is not None:
                        return True

                    if self.lsp_id is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.TransportProfile.Midpoints.Midpoint']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile/Cisco-IOS-XR-mpls-te-cfg:midpoints'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.midpoint is not None:
                    for child_ref in self.midpoint:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.TransportProfile.Midpoints']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:transport-profile'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.fault is not None and self.fault._has_data():
                return True

            if self.alarm is not None and self.alarm._has_data():
                return True

            if self.bfd is not None and self.bfd._has_data():
                return True

            if self.midpoints is not None and self.midpoints._has_data():
                return True

            if self.global_id is not None:
                return True

            if self.node_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.TransportProfile']['meta_info']


    class Interfaces(object):
        """
        Configure MPLS TE interfaces
        
        .. attribute:: interface
        
        	Configure an MPLS TE interface
        	**type**\: list of :py:class:`Interface <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Configure an MPLS TE interface
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: transport_profile_link
            
            	MPLS transport profile capable link
            	**type**\: :py:class:`TransportProfileLink <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.TransportProfileLink>`
            
            .. attribute:: lcac
            
            	LCAC specific MPLS interface configuration
            	**type**\: :py:class:`Lcac <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac>`
            
            .. attribute:: global_attributes
            
            	MPLS TE global interface configuration
            	**type**\: :py:class:`GlobalAttributes <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.transport_profile_link = MplsTe.Interfaces.Interface.TransportProfileLink()
                self.transport_profile_link.parent = self
                self.lcac = MplsTe.Interfaces.Interface.Lcac()
                self.lcac.parent = self
                self.global_attributes = MplsTe.Interfaces.Interface.GlobalAttributes()
                self.global_attributes.parent = self


            class TransportProfileLink(object):
                """
                MPLS transport profile capable link
                
                .. attribute:: links
                
                	Transport profile link table
                	**type**\: :py:class:`Links <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.TransportProfileLink.Links>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.links = MplsTe.Interfaces.Interface.TransportProfileLink.Links()
                    self.links.parent = self


                class Links(object):
                    """
                    Transport profile link table
                    
                    .. attribute:: link
                    
                    	Transport profile link
                    	**type**\: list of :py:class:`Link <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.link = YList()
                        self.link.parent = self
                        self.link.name = 'link'


                    class Link(object):
                        """
                        Transport profile link
                        
                        .. attribute:: link_id  <key>
                        
                        	Numeric link identifier
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: next_hop_type
                        
                        	Next hop type
                        	**type**\: :py:class:`LinkNextHopEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.LinkNextHopEnum>`
                        
                        .. attribute:: next_hop_address
                        
                        	Next\-hop address in IPv4 format
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.link_id = None
                            self.next_hop_type = None
                            self.next_hop_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.link_id is None:
                                raise YPYDataValidationError('Key property link_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:link[Cisco-IOS-XR-mpls-te-cfg:link-id = ' + str(self.link_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.link_id is not None:
                                return True

                            if self.next_hop_type is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.Interfaces.Interface.TransportProfileLink.Links.Link']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:links'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.link is not None:
                            for child_ref in self.link:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.TransportProfileLink.Links']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:transport-profile-link'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.links is not None and self.links._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.Interfaces.Interface.TransportProfileLink']['meta_info']


            class Lcac(object):
                """
                LCAC specific MPLS interface configuration
                
                .. attribute:: switchings
                
                	Set the te\-link switching attributes
                	**type**\: :py:class:`Switchings <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Switchings>`
                
                .. attribute:: flood_area
                
                	Set the IGP instance into which this interface is to be flooded (GMPLS only)
                	**type**\: :py:class:`FloodArea <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.FloodArea>`
                
                .. attribute:: attribute_name_xr
                
                	Set the interface attribute names
                	**type**\: :py:class:`AttributeNameXr <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.AttributeNameXr>`
                
                .. attribute:: attribute_names
                
                	Attribute name table
                	**type**\: :py:class:`AttributeNames <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.AttributeNames>`
                
                .. attribute:: srlgs
                
                	Configure SRLG membership for the interface
                	**type**\: :py:class:`Srlgs <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Srlgs>`
                
                .. attribute:: up_thresholds
                
                	Set thresholds for increased resource availability in %
                	**type**\: :py:class:`UpThresholds <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.UpThresholds>`
                
                .. attribute:: down_thresholds
                
                	Set thresholds for decreased resource availability in %
                	**type**\: :py:class:`DownThresholds <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.DownThresholds>`
                
                .. attribute:: bfd
                
                	Enable use of Bidirectional Forwarding Detection
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: fault_oam_lockout
                
                	Lockout protection on the interface for Flex LSP
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: attribute_flags
                
                	Set user defined interface attribute flags
                	**type**\: str
                
                	**pattern:** [0\-9a\-fA\-F]{1,8}
                
                .. attribute:: enable
                
                	Enable MPLS\-TE on the link
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: admin_weight
                
                	Set administrative weight for the interface
                	**type**\: int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.switchings = MplsTe.Interfaces.Interface.Lcac.Switchings()
                    self.switchings.parent = self
                    self.flood_area = MplsTe.Interfaces.Interface.Lcac.FloodArea()
                    self.flood_area.parent = self
                    self.attribute_name_xr = MplsTe.Interfaces.Interface.Lcac.AttributeNameXr()
                    self.attribute_name_xr.parent = self
                    self.attribute_names = MplsTe.Interfaces.Interface.Lcac.AttributeNames()
                    self.attribute_names.parent = self
                    self.srlgs = MplsTe.Interfaces.Interface.Lcac.Srlgs()
                    self.srlgs.parent = self
                    self.up_thresholds = MplsTe.Interfaces.Interface.Lcac.UpThresholds()
                    self.up_thresholds.parent = self
                    self.down_thresholds = MplsTe.Interfaces.Interface.Lcac.DownThresholds()
                    self.down_thresholds.parent = self
                    self.bfd = None
                    self.fault_oam_lockout = None
                    self.attribute_flags = None
                    self.enable = None
                    self.admin_weight = None


                class Switchings(object):
                    """
                    Set the te\-link switching attributes
                    
                    .. attribute:: switching
                    
                    	The te\-link switching attributes
                    	**type**\: list of :py:class:`Switching <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Switchings.Switching>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.switching = YList()
                        self.switching.parent = self
                        self.switching.name = 'switching'


                    class Switching(object):
                        """
                        The te\-link switching attributes
                        
                        .. attribute:: switching_id  <key>
                        
                        	Switching index
                        	**type**\: one of the below types:
                        
                        	**type**\: :py:class:`MplsTeSwitchingIndexEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeSwitchingIndexEnum>`
                        
                        
                        ----
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        
                        ----
                        .. attribute:: encoding
                        
                        	Set the local encoding type
                        	**type**\: :py:class:`MplsTeSwitchingEncodingEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeSwitchingEncodingEnum>`
                        
                        .. attribute:: capability
                        
                        	Set the local switching capability
                        	**type**\: :py:class:`MplsTeSwitchingCapEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeSwitchingCapEnum>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.switching_id = None
                            self.encoding = None
                            self.capability = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.switching_id is None:
                                raise YPYDataValidationError('Key property switching_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:switching[Cisco-IOS-XR-mpls-te-cfg:switching-id = ' + str(self.switching_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.switching_id is not None:
                                return True

                            if self.encoding is not None:
                                return True

                            if self.capability is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.Switchings.Switching']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:switchings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.switching is not None:
                            for child_ref in self.switching:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.Switchings']['meta_info']


                class FloodArea(object):
                    """
                    Set the IGP instance into which this
                    interface is to be flooded (GMPLS only)
                    
                    .. attribute:: igp_type
                    
                    	IGP type
                    	**type**\: :py:class:`MplsLcacFloodingIgpEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsLcacFloodingIgpEnum>`
                    
                    .. attribute:: process_name
                    
                    	Process name
                    	**type**\: str
                    
                    	**range:** 0..32
                    
                    .. attribute:: area_id
                    
                    	Area ID
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.igp_type = None
                        self.process_name = None
                        self.area_id = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:flood-area'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.igp_type is not None:
                            return True

                        if self.process_name is not None:
                            return True

                        if self.area_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.FloodArea']['meta_info']


                class AttributeNameXr(object):
                    """
                    Set the interface attribute names
                    
                    .. attribute:: attribute_name
                    
                    	Array of Attribute Names
                    	**type**\: list of str
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_name = YLeafList()
                        self.attribute_name.parent = self
                        self.attribute_name.name = 'attribute_name'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:attribute-name-xr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_name is not None:
                            for child in self.attribute_name:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNameXr']['meta_info']


                class AttributeNames(object):
                    """
                    Attribute name table
                    
                    .. attribute:: attribute_name
                    
                    	Set the interface attribute names
                    	**type**\: list of :py:class:`AttributeName <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.attribute_name = YList()
                        self.attribute_name.parent = self
                        self.attribute_name.name = 'attribute_name'


                    class AttributeName(object):
                        """
                        Set the interface attribute names
                        
                        .. attribute:: affinity_index  <key>
                        
                        	Specify the entry index
                        	**type**\: int
                        
                        	**range:** 1..9
                        
                        .. attribute:: value
                        
                        	Array of Attribute Names
                        	**type**\: list of str
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.affinity_index = None
                            self.value = YLeafList()
                            self.value.parent = self
                            self.value.name = 'value'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.affinity_index is None:
                                raise YPYDataValidationError('Key property affinity_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:attribute-name[Cisco-IOS-XR-mpls-te-cfg:affinity-index = ' + str(self.affinity_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.affinity_index is not None:
                                return True

                            if self.value is not None:
                                for child in self.value:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNames.AttributeName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:attribute-names'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.attribute_name is not None:
                            for child_ref in self.attribute_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.AttributeNames']['meta_info']


                class Srlgs(object):
                    """
                    Configure SRLG membership for the interface
                    
                    .. attribute:: srlg
                    
                    	SRLG membership number
                    	**type**\: list of :py:class:`Srlg <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.srlg = YList()
                        self.srlg.parent = self
                        self.srlg.name = 'srlg'


                    class Srlg(object):
                        """
                        SRLG membership number
                        
                        .. attribute:: srlg_number  <key>
                        
                        	SRLG membership number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.srlg_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.srlg_number is None:
                                raise YPYDataValidationError('Key property srlg_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:srlg[Cisco-IOS-XR-mpls-te-cfg:srlg-number = ' + str(self.srlg_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.srlg_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.Srlgs.Srlg']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:srlgs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.srlg is not None:
                            for child_ref in self.srlg:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.Srlgs']['meta_info']


                class UpThresholds(object):
                    """
                    Set thresholds for increased resource
                    availability in %
                    
                    .. attribute:: up_threshold
                    
                    	Array of up threshold percentage
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.up_threshold = YLeafList()
                        self.up_threshold.parent = self
                        self.up_threshold.name = 'up_threshold'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:up-thresholds'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.up_threshold is not None:
                            for child in self.up_threshold:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.UpThresholds']['meta_info']


                class DownThresholds(object):
                    """
                    Set thresholds for decreased resource
                    availability in %
                    
                    .. attribute:: down_threshold
                    
                    	Array of down threshold percentage
                    	**type**\: list of int
                    
                    	**range:** 0..100
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.down_threshold = YLeafList()
                        self.down_threshold.parent = self
                        self.down_threshold.name = 'down_threshold'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:down-thresholds'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.down_threshold is not None:
                            for child in self.down_threshold:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.Lcac.DownThresholds']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:lcac'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.switchings is not None and self.switchings._has_data():
                        return True

                    if self.flood_area is not None and self.flood_area._has_data():
                        return True

                    if self.attribute_name_xr is not None and self.attribute_name_xr._has_data():
                        return True

                    if self.attribute_names is not None and self.attribute_names._has_data():
                        return True

                    if self.srlgs is not None and self.srlgs._has_data():
                        return True

                    if self.up_thresholds is not None and self.up_thresholds._has_data():
                        return True

                    if self.down_thresholds is not None and self.down_thresholds._has_data():
                        return True

                    if self.bfd is not None:
                        return True

                    if self.fault_oam_lockout is not None:
                        return True

                    if self.attribute_flags is not None:
                        return True

                    if self.enable is not None:
                        return True

                    if self.admin_weight is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.Interfaces.Interface.Lcac']['meta_info']


            class GlobalAttributes(object):
                """
                MPLS TE global interface configuration
                
                .. attribute:: auto_tunnel
                
                	Auto tunnel configuration
                	**type**\: :py:class:`AutoTunnel <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel>`
                
                .. attribute:: backup_paths
                
                	Configure MPLS TE backup tunnels for this interface
                	**type**\: :py:class:`BackupPaths <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.auto_tunnel = MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel()
                    self.auto_tunnel.parent = self
                    self.backup_paths = MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths()
                    self.backup_paths.parent = self


                class AutoTunnel(object):
                    """
                    Auto tunnel configuration
                    
                    .. attribute:: backup
                    
                    	Auto tunnel backup configuration
                    	**type**\: :py:class:`Backup <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.backup = MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup()
                        self.backup.parent = self


                    class Backup(object):
                        """
                        Auto tunnel backup configuration
                        
                        .. attribute:: exclude
                        
                        	Auto\-tunnel backup exclusion criteria
                        	**type**\: :py:class:`Exclude <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude>`
                        
                        .. attribute:: enable
                        
                        	Enable auto\-tunnel backup on this TE link
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: attribute_set
                        
                        	The name of attribute set to be applied to this auto backup lsp
                        	**type**\: str
                        
                        	**range:** 0..64
                        
                        .. attribute:: next_hop_only
                        
                        	Enable NHOP\-only mode for auto\-tunnel backup on this TE link
                        	**type**\: :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.exclude = MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude()
                            self.exclude.parent = self
                            self.enable = None
                            self.attribute_set = None
                            self.next_hop_only = None


                        class Exclude(object):
                            """
                            Auto\-tunnel backup exclusion criteria
                            
                            .. attribute:: srlg_mode
                            
                            	Set exclude SRLG mode for auto\-tunnel backup on this TE link
                            	**type**\: :py:class:`MplsTesrlgExcludeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTesrlgExcludeEnum>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.srlg_mode = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:exclude'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.srlg_mode is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup.Exclude']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:backup'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.exclude is not None and self.exclude._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.attribute_set is not None:
                                return True

                            if self.next_hop_only is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel.Backup']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:auto-tunnel'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.backup is not None and self.backup._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.AutoTunnel']['meta_info']


                class BackupPaths(object):
                    """
                    Configure MPLS TE backup tunnels for this
                    interface
                    
                    .. attribute:: backup_path
                    
                    	Tunnel interface number
                    	**type**\: list of :py:class:`BackupPath <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.backup_path = YList()
                        self.backup_path.parent = self
                        self.backup_path.name = 'backup_path'


                    class BackupPath(object):
                        """
                        Tunnel interface number
                        
                        .. attribute:: tunnel_number  <key>
                        
                        	Tunnel interface number
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.tunnel_number = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.tunnel_number is None:
                                raise YPYDataValidationError('Key property tunnel_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:backup-path[Cisco-IOS-XR-mpls-te-cfg:tunnel-number = ' + str(self.tunnel_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.tunnel_number is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths.BackupPath']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:backup-paths'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.backup_path is not None:
                            for child_ref in self.backup_path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.Interfaces.Interface.GlobalAttributes.BackupPaths']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:global-attributes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.auto_tunnel is not None and self.auto_tunnel._has_data():
                        return True

                    if self.backup_paths is not None and self.backup_paths._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.Interfaces.Interface.GlobalAttributes']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:interfaces/Cisco-IOS-XR-mpls-te-cfg:interface[Cisco-IOS-XR-mpls-te-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                if self.transport_profile_link is not None and self.transport_profile_link._has_data():
                    return True

                if self.lcac is not None and self.lcac._has_data():
                    return True

                if self.global_attributes is not None and self.global_attributes._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.Interfaces']['meta_info']


    class GmplsNni(object):
        """
        GMPLS\-NNI configuration
        
        .. attribute:: topology_instances
        
        	GMPLS\-NNI topology instance table
        	**type**\: :py:class:`TopologyInstances <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances>`
        
        .. attribute:: tunnel_heads
        
        	GMPLS\-NNI tunnel\-head table
        	**type**\: :py:class:`TunnelHeads <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads>`
        
        .. attribute:: enable_gmpls_nni
        
        	Enable MPLS Traffic Engineering GMPLS\-NNI
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.topology_instances = MplsTe.GmplsNni.TopologyInstances()
            self.topology_instances.parent = self
            self.tunnel_heads = MplsTe.GmplsNni.TunnelHeads()
            self.tunnel_heads.parent = self
            self.enable_gmpls_nni = None


        class TopologyInstances(object):
            """
            GMPLS\-NNI topology instance table
            
            .. attribute:: topology_instance
            
            	GMPLS\-NNI topology instance configuration
            	**type**\: list of :py:class:`TopologyInstance <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.topology_instance = YList()
                self.topology_instance.parent = self
                self.topology_instance.name = 'topology_instance'


            class TopologyInstance(object):
                """
                GMPLS\-NNI topology instance configuration
                
                .. attribute:: igp_type  <key>
                
                	IGP type
                	**type**\: :py:class:`MplsTeIgpProtocolEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTeIgpProtocolEnum>`
                
                .. attribute:: igp_instance_name  <key>
                
                	Name of IGP instance
                	**type**\: str
                
                	**range:** 0..40
                
                .. attribute:: ospf_area_type  <key>
                
                	OSPF area format
                	**type**\: :py:class:`OspfAreaModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OspfAreaModeEnum>`
                
                .. attribute:: ospf_int
                
                	ospf int
                	**type**\: list of :py:class:`OspfInt <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt>`
                
                .. attribute:: ospfip_addr
                
                	ospfip addr
                	**type**\: list of :py:class:`OspfipAddr <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr>`
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.igp_type = None
                    self.igp_instance_name = None
                    self.ospf_area_type = None
                    self.ospf_int = YList()
                    self.ospf_int.parent = self
                    self.ospf_int.name = 'ospf_int'
                    self.ospfip_addr = YList()
                    self.ospfip_addr.parent = self
                    self.ospfip_addr.name = 'ospfip_addr'


                class OspfInt(object):
                    """
                    ospf int
                    
                    .. attribute:: igp_area  <key>
                    
                    	IGP area
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: controllers
                    
                    	GMPLS\-NNI controllers
                    	**type**\: :py:class:`Controllers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.igp_area = None
                        self.controllers = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers()
                        self.controllers.parent = self


                    class Controllers(object):
                        """
                        GMPLS\-NNI controllers
                        
                        .. attribute:: controller
                        
                        	Configure a GMPLS NNI controller
                        	**type**\: list of :py:class:`Controller <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.controller = YList()
                            self.controller.parent = self
                            self.controller.name = 'controller'


                        class Controller(object):
                            """
                            Configure a GMPLS NNI controller
                            
                            .. attribute:: controller_name  <key>
                            
                            	Controller name
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: tti_mode
                            
                            	Set tandem connection monitoring for the interface
                            	**type**\: :py:class:`TtiMode <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode>`
                            
                            .. attribute:: admin_weight
                            
                            	Set administrative weight for the interface
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: enable
                            
                            	Enable GMPLS\-NNI on the link
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.controller_name = None
                                self.tti_mode = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode()
                                self.tti_mode.parent = self
                                self.admin_weight = None
                                self.enable = None


                            class TtiMode(object):
                                """
                                Set tandem connection monitoring for the
                                interface
                                
                                .. attribute:: tti_mode_type
                                
                                	Type of Trail Trace Identifier
                                	**type**\: :py:class:`GmplsttiModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.GmplsttiModeEnum>`
                                
                                .. attribute:: tcmid
                                
                                	Tandem Connection Monitoring ID for the interface
                                	**type**\: int
                                
                                	**range:** 1..6
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tti_mode_type = None
                                    self.tcmid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:tti-mode'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.tti_mode_type is not None:
                                        return True

                                    if self.tcmid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                    return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller.TtiMode']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.controller_name is None:
                                    raise YPYDataValidationError('Key property controller_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:controller[Cisco-IOS-XR-mpls-te-cfg:controller-name = ' + str(self.controller_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.controller_name is not None:
                                    return True

                                if self.tti_mode is not None and self.tti_mode._has_data():
                                    return True

                                if self.admin_weight is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers.Controller']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:controllers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.controller is not None:
                                for child_ref in self.controller:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt.Controllers']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.igp_area is None:
                            raise YPYDataValidationError('Key property igp_area is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:ospf-int[Cisco-IOS-XR-mpls-te-cfg:igp-area = ' + str(self.igp_area) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.igp_area is not None:
                            return True

                        if self.controllers is not None and self.controllers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfInt']['meta_info']


                class OspfipAddr(object):
                    """
                    ospfip addr
                    
                    .. attribute:: address  <key>
                    
                    	Area ID if in IP address format
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: controllers
                    
                    	GMPLS\-NNI controllers
                    	**type**\: :py:class:`Controllers <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.controllers = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers()
                        self.controllers.parent = self


                    class Controllers(object):
                        """
                        GMPLS\-NNI controllers
                        
                        .. attribute:: controller
                        
                        	Configure a GMPLS NNI controller
                        	**type**\: list of :py:class:`Controller <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.controller = YList()
                            self.controller.parent = self
                            self.controller.name = 'controller'


                        class Controller(object):
                            """
                            Configure a GMPLS NNI controller
                            
                            .. attribute:: controller_name  <key>
                            
                            	Controller name
                            	**type**\: str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: tti_mode
                            
                            	Set tandem connection monitoring for the interface
                            	**type**\: :py:class:`TtiMode <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode>`
                            
                            .. attribute:: admin_weight
                            
                            	Set administrative weight for the interface
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: enable
                            
                            	Enable GMPLS\-NNI on the link
                            	**type**\: :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-te-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.controller_name = None
                                self.tti_mode = MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode()
                                self.tti_mode.parent = self
                                self.admin_weight = None
                                self.enable = None


                            class TtiMode(object):
                                """
                                Set tandem connection monitoring for the
                                interface
                                
                                .. attribute:: tti_mode_type
                                
                                	Type of Trail Trace Identifier
                                	**type**\: :py:class:`GmplsttiModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.GmplsttiModeEnum>`
                                
                                .. attribute:: tcmid
                                
                                	Tandem Connection Monitoring ID for the interface
                                	**type**\: int
                                
                                	**range:** 1..6
                                
                                

                                """

                                _prefix = 'mpls-te-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.tti_mode_type = None
                                    self.tcmid = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:tti-mode'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.tti_mode_type is not None:
                                        return True

                                    if self.tcmid is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                    return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller.TtiMode']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.controller_name is None:
                                    raise YPYDataValidationError('Key property controller_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:controller[Cisco-IOS-XR-mpls-te-cfg:controller-name = ' + str(self.controller_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.controller_name is not None:
                                    return True

                                if self.tti_mode is not None and self.tti_mode._has_data():
                                    return True

                                if self.admin_weight is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                                return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers.Controller']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:controllers'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.controller is not None:
                                for child_ref in self.controller:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr.Controllers']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYDataValidationError('Key property address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:ospfip-addr[Cisco-IOS-XR-mpls-te-cfg:address = ' + str(self.address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.controllers is not None and self.controllers._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance.OspfipAddr']['meta_info']

                @property
                def _common_path(self):
                    if self.igp_type is None:
                        raise YPYDataValidationError('Key property igp_type is None')
                    if self.igp_instance_name is None:
                        raise YPYDataValidationError('Key property igp_instance_name is None')
                    if self.ospf_area_type is None:
                        raise YPYDataValidationError('Key property ospf_area_type is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-nni/Cisco-IOS-XR-mpls-te-cfg:topology-instances/Cisco-IOS-XR-mpls-te-cfg:topology-instance[Cisco-IOS-XR-mpls-te-cfg:igp-type = ' + str(self.igp_type) + '][Cisco-IOS-XR-mpls-te-cfg:igp-instance-name = ' + str(self.igp_instance_name) + '][Cisco-IOS-XR-mpls-te-cfg:ospf-area-type = ' + str(self.ospf_area_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.igp_type is not None:
                        return True

                    if self.igp_instance_name is not None:
                        return True

                    if self.ospf_area_type is not None:
                        return True

                    if self.ospf_int is not None:
                        for child_ref in self.ospf_int:
                            if child_ref._has_data():
                                return True

                    if self.ospfip_addr is not None:
                        for child_ref in self.ospfip_addr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GmplsNni.TopologyInstances.TopologyInstance']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-nni/Cisco-IOS-XR-mpls-te-cfg:topology-instances'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.topology_instance is not None:
                    for child_ref in self.topology_instance:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GmplsNni.TopologyInstances']['meta_info']


        class TunnelHeads(object):
            """
            GMPLS\-NNI tunnel\-head table
            
            .. attribute:: tunnel_head
            
            	The configuration for a GMPLS NNI tunnel head\-end
            	**type**\: list of :py:class:`TunnelHead <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead>`
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.tunnel_head = YList()
                self.tunnel_head.parent = self
                self.tunnel_head.name = 'tunnel_head'


            class TunnelHead(object):
                """
                The configuration for a GMPLS NNI tunnel
                head\-end
                
                .. attribute:: tunnel_id  <key>
                
                	Tunnel ID
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: signalled_bandwidth
                
                	The existence of this configuration indicates the signalled bandwidth has been set for the tunnel
                	**type**\: :py:class:`SignalledBandwidth <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth>`
                
                .. attribute:: destination
                
                	The existence of this configuration indicates the destination has been set for the tunnel
                	**type**\: :py:class:`Destination <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination>`
                
                .. attribute:: logging
                
                	Tunnel event logging
                	**type**\: :py:class:`Logging <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging>`
                
                .. attribute:: path_options
                
                	GMPLS NNI path options
                	**type**\: :py:class:`PathOptions <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions>`
                
                .. attribute:: static_uni
                
                	The existence of this configuration indicates the static UNI endpoints have been set for the tunnel
                	**type**\: :py:class:`StaticUni <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni>`
                
                .. attribute:: enable
                
                	The existence of this configuration indicates the a new GMPLS NNI tunnel has been enabled
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: restore_lsp_shutdown
                
                	The existence of this configuration indicates the restore LSP of tunnel is shutdown
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: current_lsp_shutdown
                
                	The existence of this configuration indicates the current/working LSP of tunnel is shutdown
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: payload
                
                	The existence of this configuration indicates the Payload type have been set for the tunnel
                	**type**\: :py:class:`OtnPayloadEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OtnPayloadEnum>`
                
                .. attribute:: standby_lsp_shutdown
                
                	The existence of this configuration indicates the standby/protect LSP of tunnel is shutdown
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: shutdown
                
                	The existence of this configuration indicates the tunnel is shutdown
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: path_protection_attribute_set_profile
                
                	The name of the path\-protection profile to be included in signalling messages
                	**type**\: str
                
                	**range:** 0..64
                
                .. attribute:: record_route
                
                	Record the route used by the tunnel
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: signalled_name
                
                	The name of the tunnel to be included in signalling messages
                	**type**\: str
                
                	**range:** 0..254
                
                

                """

                _prefix = 'mpls-te-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.tunnel_id = None
                    self.signalled_bandwidth = MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth()
                    self.signalled_bandwidth.parent = self
                    self.destination = MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination()
                    self.destination.parent = self
                    self.logging = MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging()
                    self.logging.parent = self
                    self.path_options = MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions()
                    self.path_options.parent = self
                    self.static_uni = MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni()
                    self.static_uni.parent = self
                    self.enable = None
                    self.restore_lsp_shutdown = None
                    self.current_lsp_shutdown = None
                    self.payload = None
                    self.standby_lsp_shutdown = None
                    self.shutdown = None
                    self.path_protection_attribute_set_profile = None
                    self.record_route = None
                    self.signalled_name = None


                class SignalledBandwidth(object):
                    """
                    The existence of this configuration indicates
                    the signalled bandwidth has been set for the
                    tunnel
                    
                    .. attribute:: signalled_bandwidth_type
                    
                    	The g.709 signal type requested
                    	**type**\: :py:class:`OtnSignaledBandwidthEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OtnSignaledBandwidthEnum>`
                    
                    .. attribute:: bitrate
                    
                    	Bitrate value in Kbps for ODUflex framing type
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: od_uflex_framing_type
                    
                    	Framing type in case of ODUflex signal type
                    	**type**\: :py:class:`OtnSignaledBandwidthFlexFramingEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OtnSignaledBandwidthFlexFramingEnum>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.signalled_bandwidth_type = None
                        self.bitrate = None
                        self.od_uflex_framing_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:signalled-bandwidth'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.signalled_bandwidth_type is not None:
                            return True

                        if self.bitrate is not None:
                            return True

                        if self.od_uflex_framing_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.SignalledBandwidth']['meta_info']


                class Destination(object):
                    """
                    The existence of this configuration indicates
                    the destination has been set for the tunnel
                    
                    .. attribute:: destination
                    
                    	IPV4 tunnel destination
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_type
                    
                    	Destination type whether it is unicast or unnumbered
                    	**type**\: :py:class:`OtnDestinationEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OtnDestinationEnum>`
                    
                    .. attribute:: interface_if_index
                    
                    	Interface index of port
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.destination = None
                        self.destination_type = None
                        self.interface_if_index = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:destination'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.destination is not None:
                            return True

                        if self.destination_type is not None:
                            return True

                        if self.interface_if_index is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.Destination']['meta_info']


                class Logging(object):
                    """
                    Tunnel event logging
                    
                    .. attribute:: active_lsp_message
                    
                    	Log all tunnel messages for changes in Active LSP
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: signalling_state_message
                    
                    	Log all tunnel sub\-LSP state messages
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: static_cross_connect_message
                    
                    	Log all tunnel messages for static cross\-connect messages
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: insufficient_bw_message
                    
                    	Log tunnel messages for insufficient bandwidth
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.active_lsp_message = None
                        self.signalling_state_message = None
                        self.static_cross_connect_message = None
                        self.insufficient_bw_message = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:logging'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.active_lsp_message is not None:
                            return True

                        if self.signalling_state_message is not None:
                            return True

                        if self.static_cross_connect_message is not None:
                            return True

                        if self.insufficient_bw_message is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.Logging']['meta_info']


                class PathOptions(object):
                    """
                    GMPLS NNI path options
                    
                    .. attribute:: path_option
                    
                    	The existence of this configuration indicates the path options have been set for the tunnel
                    	**type**\: list of :py:class:`PathOption <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.path_option = YList()
                        self.path_option.parent = self
                        self.path_option.name = 'path_option'


                    class PathOption(object):
                        """
                        The existence of this configuration
                        indicates the path options have been set for
                        the tunnel
                        
                        .. attribute:: preference_level  <key>
                        
                        	Preference level for this path option
                        	**type**\: int
                        
                        	**range:** 1..1000
                        
                        .. attribute:: path_type
                        
                        	The type of the path option
                        	**type**\: :py:class:`MplsTePathOptionEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionEnum>`
                        
                        .. attribute:: path_id
                        
                        	The ID of the IP explicit path associated with this option
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: path_name
                        
                        	The name of the IP explicit path associated with this option
                        	**type**\: str
                        
                        .. attribute:: protected_by_preference_level
                        
                        	Preference level of the protecting explicit path. 
                        	**type**\: int
                        
                        	**range:** 1..1001
                        
                        .. attribute:: restore_by_preference_level
                        
                        	Preference level of the restore path. 
                        	**type**\: int
                        
                        	**range:** 1..1000
                        
                        .. attribute:: lockdown
                        
                        	Lockdown properties
                        	**type**\: :py:class:`MplsTePathOptionPropertyEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTePathOptionPropertyEnum>`
                        
                        

                        """

                        _prefix = 'mpls-te-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.preference_level = None
                            self.path_type = None
                            self.path_id = None
                            self.path_name = None
                            self.protected_by_preference_level = None
                            self.restore_by_preference_level = None
                            self.lockdown = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.preference_level is None:
                                raise YPYDataValidationError('Key property preference_level is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-option[Cisco-IOS-XR-mpls-te-cfg:preference-level = ' + str(self.preference_level) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.preference_level is not None:
                                return True

                            if self.path_type is not None:
                                return True

                            if self.path_id is not None:
                                return True

                            if self.path_name is not None:
                                return True

                            if self.protected_by_preference_level is not None:
                                return True

                            if self.restore_by_preference_level is not None:
                                return True

                            if self.lockdown is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                            return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions.PathOption']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:path-options'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.path_option is not None:
                            for child_ref in self.path_option:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.PathOptions']['meta_info']


                class StaticUni(object):
                    """
                    The existence of this configuration indicates
                    the static UNI endpoints have been set for
                    the tunnel
                    
                    .. attribute:: ingress_controller_name
                    
                    	Name of  ingress controller
                    	**type**\: str
                    
                    	**range:** 0..255
                    
                    .. attribute:: egress_controller_if_index
                    
                    	Interface index of Egress controller
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: ingress_type
                    
                    	Ingress type whether it is xconnect or terminated
                    	**type**\: :py:class:`OtnStaticUniEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OtnStaticUniEnum>`
                    
                    .. attribute:: egress_type
                    
                    	Egress type whether it is xconnect or terminated
                    	**type**\: :py:class:`OtnStaticUniEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.OtnStaticUniEnum>`
                    
                    

                    """

                    _prefix = 'mpls-te-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ingress_controller_name = None
                        self.egress_controller_if_index = None
                        self.ingress_type = None
                        self.egress_type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-te-cfg:static-uni'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.ingress_controller_name is not None:
                            return True

                        if self.egress_controller_if_index is not None:
                            return True

                        if self.ingress_type is not None:
                            return True

                        if self.egress_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                        return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead.StaticUni']['meta_info']

                @property
                def _common_path(self):
                    if self.tunnel_id is None:
                        raise YPYDataValidationError('Key property tunnel_id is None')

                    return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-nni/Cisco-IOS-XR-mpls-te-cfg:tunnel-heads/Cisco-IOS-XR-mpls-te-cfg:tunnel-head[Cisco-IOS-XR-mpls-te-cfg:tunnel-id = ' + str(self.tunnel_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.tunnel_id is not None:
                        return True

                    if self.signalled_bandwidth is not None and self.signalled_bandwidth._has_data():
                        return True

                    if self.destination is not None and self.destination._has_data():
                        return True

                    if self.logging is not None and self.logging._has_data():
                        return True

                    if self.path_options is not None and self.path_options._has_data():
                        return True

                    if self.static_uni is not None and self.static_uni._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.restore_lsp_shutdown is not None:
                        return True

                    if self.current_lsp_shutdown is not None:
                        return True

                    if self.payload is not None:
                        return True

                    if self.standby_lsp_shutdown is not None:
                        return True

                    if self.shutdown is not None:
                        return True

                    if self.path_protection_attribute_set_profile is not None:
                        return True

                    if self.record_route is not None:
                        return True

                    if self.signalled_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                    return meta._meta_table['MplsTe.GmplsNni.TunnelHeads.TunnelHead']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-nni/Cisco-IOS-XR-mpls-te-cfg:tunnel-heads'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.tunnel_head is not None:
                    for child_ref in self.tunnel_head:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.GmplsNni.TunnelHeads']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:gmpls-nni'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.topology_instances is not None and self.topology_instances._has_data():
                return True

            if self.tunnel_heads is not None and self.tunnel_heads._has_data():
                return True

            if self.enable_gmpls_nni is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.GmplsNni']['meta_info']


    class Lcac(object):
        """
        LCAC specific MPLS global configuration
        
        .. attribute:: bfd
        
        	BFD configuration
        	**type**\: :py:class:`Bfd <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Lcac.Bfd>`
        
        .. attribute:: flooding_threshold
        
        	Configure flooding threshold as percentage of total link bandwidth
        	**type**\: :py:class:`FloodingThreshold <ydk.models.mpls.Cisco_IOS_XR_mpls_te_cfg.MplsTe.Lcac.FloodingThreshold>`
        
        .. attribute:: bandwidth_hold_timer
        
        	Bandwidth hold timer value (seconds)
        	**type**\: int
        
        	**range:** 1..300
        
        .. attribute:: delay_preempt_bundle_capacity_timer
        
        	Bundle capacity preemption timer value (seconds)
        	**type**\: int
        
        	**range:** 0..300
        
        .. attribute:: periodic_flooding_timer
        
        	Periodic flooding value (seconds)
        	**type**\: int
        
        	**range:** 0..3600
        
        

        """

        _prefix = 'mpls-te-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.bfd = MplsTe.Lcac.Bfd()
            self.bfd.parent = self
            self.flooding_threshold = MplsTe.Lcac.FloodingThreshold()
            self.flooding_threshold.parent = self
            self.bandwidth_hold_timer = None
            self.delay_preempt_bundle_capacity_timer = None
            self.periodic_flooding_timer = None


        class Bfd(object):
            """
            BFD configuration
            
            .. attribute:: interval
            
            	Hello interval for BFD sessions created by TE
            	**type**\: int
            
            	**range:** 15..200
            
            .. attribute:: detection_multiplier
            
            	Detection multiplier for BFD sessions created by TE
            	**type**\: int
            
            	**range:** 2..10
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interval = None
                self.detection_multiplier = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:lcac/Cisco-IOS-XR-mpls-te-cfg:bfd'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interval is not None:
                    return True

                if self.detection_multiplier is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.Lcac.Bfd']['meta_info']


        class FloodingThreshold(object):
            """
            Configure flooding threshold as percentage of
            total link bandwidth.
            
            .. attribute:: up_stream
            
            	Upward flooding Threshold in percentages of total bandwidth
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: down_stream
            
            	Downward flooding Threshold in percentages of total bandwidth
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'mpls-te-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.up_stream = None
                self.down_stream = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:lcac/Cisco-IOS-XR-mpls-te-cfg:flooding-threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.up_stream is not None:
                    return True

                if self.down_stream is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
                return meta._meta_table['MplsTe.Lcac.FloodingThreshold']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te/Cisco-IOS-XR-mpls-te-cfg:lcac'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.bfd is not None and self.bfd._has_data():
                return True

            if self.flooding_threshold is not None and self.flooding_threshold._has_data():
                return True

            if self.bandwidth_hold_timer is not None:
                return True

            if self.delay_preempt_bundle_capacity_timer is not None:
                return True

            if self.periodic_flooding_timer is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
            return meta._meta_table['MplsTe.Lcac']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-te-cfg:mpls-te'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.diff_serv_traffic_engineering is not None and self.diff_serv_traffic_engineering._has_data():
            return True

        if self.gmpls_uni is not None and self.gmpls_uni._has_data():
            return True

        if self.global_attributes is not None and self.global_attributes._has_data():
            return True

        if self.transport_profile is not None and self.transport_profile._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.gmpls_nni is not None and self.gmpls_nni._has_data():
            return True

        if self.lcac is not None and self.lcac._has_data():
            return True

        if self.enable_traffic_engineering is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_te_cfg as meta
        return meta._meta_table['MplsTe']['meta_info']


