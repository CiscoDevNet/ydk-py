""" MPLS_TC_MIB 

This MIB module defines Textual Conventions and
OBJECT\-IDENTITIES for use in documents defining
management information bases (MIBs) for managing
MPLS networks.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Mplsinitialcreationsource(Enum):
    """
    Mplsinitialcreationsource

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

    .. data:: other = 1

    .. data:: snmp = 2

    .. data:: ldp = 3

    .. data:: rsvp = 4

    .. data:: crldp = 5

    .. data:: policyAgent = 6

    .. data:: unknown = 7

    """

    other = Enum.YLeaf(1, "other")

    snmp = Enum.YLeaf(2, "snmp")

    ldp = Enum.YLeaf(3, "ldp")

    rsvp = Enum.YLeaf(4, "rsvp")

    crldp = Enum.YLeaf(5, "crldp")

    policyAgent = Enum.YLeaf(6, "policyAgent")

    unknown = Enum.YLeaf(7, "unknown")


class Mplsldplabeltypes(Enum):
    """
    Mplsldplabeltypes

    The Layer 2 label types which are defined for MPLS

    LDP/CRLDP are generic(1), atm(2), or

    frameRelay(3).

    .. data:: generic = 1

    .. data:: atm = 2

    .. data:: frameRelay = 3

    """

    generic = Enum.YLeaf(1, "generic")

    atm = Enum.YLeaf(2, "atm")

    frameRelay = Enum.YLeaf(3, "frameRelay")



