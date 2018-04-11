""" openconfig_segment_routing 

Configuration and operational state parameters relating to the
segment routing. This module defines a number of elements which are
instantiated in multiple places throughout the OpenConfig collection
of models.

Particularly\:
 \- SRGB+LB dataplane instances \- directly instantied by SR.
 \- SRGB+LB dataplane reservations \- instantiated within MPLS and future SR
                                 dataplanes.
 \- SR SID advertisements \- instantiated within the relevant IGP.
 \- SR\-specific counters \- instantied within the relevant dataplane.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsLabel(Enum):
    """
    MplsLabel (Enum Class)

    type for MPLS label value encoding

    .. data:: IPV4_EXPLICIT_NULL = 0

    	valid at the bottom of the label stack,

    	indicates that stack must be popped and packet forwarded

    	based on IPv4 header

    .. data:: ROUTER_ALERT = 1

    	allowed anywhere in the label stack except

    	the bottom, local router delivers packet to the local CPU

    	when this label is at the top of the stack

    .. data:: IPV6_EXPLICIT_NULL = 2

    	valid at the bottom of the label stack,

    	indicates that stack must be popped and packet forwarded

    	based on IPv6 header

    .. data:: IMPLICIT_NULL = 3

    	assigned by local LSR but not carried in

    	packets

    .. data:: ENTROPY_LABEL_INDICATOR = 7

    	Entropy label indicator, to allow an LSR

    	to distinguish between entropy label and applicaiton

    	labels RFC 6790

    """

    IPV4_EXPLICIT_NULL = Enum.YLeaf(0, "IPV4_EXPLICIT_NULL")

    ROUTER_ALERT = Enum.YLeaf(1, "ROUTER_ALERT")

    IPV6_EXPLICIT_NULL = Enum.YLeaf(2, "IPV6_EXPLICIT_NULL")

    IMPLICIT_NULL = Enum.YLeaf(3, "IMPLICIT_NULL")

    ENTROPY_LABEL_INDICATOR = Enum.YLeaf(7, "ENTROPY_LABEL_INDICATOR")


class SrDataplaneType(Enum):
    """
    SrDataplaneType (Enum Class)

    Types of data plane that can be used to instantiate a Segment

    Routing block of SIDs.

    .. data:: MPLS = 0

    	The entity uses MPLS labels as Segment Identifiers.

    .. data:: IPV6 = 1

    	The entity uses IPv6 prefixes as Segment Identifiers.

    """

    MPLS = Enum.YLeaf(0, "MPLS")

    IPV6 = Enum.YLeaf(1, "IPV6")



