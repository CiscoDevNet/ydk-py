""" Cisco_IOS_XR_qos_ma_bng_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR qos\-ma\-bng package configuration.

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



class Qosl2DataLinkEnum(Enum):
    """
    Qosl2DataLinkEnum

    Qosl2 data link

    .. data:: aal5 = 0

    	ATM adaption layer AAL5

    """

    aal5 = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_qos_ma_bng_cfg as meta
        return meta._meta_table['Qosl2DataLinkEnum']


class Qosl2EncapEnum(Enum):
    """
    Qosl2EncapEnum

    Qosl2 encap

    .. data:: snap_pppoa = 1

    	snap-pppoa encap used between the DSLAM and CPE

    .. data:: mux_pppoa = 2

    	mux-pppoa encap used between the DSLAM and CPE

    .. data:: snap1483_routed = 3

    	snap-1483routed encap used between the DSLAM

    	and CPE

    .. data:: mux1483_routed = 4

    	mux-1483routed encap used between the DSLAM and

    	CPE

    .. data:: snap_rbe = 5

    	snap-rbe encap used between the DSLAM and CPE

    .. data:: snap_dot1qrbe = 6

    	snap-dot1q-rbe encap used between the DSLAM and

    	CPE

    .. data:: mux_rbe = 7

    	mux-rbe encap used between the DSLAM and CPE

    .. data:: mux_dot1qrbe = 8

    	mux-dot1q-rbe encap used between the DSLAM and

    	CPE

    """

    snap_pppoa = 1

    mux_pppoa = 2

    snap1483_routed = 3

    mux1483_routed = 4

    snap_rbe = 5

    snap_dot1qrbe = 6

    mux_rbe = 7

    mux_dot1qrbe = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_qos_ma_bng_cfg as meta
        return meta._meta_table['Qosl2EncapEnum']



