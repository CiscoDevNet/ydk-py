""" cisco_ospf 

This YANG module defines the Cisco OSPF common 
yang model
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AccessListInOutType(Enum):
    """
    AccessListInOutType

    Access list in and out

    .. data:: in_ = 0

    	Filter incoming routing updates

    .. data:: out = 1

    	Filter outgoing routing updates

    """

    in_ = Enum.YLeaf(0, "in")

    out = Enum.YLeaf(1, "out")


class OspfExternalType(Enum):
    """
    OspfExternalType

    external route types

    .. data:: Y_1 = 0

    	type 1

    .. data:: Y_2 = 1

    	type 2

    """

    Y_1 = Enum.YLeaf(0, "1")

    Y_2 = Enum.YLeaf(1, "2")


class OspfLogAdj(Enum):
    """
    OspfLogAdj

    Ospf log adjacency changes

    .. data:: enable = 0

    	Enable log adjacency brief

    .. data:: detail = 1

    	Enable log adjcency detail

    .. data:: disable = 2

    	disable log adjacency

    """

    enable = Enum.YLeaf(0, "enable")

    detail = Enum.YLeaf(1, "detail")

    disable = Enum.YLeaf(2, "disable")


class PrefixApplicability(Enum):
    """
    PrefixApplicability

    Ospf uloop avoidance

    .. data:: protected = 1

    	Protected prefixes only

    .. data:: all = 2

    	All prefixes

    """

    protected = Enum.YLeaf(1, "protected")

    all = Enum.YLeaf(2, "all")



