


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'AlarmLoggerSeverityLevelEnum' : _MetaInfoEnum('AlarmLoggerSeverityLevelEnum', 'ydk.models.infra.Cisco_IOS_XR_infra_alarm_logger_datatypes',
        {
            'emergency':'EMERGENCY',
            'alert':'ALERT',
            'critical':'CRITICAL',
            'error':'ERROR',
            'warning':'WARNING',
            'notice':'NOTICE',
            'informational':'INFORMATIONAL',
        }, 'Cisco-IOS-XR-infra-alarm-logger-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-datatypes']),
}
