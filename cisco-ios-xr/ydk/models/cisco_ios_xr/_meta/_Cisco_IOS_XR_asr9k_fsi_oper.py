


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Counter
                ''',
                'count',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Counter Name
                ''',
                'counter_name',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'fsi-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
    'FabricStats.Nodes.Node.Statses.Stats.StatsTable' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses.Stats.StatsTable',
            False, 
            [
            _MetaInfoClassMember('fsi-stat', REFERENCE_LIST, 'FsiStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat', 
                [], [], 
                '''                Stats Table
                ''',
                'fsi_stat',
                'Cisco-IOS-XR-asr9k-fsi-oper', False, max_elements=60),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'stats-table',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
    'FabricStats.Nodes.Node.Statses.Stats' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses.Stats',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Fabric asic type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-fsi-oper', True),
            _MetaInfoClassMember('stat-table-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Stat Table Name
                ''',
                'stat_table_name',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            _MetaInfoClassMember('stats-table', REFERENCE_LIST, 'StatsTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses.Stats.StatsTable', 
                [], [], 
                '''                Array of counters 
                ''',
                'stats_table',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
    'FabricStats.Nodes.Node.Statses' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node.Statses',
            False, 
            [
            _MetaInfoClassMember('stats', REFERENCE_LIST, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses.Stats', 
                [], [], 
                '''                Stats information for a particular type
                ''',
                'stats',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'statses',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
    'FabricStats.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-fsi-oper', True),
            _MetaInfoClassMember('statses', REFERENCE_CLASS, 'Statses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node.Statses', 
                [], [], 
                '''                Table of stats information
                ''',
                'statses',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
    'FabricStats.Nodes' : {
        'meta_info' : _MetaInfoClass('FabricStats.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes.Node', 
                [], [], 
                '''                Information about a particular node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
    'FabricStats' : {
        'meta_info' : _MetaInfoClass('FabricStats',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper', 'FabricStats.Nodes', 
                [], [], 
                '''                Table of Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-fsi-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-fsi-oper',
            'fabric-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-fsi-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fsi_oper'
        ),
    },
}
_meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable.FsiStat']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable']['meta_info']
_meta_table['FabricStats.Nodes.Node.Statses.Stats.StatsTable']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node.Statses.Stats']['meta_info']
_meta_table['FabricStats.Nodes.Node.Statses.Stats']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node.Statses']['meta_info']
_meta_table['FabricStats.Nodes.Node.Statses']['meta_info'].parent =_meta_table['FabricStats.Nodes.Node']['meta_info']
_meta_table['FabricStats.Nodes.Node']['meta_info'].parent =_meta_table['FabricStats.Nodes']['meta_info']
_meta_table['FabricStats.Nodes']['meta_info'].parent =_meta_table['FabricStats']['meta_info']
