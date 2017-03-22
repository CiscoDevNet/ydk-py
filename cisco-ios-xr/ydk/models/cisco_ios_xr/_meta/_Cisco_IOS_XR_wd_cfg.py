


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
                '''                Threshold, Range(3, severe)
                ''',
                'critical',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('5', '40')], [], 
                '''                Threshold, Range(5, 40)
                ''',
                'minor',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [('4', '40')], [], 
                '''                Threshold, Range(4, minor)
                ''',
                'severe',
                'Cisco-IOS-XR-wd-cfg', False),
            ],
            'Cisco-IOS-XR-wd-cfg',
            'threshold-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_cfg'
        ),
    },
    'Watchdog' : {
        'meta_info' : _MetaInfoClass('Watchdog',
            False, 
            [
            _MetaInfoClassMember('monitor-cpuhog-timeout', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Watchdog monitor cpu-hog persistent timeout
                configuration
                ''',
                'monitor_cpuhog_timeout',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('monitor-procnto-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '3600')], [], 
                '''                Watchdog monitor procnto timeout configuration
                ''',
                'monitor_procnto_timeout',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('monitor-qnet-timeout', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Watchdog monitor transport qnet timeout
                ''',
                'monitor_qnet_timeout',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('overload-notification', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable critical event notification
                ''',
                'overload_notification',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('overload-throttle-timeout', ATTRIBUTE, 'int' , None, None, 
                [('5', '120')], [], 
                '''                Watchdog overload throttle timeout configuration
                ''',
                'overload_throttle_timeout',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('restart-cpuhog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable watchdog restart cpu-hog
                ''',
                'restart_cpuhog_disable',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('restart-deadlock-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable watchdog restart deadlock
                ''',
                'restart_deadlock_disable',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('restart-memoryhog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable watchdog restart memory-hog
                ''',
                'restart_memoryhog_disable',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('threshold-memory', REFERENCE_CLASS, 'ThresholdMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_cfg', 'Watchdog.ThresholdMemory', 
                [], [], 
                '''                Memory thresholds
                ''',
                'threshold_memory',
                'Cisco-IOS-XR-wd-cfg', False),
            _MetaInfoClassMember('threshold-memory-switchover', ATTRIBUTE, 'int' , None, None, 
                [('2', '4')], [], 
                '''                switchover the RP at configured memory state
                ''',
                'threshold_memory_switchover',
                'Cisco-IOS-XR-wd-cfg', False),
            ],
            'Cisco-IOS-XR-wd-cfg',
            'watchdog',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_cfg'
        ),
    },
}
_meta_table['Watchdog.ThresholdMemory']['meta_info'].parent =_meta_table['Watchdog']['meta_info']
