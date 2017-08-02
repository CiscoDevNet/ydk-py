""" Cisco_IOS_XE_bgp_route_oper 

This module contains a collection of YANG definitions
route for bgp route operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpOriginCode(Enum):
    """
    BgpOriginCode

    BGP origin code

    .. data:: origin_igp = 0

    	BGP origin code IGP

    .. data:: origin_egp = 1

    	BGP origin code EGP

    .. data:: origin_incomplete = 2

    	BGP origin code incomplete

    """

    origin_igp = Enum.YLeaf(0, "origin-igp")

    origin_egp = Enum.YLeaf(1, "origin-egp")

    origin_incomplete = Enum.YLeaf(2, "origin-incomplete")


class BgpRouteFilters(Enum):
    """
    BgpRouteFilters

    BGP route filters

    .. data:: bgp_rf_all = 0

    	BGP all route filter

    .. data:: bgp_rf_cidr_only = 1

    	BGP CIDR only route filter

    .. data:: bgp_rf_label = 2

    	BGP label route filter

    .. data:: bgp_rf_rib_failure = 3

    	BGP RIB failure route filter

    .. data:: bgp_rf_injected = 4

    	BGP injected route filter

    .. data:: bgp_rf_inconsistent = 5

    	BGP inconsistent route filter

    .. data:: bgp_rf_community = 6

    	BGP community route filter

    .. data:: bgp_rf_extcommunity = 7

    	BGP extcommunity route filter

    .. data:: bgp_rf_oer_controlled = 8

    	BGP OER controlled route filter

    .. data:: bgp_rf_pending = 9

    	BGP pending route filter

    """

    bgp_rf_all = Enum.YLeaf(0, "bgp-rf-all")

    bgp_rf_cidr_only = Enum.YLeaf(1, "bgp-rf-cidr-only")

    bgp_rf_label = Enum.YLeaf(2, "bgp-rf-label")

    bgp_rf_rib_failure = Enum.YLeaf(3, "bgp-rf-rib-failure")

    bgp_rf_injected = Enum.YLeaf(4, "bgp-rf-injected")

    bgp_rf_inconsistent = Enum.YLeaf(5, "bgp-rf-inconsistent")

    bgp_rf_community = Enum.YLeaf(6, "bgp-rf-community")

    bgp_rf_extcommunity = Enum.YLeaf(7, "bgp-rf-extcommunity")

    bgp_rf_oer_controlled = Enum.YLeaf(8, "bgp-rf-oer-controlled")

    bgp_rf_pending = Enum.YLeaf(9, "bgp-rf-pending")


class BgpRpkiStatus(Enum):
    """
    BgpRpkiStatus

    BGP RPKI status

    .. data:: rpki_valid = 0

    .. data:: rpki_invalid = 1

    .. data:: rpki_not_found = 2

    .. data:: rpki_not_enabled = 3

    .. data:: rpki_illegal = 4

    """

    rpki_valid = Enum.YLeaf(0, "rpki-valid")

    rpki_invalid = Enum.YLeaf(1, "rpki-invalid")

    rpki_not_found = Enum.YLeaf(2, "rpki-not-found")

    rpki_not_enabled = Enum.YLeaf(3, "rpki-not-enabled")

    rpki_illegal = Enum.YLeaf(4, "rpki-illegal")



