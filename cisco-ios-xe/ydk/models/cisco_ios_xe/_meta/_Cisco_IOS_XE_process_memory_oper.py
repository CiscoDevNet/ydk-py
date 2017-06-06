


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MemoryUsageProcesses.MemoryUsageProcess' : {
        'meta_info' : _MetaInfoClass('MemoryUsageProcesses.MemoryUsageProcess',
            False, 
            [
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Process-ID of the process.
                ''',
                'pid',
                'Cisco-IOS-XE-process-memory-oper', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the process.
                ''',
                'name',
                'Cisco-IOS-XE-process-memory-oper', True),
            _MetaInfoClassMember('allocated-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total memory allocated to this process (bytes)
                ''',
                'allocated_memory',
                'Cisco-IOS-XE-process-memory-oper', False),
            _MetaInfoClassMember('freed-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total memory freed by this process (bytes)
                ''',
                'freed_memory',
                'Cisco-IOS-XE-process-memory-oper', False),
            _MetaInfoClassMember('get-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Get Buffers of this process (bytes)
                ''',
                'get_buffers',
                'Cisco-IOS-XE-process-memory-oper', False),
            _MetaInfoClassMember('holding-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total memory currently held by this process (bytes)
                ''',
                'holding_memory',
                'Cisco-IOS-XE-process-memory-oper', False),
            _MetaInfoClassMember('ret-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Return Buffers of this process (bytes)
                ''',
                'ret_buffers',
                'Cisco-IOS-XE-process-memory-oper', False),
            _MetaInfoClassMember('tty', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TTY bound to by the process.
                ''',
                'tty',
                'Cisco-IOS-XE-process-memory-oper', False),
            ],
            'Cisco-IOS-XE-process-memory-oper',
            'memory-usage-process',
            _yang_ns._namespaces['Cisco-IOS-XE-process-memory-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_memory_oper'
        ),
    },
    'MemoryUsageProcesses' : {
        'meta_info' : _MetaInfoClass('MemoryUsageProcesses',
            False, 
            [
            _MetaInfoClassMember('memory-usage-process', REFERENCE_LIST, 'MemoryUsageProcess' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_memory_oper', 'MemoryUsageProcesses.MemoryUsageProcess', 
                [], [], 
                '''                The list of software processes on the device.
                ''',
                'memory_usage_process',
                'Cisco-IOS-XE-process-memory-oper', False),
            ],
            'Cisco-IOS-XE-process-memory-oper',
            'memory-usage-processes',
            _yang_ns._namespaces['Cisco-IOS-XE-process-memory-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_process_memory_oper'
        ),
    },
}
_meta_table['MemoryUsageProcesses.MemoryUsageProcess']['meta_info'].parent =_meta_table['MemoryUsageProcesses']['meta_info']
