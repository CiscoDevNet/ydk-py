""" ietf_nvo_qos_types 

ietf\-nvo\-qos\-types

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class ActiontypeEnum(Enum):
    """
    ActiontypeEnum

    ActionType

    .. data:: nop = 0

    	nop

    .. data:: bandwidth = 1

    	bandwidth

    .. data:: pass_ = 2

    	pass

    .. data:: discard = 3

    	discard

    .. data:: remark = 4

    	remark

    .. data:: redirect = 5

    	redirect

    .. data:: recolor = 6

    	recolor

    .. data:: addRt = 7

    	addRt

    """

    nop = 0

    bandwidth = 1

    pass_ = 2

    discard = 3

    remark = 4

    redirect = 5

    recolor = 6

    addRt = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['ActiontypeEnum']


class ClassifierdetailtypeEnum(Enum):
    """
    ClassifierdetailtypeEnum

    classifierDetailType

    .. data:: nop = 0

    	nop

    .. data:: ipPrefixList = 1

    	ipPrefixList

    """

    nop = 0

    ipPrefixList = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['ClassifierdetailtypeEnum']


class ClassifiertypeEnum(Enum):
    """
    ClassifiertypeEnum

    ClassifierType

    .. data:: Y_802dot1p = 0

    	802dot1p

    .. data:: dscp = 1

    	dscp

    .. data:: cos = 2

    	cos

    .. data:: mpls_exp = 3

    	mpls-exp

    .. data:: sourceIP = 4

    	sourceIP

    .. data:: destinationIP = 5

    	destinationIP

    """

    Y_802dot1p = 0

    dscp = 1

    cos = 2

    mpls_exp = 3

    sourceIP = 4

    destinationIP = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['ClassifiertypeEnum']


class DatakindEnum(Enum):
    """
    DatakindEnum

    dataKind

    .. data:: green = 0

    	green

    .. data:: yellow = 1

    	yellow

    .. data:: red = 2

    	red

    .. data:: all = 3

    	all

    """

    green = 0

    yellow = 1

    red = 2

    all = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['DatakindEnum']


class FlowclassifiertypeEnum(Enum):
    """
    FlowclassifiertypeEnum

    flowClassifierType

    .. data:: nop = 0

    	nop

    .. data:: aluFlowClassifier = 1

    	aluFlowClassifier

    """

    nop = 0

    aluFlowClassifier = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['FlowclassifiertypeEnum']


class MatchmodetypeEnum(Enum):
    """
    MatchmodetypeEnum

    MatchModeType

    .. data:: nop = 0

    	nop

    .. data:: match = 1

    	match

    .. data:: unmatch = 2

    	unmatch

    """

    nop = 0

    match = 1

    unmatch = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['MatchmodetypeEnum']


class OrchpermittypeEnum(Enum):
    """
    OrchpermittypeEnum

    OrchPermitType

    .. data:: readUse = 0

    	readUse

    .. data:: crud = 1

    	crud

    """

    readUse = 0

    crud = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['OrchpermittypeEnum']


class ProfiletypeEnum(Enum):
    """
    ProfiletypeEnum

    profileType

    .. data:: profile = 0

    	profile

    """

    profile = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['ProfiletypeEnum']


class QosbehaviordirectiontypeEnum(Enum):
    """
    QosbehaviordirectiontypeEnum

    qosBehaviorDirectionType

    .. data:: upstream = 0

    	upstream

    .. data:: downstream = 1

    	downstream

    .. data:: bidirectional = 2

    	bidirectional

    """

    upstream = 0

    downstream = 1

    bidirectional = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['QosbehaviordirectiontypeEnum']


class QosbehaviortypeEnum(Enum):
    """
    QosbehaviortypeEnum

    qosBehaviorType

    .. data:: qosCarBehavior = 0

    	qosCarBehavior

    .. data:: qosServiceChainBehavior = 1

    	qosServiceChainBehavior

    """

    qosCarBehavior = 0

    qosServiceChainBehavior = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['QosbehaviortypeEnum']


class QosconfigtypeEnum(Enum):
    """
    QosconfigtypeEnum

    QosConfigType

    .. data:: nop = 0

    	nop

    .. data:: template = 1

    	template

    .. data:: agile = 2

    	agile

    """

    nop = 0

    template = 1

    agile = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['QosconfigtypeEnum']


class QosdetailtypeEnum(Enum):
    """
    QosdetailtypeEnum

    QosDetailType

    .. data:: nop = 0

    	nop

    .. data:: car = 1

    	car

    .. data:: qosProfile = 2

    	qosProfile

    .. data:: diffServDomain = 3

    	diffServDomain

    .. data:: diffServ = 4

    	diffServ

    .. data:: aluDiffServ = 5

    	aluDiffServ

    """

    nop = 0

    car = 1

    qosProfile = 2

    diffServDomain = 3

    diffServ = 4

    aluDiffServ = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['QosdetailtypeEnum']


class QosprioritytypeEnum(Enum):
    """
    QosprioritytypeEnum

    qosPriorityType

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
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['QosprioritytypeEnum']


class RuleoperatortypeEnum(Enum):
    """
    RuleoperatortypeEnum

    ruleOperatorType

    .. data:: and_ = 0

    	and

    .. data:: or_ = 1

    	or

    """

    and_ = 0

    or_ = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['RuleoperatortypeEnum']


class RuletypeEnum(Enum):
    """
    RuletypeEnum

    ruleType

    .. data:: Y_802dot1p = 0

    	802dot1p

    .. data:: dscp = 1

    	dscp

    .. data:: cos = 2

    	cos

    .. data:: mpls_exp = 3

    	mpls_exp

    .. data:: source_ip = 4

    	source_ip

    .. data:: destination_ip = 5

    	destination_ip

    """

    Y_802dot1p = 0

    dscp = 1

    cos = 2

    mpls_exp = 3

    source_ip = 4

    destination_ip = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ietf._meta import _ietf_nvo_qos_types as meta
        return meta._meta_table['RuletypeEnum']



