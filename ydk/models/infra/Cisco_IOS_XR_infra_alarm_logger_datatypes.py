""" Cisco_IOS_XR_infra_alarm_logger_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AlarmLoggerSeverityLevelEnum(Enum):
    """
    AlarmLoggerSeverityLevelEnum

    Alarm logger severity level

    .. data:: EMERGENCY = 0

    	Emergency

    .. data:: ALERT = 1

    	Alert

    .. data:: CRITICAL = 2

    	Critical

    .. data:: ERROR = 3

    	Error

    .. data:: WARNING = 4

    	Warning

    .. data:: NOTICE = 5

    	Notice

    .. data:: INFORMATIONAL = 6

    	Informational

    """

    EMERGENCY = 0

    ALERT = 1

    CRITICAL = 2

    ERROR = 3

    WARNING = 4

    NOTICE = 5

    INFORMATIONAL = 6


    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_alarm_logger_datatypes as meta
        return meta._meta_table['AlarmLoggerSeverityLevelEnum']



