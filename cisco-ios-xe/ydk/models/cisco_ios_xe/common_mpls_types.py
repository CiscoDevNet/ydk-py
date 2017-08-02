""" common_mpls_types 

This module contains a collection of generally useful YANG types
that are specific to MPLS that can be usefully shared
between multiple models.

Terms and Acronyms

MPLS\: Multi Protocol Label Switching

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IetfMplsLabel(Enum):
    """
    IetfMplsLabel

    Temporary type until IETF definition

    .. data:: v4_explicit_null = 0

    	IETF MPLS IPv4 explicit null Label (0)

    .. data:: v6_explicit_null = 2

    	IETF MPLS IPv6 explicit null label (2)

    .. data:: implicit_null = 3

    	IETF MPLS implicit null label (3)

    """

    v4_explicit_null = Enum.YLeaf(0, "v4-explicit-null")

    v6_explicit_null = Enum.YLeaf(2, "v6-explicit-null")

    implicit_null = Enum.YLeaf(3, "implicit-null")



