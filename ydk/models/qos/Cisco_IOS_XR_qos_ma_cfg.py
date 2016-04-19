""" Cisco_IOS_XR_qos_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR qos\-ma package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class QosPolicyAccountEnum(Enum):
    """
    QosPolicyAccountEnum

    Qos policy account

    .. data:: NO_PREFERENCE = 0

    	No account turn off preference

    .. data:: LAYER2 = 1

    	Turn on layer 2 accounting

    .. data:: NO_LAYER2 = 2

    	Turn off layer 2 accounting

    .. data:: USER_DEFINED = 4

    	User defined accounting

    .. data:: LAYER1 = 8

    	Turn on layer 1 accounting

    """

    NO_PREFERENCE = 0

    LAYER2 = 1

    NO_LAYER2 = 2

    USER_DEFINED = 4

    LAYER1 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.qos._meta import _Cisco_IOS_XR_qos_ma_cfg as meta
        return meta._meta_table['QosPolicyAccountEnum']


class Qosl2DataLinkEnum(Enum):
    """
    Qosl2DataLinkEnum

    Qosl2 data link

    .. data:: AAL5 = 0

    	ATM adaption layer AAL5

    """

    AAL5 = 0


    @staticmethod
    def _meta_info():
        from ydk.models.qos._meta import _Cisco_IOS_XR_qos_ma_cfg as meta
        return meta._meta_table['Qosl2DataLinkEnum']


class Qosl2EncapEnum(Enum):
    """
    Qosl2EncapEnum

    Qosl2 encap

    .. data:: SNAP_PPPOA = 1

    	snap-pppoa encap used between the DSLAM and CPE

    .. data:: MUX_PPPOA = 2

    	mux-pppoa encap used between the DSLAM and CPE

    .. data:: SNAP1483_ROUTED = 3

    	snap-1483routed encap used between the DSLAM

    	and CPE

    .. data:: MUX1483_ROUTED = 4

    	mux-1483routed encap used between the DSLAM and

    	CPE

    .. data:: SNAP_RBE = 5

    	snap-rbe encap used between the DSLAM and CPE

    .. data:: SNAP_DOT1QRBE = 6

    	snap-dot1q-rbe encap used between the DSLAM and

    	CPE

    .. data:: MUX_RBE = 7

    	mux-rbe encap used between the DSLAM and CPE

    .. data:: MUX_DOT1QRBE = 8

    	mux-dot1q-rbe encap used between the DSLAM and

    	CPE

    """

    SNAP_PPPOA = 1

    MUX_PPPOA = 2

    SNAP1483_ROUTED = 3

    MUX1483_ROUTED = 4

    SNAP_RBE = 5

    SNAP_DOT1QRBE = 6

    MUX_RBE = 7

    MUX_DOT1QRBE = 8


    @staticmethod
    def _meta_info():
        from ydk.models.qos._meta import _Cisco_IOS_XR_qos_ma_cfg as meta
        return meta._meta_table['Qosl2EncapEnum']



