


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PlatformLptspIfib.Nodes.Node.Police.PoliceInfo' : {
        'meta_info' : _MetaInfoClass('PlatformLptspIfib.Nodes.Node.Police.PoliceInfo',
            False, 
            [
            _MetaInfoClassMember('accepted-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                accepted stats
                ''',
                'accepted_stats',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('acl-config', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                acl config
                ''',
                'acl_config',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('acl-str', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                acl str
                ''',
                'acl_str',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('avgrate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                avgrate
                ''',
                'avgrate',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('avgrate-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                avgrate type
                ''',
                'avgrate_type',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                burst
                ''',
                'burst',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('change-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                change type
                ''',
                'change_type',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('dropped-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                dropped stats
                ''',
                'dropped_stats',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('flow-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                flow type
                ''',
                'flow_type',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('iptos-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                iptos value
                ''',
                'iptos_value',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('np', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                np
                ''',
                'np',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('policer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer
                ''',
                'policer',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('static-avgrate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                static avgrate
                ''',
                'static_avgrate',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lpts-oper',
            'police-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lpts-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper'
        ),
    },
    'PlatformLptspIfib.Nodes.Node.Police' : {
        'meta_info' : _MetaInfoClass('PlatformLptspIfib.Nodes.Node.Police',
            False, 
            [
            _MetaInfoClassMember('police-info', REFERENCE_LIST, 'PoliceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper', 'PlatformLptspIfib.Nodes.Node.Police.PoliceInfo', 
                [], [], 
                '''                Per flow type police info
                ''',
                'police_info',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lpts-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lpts-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper'
        ),
    },
    'PlatformLptspIfib.Nodes.Node.Stats' : {
        'meta_info' : _MetaInfoClass('PlatformLptspIfib.Nodes.Node.Stats',
            False, 
            [
            _MetaInfoClassMember('accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Deleted-entry accepted packets counter
                ''',
                'accepted',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('clear-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Statistics clear timestamp
                ''',
                'clear_ts',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Deleted-entry dropped packets counter
                ''',
                'dropped',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('no-stats-mem-err', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                No statistics memory error
                ''',
                'no_stats_mem_err',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lpts-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lpts-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper'
        ),
    },
    'PlatformLptspIfib.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PlatformLptspIfib.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-lpts-oper', True),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper', 'PlatformLptspIfib.Nodes.Node.Police', 
                [], [], 
                '''                pl_pifib police data
                ''',
                'police',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper', 'PlatformLptspIfib.Nodes.Node.Stats', 
                [], [], 
                '''                pl_pifib stats
                ''',
                'stats',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lpts-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lpts-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper'
        ),
    },
    'PlatformLptspIfib.Nodes' : {
        'meta_info' : _MetaInfoClass('PlatformLptspIfib.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper', 'PlatformLptspIfib.Nodes.Node', 
                [], [], 
                '''                Node with platform specific lpts data
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lpts-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lpts-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper'
        ),
    },
    'PlatformLptspIfib' : {
        'meta_info' : _MetaInfoClass('PlatformLptspIfib',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper', 'PlatformLptspIfib.Nodes', 
                [], [], 
                '''                List of nodes with platform specific lpts
                operation data
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-lpts-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lpts-oper',
            'platform-lptsp-ifib',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lpts-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lpts_oper'
        ),
    },
}
_meta_table['PlatformLptspIfib.Nodes.Node.Police.PoliceInfo']['meta_info'].parent =_meta_table['PlatformLptspIfib.Nodes.Node.Police']['meta_info']
_meta_table['PlatformLptspIfib.Nodes.Node.Police']['meta_info'].parent =_meta_table['PlatformLptspIfib.Nodes.Node']['meta_info']
_meta_table['PlatformLptspIfib.Nodes.Node.Stats']['meta_info'].parent =_meta_table['PlatformLptspIfib.Nodes.Node']['meta_info']
_meta_table['PlatformLptspIfib.Nodes.Node']['meta_info'].parent =_meta_table['PlatformLptspIfib.Nodes']['meta_info']
_meta_table['PlatformLptspIfib.Nodes']['meta_info'].parent =_meta_table['PlatformLptspIfib']['meta_info']
