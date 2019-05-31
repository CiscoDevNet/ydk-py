""" Cisco_IOS_XR_infra_xtc_agent_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-xtc\-agent package configuration.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class XtcAffinityRule(Enum):
    """
    XtcAffinityRule (Enum Class)

    Xtc affinity rule

    .. data:: affinity_include_all = 0

    	Include-all affinity rule

    .. data:: affinity_exclude_any = 1

    	Exclude-any affinity rule

    .. data:: affinity_include_any = 2

    	Include-any affinity rule

    """

    affinity_include_all = Enum.YLeaf(0, "affinity-include-all")

    affinity_exclude_any = Enum.YLeaf(1, "affinity-exclude-any")

    affinity_include_any = Enum.YLeaf(2, "affinity-include-any")


class XtcMetricValue(Enum):
    """
    XtcMetricValue (Enum Class)

    Xtc metric value

    .. data:: relative = 1

    	Relative metric value

    .. data:: absolute = 2

    	Absolute metric value

    """

    relative = Enum.YLeaf(1, "relative")

    absolute = Enum.YLeaf(2, "absolute")



