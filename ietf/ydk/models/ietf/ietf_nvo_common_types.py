""" ietf_nvo_common_types 

ietf\-nvo\-common\-types

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AdminstatusEnum(Enum):
    """
    AdminstatusEnum

    AdminStatus

    .. data:: active = 0

    	Active status

    .. data:: inactive = 1

    	Inactive status

    .. data:: partial = 2

    	Partial status

    """

    active = 0

    inactive = 1

    partial = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['AdminstatusEnum']


class ColortypeEnum(Enum):
    """
    ColortypeEnum

    ColorType

    .. data:: nop = 0

    	nop

    .. data:: green = 1

    	green

    .. data:: yellow = 2

    	yellow

    .. data:: red = 3

    	red

    """

    nop = 0

    green = 1

    yellow = 2

    red = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['ColortypeEnum']


class ConnectiondirectionEnum(Enum):
    """
    ConnectiondirectionEnum

    ConnectionDirection

    .. data:: CD_UNI = 0

    	CD-UNI

    .. data:: CD_BI = 1

    	CD-BI

    """

    CD_UNI = 0

    CD_BI = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['ConnectiondirectionEnum']


class DiversitytypeEnum(Enum):
    """
    DiversitytypeEnum

    DiversityType

    .. data:: NOP = 0

    	NOP

    .. data:: PE_DIFF = 1

    	PE-DIFF

    .. data:: MAIN_TP_DIFF = 2

    	MAIN-TP-DIFF

    """

    NOP = 0

    PE_DIFF = 1

    MAIN_TP_DIFF = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['DiversitytypeEnum']


class DomainroleEnum(Enum):
    """
    DomainroleEnum

    DomainRole

    .. data:: nop = 0

    	nop

    .. data:: external = 1

    	external

    .. data:: internal = 2

    	internal

    .. data:: asb = 3

    	asb

    """

    nop = 0

    external = 1

    internal = 2

    asb = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['DomainroleEnum']


class EdgepointroleEnum(Enum):
    """
    EdgepointroleEnum

    EdgePointRole

    .. data:: nop = 0

    	nop

    .. data:: PE = 1

    	PE

    .. data:: P = 2

    	P

    .. data:: UNI = 3

    	UNI

    .. data:: NNI = 4

    	NNI

    .. data:: AsbTP = 5

    	AsbTP

    """

    nop = 0

    PE = 1

    P = 2

    UNI = 3

    NNI = 4

    AsbTP = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['EdgepointroleEnum']


class EthernetactionEnum(Enum):
    """
    EthernetactionEnum

    EthernetAction

    .. data:: nop = 0

    	nop

    .. data:: UNTAG = 1

    	UNTAG

    .. data:: STACKING = 2

    	STACKING

    """

    nop = 0

    UNTAG = 1

    STACKING = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['EthernetactionEnum']


class EthernetencaptypeEnum(Enum):
    """
    EthernetencaptypeEnum

    EthernetEncapType

    .. data:: DEFAULT = 0

    	DEFAULT

    .. data:: DOT1Q = 1

    	DOT1Q

    .. data:: QINQ = 2

    	QINQ

    .. data:: UNTAG = 3

    	UNTAG

    """

    DEFAULT = 0

    DOT1Q = 1

    QINQ = 2

    UNTAG = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['EthernetencaptypeEnum']


class FlowclassifiertypeEnum(Enum):
    """
    FlowclassifiertypeEnum

    FlowClassifierType

    .. data:: nop = 0

    	nop

    .. data:: Y_802dot1p = 1

    	802dot1p

    .. data:: dscp = 2

    	dscp

    .. data:: cos = 3

    	cos

    .. data:: mpls_exp = 4

    	mpls-exp

    .. data:: sourceIP = 5

    	sourceIP

    .. data:: destinationIP = 6

    	destinationIP

    """

    nop = 0

    Y_802dot1p = 1

    dscp = 2

    cos = 3

    mpls_exp = 4

    sourceIP = 5

    destinationIP = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['FlowclassifiertypeEnum']


class LayerrateEnum(Enum):
    """
    LayerrateEnum

    LayerRate

    .. data:: LR_UNKNOW = 0

    	LR_UNKNOW

    .. data:: LR_IP = 1

    	LR_IP

    .. data:: LR_ETHERNET = 2

    	LR_ETHERNET

    .. data:: LR_VXLAN = 3

    	LR_VXLAN

    """

    LR_UNKNOW = 0

    LR_IP = 1

    LR_ETHERNET = 2

    LR_VXLAN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['LayerrateEnum']


class ObjectdirectionEnum(Enum):
    """
    ObjectdirectionEnum

    ObjectDirection

    .. data:: IN = 0

    	IN

    .. data:: OUT = 1

    	OUT

    .. data:: BI_DIRECTION = 2

    	BI-DIRECTION

    """

    IN = 0

    OUT = 1

    BI_DIRECTION = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['ObjectdirectionEnum']


class ObjecttypeEnum(Enum):
    """
    ObjecttypeEnum

    ObjectType

    .. data:: nop = 0

    	nop

    .. data:: SEG_VPN = 1

    	SEG-VPN

    .. data:: TP = 2

    	TP

    .. data:: TPL = 3

    	TPL

    .. data:: NE = 4

    	NE

    .. data:: BUSINESSTYPE = 5

    	BUSINESSTYPE

    .. data:: COMPOSED_VPN = 6

    	COMPOSED-VPN

    .. data:: SUBNETWORK = 7

    	SUBNETWORK

    """

    nop = 0

    SEG_VPN = 1

    TP = 2

    TPL = 3

    NE = 4

    BUSINESSTYPE = 5

    COMPOSED_VPN = 6

    SUBNETWORK = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['ObjecttypeEnum']


class OperstatusEnum(Enum):
    """
    OperstatusEnum

    OperStatus

    .. data:: up = 0

    	Up status

    .. data:: down = 1

    	Down status

    .. data:: degrade = 2

    	Degrade status

    """

    up = 0

    down = 1

    degrade = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['OperstatusEnum']


class QosprioritytypeEnum(Enum):
    """
    QosprioritytypeEnum

    QosPriorityType

    .. data:: nop = 0

    	nop

    .. data:: Y_802dot1p = 1

    	802dot1p

    .. data:: dscp = 2

    	dscp

    .. data:: mplsExp = 3

    	mplsExp

    .. data:: cos = 4

    	cos

    .. data:: ipPrecedence = 5

    	ipPrecedence

    """

    nop = 0

    Y_802dot1p = 1

    dscp = 2

    mplsExp = 3

    cos = 4

    ipPrecedence = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['QosprioritytypeEnum']


class RouteprotocoltypeEnum(Enum):
    """
    RouteprotocoltypeEnum

    RouteProtocolType

    .. data:: staticRouting = 0

    	staticRouting

    .. data:: bgp = 1

    	bgp

    .. data:: rip = 2

    	rip

    .. data:: ospf = 3

    	ospf

    .. data:: isis = 4

    	isis

    """

    staticRouting = 0

    bgp = 1

    rip = 2

    ospf = 3

    isis = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['RouteprotocoltypeEnum']


class SyncstatusEnum(Enum):
    """
    SyncstatusEnum

    SyncStatus

    .. data:: SYNC = 0

    	Sync status

    .. data:: OUT_SYNC = 1

    	Out sync status

    """

    SYNC = 0

    OUT_SYNC = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['SyncstatusEnum']


class TechnologyEnum(Enum):
    """
    TechnologyEnum

    Technology

    .. data:: mpls = 0

    	mpls

    .. data:: rosen_multivpn = 1

    	rosen_multivpn

    .. data:: ng_multivpn = 2

    	ng_multivpn

    .. data:: vxlan_overlay_l3vpn = 3

    	vxlan_overlay_l3vpn

    .. data:: eth_oversdh = 4

    	eth_oversdh

    """

    mpls = 0

    rosen_multivpn = 1

    ng_multivpn = 2

    vxlan_overlay_l3vpn = 3

    eth_oversdh = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['TechnologyEnum']


class TopologyEnum(Enum):
    """
    TopologyEnum

    Topology

    .. data:: full_mesh = 0

    	full-mesh

    .. data:: point_to_multipoint = 1

    	point_to_multipoint

    .. data:: point_to_point = 2

    	point_to_point

    .. data:: complex = 3

    	complex

    """

    full_mesh = 0

    point_to_multipoint = 1

    point_to_point = 2

    complex = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['TopologyEnum']


class ToponoderoleEnum(Enum):
    """
    ToponoderoleEnum

    TopoNodeRole

    .. data:: other = 0

    	other

    .. data:: hub = 1

    	hub

    .. data:: spoke = 2

    	spoke

    """

    other = 0

    hub = 1

    spoke = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['ToponoderoleEnum']


class TptypeEnum(Enum):
    """
    TptypeEnum

    TpType

    .. data:: nop = 0

    	nop

    .. data:: PTP = 1

    	PTP

    .. data:: CTP = 2

    	CTP

    .. data:: TRUNK = 3

    	TRUNK

    .. data:: LoopBack = 4

    	LoopBack

    .. data:: TPPool = 5

    	TPPool

    """

    nop = 0

    PTP = 1

    CTP = 2

    TRUNK = 3

    LoopBack = 4

    TPPool = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_common_types as meta
        return meta._meta_table['TptypeEnum']



