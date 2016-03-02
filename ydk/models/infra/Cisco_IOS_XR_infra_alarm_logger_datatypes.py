""" Cisco_IOS_XR_infra_alarm_logger_datatypes 

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



class AlarmLoggerSeverityLevel_Enum(Enum):
    """
    AlarmLoggerSeverityLevel_Enum

    Alarm logger severity level

    """

    """

    Emergency

    """
    EMERGENCY = 0

    """

    Alert

    """
    ALERT = 1

    """

    Critical

    """
    CRITICAL = 2

    """

    Error

    """
    ERROR = 3

    """

    Warning

    """
    WARNING = 4

    """

    Notice

    """
    NOTICE = 5

    """

    Informational

    """
    INFORMATIONAL = 6


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_alarm_logger_datatypes as meta
        return meta._meta_table['AlarmLoggerSeverityLevel_Enum']



