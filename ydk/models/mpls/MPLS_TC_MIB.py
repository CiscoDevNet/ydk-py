""" MPLS_TC_MIB 

This MIB module defines Textual Conventions and
OBJECT\-IDENTITIES for use in documents defining
management information bases (MIBs) for managing
MPLS networks.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MplsInitialCreationSource_Enum(Enum):
    """
    MplsInitialCreationSource_Enum

    The entity that originally created the object in
    question. The values of this enumeration are
    defined as follows\:
    
    other(1) \- This is used when an entity which has not
    been enumerated in this textual convention but
    which is known by the agent.
    
    snmp(2) \- The Simple Network Management Protocol was
    used to configure this object initially.
    
    ldp(3 \- The Label Distribution Protocol was used to
    configure this object initially.
    
    rsvp(4) \- The Resource Reservation Protocol was used
    to configure this object initially.
    
    crldp(5) \- The Constraint\-Based Label Distribution
    Protocol was used to configure this object
    initially.
    
    policyAgent(6) \- A policy agent (perhaps in
    combination with one of the above protocols) was
    used to configure this object initially.
    
    unknown(7) \- the agent cannot discern which
    component created the object.

    """

    OTHER = 1

    SNMP = 2

    LDP = 3

    RSVP = 4

    CRLDP = 5

    POLICYAGENT = 6

    UNKNOWN = 7


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_MIB as meta
        return meta._meta_table['MplsInitialCreationSource_Enum']


class MplsLdpLabelTypes_Enum(Enum):
    """
    MplsLdpLabelTypes_Enum

    The Layer 2 label types which are defined for MPLS
    LDP/CRLDP are generic(1), atm(2), or
    frameRelay(3).

    """

    GENERIC = 1

    ATM = 2

    FRAMERELAY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _MPLS_TC_MIB as meta
        return meta._meta_table['MplsLdpLabelTypes_Enum']



