""" openconfig_bgp_policy 

This module contains data definitions for BGP routing policy.
It augments the base routing\-policy module with BGP\-specific
options for conditions and actions.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpNextHopTypeEnum(Enum):
    """
    BgpNextHopTypeEnum

    type definition for specifying next\-hop in policy actions

    .. data:: SELF = 0

    	special designation for local router's own

    	address, i.e., next-hop-self

    """

    SELF = 0


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_policy as meta
        return meta._meta_table['BgpNextHopTypeEnum']


class BgpSetCommunityOptionTypeEnum(Enum):
    """
    BgpSetCommunityOptionTypeEnum

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

    ADD = 0

    REMOVE = 1

    REPLACE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_policy as meta
        return meta._meta_table['BgpSetCommunityOptionTypeEnum']


class BgpSetMedTypeEnum(Enum):
    """
    BgpSetMedTypeEnum

    Type definition for specifying how the BGP MED can

    be set in BGP policy actions. The three choices are to set

    the MED directly, increment/decrement using +/\- notation,

    and setting it to the IGP cost (predefined value).

    .. data:: IGP = 0

    	set the MED value to the IGP cost toward the

    	next hop for the route

    """

    IGP = 0


    @staticmethod
    def _meta_info():
        from ydk.models.openconfig._meta import _openconfig_bgp_policy as meta
        return meta._meta_table['BgpSetMedTypeEnum']



