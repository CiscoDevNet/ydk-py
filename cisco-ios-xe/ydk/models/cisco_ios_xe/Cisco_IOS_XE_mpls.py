""" Cisco_IOS_XE_mpls 

Cisco XE Native Multiprotocol Label Switching (MPLS) Yang model.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LdpDiscoveryAddressType(Enum):
    """
    LdpDiscoveryAddressType

    .. data:: interface = 0

    """

    interface = Enum.YLeaf(0, "interface")


class MplsTeTiebreakerType(Enum):
    """
    MplsTeTiebreakerType

    .. data:: max_fill = 0

    	Use max-fill tiebreaker

    .. data:: min_fill = 1

    	Use min-fill tiebreaker

    .. data:: random = 2

    	Use random tiebreaker

    """

    max_fill = Enum.YLeaf(0, "max-fill")

    min_fill = Enum.YLeaf(1, "min-fill")

    random = Enum.YLeaf(2, "random")



