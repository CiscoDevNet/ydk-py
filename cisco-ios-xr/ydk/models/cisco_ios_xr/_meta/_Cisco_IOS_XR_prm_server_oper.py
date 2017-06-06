


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Index value
                ''',
                'index',
                'Cisco-IOS-XR-prm-server-oper', True),
            _MetaInfoClassMember('accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accepted
                ''',
                'accepted',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Burst
                ''',
                'burst',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('cos-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                CosQ No
                ''',
                'cos_q',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('cos-q-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 1024)], [], 
                '''                CosQ Name
                ''',
                'cos_q_name',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('flow-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Rate
                ''',
                'flow_rate',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('rx-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rx DMA Channel
                ''',
                'rx_channel',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'index',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.Cpu.Indexes' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.Cpu.Indexes',
            False, 
            [
            _MetaInfoClassMember('index', REFERENCE_LIST, 'Index' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index', 
                [], [], 
                '''                Queue Stats
                ''',
                'index',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.Cpu' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.Cpu',
            False, 
            [
            _MetaInfoClassMember('indexes', REFERENCE_CLASS, 'Indexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.Cpu.Indexes', 
                [], [], 
                '''                Data for software resource
                ''',
                'indexes',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'cpu',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Index value
                ''',
                'index',
                'Cisco-IOS-XR-prm-server-oper', True),
            _MetaInfoClassMember('buffer-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Buffer Length
                ''',
                'buffer_len',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('captured-pak', ATTRIBUTE, 'str' , None, None, 
                [(0, 1024)], [], 
                '''                Captured Packet
                ''',
                'captured_pak',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('days', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Days
                ''',
                'days',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('hours', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Hours
                ''',
                'hours',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If Handle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('mins', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Minutes
                ''',
                'mins',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('pkt-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Packet Index
                ''',
                'pkt_index',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reason
                ''',
                'reason',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('reason-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reason Hi
                ''',
                'reason_hi',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('secs', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Seconds
                ''',
                'secs',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('total-captured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total packets Captured
                ''',
                'total_captured',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('years', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Year
                ''',
                'years',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'indx',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes',
            False, 
            [
            _MetaInfoClassMember('indx', REFERENCE_LIST, 'Indx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx', 
                [], [], 
                '''                Captured packets
                ''',
                'indx',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'indxes',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Index value
                ''',
                'index',
                'Cisco-IOS-XR-prm-server-oper', True),
            _MetaInfoClassMember('counters', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Counter
                ''',
                'counters',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('drop-reason', ATTRIBUTE, 'str' , None, None, 
                [(0, 1024)], [], 
                '''                Drop Reason
                ''',
                'drop_reason',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'idx',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes',
            False, 
            [
            _MetaInfoClassMember('idx', REFERENCE_LIST, 'Idx' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx', 
                [], [], 
                '''                Drop Stats
                ''',
                'idx',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'idxes',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np.PlatformDrop' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np.PlatformDrop',
            False, 
            [
            _MetaInfoClassMember('idxes', REFERENCE_CLASS, 'Idxes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes', 
                [], [], 
                '''                Stats for Drop packets
                ''',
                'idxes',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('indxes', REFERENCE_CLASS, 'Indxes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes', 
                [], [], 
                '''                Captured Packets
                ''',
                'indxes',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'platform-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node.Np' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node.Np',
            False, 
            [
            _MetaInfoClassMember('cpu', REFERENCE_CLASS, 'Cpu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.Cpu', 
                [], [], 
                '''                Resource specific
                ''',
                'cpu',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('platform-drop', REFERENCE_CLASS, 'PlatformDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np.PlatformDrop', 
                [], [], 
                '''                Platform drops
                ''',
                'platform_drop',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'np',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-prm-server-oper', True),
            _MetaInfoClassMember('np', REFERENCE_CLASS, 'Np' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node.Np', 
                [], [], 
                '''                Server specific
                ''',
                'np',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModule.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes.Node', 
                [], [], 
                '''                Node Information
                ''',
                'node',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'HardwareModule' : {
        'meta_info' : _MetaInfoClass('HardwareModule',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'HardwareModule.Nodes', 
                [], [], 
                '''                List of PRM Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'hardware-module',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm.Nodes.Node.Server.Resource.Indexes.Index' : {
        'meta_info' : _MetaInfoClass('Prm.Nodes.Node.Server.Resource.Indexes.Index',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Index value
                ''',
                'index',
                'Cisco-IOS-XR-prm-server-oper', True),
            _MetaInfoClassMember('availability-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Availability Status
                ''',
                'availability_status',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('first-available-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next Free Index
                ''',
                'first_available_index',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Resource Flags
                ''',
                'flags',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('free-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free Resource Count
                ''',
                'free_num',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('inconsistent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Inconsistice Flags
                ''',
                'inconsistent',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('resource-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 1024)], [], 
                '''                Resource Name
                ''',
                'resource_name',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('resource-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Resource Type
                ''',
                'resource_type',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('start-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Start Index
                ''',
                'start_index',
                'Cisco-IOS-XR-prm-server-oper', False),
            _MetaInfoClassMember('total-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Resource Count
                ''',
                'total_num',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'index',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm.Nodes.Node.Server.Resource.Indexes' : {
        'meta_info' : _MetaInfoClass('Prm.Nodes.Node.Server.Resource.Indexes',
            False, 
            [
            _MetaInfoClassMember('index', REFERENCE_LIST, 'Index' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'Prm.Nodes.Node.Server.Resource.Indexes.Index', 
                [], [], 
                '''                Data for software resource
                ''',
                'index',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm.Nodes.Node.Server.Resource' : {
        'meta_info' : _MetaInfoClass('Prm.Nodes.Node.Server.Resource',
            False, 
            [
            _MetaInfoClassMember('indexes', REFERENCE_CLASS, 'Indexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'Prm.Nodes.Node.Server.Resource.Indexes', 
                [], [], 
                '''                Data for software resource
                ''',
                'indexes',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'resource',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm.Nodes.Node.Server' : {
        'meta_info' : _MetaInfoClass('Prm.Nodes.Node.Server',
            False, 
            [
            _MetaInfoClassMember('resource', REFERENCE_CLASS, 'Resource' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'Prm.Nodes.Node.Server.Resource', 
                [], [], 
                '''                Resource specific
                ''',
                'resource',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Prm.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-prm-server-oper', True),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'Prm.Nodes.Node.Server', 
                [], [], 
                '''                Server specific
                ''',
                'server',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm.Nodes' : {
        'meta_info' : _MetaInfoClass('Prm.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'Prm.Nodes.Node', 
                [], [], 
                '''                Node Information
                ''',
                'node',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
    'Prm' : {
        'meta_info' : _MetaInfoClass('Prm',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper', 'Prm.Nodes', 
                [], [], 
                '''                List of PRM Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-prm-server-oper', False),
            ],
            'Cisco-IOS-XR-prm-server-oper',
            'prm',
            _yang_ns._namespaces['Cisco-IOS-XR-prm-server-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_prm_server_oper'
        ),
    },
}
_meta_table['HardwareModule.Nodes.Node.Np.Cpu.Indexes.Index']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np.Cpu.Indexes']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.Cpu.Indexes']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np.Cpu']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes.Indx']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes.Idx']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Indxes']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop.Idxes']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.Cpu']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np.PlatformDrop']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node.Np']['meta_info']
_meta_table['HardwareModule.Nodes.Node.Np']['meta_info'].parent =_meta_table['HardwareModule.Nodes.Node']['meta_info']
_meta_table['HardwareModule.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModule.Nodes']['meta_info']
_meta_table['HardwareModule.Nodes']['meta_info'].parent =_meta_table['HardwareModule']['meta_info']
_meta_table['Prm.Nodes.Node.Server.Resource.Indexes.Index']['meta_info'].parent =_meta_table['Prm.Nodes.Node.Server.Resource.Indexes']['meta_info']
_meta_table['Prm.Nodes.Node.Server.Resource.Indexes']['meta_info'].parent =_meta_table['Prm.Nodes.Node.Server.Resource']['meta_info']
_meta_table['Prm.Nodes.Node.Server.Resource']['meta_info'].parent =_meta_table['Prm.Nodes.Node.Server']['meta_info']
_meta_table['Prm.Nodes.Node.Server']['meta_info'].parent =_meta_table['Prm.Nodes.Node']['meta_info']
_meta_table['Prm.Nodes.Node']['meta_info'].parent =_meta_table['Prm.Nodes']['meta_info']
_meta_table['Prm.Nodes']['meta_info'].parent =_meta_table['Prm']['meta_info']
