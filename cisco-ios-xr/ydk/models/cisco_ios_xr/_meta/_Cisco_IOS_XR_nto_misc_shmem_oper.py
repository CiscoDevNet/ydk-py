


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MemorySummary.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('boot-ram-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Boot RAM size in bytes
                ''',
                'boot_ram_size',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('flash-system', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flash System size in bytes
                ''',
                'flash_system',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('free-application-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Application memory available in bytes
                ''',
                'free_application_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('free-physical-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Physical memory available in bytes
                ''',
                'free_physical_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('image-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Image memory size in bytes
                ''',
                'image_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('io-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                IO memory size in bytes
                ''',
                'io_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('page-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Page size in bytes
                ''',
                'page_size',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('ram-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Physical memory size in bytes
                ''',
                'ram_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('reserved-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Reserved memory size in bytes
                ''',
                'reserved_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('system-ram-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Application memory size in bytes
                ''',
                'system_ram_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-shmem-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-shmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper'
        ),
    },
    'MemorySummary.Nodes.Node.Detail.SharedWindow' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes.Node.Detail.SharedWindow',
            False, 
            [
            _MetaInfoClassMember('shared-window', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of shared window
                ''',
                'shared_window',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Size of shared window
                ''',
                'window_size',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-shmem-oper',
            'shared-window',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-shmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper'
        ),
    },
    'MemorySummary.Nodes.Node.Detail' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes.Node.Detail',
            False, 
            [
            _MetaInfoClassMember('allocated-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Allocated Memory Size
                ''',
                'allocated_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('boot-ram-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Boot RAM size in bytes
                ''',
                'boot_ram_size',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('flash-system', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flash System size in bytes
                ''',
                'flash_system',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('free-application-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Application memory available in bytes
                ''',
                'free_application_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('free-physical-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Physical memory available in bytes
                ''',
                'free_physical_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('image-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Image memory size in bytes
                ''',
                'image_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('io-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                IO memory size in bytes
                ''',
                'io_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('page-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Page size in bytes
                ''',
                'page_size',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('private-physical-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Private Physical memory in bytes
                ''',
                'private_physical_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('program-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Program Data Size
                ''',
                'program_data',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('program-stack', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Program Stack Size
                ''',
                'program_stack',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('program-text', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Program Text Size
                ''',
                'program_text',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('ram-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Physical memory size in bytes
                ''',
                'ram_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('reserved-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Reserved memory size in bytes
                ''',
                'reserved_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('shared-window', REFERENCE_LIST, 'SharedWindow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper', 'MemorySummary.Nodes.Node.Detail.SharedWindow', 
                [], [], 
                '''                Available Shared windows
                ''',
                'shared_window',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('system-ram-memory', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Application memory size in bytes
                ''',
                'system_ram_memory',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('total-shared-window', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total Shared window
                ''',
                'total_shared_window',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-shmem-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-shmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper'
        ),
    },
    'MemorySummary.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-nto-misc-shmem-oper', True),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper', 'MemorySummary.Nodes.Node.Detail', 
                [], [], 
                '''                Detail Memory summary information for a
                specific node
                ''',
                'detail',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper', 'MemorySummary.Nodes.Node.Summary', 
                [], [], 
                '''                Memory summary information for a specific node
                ''',
                'summary',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-shmem-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-shmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper'
        ),
    },
    'MemorySummary.Nodes' : {
        'meta_info' : _MetaInfoClass('MemorySummary.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper', 'MemorySummary.Nodes.Node', 
                [], [], 
                '''                Name of nodes
                ''',
                'node',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-shmem-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-shmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper'
        ),
    },
    'MemorySummary' : {
        'meta_info' : _MetaInfoClass('MemorySummary',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper', 'MemorySummary.Nodes', 
                [], [], 
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-nto-misc-shmem-oper', False),
            ],
            'Cisco-IOS-XR-nto-misc-shmem-oper',
            'memory-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-nto-misc-shmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_nto_misc_shmem_oper'
        ),
    },
}
_meta_table['MemorySummary.Nodes.Node.Detail.SharedWindow']['meta_info'].parent =_meta_table['MemorySummary.Nodes.Node.Detail']['meta_info']
_meta_table['MemorySummary.Nodes.Node.Summary']['meta_info'].parent =_meta_table['MemorySummary.Nodes.Node']['meta_info']
_meta_table['MemorySummary.Nodes.Node.Detail']['meta_info'].parent =_meta_table['MemorySummary.Nodes.Node']['meta_info']
_meta_table['MemorySummary.Nodes.Node']['meta_info'].parent =_meta_table['MemorySummary.Nodes']['meta_info']
_meta_table['MemorySummary.Nodes']['meta_info'].parent =_meta_table['MemorySummary']['meta_info']
