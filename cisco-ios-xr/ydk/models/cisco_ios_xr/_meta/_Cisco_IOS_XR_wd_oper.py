


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OverloadCtrlNotifEnum' : _MetaInfoEnum('OverloadCtrlNotifEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-wd-oper', _yang_ns._namespaces['Cisco-IOS-XR-wd-oper']),
    'MemoryStateEnum' : _MetaInfoEnum('MemoryStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper',
        {
            'unknown':'unknown',
            'normal':'normal',
            'minor':'minor',
            'severe':'severe',
            'critical':'critical',
        }, 'Cisco-IOS-XR-wd-oper', _yang_ns._namespaces['Cisco-IOS-XR-wd-oper']),
    'Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Critical memory in bytes
                ''',
                'critical',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minor memory threshold in bytes
                ''',
                'minor',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Severe memory threshold in bytes
                ''',
                'severe',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'configured-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.ThresholdMemory.Default.Memory' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.ThresholdMemory.Default.Memory',
            False, 
            [
            _MetaInfoClassMember('free-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Free memory in bytes
                ''',
                'free_memory',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('memory-state', REFERENCE_ENUM_CLASS, 'MemoryStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'MemoryStateEnum', 
                [], [], 
                '''                State of memory
                ''',
                'memory_state',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('physical-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Physical memory in bytes
                ''',
                'physical_memory',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'memory',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.ThresholdMemory.Default' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.ThresholdMemory.Default',
            False, 
            [
            _MetaInfoClassMember('configured-memory', REFERENCE_CLASS, 'ConfiguredMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory', 
                [], [], 
                '''                Configured memory
                ''',
                'configured_memory',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('memory', REFERENCE_CLASS, 'Memory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.ThresholdMemory.Default.Memory', 
                [], [], 
                '''                Memory Information
                ''',
                'memory',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'default',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.ThresholdMemory.Configured' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.ThresholdMemory.Configured',
            False, 
            [
            _MetaInfoClassMember('critical', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Critical memory in bytes
                ''',
                'critical',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minor memory threshold in bytes
                ''',
                'minor',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('severe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Severe memory threshold in bytes
                ''',
                'severe',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'configured',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.ThresholdMemory' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.ThresholdMemory',
            False, 
            [
            _MetaInfoClassMember('configured', REFERENCE_CLASS, 'Configured' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.ThresholdMemory.Configured', 
                [], [], 
                '''                Memory configured by user
                ''',
                'configured',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.ThresholdMemory.Default', 
                [], [], 
                '''                System default memory
                ''',
                'default',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'threshold-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.MemoryState' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.MemoryState',
            False, 
            [
            _MetaInfoClassMember('free-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Free memory in bytes
                ''',
                'free_memory',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('memory-state', REFERENCE_ENUM_CLASS, 'MemoryStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'MemoryStateEnum', 
                [], [], 
                '''                State of memory
                ''',
                'memory_state',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('physical-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Physical memory in bytes
                ''',
                'physical_memory',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'memory-state',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.OverloadState.CurrentThrottle' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.OverloadState.CurrentThrottle',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 25)], [], 
                '''                Current throttle start time in format 
                :day-of-week month date-of-month HH:MM:SS year
                eg: Thu Feb 1 18:32:14 2011
                ''',
                'start_time',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('throttle-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current throttle duration in seconds
                ''',
                'throttle_duration',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'current-throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.OverloadState.LastThrottle' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.OverloadState.LastThrottle',
            False, 
            [
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 25)], [], 
                '''                Last throttle start time in format :day-of-week
                month date-of-month HH:MM:SS year eg: Thu Feb 1
                18:32:14 2011
                ''',
                'start_time',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('stop-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 25)], [], 
                '''                Last throttle stop time in format :day-of-week
                month date-of-month HH:MM:SS year eg: Thu Feb 1
                18:32:14 2011
                ''',
                'stop_time',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('throttle-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last throttle duration in seconds
                ''',
                'throttle_duration',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'last-throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node.OverloadState' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node.OverloadState',
            False, 
            [
            _MetaInfoClassMember('configured-wdsysmon-throttle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured resmon throttle
                ''',
                'configured_wdsysmon_throttle',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('current-throttle', REFERENCE_CLASS, 'CurrentThrottle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.OverloadState.CurrentThrottle', 
                [], [], 
                '''                Current throttle information
                ''',
                'current_throttle',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('default-wdsysmon-throttle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default resmon throttle
                ''',
                'default_wdsysmon_throttle',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('last-throttle', REFERENCE_LIST, 'LastThrottle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.OverloadState.LastThrottle', 
                [], [], 
                '''                Last throttle information
                ''',
                'last_throttle',
                'Cisco-IOS-XR-wd-oper', False, max_elements=20),
            _MetaInfoClassMember('overload-control-notification', REFERENCE_ENUM_CLASS, 'OverloadCtrlNotifEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'OverloadCtrlNotifEnum', 
                [], [], 
                '''                State of overload control notification
                ''',
                'overload_control_notification',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'overload-state',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-wd-oper', True),
            _MetaInfoClassMember('memory-state', REFERENCE_CLASS, 'MemoryState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.MemoryState', 
                [], [], 
                '''                Memory state
                ''',
                'memory_state',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('overload-state', REFERENCE_CLASS, 'OverloadState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.OverloadState', 
                [], [], 
                '''                Display overload control state
                ''',
                'overload_state',
                'Cisco-IOS-XR-wd-oper', False),
            _MetaInfoClassMember('threshold-memory', REFERENCE_CLASS, 'ThresholdMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node.ThresholdMemory', 
                [], [], 
                '''                Threshold memory
                ''',
                'threshold_memory',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog.Nodes' : {
        'meta_info' : _MetaInfoClass('Watchdog.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes.Node', 
                [], [], 
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
    'Watchdog' : {
        'meta_info' : _MetaInfoClass('Watchdog',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper', 'Watchdog.Nodes', 
                [], [], 
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-wd-oper', False),
            ],
            'Cisco-IOS-XR-wd-oper',
            'watchdog',
            _yang_ns._namespaces['Cisco-IOS-XR-wd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_oper'
        ),
    },
}
_meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default.ConfiguredMemory']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default']['meta_info']
_meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default.Memory']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default']['meta_info']
_meta_table['Watchdog.Nodes.Node.ThresholdMemory.Default']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node.ThresholdMemory']['meta_info']
_meta_table['Watchdog.Nodes.Node.ThresholdMemory.Configured']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node.ThresholdMemory']['meta_info']
_meta_table['Watchdog.Nodes.Node.OverloadState.CurrentThrottle']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node.OverloadState']['meta_info']
_meta_table['Watchdog.Nodes.Node.OverloadState.LastThrottle']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node.OverloadState']['meta_info']
_meta_table['Watchdog.Nodes.Node.ThresholdMemory']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node']['meta_info']
_meta_table['Watchdog.Nodes.Node.MemoryState']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node']['meta_info']
_meta_table['Watchdog.Nodes.Node.OverloadState']['meta_info'].parent =_meta_table['Watchdog.Nodes.Node']['meta_info']
_meta_table['Watchdog.Nodes.Node']['meta_info'].parent =_meta_table['Watchdog.Nodes']['meta_info']
_meta_table['Watchdog.Nodes']['meta_info'].parent =_meta_table['Watchdog']['meta_info']
