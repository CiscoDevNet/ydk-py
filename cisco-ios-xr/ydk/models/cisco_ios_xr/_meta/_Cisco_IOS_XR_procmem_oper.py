


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ProcessesMemory.Nodes.Node.ProcessIds.ProcessId' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node.ProcessIds.ProcessId',
            False, 
            [
            _MetaInfoClassMember('process-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Process Id
                ''',
                'process_id',
                'Cisco-IOS-XR-procmem-oper', True),
            _MetaInfoClassMember('data-seg-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data Segment Size
                ''',
                'data_seg_size',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('dyn-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dynamic memory limit
                ''',
                'dyn_limit',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('jid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Job ID
                ''',
                'jid',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('malloc-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Malloced Memory Size
                ''',
                'malloc_size',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process name
                ''',
                'name',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('physical-mem', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Physical memory size
                ''',
                'physical_mem',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Process ID
                ''',
                'pid',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('shared-mem', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Shared memory size
                ''',
                'shared_mem',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('stack-seg-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stack Segment Size
                ''',
                'stack_seg_size',
                'Cisco-IOS-XR-procmem-oper', False),
            _MetaInfoClassMember('text-seg-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Text Segment Size
                ''',
                'text_seg_size',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'process-id',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory.Nodes.Node.ProcessIds' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node.ProcessIds',
            False, 
            [
            _MetaInfoClassMember('process-id', REFERENCE_LIST, 'ProcessId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node.ProcessIds.ProcessId', 
                [], [], 
                '''                Process Id
                ''',
                'process_id',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'process-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-procmem-oper', True),
            _MetaInfoClassMember('process-ids', REFERENCE_CLASS, 'ProcessIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node.ProcessIds', 
                [], [], 
                '''                List of jobs
                ''',
                'process_ids',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory.Nodes' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes.Node', 
                [], [], 
                '''                Node ID
                ''',
                'node',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper'
        ),
    },
    'ProcessesMemory' : {
        'meta_info' : _MetaInfoClass('ProcessesMemory',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper', 'ProcessesMemory.Nodes', 
                [], [], 
                '''                List of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-procmem-oper', False),
            ],
            'Cisco-IOS-XR-procmem-oper',
            'processes-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-procmem-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_procmem_oper'
        ),
    },
}
_meta_table['ProcessesMemory.Nodes.Node.ProcessIds.ProcessId']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes.Node.ProcessIds']['meta_info']
_meta_table['ProcessesMemory.Nodes.Node.ProcessIds']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes.Node']['meta_info']
_meta_table['ProcessesMemory.Nodes.Node']['meta_info'].parent =_meta_table['ProcessesMemory.Nodes']['meta_info']
_meta_table['ProcessesMemory.Nodes']['meta_info'].parent =_meta_table['ProcessesMemory']['meta_info']
