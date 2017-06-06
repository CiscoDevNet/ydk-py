""" CISCO_CBP_TARGET_TC_MIB 

This MIB module defines Textual Conventions for
representing targets which have class based policy 
mappings. A target can be any logical interface 
or entity to which a class based policy is able to be 
associated.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CcbptpolicysourcetypeEnum(Enum):
    """
    CcbptpolicysourcetypeEnum

    This Textual Convention represents the types of sources of 

    policies.

    ciscoCbQos(1)      Cisco Class Based QOS policy source.

                       The source of the policy is Cisco Class 

                       Based QOS specific.

    ciscoCbpCommon(2)  Cisco Common Class Based Policy type.

                       The source of the policy is Cisco Common

                       Class Based.

    .. data:: ciscoCbQos = 1

    .. data:: ciscoCbpBase = 2

    """

    ciscoCbQos = 1

    ciscoCbpBase = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CBP_TARGET_TC_MIB as meta
        return meta._meta_table['CcbptpolicysourcetypeEnum']


class CcbpttargetdirectionEnum(Enum):
    """
    CcbpttargetdirectionEnum

    A Textual Convention that represents a direction for a target.

    undirected(1)    Indicates that direction has no meaning 

                     relative to the target.

    input(2)    Refers to the input direction relative to the 

                target.

    output(3)   Refers to the output direction relative to the

                target.

    inOut(4)    Refers to both the input and output directions

                relative to the target.

    .. data:: undirected = 1

    .. data:: input = 2

    .. data:: output = 3

    .. data:: inOut = 4

    """

    undirected = 1

    input = 2

    output = 3

    inOut = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CBP_TARGET_TC_MIB as meta
        return meta._meta_table['CcbpttargetdirectionEnum']


class CcbpttargettypeEnum(Enum):
    """
    CcbpttargettypeEnum

    A Textual Convention that represents a type of target.

    genIf(1)    A target of type interface defined by 

                CcbptTargetIdIf Textual Convention.

    atmPvc(2)   A target of type ATM PVC defined 

                by the CcbptTargetIdAtmPvc Textual Convention.

    frDlci(3)   A target of type Frame Relay DLCI 

                defined by the CcbptTargetIdFrDlci Textual 

                Convention.

    entity(4) A target of type entity defined by the 

              CcbptTargetIdEntity Textual Convention.  This target

              type is used to indicate the attachment of a Class 

              Based Policy to a physical entity.

    fwZone(5)   A target of type Firewall Security Zone

                defined by the CcbptTargetIdNameString 

                Textual Convention.

    fwZonePair(6) A target of type Firewall Security Zone 

                  defined by the CcbptTargetIdNameString

                  Textual Convention.

    aaaSession(7) A target of type AAA Session define by the

                  CcbptTargetIdAaaSession Textual Convention.

    .. data:: genIf = 1

    .. data:: atmPvc = 2

    .. data:: frDlci = 3

    .. data:: entity = 4

    .. data:: fwZone = 5

    .. data:: fwZonePair = 6

    .. data:: aaaSession = 7

    """

    genIf = 1

    atmPvc = 2

    frDlci = 3

    entity = 4

    fwZone = 5

    fwZonePair = 6

    aaaSession = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_CBP_TARGET_TC_MIB as meta
        return meta._meta_table['CcbpttargettypeEnum']



