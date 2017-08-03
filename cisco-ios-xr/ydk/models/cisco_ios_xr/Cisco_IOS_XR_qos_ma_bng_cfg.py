""" Cisco_IOS_XR_qos_ma_bng_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR qos\-ma\-bng package configuration.

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


class Qosl2DataLink(Enum):
    """
    Qosl2DataLink

    Qosl2 data link

    .. data:: aal5 = 0

    	ATM adaption layer AAL5

    """

    aal5 = Enum.YLeaf(0, "aal5")


class Qosl2Encap(Enum):
    """
    Qosl2Encap

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

    snap_pppoa = Enum.YLeaf(1, "snap-pppoa")

    mux_pppoa = Enum.YLeaf(2, "mux-pppoa")

    snap1483_routed = Enum.YLeaf(3, "snap1483-routed")

    mux1483_routed = Enum.YLeaf(4, "mux1483-routed")

    snap_rbe = Enum.YLeaf(5, "snap-rbe")

    snap_dot1qrbe = Enum.YLeaf(6, "snap-dot1qrbe")

    mux_rbe = Enum.YLeaf(7, "mux-rbe")

    mux_dot1qrbe = Enum.YLeaf(8, "mux-dot1qrbe")



