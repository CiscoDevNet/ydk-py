""" Cisco_IOS_XE_mdt_common_defs 

This module contains a collection of common YANG 
definitions for streaming telemetry.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MdtSubFilterType(Enum):
    """
    MdtSubFilterType

    Types of subscription filters.

    .. data:: sub_filter_type_none = 0

    	Indicates that no filter has been specified.

    .. data:: sub_filter_type_xpath = 1

    	Xpath defining the data items of interest.

    	A limited set of the Xpath 1.0 expressions is

    	supported.

    """

    sub_filter_type_none = Enum.YLeaf(0, "sub-filter-type-none")

    sub_filter_type_xpath = Enum.YLeaf(1, "sub-filter-type-xpath")


class MdtSubUpdateTrigger(Enum):
    """
    MdtSubUpdateTrigger

    Types of subscription update triggers.

    .. data:: sub_upd_trig_none = 0

    	Indicates trigger has not been specified.

    .. data:: sub_upd_trig_periodic = 1

    	Subscription is triggered on a periodic basis.

    .. data:: sub_upd_trig_on_change = 2

    	Subscription is triggered when a value changes.

    """

    sub_upd_trig_none = Enum.YLeaf(0, "sub-upd-trig-none")

    sub_upd_trig_periodic = Enum.YLeaf(1, "sub-upd-trig-periodic")

    sub_upd_trig_on_change = Enum.YLeaf(2, "sub-upd-trig-on-change")



