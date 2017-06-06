


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FlowMonitors.FlowMonitor.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('FlowMonitors.FlowMonitor.Flows.Flow',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source address of the flow
                ''',
                'source_address',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination address of the flow
                ''',
                'destination_address',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('interface-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input interface of the flow
                ''',
                'interface_input',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('is-multicast', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Multicast flow
                ''',
                'is_multicast',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('vrf-id-input', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                Vrf id input
                ''',
                'vrf_id_input',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                The source port number
                ''',
                'source_port',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                The destination port number
                ''',
                'destination_port',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('ip-tos', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ip-tos value
                ''',
                'ip_tos',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('ip-protocol', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                IP protocol number
                ''',
                'ip_protocol',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                Number of bytes passed through
                ''',
                'bytes',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            _MetaInfoClassMember('interface-output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output interface of the flow
                ''',
                'interface_output',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                Number of packets passed through
                ''',
                'packets',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            ],
            'Cisco-IOS-XE-flow-monitor-oper',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XE-flow-monitor-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper'
        ),
    },
    'FlowMonitors.FlowMonitor.Flows' : {
        'meta_info' : _MetaInfoClass('FlowMonitors.FlowMonitor.Flows',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper', 'FlowMonitors.FlowMonitor.Flows.Flow', 
                [], [], 
                '''                A flow
                ''',
                'flow',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            ],
            'Cisco-IOS-XE-flow-monitor-oper',
            'flows',
            _yang_ns._namespaces['Cisco-IOS-XE-flow-monitor-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper'
        ),
    },
    'FlowMonitors.FlowMonitor' : {
        'meta_info' : _MetaInfoClass('FlowMonitors.FlowMonitor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the flow monitor
                ''',
                'name',
                'Cisco-IOS-XE-flow-monitor-oper', True),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper', 'FlowMonitors.FlowMonitor.Flows', 
                [], [], 
                '''                All the flows for this flow monitor
                ''',
                'flows',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            _MetaInfoClassMember('time-collected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time the flow monitor data was collected in seconds.
                ''',
                'time_collected',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            ],
            'Cisco-IOS-XE-flow-monitor-oper',
            'flow-monitor',
            _yang_ns._namespaces['Cisco-IOS-XE-flow-monitor-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper'
        ),
    },
    'FlowMonitors' : {
        'meta_info' : _MetaInfoClass('FlowMonitors',
            False, 
            [
            _MetaInfoClassMember('flow-monitor', REFERENCE_LIST, 'FlowMonitor' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper', 'FlowMonitors.FlowMonitor', 
                [], [], 
                '''                A flow monitor
                ''',
                'flow_monitor',
                'Cisco-IOS-XE-flow-monitor-oper', False),
            ],
            'Cisco-IOS-XE-flow-monitor-oper',
            'flow-monitors',
            _yang_ns._namespaces['Cisco-IOS-XE-flow-monitor-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper'
        ),
    },
}
_meta_table['FlowMonitors.FlowMonitor.Flows.Flow']['meta_info'].parent =_meta_table['FlowMonitors.FlowMonitor.Flows']['meta_info']
_meta_table['FlowMonitors.FlowMonitor.Flows']['meta_info'].parent =_meta_table['FlowMonitors.FlowMonitor']['meta_info']
_meta_table['FlowMonitors.FlowMonitor']['meta_info'].parent =_meta_table['FlowMonitors']['meta_info']
