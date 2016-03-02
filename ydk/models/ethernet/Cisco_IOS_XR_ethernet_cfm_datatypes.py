""" Cisco_IOS_XR_ethernet_cfm_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BandwidthNotificationState_Enum(Enum):
    """
    BandwidthNotificationState_Enum

    Bandwidth notification state

    """

    """

    Link is not degraded

    """
    OK = 1

    """

    Link is in degraded state

    """
    DEGRADED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['BandwidthNotificationState_Enum']


class CfmAisInterval_Enum(Enum):
    """
    CfmAisInterval_Enum

    Cfm ais interval

    """

    """

    1s

    """
    Y_1S = 4

    """

    1m

    """
    Y_1M = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmAisInterval_Enum']


class CfmCcmInterval_Enum(Enum):
    """
    CfmCcmInterval_Enum

    Cfm ccm interval

    """

    """

    3.3ms

    """
    Y_3__DOT__3MS = 1

    """

    10ms

    """
    Y_10MS = 2

    """

    100ms

    """
    Y_100MS = 3

    """

    1s

    """
    Y_1S = 4

    """

    10s

    """
    Y_10S = 5

    """

    1m

    """
    Y_1M = 6

    """

    10m

    """
    Y_10M = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmCcmInterval_Enum']


class CfmMepDir_Enum(Enum):
    """
    CfmMepDir_Enum

    Cfm mep dir

    """

    """

    Up MEP

    """
    UP = 0

    """

    Down MEP

    """
    DOWN = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_ethernet_cfm_datatypes as meta
        return meta._meta_table['CfmMepDir_Enum']



