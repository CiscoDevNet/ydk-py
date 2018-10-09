""" Cisco_IOS_XR_infra_alarm_logger_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AlarmLoggerSeverityLevel(Enum):
    """
    AlarmLoggerSeverityLevel (Enum Class)

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

    emergency = Enum.YLeaf(0, "emergency")

    alert = Enum.YLeaf(1, "alert")

    critical = Enum.YLeaf(2, "critical")

    error = Enum.YLeaf(3, "error")

    warning = Enum.YLeaf(4, "warning")

    notice = Enum.YLeaf(5, "notice")

    informational = Enum.YLeaf(6, "informational")



