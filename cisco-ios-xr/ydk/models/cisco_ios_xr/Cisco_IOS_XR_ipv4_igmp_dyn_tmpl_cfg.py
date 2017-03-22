""" Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-igmp\-dyn\-tmpl package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class DynTmplMulticastModeEnum(Enum):
    """
    DynTmplMulticastModeEnum

    Dyn tmpl multicast mode

    .. data:: qos_correlation = 1

    	QOS Correlation

    .. data:: passive = 2

    	Passive

    """

    qos_correlation = 1

    passive = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_igmp_dyn_tmpl_cfg as meta
        return meta._meta_table['DynTmplMulticastModeEnum']



