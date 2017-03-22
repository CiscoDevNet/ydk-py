


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AlarmLoggerSeverityLevelEnum' : _MetaInfoEnum('AlarmLoggerSeverityLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_alarm_logger_datatypes',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
        }, 'Cisco-IOS-XR-infra-alarm-logger-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-infra-alarm-logger-datatypes']),
}
