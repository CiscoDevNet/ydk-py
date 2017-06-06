


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AsicErrorStats.Nodes.Node.Counts.Count.SumData' : {
        'meta_info' : _MetaInfoClass('AsicErrorStats.Nodes.Node.Counts.Count.SumData',
            False, 
            [
            _MetaInfoClassMember('crc-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                crc err count
                ''',
                'crc_err_count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('gen-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                gen err count
                ''',
                'gen_err_count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('mbe-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mbe err count
                ''',
                'mbe_err_count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('node-key', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                node key
                ''',
                'node_key',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('num-nodes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num nodes
                ''',
                'num_nodes',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('par-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                par err count
                ''',
                'par_err_count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('reset-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                reset err count
                ''',
                'reset_err_count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            _MetaInfoClassMember('sbe-err-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sbe err count
                ''',
                'sbe_err_count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-asic-errors-oper',
            'sum-data',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper'
        ),
    },
    'AsicErrorStats.Nodes.Node.Counts.Count' : {
        'meta_info' : _MetaInfoClass('AsicErrorStats.Nodes.Node.Counts.Count',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Asic Type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', True),
            _MetaInfoClassMember('sum-data', REFERENCE_LIST, 'SumData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper', 'AsicErrorStats.Nodes.Node.Counts.Count.SumData', 
                [], [], 
                '''                sum data
                ''',
                'sum_data',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-asic-errors-oper',
            'count',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper'
        ),
    },
    'AsicErrorStats.Nodes.Node.Counts' : {
        'meta_info' : _MetaInfoClass('AsicErrorStats.Nodes.Node.Counts',
            False, 
            [
            _MetaInfoClassMember('count', REFERENCE_LIST, 'Count' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper', 'AsicErrorStats.Nodes.Node.Counts.Count', 
                [], [], 
                '''                Summary Asic error counts for a Asic Type
                ''',
                'count',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-asic-errors-oper',
            'counts',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper'
        ),
    },
    'AsicErrorStats.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('AsicErrorStats.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', True),
            _MetaInfoClassMember('counts', REFERENCE_CLASS, 'Counts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper', 'AsicErrorStats.Nodes.Node.Counts', 
                [], [], 
                '''                Table of all Asic Types information on a node
                ''',
                'counts',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-asic-errors-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper'
        ),
    },
    'AsicErrorStats.Nodes' : {
        'meta_info' : _MetaInfoClass('AsicErrorStats.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper', 'AsicErrorStats.Nodes.Node', 
                [], [], 
                '''                Information about a particular node
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-asic-errors-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper'
        ),
    },
    'AsicErrorStats' : {
        'meta_info' : _MetaInfoClass('AsicErrorStats',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper', 'AsicErrorStats.Nodes', 
                [], [], 
                '''                Table of Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-asic-errors-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-asic-errors-oper',
            'asic-error-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-asic-errors-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_asic_errors_oper'
        ),
    },
}
_meta_table['AsicErrorStats.Nodes.Node.Counts.Count.SumData']['meta_info'].parent =_meta_table['AsicErrorStats.Nodes.Node.Counts.Count']['meta_info']
_meta_table['AsicErrorStats.Nodes.Node.Counts.Count']['meta_info'].parent =_meta_table['AsicErrorStats.Nodes.Node.Counts']['meta_info']
_meta_table['AsicErrorStats.Nodes.Node.Counts']['meta_info'].parent =_meta_table['AsicErrorStats.Nodes.Node']['meta_info']
_meta_table['AsicErrorStats.Nodes.Node']['meta_info'].parent =_meta_table['AsicErrorStats.Nodes']['meta_info']
_meta_table['AsicErrorStats.Nodes']['meta_info'].parent =_meta_table['AsicErrorStats']['meta_info']
