


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Watchdog.ThresholdMemory' : {
        'meta_info' : _MetaInfoClass('Watchdog.ThresholdMemory',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [('3', '40')], [], 
                '''                Threshold, Range (3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('5', '40')], [], 
                '''                Threshold, Range (5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [('4', '40')], [], 
                '''                Threshold, Range (4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'threshold-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg'
        ),
    },
    'Watchdog' : {
        'meta_info' : _MetaInfoClass('Watchdog',
            False, 
            [
            _MetaInfoClassMember('overload-notification', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable critical event notification
                ''',
                'overload_notification',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('overload-throttle-timeout', ATTRIBUTE, 'int' , None, None, 
                [('5', '120')], [], 
                '''                Watchdog overload throttle timeout configuration
                ''',
                'overload_throttle_timeout',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('restart-deadlock-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable watchdog restart deadlock
                ''',
                'restart_deadlock_disable',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('restart-memoryhog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable watchdog restart memory-hog
                ''',
                'restart_memoryhog_disable',
                'Cisco-IOS-XR-watchd-cfg', False),
            _MetaInfoClassMember('threshold-memory', REFERENCE_CLASS, 'ThresholdMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg', 'Watchdog.ThresholdMemory', 
                [], [], 
                '''                Memory thresholds
                ''',
                'threshold_memory',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'watchdog',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg'
        ),
    },
    'Watchd' : {
        'meta_info' : _MetaInfoClass('Watchd',
            False, 
            [
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Length of timeout in seconds
                ''',
                'timeout',
                'Cisco-IOS-XR-watchd-cfg', False),
            ],
            'Cisco-IOS-XR-watchd-cfg',
            'watchd',
            _yang_ns._namespaces['Cisco-IOS-XR-watchd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg'
        ),
    },
}
_meta_table['Watchdog.ThresholdMemory']['meta_info'].parent =_meta_table['Watchdog']['meta_info']
