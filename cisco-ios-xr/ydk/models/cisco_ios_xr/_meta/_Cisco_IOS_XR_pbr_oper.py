


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PolicyStateEnum' : _MetaInfoEnum('PolicyStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper',
        {
            'active':'active',
            'suspended':'suspended',
        }, 'Cisco-IOS-XR-pbr-oper', _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper']),
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats',
            False, 
            [
            _MetaInfoClassMember('match-data-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incoming matched data rate in kbps
                ''',
                'match_data_rate',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('pre-policy-matched-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Matched bytes before applying policy
                ''',
                'pre_policy_matched_bytes',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('pre-policy-matched-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Matched pkts before applying policy
                ''',
                'pre_policy_matched_packets',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('total-drop-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped bytes (packets/bytes)
                ''',
                'total_drop_bytes',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('total-drop-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped packets (packets/bytes)
                ''',
                'total_drop_packets',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('total-drop-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total drop rate (packets/bytes)
                ''',
                'total_drop_rate',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('total-transmit-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total transmit rate in kbps
                ''',
                'total_transmit_rate',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('transmit-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted bytes (packets/bytes)
                ''',
                'transmit_bytes',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('transmit-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Transmitted packets (packets/bytes)
                ''',
                'transmit_packets',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'general-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats',
            False, 
            [
            _MetaInfoClassMember('drop-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped bytes
                ''',
                'drop_bytes',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('drop-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped  packets
                ''',
                'drop_packets',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('resp-sent-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TotalNum of Bytes HTTPR response sent
                ''',
                'resp_sent_bytes',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('resp-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TotalNum of pkts HTTPR response sent
                ''',
                'resp_sent_packets',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('rqst-rcvd-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TotalNum of Bytes HTTP request received
                ''',
                'rqst_rcvd_bytes',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('rqst-rcvd-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TotalNum of pkts HTTP request received
                ''',
                'rqst_rcvd_packets',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'httpr-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat',
            False, 
            [
            _MetaInfoClassMember('class-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ClassId
                ''',
                'class_id',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('class-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                ClassName
                ''',
                'class_name',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('counter-validity-bitmask', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 Bitmask to indicate which counter or counters
                are undetermined. Counters will be marked
                undetermined when one or more classes share
                queues with class-default because in such cases
                the value of counters for each class is invalid.
                Based on the flag(s) set, the following counters
                will be marked undetermined. For example, if
                value of this object returned is 0x00000101,
                counters
                TransmitPackets/TransmitBytes/TotalTransmitRate
                and DropPackets/DropBytes are undetermined
                .0x00000001 - Transmit
                (TransmitPackets/TransmitBytes/TotalTransmitRate
                ), 0x00000002 - Drop
                (TotalDropPackets/TotalDropBytes/TotalDropRate),
                0x00000004 - Httpr
                (HttprTransmitPackets/HttprTransmitBytes), 
                ''',
                'counter_validity_bitmask',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('general-stats', REFERENCE_CLASS, 'GeneralStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats', 
                [], [], 
                '''                general stats
                ''',
                'general_stats',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('httpr-stats', REFERENCE_CLASS, 'HttprStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats', 
                [], [], 
                '''                HTTPR stats
                ''',
                'httpr_stats',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'class-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input',
            False, 
            [
            _MetaInfoClassMember('class-stat', REFERENCE_LIST, 'ClassStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat', 
                [], [], 
                '''                Array of classes contained in policy
                ''',
                'class_stat',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 42)], [], 
                '''                NodeName
                ''',
                'node_name',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                PolicyName
                ''',
                'policy_name',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PolicyStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'PolicyStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-pbr-oper', False),
            _MetaInfoClassMember('state-description', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                StateDescription
                ''',
                'state_description',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input', 
                [], [], 
                '''                PBR policy statistics
                ''',
                'input',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'direction',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-pbr-oper', True),
            _MetaInfoClassMember('direction', REFERENCE_CLASS, 'Direction' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction', 
                [], [], 
                '''                PBR direction
                ''',
                'direction',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces.Interface', 
                [], [], 
                '''                PBR action data for a particular interface
                ''',
                'interface',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node.PolicyMap' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node.PolicyMap',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap.Interfaces', 
                [], [], 
                '''                Operational data for all interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'policy-map',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node
                ''',
                'node_name',
                'Cisco-IOS-XR-pbr-oper', True),
            _MetaInfoClassMember('policy-map', REFERENCE_CLASS, 'PolicyMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node.PolicyMap', 
                [], [], 
                '''                Operational data for policymaps
                ''',
                'policy_map',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr.Nodes' : {
        'meta_info' : _MetaInfoClass('Pbr.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes.Node', 
                [], [], 
                '''                PBR operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
    'Pbr' : {
        'meta_info' : _MetaInfoClass('Pbr',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper', 'Pbr.Nodes', 
                [], [], 
                '''                Node-specific PBR operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-pbr-oper', False),
            ],
            'Cisco-IOS-XR-pbr-oper',
            'pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-pbr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_pbr_oper'
        ),
    },
}
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.GeneralStats']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat.HttprStats']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input.ClassStat']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction.Input']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface.Direction']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces.Interface']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap.Interfaces']['meta_info'].parent =_meta_table['Pbr.Nodes.Node.PolicyMap']['meta_info']
_meta_table['Pbr.Nodes.Node.PolicyMap']['meta_info'].parent =_meta_table['Pbr.Nodes.Node']['meta_info']
_meta_table['Pbr.Nodes.Node']['meta_info'].parent =_meta_table['Pbr.Nodes']['meta_info']
_meta_table['Pbr.Nodes']['meta_info'].parent =_meta_table['Pbr']['meta_info']
