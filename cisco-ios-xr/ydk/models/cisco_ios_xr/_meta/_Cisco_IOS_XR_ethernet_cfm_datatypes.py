


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BandwidthNotificationStateEnum' : _MetaInfoEnum('BandwidthNotificationStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            'ok':'ok',
            'degraded':'degraded',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmAisIntervalEnum' : _MetaInfoEnum('CfmAisIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            '1s':'Y_1s',
            '1m':'Y_1m',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmCcmIntervalEnum' : _MetaInfoEnum('CfmCcmIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            '3.3ms':'Y_3__DOT__3ms',
            '10ms':'Y_10ms',
            '100ms':'Y_100ms',
            '1s':'Y_1s',
            '10s':'Y_10s',
            '1m':'Y_1m',
            '10m':'Y_10m',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
    'CfmMepDirEnum' : _MetaInfoEnum('CfmMepDirEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_cfm_datatypes',
        {
            'up':'up',
            'down':'down',
        }, 'Cisco-IOS-XR-ethernet-cfm-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-datatypes']),
}
