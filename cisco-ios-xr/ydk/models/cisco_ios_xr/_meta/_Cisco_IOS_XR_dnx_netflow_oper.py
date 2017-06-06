


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NetFlow.Statistics.Statistic.Producer.Statistics_' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Producer.Statistics_',
            False, 
            [
            _MetaInfoClassMember('drops-no-space', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Drops (no space)
                ''',
                'drops_no_space',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('drops-others', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Drops (others)
                ''',
                'drops_others',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('ipv4-egress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                IPv4 egress flows
                ''',
                'ipv4_egress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('ipv4-ingress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                IPv4 ingress flows
                ''',
                'ipv4_ingress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('ipv6-egress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                IPv6 egress flows
                ''',
                'ipv6_egress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('ipv6-ingress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                IPv6 ingress flows
                ''',
                'ipv6_ingress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-cleared', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last time Statistics cleared in 'Mon Jan 1 12:00
                :00 2xxx' format
                ''',
                'last_cleared',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('mpls-egress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MPLS egress flows
                ''',
                'mpls_egress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('mpls-ingress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                MPLS ingress flows
                ''',
                'mpls_ingress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('unknown-egress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unknown egress flows
                ''',
                'unknown_egress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('unknown-ingress-flows', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unknown ingress flows
                ''',
                'unknown_ingress_flows',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('waiting-servers', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of waiting servers
                ''',
                'waiting_servers',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Producer' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Producer',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Producer.Statistics_', 
                [], [], 
                '''                Statistics information
                ''',
                'statistics',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'producer',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector',
            False, 
            [
            _MetaInfoClassMember('bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes dropped
                ''',
                'bytes_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bytes sent
                ''',
                'bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination IPv4 address in AAA.BBB.CCC.DDD
                format
                ''',
                'destination_address',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Destination port number
                ''',
                'destination_port',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('exporter-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exporter state
                ''',
                'exporter_state',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('flow-bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flow bytes dropped
                ''',
                'flow_bytes_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('flow-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flow bytes sent
                ''',
                'flow_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('flows-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flows dropped
                ''',
                'flows_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('flows-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flows sent
                ''',
                'flows_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-hour-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes exported over the last one hour
                ''',
                'last_hour_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-hour-flows-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total flows exported over the of last one hour
                ''',
                'last_hour_flows_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-hour-packest-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total packets exported over the last one hour
                ''',
                'last_hour_packest_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-minute-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes exported over the last one minute
                ''',
                'last_minute_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-minute-flows-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total flows exported over the last one minute
                ''',
                'last_minute_flows_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-minute-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total packets exported over the last one minute
                ''',
                'last_minute_packets',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-second-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total bytes exported over the last one second
                ''',
                'last_second_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-second-flows-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total flows exported over the last one second
                ''',
                'last_second_flows_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('last-second-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total packets exported over the last one second
                ''',
                'last_second_packets_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-data-bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option data dropped
                ''',
                'option_data_bytes_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-data-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option data bytes sent
                ''',
                'option_data_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-data-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option data dropped
                ''',
                'option_data_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-data-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option data sent
                ''',
                'option_data_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-template-bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option template bytes dropped
                ''',
                'option_template_bytes_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-template-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option template bytes sent
                ''',
                'option_template_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-templates-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option templates dropped
                ''',
                'option_templates_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('option-templates-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Option templates sent
                ''',
                'option_templates_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('packets-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped
                ''',
                'packets_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets sent
                ''',
                'packets_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('souce-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Source port number
                ''',
                'souce_port',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source IPv4 address in AAA.BBB.CCC.DDD format
                ''',
                'source_address',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('template-bytes-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Template bytes dropped
                ''',
                'template_bytes_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('template-bytes-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Template bytes sent
                ''',
                'template_bytes_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('templates-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Templates dropped
                ''',
                'templates_dropped',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('templates-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Templates sent
                ''',
                'templates_sent',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('transport-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transport protocol
                ''',
                'transport_protocol',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'collector',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_',
            False, 
            [
            _MetaInfoClassMember('collector', REFERENCE_LIST, 'Collector' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector', 
                [], [], 
                '''                Statistics of all collectors
                ''',
                'collector',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('memory-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Memory usage
                ''',
                'memory_usage',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exporter name
                ''',
                'name',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('used-by-flow-monitor', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of flow monitors that use the exporter
                ''',
                'used_by_flow_monitor',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter',
            False, 
            [
            _MetaInfoClassMember('statistic', REFERENCE_LIST, 'Statistic_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_', 
                [], [], 
                '''                Array of flow exporters
                ''',
                'statistic',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'exporter',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter',
            False, 
            [
            _MetaInfoClassMember('exporter-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Exporter name
                ''',
                'exporter_name',
                'Cisco-IOS-XR-dnx-netflow-oper', True),
            _MetaInfoClassMember('exporter', REFERENCE_CLASS, 'Exporter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter', 
                [], [], 
                '''                Statistics information for the exporter
                ''',
                'exporter',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-exporter',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Server.FlowExporters' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters',
            False, 
            [
            _MetaInfoClassMember('flow-exporter', REFERENCE_LIST, 'FlowExporter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter', 
                [], [], 
                '''                Exporter information
                ''',
                'flow_exporter',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-exporters',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Server' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server',
            False, 
            [
            _MetaInfoClassMember('flow-exporters', REFERENCE_CLASS, 'FlowExporters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters', 
                [], [], 
                '''                Flow exporter information
                ''',
                'flow_exporters',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node location
                ''',
                'node',
                'Cisco-IOS-XR-dnx-netflow-oper', True),
            _MetaInfoClassMember('producer', REFERENCE_CLASS, 'Producer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Producer', 
                [], [], 
                '''                NetFlow producer statistics
                ''',
                'producer',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server', 
                [], [], 
                '''                NetFlow server statistics
                ''',
                'server',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics',
            False, 
            [
            _MetaInfoClassMember('statistic', REFERENCE_LIST, 'Statistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic', 
                [], [], 
                '''                NetFlow statistics information for a particular
                node
                ''',
                'statistic',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow' : {
        'meta_info' : _MetaInfoClass('NetFlow',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics', 
                [], [], 
                '''                Node-specific NetFlow statistics information
                ''',
                'statistics',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'net-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
}
_meta_table['NetFlow.Statistics.Statistic.Producer.Statistics_']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Producer']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_.Collector']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic_']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Producer']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic']['meta_info']
_meta_table['NetFlow.Statistics.Statistic']['meta_info'].parent =_meta_table['NetFlow.Statistics']['meta_info']
_meta_table['NetFlow.Statistics']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
