


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MemoryStats.MemoryStat' : {
        'meta_info' : _MetaInfoClass('MemoryStats.MemoryStat',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the memory pool.
                ''',
                'name',
                'Cisco-IOS-XE-memory-oper', True),
            _MetaInfoClassMember('free-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total free memory in the pool (bytes)
                ''',
                'free_memory',
                'Cisco-IOS-XE-memory-oper', False),
            _MetaInfoClassMember('highest-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Historical highest memory usage (bytes)
                ''',
                'highest_usage',
                'Cisco-IOS-XE-memory-oper', False),
            _MetaInfoClassMember('lowest-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Historical lowest memory usage (bytes)
                ''',
                'lowest_usage',
                'Cisco-IOS-XE-memory-oper', False),
            _MetaInfoClassMember('total-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total memory in the pool (bytes)
                ''',
                'total_memory',
                'Cisco-IOS-XE-memory-oper', False),
            _MetaInfoClassMember('used-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total used memory in the pool (bytes)
                ''',
                'used_memory',
                'Cisco-IOS-XE-memory-oper', False),
            ],
            'Cisco-IOS-XE-memory-oper',
            'memory-stat',
            _yang_ns._namespaces['Cisco-IOS-XE-memory-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper'
        ),
    },
    'MemoryStats' : {
        'meta_info' : _MetaInfoClass('MemoryStats',
            False, 
            [
            _MetaInfoClassMember('memory-stat', REFERENCE_LIST, 'MemoryStat' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper', 'MemoryStats.MemoryStat', 
                [], [], 
                '''                The list of software memory pools in the system.
                ''',
                'memory_stat',
                'Cisco-IOS-XE-memory-oper', False),
            ],
            'Cisco-IOS-XE-memory-oper',
            'memory-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-memory-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_memory_oper'
        ),
    },
}
_meta_table['MemoryStats.MemoryStat']['meta_info'].parent =_meta_table['MemoryStats']['meta_info']
