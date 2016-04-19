


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MemorySummary.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('boot-ram-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Boot RAM size in bytes
                ''',
                'boot_ram_size',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('flash-system', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Flash System size in bytes
                ''',
                'flash_system',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('free-application-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Application memory available in bytes
                ''',
                'free_application_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('free-physical-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Physical memory available in bytes
                ''',
                'free_physical_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('image-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Image memory size in bytes
                ''',
                'image_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('io-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                IO memory size in bytes
                ''',
                'io_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('page-size', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Page size in bytes
                ''',
                'page_size',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('ram-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Physical memory size in bytes
                ''',
                'ram_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('reserved-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Reserved memory size in bytes
                ''',
                'reserved_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            _MetaInfoClassMember('system-ram-memory', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Application memory size in bytes
                ''',
                'system_ram_memory',
                'Cisco-IOS-XR-nto-misc-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-oper'],
        'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper'
        ),
    },
    'MemorySummary.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-nto-misc-oper', True),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper', 'MemorySummary.Nodes.Node.Summary', 
                [], [], 
                '''                Memory summary information for a specific node
                ''',
                'summary',
                'Cisco-IOS-XR-nto-misc-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-oper'],
        'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper'
        ),
    },
    'MemorySummary.Nodes' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper', 'MemorySummary.Nodes.Node', 
                [], [], 
                '''                Name of nodes
                ''',
                'node',
                'Cisco-IOS-XR-nto-misc-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-oper'],
        'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper'
        ),
    },
    'MemorySummary' : {
        'meta_info' : _MetaInfoClass('MemorySummary',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper', 'MemorySummary.Nodes', 
                [], [], 
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-nto-misc-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-oper',
            'memory-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-oper'],
        'ydk.models.nto.Cisco_IOS_XR_nto_misc_oper'
        ),
    },
}
_meta_table['MemorySummary.Nodes.Node.Summary']['meta_info'].parent =_meta_table['MemorySummary.Nodes.Node']['meta_info']
_meta_table['MemorySummary.Nodes.Node']['meta_info'].parent =_meta_table['MemorySummary.Nodes']['meta_info']
_meta_table['MemorySummary.Nodes']['meta_info'].parent =_meta_table['MemorySummary']['meta_info']
