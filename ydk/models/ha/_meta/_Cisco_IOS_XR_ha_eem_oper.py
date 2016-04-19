


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SystemMonitoring.CpuUtilization.ProcessCpu' : {
        'meta_info' : _MetaInfoClass('SystemMonitoring.CpuUtilization.ProcessCpu',
            False, 
            [
            _MetaInfoClassMember('process-cpu-fifteen-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Process CPU utilization in percent for past 15
                minute
                ''',
                'process_cpu_fifteen_minute',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('process-cpu-five-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Process CPU utilization in percent for past 5
                minute
                ''',
                'process_cpu_five_minute',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('process-cpu-one-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Process CPU utilization in percent for past 1
                minute
                ''',
                'process_cpu_one_minute',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('process-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Process ID
                ''',
                'process_id',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process name
                ''',
                'process_name',
                'Cisco-IOS-XR-ha-eem-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-oper',
            'process-cpu',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-oper'],
        'ydk.models.ha.Cisco_IOS_XR_ha_eem_oper'
        ),
    },
    'SystemMonitoring.CpuUtilization' : {
        'meta_info' : _MetaInfoClass('SystemMonitoring.CpuUtilization',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ha-eem-oper', True),
            _MetaInfoClassMember('process-cpu', REFERENCE_LIST, 'ProcessCpu' , 'ydk.models.ha.Cisco_IOS_XR_ha_eem_oper', 'SystemMonitoring.CpuUtilization.ProcessCpu', 
                [], [], 
                '''                Per process CPU utilization
                ''',
                'process_cpu',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('total-cpu-fifteen-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total CPU utilization in past 15 minute
                ''',
                'total_cpu_fifteen_minute',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('total-cpu-five-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total CPU utilization in past 5 minute
                ''',
                'total_cpu_five_minute',
                'Cisco-IOS-XR-ha-eem-oper', False),
            _MetaInfoClassMember('total-cpu-one-minute', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total CPU utilization in past 1 minute
                ''',
                'total_cpu_one_minute',
                'Cisco-IOS-XR-ha-eem-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-oper',
            'cpu-utilization',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-oper'],
        'ydk.models.ha.Cisco_IOS_XR_ha_eem_oper'
        ),
    },
    'SystemMonitoring' : {
        'meta_info' : _MetaInfoClass('SystemMonitoring',
            False, 
            [
            _MetaInfoClassMember('cpu-utilization', REFERENCE_LIST, 'CpuUtilization' , 'ydk.models.ha.Cisco_IOS_XR_ha_eem_oper', 'SystemMonitoring.CpuUtilization', 
                [], [], 
                '''                Processes CPU utilization information
                ''',
                'cpu_utilization',
                'Cisco-IOS-XR-ha-eem-oper', False),
            ],
            'Cisco-IOS-XR-ha-eem-oper',
            'system-monitoring',
            _yang_ns._namespaces['Cisco-IOS-XR-ha-eem-oper'],
        'ydk.models.ha.Cisco_IOS_XR_ha_eem_oper'
        ),
    },
}
_meta_table['SystemMonitoring.CpuUtilization.ProcessCpu']['meta_info'].parent =_meta_table['SystemMonitoring.CpuUtilization']['meta_info']
_meta_table['SystemMonitoring.CpuUtilization']['meta_info'].parent =_meta_table['SystemMonitoring']['meta_info']
