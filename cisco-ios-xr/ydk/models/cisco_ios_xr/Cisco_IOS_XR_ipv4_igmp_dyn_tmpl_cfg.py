""" Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-igmp\-dyn\-tmpl package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DynTmplMulticastMode(Enum):
    """
    DynTmplMulticastMode

    Dyn tmpl multicast mode

    .. data:: qos_correlation = 1

    	QOS Correlation

    .. data:: passive = 2

    	Passive

    """

    qos_correlation = Enum.YLeaf(1, "qos-correlation")

    passive = Enum.YLeaf(2, "passive")



