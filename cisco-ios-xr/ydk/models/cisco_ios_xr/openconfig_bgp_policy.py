""" openconfig_bgp_policy 

This module contains data definitions for BGP routing policy.
It augments the base routing\-policy module with BGP\-specific
options for conditions and actions.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpNextHopType(Enum):
    """
    BgpNextHopType

    type definition for specifying next\-hop in policy actions

    .. data:: SELF = 0

    	special designation for local router's own

    	address, i.e., next-hop-self

    """

    SELF = Enum.YLeaf(0, "SELF")


class BgpSetCommunityOptionType(Enum):
    """
    BgpSetCommunityOptionType

    Type definition for options when setting the community

    attribute in a policy action

    .. data:: ADD = 0

    	add the specified communities to the existing

    	community attribute

    .. data:: REMOVE = 1

    	remove the specified communities from the

    	existing community attribute

    .. data:: REPLACE = 2

    	replace the existing community attribute with

    	the specified communities. If an empty set is

    	specified, this removes the community attribute

    	from the route.

    """

    ADD = Enum.YLeaf(0, "ADD")

    REMOVE = Enum.YLeaf(1, "REMOVE")

    REPLACE = Enum.YLeaf(2, "REPLACE")


class BgpSetMedType(Enum):
    """
    BgpSetMedType

    Type definition for specifying how the BGP MED can

    be set in BGP policy actions. The three choices are to set

    the MED directly, increment/decrement using +/\- notation,

    and setting it to the IGP cost (predefined value).

    .. data:: IGP = 0

    	set the MED value to the IGP cost toward the

    	next hop for the route

    """

    IGP = Enum.YLeaf(0, "IGP")



