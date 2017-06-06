


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats',
            False, 
            [
            _MetaInfoClassMember('load-average-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'load_average_status',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'load-average-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status',
            False, 
            [
            _MetaInfoClassMember('condition', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Need description
                ''',
                'condition',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('threshold-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Need description
                ''',
                'threshold_status',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Format: Decimal with 2 fraction digits
                ''',
                'threshold_value',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'status',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of minutes the average was calculated on.
                ''',
                'number',
                'Cisco-IOS-XE-platform-software-oper', True),
            _MetaInfoClassMember('average', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Format: Decimal with 2 fraction digits
                ''',
                'average',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('status', REFERENCE_CLASS, 'Status' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status', 
                [], [], 
                '''                ''',
                'status',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'load-avg-minute',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes',
            False, 
            [
            _MetaInfoClassMember('load-avg-minute', REFERENCE_LIST, 'LoadAvgMinute' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute', 
                [], [], 
                '''                Load average statistics based on a time frame
                ''',
                'load_avg_minute',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'load-avg-minutes',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status',
            False, 
            [
            _MetaInfoClassMember('condition', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Need description
                ''',
                'condition',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('threshold-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Need description
                ''',
                'threshold_status',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('threshold-value-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Need description
                ''',
                'threshold_value_percent',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'status',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats',
            False, 
            [
            _MetaInfoClassMember('available-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of available memory in kb
                ''',
                'available_number',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('available-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The percentage of available memory
                ''',
                'available_percent',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('committed-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of committed memory in kb
                ''',
                'committed_number',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('committed-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The percentage of comitted memory
                ''',
                'committed_percent',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('free-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of free memory in kb
                ''',
                'free_number',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('free-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The percentage of free memory
                ''',
                'free_percent',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('memory-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The status of the memory
                ''',
                'memory_status',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('status', REFERENCE_CLASS, 'Status' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status', 
                [], [], 
                '''                ''',
                'status',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of memory in kb
                ''',
                'total',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('used-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of memory being used in kb
                ''',
                'used_number',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('used-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The percentage of memory being used
                ''',
                'used_percent',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'memory-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the core
                ''',
                'name',
                'Cisco-IOS-XE-platform-software-oper', True),
            _MetaInfoClassMember('idle', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage that is idle
                                Format: Decimal with 2 fraction digits
                ''',
                'idle',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('io-wait', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage of utilization by IOwait
                                Format: Decimal with 2 fraction digits
                ''',
                'io_wait',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('irq', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage of utilizaion by irq
                                Format: Decimal with 2 fraction digits
                ''',
                'irq',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('nice', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage of utilization by nice
                                Format: Decimal with 2 fraction digits
                ''',
                'nice',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('sirq', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage of utilizaion by sirq
                                Format: Decimal with 2 fraction digits
                ''',
                'sirq',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('system', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage of utilization by the system
                                Format: Decimal with 2 fraction digits
                ''',
                'system',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('user', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The percentage of utilization by user
                                Format: Decimal with 2 fraction digits
                ''',
                'user',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'per-core-stat',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats',
            False, 
            [
            _MetaInfoClassMember('per-core-stat', REFERENCE_LIST, 'PerCoreStat' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat', 
                [], [], 
                '''                A Core
                ''',
                'per_core_stat',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'per-core-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the control process
                ''',
                'name',
                'Cisco-IOS-XE-platform-software-oper', True),
            _MetaInfoClassMember('load-average-stats', REFERENCE_CLASS, 'LoadAverageStats' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats', 
                [], [], 
                '''                Statistics on the load average.
                ''',
                'load_average_stats',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('load-avg-minutes', REFERENCE_CLASS, 'LoadAvgMinutes' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes', 
                [], [], 
                '''                ''',
                'load_avg_minutes',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('memory-stats', REFERENCE_CLASS, 'MemoryStats' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats', 
                [], [], 
                '''                The statistics on the memory
                ''',
                'memory_stats',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('per-core-stats', REFERENCE_CLASS, 'PerCoreStats' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats', 
                [], [], 
                '''                Statistics on each core
                ''',
                'per_core_stats',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Status of the control processer
                ''',
                'status',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('updated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of seconds since the data has been updated.
                ''',
                'updated',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'control-process',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses',
            False, 
            [
            _MetaInfoClassMember('control-process', REFERENCE_LIST, 'ControlProcess' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess', 
                [], [], 
                '''                Control process
                ''',
                'control_process',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'control-processes',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses',
            False, 
            [
            _MetaInfoClassMember('control-processes', REFERENCE_CLASS, 'ControlProcesses' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses', 
                [], [], 
                '''                ''',
                'control_processes',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'platform-software-status-control-processes',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces.XosInterface' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces.XosInterface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DESCRPITION NEEDED
                ''',
                'name',
                'Cisco-IOS-XE-platform-software-oper', True),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DESCRPITION NEEDED
                ''',
                'id',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('qfp-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DESCRPITION NEEDED
                ''',
                'qfp_id',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'xos-interface',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces',
            False, 
            [
            _MetaInfoClassMember('xos-interface', REFERENCE_LIST, 'XosInterface' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces.XosInterface', 
                [], [], 
                '''                DESCRIPTION NEEDED
                ''',
                'xos_interface',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'xos-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding',
            False, 
            [
            _MetaInfoClassMember('xos-interfaces', REFERENCE_CLASS, 'XosInterfaces' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces', 
                [], [], 
                '''                ''',
                'xos_interfaces',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'platform-software-interface-rp-active-brief-forwarding',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
    'CiscoPlatformSoftware' : {
        'meta_info' : _MetaInfoClass('CiscoPlatformSoftware',
            False, 
            [
            _MetaInfoClassMember('platform-software-interface-rp-active-brief-forwarding', REFERENCE_CLASS, 'PlatformSoftwareInterfaceRpActiveBriefForwarding' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding', 
                [], [], 
                '''                DESCRIPTION NEEDED
                ''',
                'platform_software_interface_rp_active_brief_forwarding',
                'Cisco-IOS-XE-platform-software-oper', False),
            _MetaInfoClassMember('platform-software-status-control-processes', REFERENCE_CLASS, 'PlatformSoftwareStatusControlProcesses' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper', 'CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses', 
                [], [], 
                '''                Contents of the show platform software status control process cli.
                ''',
                'platform_software_status_control_processes',
                'Cisco-IOS-XE-platform-software-oper', False),
            ],
            'Cisco-IOS-XE-platform-software-oper',
            'cisco-platform-software',
            _yang_ns._namespaces['Cisco-IOS-XE-platform-software-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_platform_software_oper'
        ),
    },
}
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute.Status']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes.LoadAvgMinute']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats.Status']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats.PerCoreStat']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAverageStats']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.LoadAvgMinutes']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.MemoryStats']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess.PerCoreStats']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses.ControlProcess']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses.ControlProcesses']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces.XosInterface']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding.XosInterfaces']['meta_info'].parent =_meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareStatusControlProcesses']['meta_info'].parent =_meta_table['CiscoPlatformSoftware']['meta_info']
_meta_table['CiscoPlatformSoftware.PlatformSoftwareInterfaceRpActiveBriefForwarding']['meta_info'].parent =_meta_table['CiscoPlatformSoftware']['meta_info']
