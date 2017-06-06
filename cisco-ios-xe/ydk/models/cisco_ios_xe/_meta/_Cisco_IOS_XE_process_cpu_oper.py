


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess' : {
        'meta_info' : _MetaInfoClass('CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess',
            False, 
            [
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Process-ID of the process.
                ''',
                'pid',
                'Cisco-IOS-XE-process-cpu-oper', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the process.
                ''',
                'name',
                'Cisco-IOS-XE-process-cpu-oper', True),
            _MetaInfoClassMember('avg-run-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Average Run-time of this process (uSec)
                ''',
                'avg_run_time',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('five-minutes', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Busy percentage in last five minutes
                ''',
                'five_minutes',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('five-seconds', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Busy percentage in last 5-seconds
                ''',
                'five_seconds',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('invocation-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of invocations
                ''',
                'invocation_count',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('one-minute', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Busy percentage in last one minute
                ''',
                'one_minute',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('total-run-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total Run-time of this process (mSec)
                ''',
                'total_run_time',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('tty', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TTY bound to by the process.
                ''',
                'tty',
                'Cisco-IOS-XE-process-cpu-oper', False),
            ],
            'Cisco-IOS-XE-process-cpu-oper',
            'cpu-usage-process',
            _yang_ns._namespaces['Cisco-IOS-XE-process-cpu-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper'
        ),
    },
    'CpuUsage.CpuUtilization.CpuUsageProcesses' : {
        'meta_info' : _MetaInfoClass('CpuUsage.CpuUtilization.CpuUsageProcesses',
            False, 
            [
            _MetaInfoClassMember('cpu-usage-process', REFERENCE_LIST, 'CpuUsageProcess' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper', 'CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess', 
                [], [], 
                '''                The list of software processes on the device.
                ''',
                'cpu_usage_process',
                'Cisco-IOS-XE-process-cpu-oper', False),
            ],
            'Cisco-IOS-XE-process-cpu-oper',
            'cpu-usage-processes',
            _yang_ns._namespaces['Cisco-IOS-XE-process-cpu-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper'
        ),
    },
    'CpuUsage.CpuUtilization' : {
        'meta_info' : _MetaInfoClass('CpuUsage.CpuUtilization',
            False, 
            [
            _MetaInfoClassMember('cpu-usage-processes', REFERENCE_CLASS, 'CpuUsageProcesses' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper', 'CpuUsage.CpuUtilization.CpuUsageProcesses', 
                [], [], 
                '''                Data nodes for System wide Process CPU usage Statistics.
                ''',
                'cpu_usage_processes',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('five-minutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Busy percentage in last five minutes
                ''',
                'five_minutes',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('five-seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Busy percentage in last 5-seconds
                ''',
                'five_seconds',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('five-seconds-intr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Interrupt busy percentage in last 5-seconds
                ''',
                'five_seconds_intr',
                'Cisco-IOS-XE-process-cpu-oper', False),
            _MetaInfoClassMember('one-minute', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Busy percentage in last one minute
                ''',
                'one_minute',
                'Cisco-IOS-XE-process-cpu-oper', False),
            ],
            'Cisco-IOS-XE-process-cpu-oper',
            'cpu-utilization',
            _yang_ns._namespaces['Cisco-IOS-XE-process-cpu-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper'
        ),
    },
    'CpuUsage' : {
        'meta_info' : _MetaInfoClass('CpuUsage',
            False, 
            [
            _MetaInfoClassMember('cpu-utilization', REFERENCE_CLASS, 'CpuUtilization' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper', 'CpuUsage.CpuUtilization', 
                [], [], 
                '''                Data nodes for Total CPU Utilizations Statistics.
                ''',
                'cpu_utilization',
                'Cisco-IOS-XE-process-cpu-oper', False),
            ],
            'Cisco-IOS-XE-process-cpu-oper',
            'cpu-usage',
            _yang_ns._namespaces['Cisco-IOS-XE-process-cpu-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_cpu_oper'
        ),
    },
}
_meta_table['CpuUsage.CpuUtilization.CpuUsageProcesses.CpuUsageProcess']['meta_info'].parent =_meta_table['CpuUsage.CpuUtilization.CpuUsageProcesses']['meta_info']
_meta_table['CpuUsage.CpuUtilization.CpuUsageProcesses']['meta_info'].parent =_meta_table['CpuUsage.CpuUtilization']['meta_info']
_meta_table['CpuUsage.CpuUtilization']['meta_info'].parent =_meta_table['CpuUsage']['meta_info']
