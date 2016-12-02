""" Cisco_IOS_XR_ethernet_cfm_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BandwidthNotificationStateEnum(Enum):
    """
    BandwidthNotificationStateEnum

    Bandwidth notification state

    .. data:: ok = 1

    	Link is not degraded

    .. data:: degraded = 2

    	Link is in degraded state

    """

    ok = 1

    degraded = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['BandwidthNotificationStateEnum']


class CfmAisIntervalEnum(Enum):
    """
    CfmAisIntervalEnum

    Cfm ais interval

    .. data:: Y_1s = 4

    	1s

    .. data:: Y_1m = 6

    	1m

    """

    Y_1s = 4

    Y_1m = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmAisIntervalEnum']


class CfmCcmIntervalEnum(Enum):
    """
    CfmCcmIntervalEnum

    Cfm ccm interval

    .. data:: Y_3__DOT__3ms = 1

    	3.3ms

    .. data:: Y_10ms = 2

    	10ms

    .. data:: Y_100ms = 3

    	100ms

    .. data:: Y_1s = 4

    	1s

    .. data:: Y_10s = 5

    	10s

    .. data:: Y_1m = 6

    	1m

    .. data:: Y_10m = 7

    	10m

    """

    Y_3__DOT__3ms = 1

    Y_10ms = 2

    Y_100ms = 3

    Y_1s = 4

    Y_10s = 5

    Y_1m = 6

    Y_10m = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmCcmIntervalEnum']


class CfmMepDirEnum(Enum):
    """
    CfmMepDirEnum

    Cfm mep dir

    .. data:: up = 0

    	Up MEP

    .. data:: down = 1

    	Down MEP

    """

    up = 0

    down = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmMepDirEnum']



