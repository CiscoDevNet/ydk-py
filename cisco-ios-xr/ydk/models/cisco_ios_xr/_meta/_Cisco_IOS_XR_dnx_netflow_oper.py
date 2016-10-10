


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'NfmgrFemEdmExpVerEnum' : _MetaInfoEnum('NfmgrFemEdmExpVerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper',
        {
            'v9':'V9',
            'ip-fix':'IP_FIX',
        }, 'Cisco-IOS-XR-dnx-netflow-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper']),
    'NfmgrFemEdmTransProtoEnum' : _MetaInfoEnum('NfmgrFemEdmTransProtoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper',
        {
            'unspecified':'UNSPECIFIED',
            'udp':'UDP',
        }, 'Cisco-IOS-XR-dnx-netflow-oper', _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper']),
    'NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap.Exporter' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap.Exporter',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exporter name
                ''',
                'name',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'exporter',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap',
            False, 
            [
            _MetaInfoClassMember('monitor-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Monitor name
                ''',
                'monitor_name',
                'Cisco-IOS-XR-dnx-netflow-oper', True),
            _MetaInfoClassMember('cache-active-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache active flow timeout in seconds
                ''',
                'cache_active_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('cache-aging-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aging mode for flow cache
                ''',
                'cache_aging_mode',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('cache-inactive-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache inactive flow timeout in seconds
                ''',
                'cache_inactive_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('cache-max-entry', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max num of entries in flow cache
                ''',
                'cache_max_entry',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('cache-timeout-rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of entries to age each second
                ''',
                'cache_timeout_rate_limit',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('cache-update-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache update timeout in seconds
                ''',
                'cache_update_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('exporter', REFERENCE_LIST, 'Exporter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap.Exporter', 
                [], [], 
                '''                Name of the flow exporters used by the flow
                monitor
                ''',
                'exporter',
                'Cisco-IOS-XR-dnx-netflow-oper', False, max_elements=8),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unique ID in the global flow monitor ID space
                ''',
                'id',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the flow monitor map
                ''',
                'name',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('number-of-labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of MPLS labels in key
                ''',
                'number_of_labels',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('options', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Options applied to the flow monitor
                ''',
                'options',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('record-map', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the flow record map
                ''',
                'record_map',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-monitor-map',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowMonitorMaps' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowMonitorMaps',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-map', REFERENCE_LIST, 'FlowMonitorMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap', 
                [], [], 
                '''                Flow monitor map information
                ''',
                'flow_monitor_map',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-monitor-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowSamplerMaps.FlowSamplerMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowSamplerMaps.FlowSamplerMap',
            False, 
            [
            _MetaInfoClassMember('sampler-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sampler name
                ''',
                'sampler_name',
                'Cisco-IOS-XR-dnx-netflow-oper', True),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unique ID in the global flow sampler ID space
                ''',
                'id',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the flow sampler map
                ''',
                'name',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('sampling-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sampling mode and parameters
                ''',
                'sampling_mode',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-sampler-map',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowSamplerMaps' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowSamplerMaps',
            False, 
            [
            _MetaInfoClassMember('flow-sampler-map', REFERENCE_LIST, 'FlowSamplerMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowSamplerMaps.FlowSamplerMap', 
                [], [], 
                '''                Flow sampler map information
                ''',
                'flow_sampler_map',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-sampler-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9',
            False, 
            [
            _MetaInfoClassMember('common-template-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Common template export timeout in seconds
                ''',
                'common_template_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('data-template-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data template export timeout in seconds
                ''',
                'data_template_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('interface-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface table export timeout in seconds
                ''',
                'interface_table_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('options-template-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Options template export timeout in seconds
                ''',
                'options_template_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('sampler-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sampler table export timeout in seconds
                ''',
                'sampler_table_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('vrf-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF table export timeout in seconds
                ''',
                'vrf_table_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'version9',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix',
            False, 
            [
            _MetaInfoClassMember('common-template-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Common template export timeout in seconds
                ''',
                'common_template_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('data-template-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Data template export timeout in seconds
                ''',
                'data_template_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('interface-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface table export timeout in seconds
                ''',
                'interface_table_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('options-template-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Options template export timeout in seconds
                ''',
                'options_template_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('sampler-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sampler table export timeout in seconds
                ''',
                'sampler_table_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('vrf-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF table export timeout in seconds
                ''',
                'vrf_table_export_timeout',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'ipfix',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version',
            False, 
            [
            _MetaInfoClassMember('ipfix', REFERENCE_CLASS, 'Ipfix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix', 
                [], [], 
                '''                ipfix
                ''',
                'ipfix',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'NfmgrFemEdmExpVerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NfmgrFemEdmExpVerEnum', 
                [], [], 
                '''                version
                ''',
                'version',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('version9', REFERENCE_CLASS, 'Version9' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9', 
                [], [], 
                '''                version9
                ''',
                'version9',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'version',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Collector' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Collector',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination IPv4 address in AAA.BBB.CCC.DDD
                format
                ''',
                'destination_address',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Transport destination port number
                ''',
                'destination_port',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                DSCP
                ''',
                'dscp',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source IPv4 address in AAA.BBB.CCC.DDD format
                ''',
                'source_address',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source interface name
                ''',
                'source_interface',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('transport-protocol', REFERENCE_ENUM_CLASS, 'NfmgrFemEdmTransProtoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NfmgrFemEdmTransProtoEnum', 
                [], [], 
                '''                Transport protocol
                ''',
                'transport_protocol',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
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
    'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowExporterMaps.FlowExporterMap',
            False, 
            [
            _MetaInfoClassMember('exporter-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Exporter name
                ''',
                'exporter_name',
                'Cisco-IOS-XR-dnx-netflow-oper', True),
            _MetaInfoClassMember('collector', REFERENCE_LIST, 'Collector' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Collector', 
                [], [], 
                '''                Export collector array
                ''',
                'collector',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unique ID in the global flow exporter ID space
                ''',
                'id',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the flow exporter map
                ''',
                'name',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('version', REFERENCE_CLASS, 'Version' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version', 
                [], [], 
                '''                Export version data
                ''',
                'version',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-exporter-map',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration.FlowExporterMaps' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration.FlowExporterMaps',
            False, 
            [
            _MetaInfoClassMember('flow-exporter-map', REFERENCE_LIST, 'FlowExporterMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowExporterMaps.FlowExporterMap', 
                [], [], 
                '''                Flow exporter map information
                ''',
                'flow_exporter_map',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'flow-exporter-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Configuration' : {
        'meta_info' : _MetaInfoClass('NetFlow.Configuration',
            False, 
            [
            _MetaInfoClassMember('flow-exporter-maps', REFERENCE_CLASS, 'FlowExporterMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowExporterMaps', 
                [], [], 
                '''                Flow exporter map configuration information
                ''',
                'flow_exporter_maps',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('flow-monitor-maps', REFERENCE_CLASS, 'FlowMonitorMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowMonitorMaps', 
                [], [], 
                '''                Flow monitor map configuration information
                ''',
                'flow_monitor_maps',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            _MetaInfoClassMember('flow-sampler-maps', REFERENCE_CLASS, 'FlowSamplerMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration.FlowSamplerMaps', 
                [], [], 
                '''                Flow sampler map configuration information
                ''',
                'flow_sampler_maps',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
            ],
            'Cisco-IOS-XR-dnx-netflow-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-netflow-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper'
        ),
    },
    'NetFlow.Statistics.Statistic.Producer.Statistics' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Producer.Statistics',
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
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Producer.Statistics', 
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
    'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector',
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
    'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic' : {
        'meta_info' : _MetaInfoClass('NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic',
            False, 
            [
            _MetaInfoClassMember('collector', REFERENCE_LIST, 'Collector' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector', 
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
            _MetaInfoClassMember('statistic', REFERENCE_LIST, 'Statistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic', 
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
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
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
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
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
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_netflow_oper', 'NetFlow.Configuration', 
                [], [], 
                '''                NetFlow configuration information
                ''',
                'configuration',
                'Cisco-IOS-XR-dnx-netflow-oper', False),
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
_meta_table['NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap.Exporter']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.Configuration.FlowMonitorMaps.FlowMonitorMap']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowMonitorMaps']['meta_info']
_meta_table['NetFlow.Configuration.FlowSamplerMaps.FlowSamplerMap']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowSamplerMaps']['meta_info']
_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Version9']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version']['meta_info']
_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version.Ipfix']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version']['meta_info']
_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Version']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap']['meta_info']
_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap.Collector']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap']['meta_info']
_meta_table['NetFlow.Configuration.FlowExporterMaps.FlowExporterMap']['meta_info'].parent =_meta_table['NetFlow.Configuration.FlowExporterMaps']['meta_info']
_meta_table['NetFlow.Configuration.FlowMonitorMaps']['meta_info'].parent =_meta_table['NetFlow.Configuration']['meta_info']
_meta_table['NetFlow.Configuration.FlowSamplerMaps']['meta_info'].parent =_meta_table['NetFlow.Configuration']['meta_info']
_meta_table['NetFlow.Configuration.FlowExporterMaps']['meta_info'].parent =_meta_table['NetFlow.Configuration']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Producer.Statistics']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Producer']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic.Collector']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter.Statistic']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter.Exporter']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters.FlowExporter']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server.FlowExporters']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic.Server']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Producer']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic']['meta_info']
_meta_table['NetFlow.Statistics.Statistic.Server']['meta_info'].parent =_meta_table['NetFlow.Statistics.Statistic']['meta_info']
_meta_table['NetFlow.Statistics.Statistic']['meta_info'].parent =_meta_table['NetFlow.Statistics']['meta_info']
_meta_table['NetFlow.Configuration']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
_meta_table['NetFlow.Statistics']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
