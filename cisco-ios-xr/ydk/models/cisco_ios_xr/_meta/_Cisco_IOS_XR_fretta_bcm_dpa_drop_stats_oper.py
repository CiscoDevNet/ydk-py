


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData' : {
        'meta_info' : _MetaInfoClass('Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData',
            False, 
            [
            _MetaInfoClassMember('drop-data', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Drop ID
                ''',
                'drop_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', True),
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                count
                ''',
                'count',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                id
                ''',
                'id',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper',
            'drop-specific-stats-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper'
        ),
    },
    'Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat' : {
        'meta_info' : _MetaInfoClass('Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat',
            False, 
            [
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                NPU number
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', True),
            _MetaInfoClassMember('drop-specific-stats-data', REFERENCE_LIST, 'DropSpecificStatsData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper', 'Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData', 
                [], [], 
                '''                Second argument to the module
                ''',
                'drop_specific_stats_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper',
            'npu-number-for-drop-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper'
        ),
    },
    'Drop.Nodes.Node.NpuNumberForDropStats' : {
        'meta_info' : _MetaInfoClass('Drop.Nodes.Node.NpuNumberForDropStats',
            False, 
            [
            _MetaInfoClassMember('npu-number-for-drop-stat', REFERENCE_LIST, 'NpuNumberForDropStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper', 'Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat', 
                [], [], 
                '''                All drop stats for a particular NPU
                ''',
                'npu_number_for_drop_stat',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper',
            'npu-number-for-drop-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper'
        ),
    },
    'Drop.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Drop.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', True),
            _MetaInfoClassMember('npu-number-for-drop-stats', REFERENCE_CLASS, 'NpuNumberForDropStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper', 'Drop.Nodes.Node.NpuNumberForDropStats', 
                [], [], 
                '''                NPU drop stats
                ''',
                'npu_number_for_drop_stats',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper'
        ),
    },
    'Drop.Nodes' : {
        'meta_info' : _MetaInfoClass('Drop.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper', 'Drop.Nodes.Node', 
                [], [], 
                '''                Drop stats data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper'
        ),
    },
    'Drop' : {
        'meta_info' : _MetaInfoClass('Drop',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper', 'Drop.Nodes', 
                [], [], 
                '''                Drop data per node
                ''',
                'nodes',
                'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper',
            'drop',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-drop-stats-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_drop_stats_oper'
        ),
    },
}
_meta_table['Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat.DropSpecificStatsData']['meta_info'].parent =_meta_table['Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat']['meta_info']
_meta_table['Drop.Nodes.Node.NpuNumberForDropStats.NpuNumberForDropStat']['meta_info'].parent =_meta_table['Drop.Nodes.Node.NpuNumberForDropStats']['meta_info']
_meta_table['Drop.Nodes.Node.NpuNumberForDropStats']['meta_info'].parent =_meta_table['Drop.Nodes.Node']['meta_info']
_meta_table['Drop.Nodes.Node']['meta_info'].parent =_meta_table['Drop.Nodes']['meta_info']
_meta_table['Drop.Nodes']['meta_info'].parent =_meta_table['Drop']['meta_info']
