""" openconfig_aft_types 

Types related to the OpenConfig Abstract Forwarding
Table (AFT) model

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EncapsulationHeaderType(Enum):
    """
    EncapsulationHeaderType (Enum Class)

    Types of tunnel encapsulation that are supported by systems as either

    head\- or tail\-end.

    .. data:: GRE = 0

    	The encapsulation header is a Generic Routing Encapsulation

    	header.

    .. data:: IPV4 = 1

    	The encapsulation header is an IPv4 packet header

    .. data:: IPV6 = 2

    	The encapsulation header is an IPv6 packet header

    .. data:: MPLS = 3

    	The encapsulation header is one or more MPLS labels indicated

    	by the pushed and popped label stack lists.

    """

    GRE = Enum.YLeaf(0, "GRE")

    IPV4 = Enum.YLeaf(1, "IPV4")

    IPV6 = Enum.YLeaf(2, "IPV6")

    MPLS = Enum.YLeaf(3, "MPLS")



