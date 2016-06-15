


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'BandwidthNotificationStateEnum' : _MetaInfoEnum('BandwidthNotificationStateEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            'ok':'OK',
            'degraded':'DEGRADED',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmMepDirEnum' : _MetaInfoEnum('CfmMepDirEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmCcmIntervalEnum' : _MetaInfoEnum('CfmCcmIntervalEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            '3.3ms':'Y_3__DOT__3MS',
            '10ms':'Y_10MS',
            '100ms':'Y_100MS',
            '1s':'Y_1S',
            '10s':'Y_10S',
            '1m':'Y_1M',
            '10m':'Y_10M',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmAisIntervalEnum' : _MetaInfoEnum('CfmAisIntervalEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            '1s':'Y_1S',
            '1m':'Y_1M',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
}
