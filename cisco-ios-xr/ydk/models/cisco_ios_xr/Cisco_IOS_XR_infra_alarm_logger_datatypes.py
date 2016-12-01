""" Cisco_IOS_XR_infra_alarm_logger_datatypes 

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



class AlarmLoggerSeverityLevelEnum(Enum):
    """
    AlarmLoggerSeverityLevelEnum

    Alarm logger severity level

    .. data:: emergency = 0

    	Emergency

    .. data:: alert = 1

    	Alert

    .. data:: critical = 2

    	Critical

    .. data:: error = 3

    	Error

    .. data:: warning = 4

    	Warning

    .. data:: notice = 5

    	Notice

    .. data:: informational = 6

    	Informational

    """

    emergency = 0

    alert = 1

    critical = 2

    error = 3

    warning = 4

    notice = 5

    informational = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_alarm_logger_datatypes as meta
        return meta._meta_table['AlarmLoggerSeverityLevelEnum']



