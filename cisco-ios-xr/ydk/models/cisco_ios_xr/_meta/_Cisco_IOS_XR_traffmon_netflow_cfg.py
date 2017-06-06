


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NfSamplingModeEnum' : _MetaInfoEnum('NfSamplingModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg',
        {
            'random':'random',
        }, 'Cisco-IOS-XR-traffmon-netflow-cfg', _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg']),
    'NfCacheAgingModeEnum' : _MetaInfoEnum('NfCacheAgingModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg',
        {
            'normal':'normal',
            'permanent':'permanent',
            'immediate':'immediate',
        }, 'Cisco-IOS-XR-traffmon-netflow-cfg', _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg']),
    'NetFlow.FlowExporterMaps.FlowExporterMap.Udp' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps.FlowExporterMap.Udp',
            False, 
            [
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('1024', '65535')], [], 
                '''                Configure Destination UDP port
                ''',
                'destination_port',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'udp',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options',
            False, 
            [
            _MetaInfoClassMember('interface-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specify timeout for exporting interface
                table
                ''',
                'interface_table_export_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('sampler-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specify timeout for exporting sampler table
                ''',
                'sampler_table_export_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('vrf-table-export-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specify timeout for exporting vrf table
                ''',
                'vrf_table_export_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'options',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version',
            False, 
            [
            _MetaInfoClassMember('version-number', ATTRIBUTE, 'int' , None, None, 
                [('9', '10')], [], 
                '''                Export version number
                ''',
                'version_number',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('common-template-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Specify custom timeout for the template
                ''',
                'common_template_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('data-template-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Data template configuration options
                ''',
                'data_template_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('options', REFERENCE_CLASS, 'Options' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options', 
                [], [], 
                '''                Specify options for exporting templates
                ''',
                'options',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('options-template-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Option template configuration options
                ''',
                'options_template_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'version',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowExporterMaps.FlowExporterMap.Versions' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps.FlowExporterMap.Versions',
            False, 
            [
            _MetaInfoClassMember('version', REFERENCE_LIST, 'Version' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version', 
                [], [], 
                '''                Configure export version options
                ''',
                'version',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'versions',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowExporterMaps.FlowExporterMap.Destination' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps.FlowExporterMap.Destination',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPV6 address of the tunnel destination
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'destination',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowExporterMaps.FlowExporterMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps.FlowExporterMap',
            False, 
            [
            _MetaInfoClassMember('exporter-map-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Exporter map name
                ''',
                'exporter_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('destination', REFERENCE_CLASS, 'Destination' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps.FlowExporterMap.Destination', 
                [], [], 
                '''                Configure export destination (collector)
                ''',
                'destination',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Specify DSCP value for export packets
                ''',
                'dscp',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('packet-length', ATTRIBUTE, 'int' , None, None, 
                [('512', '1468')], [], 
                '''                Configure Maximum Value for Export Packet size
                ''',
                'packet_length',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure source interface for collector
                ''',
                'source_interface',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('udp', REFERENCE_CLASS, 'Udp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps.FlowExporterMap.Udp', 
                [], [], 
                '''                Use UDP as transport protocol
                ''',
                'udp',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('versions', REFERENCE_CLASS, 'Versions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps.FlowExporterMap.Versions', 
                [], [], 
                '''                Specify export version parameters
                ''',
                'versions',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-exporter-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowExporterMaps' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowExporterMaps',
            False, 
            [
            _MetaInfoClassMember('flow-exporter-map', REFERENCE_LIST, 'FlowExporterMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps.FlowExporterMap', 
                [], [], 
                '''                Exporter map name
                ''',
                'flow_exporter_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-exporter-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode',
            False, 
            [
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'NfSamplingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NfSamplingModeEnum', 
                [], [], 
                '''                Sampling mode
                ''',
                'mode',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Sampling interval in units of packets
                ''',
                'interval',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('sample-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets to be sampled in the
                sampling interval
                ''',
                'sample_number',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'sampling-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes',
            False, 
            [
            _MetaInfoClassMember('sampling-mode', REFERENCE_LIST, 'SamplingMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode', 
                [], [], 
                '''                Configure sampling mode
                ''',
                'sampling_mode',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'sampling-modes',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowSamplerMaps.FlowSamplerMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowSamplerMaps.FlowSamplerMap',
            False, 
            [
            _MetaInfoClassMember('sampler-map-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Sampler map name
                ''',
                'sampler_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('sampling-modes', REFERENCE_CLASS, 'SamplingModes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes', 
                [], [], 
                '''                Configure packet sampling mode
                ''',
                'sampling_modes',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-sampler-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowSamplerMaps' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowSamplerMaps',
            False, 
            [
            _MetaInfoClassMember('flow-sampler-map', REFERENCE_LIST, 'FlowSamplerMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowSamplerMaps.FlowSamplerMap', 
                [], [], 
                '''                Sampler map name
                ''',
                'flow_sampler_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-sampler-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option',
            False, 
            [
            _MetaInfoClassMember('bgp-attr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify if BGP Attributes AS_PATH STD_COMM
                should be exported
                ''',
                'bgp_attr',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('filtered', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify whether data should be filtered
                ''',
                'filtered',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('out-bundle-member', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify whether to export physical ifh for
                bundle interface
                ''',
                'out_bundle_member',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('out-phys-int', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify whether it exports the physical output
                interface
                ''',
                'out_phys_int',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter',
            False, 
            [
            _MetaInfoClassMember('exporter-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Exporter name
                ''',
                'exporter_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'exporter',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters',
            False, 
            [
            _MetaInfoClassMember('exporter', REFERENCE_LIST, 'Exporter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter', 
                [], [], 
                '''                Configure exporter to be used by the
                monitor-map
                ''',
                'exporter',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'exporters',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                Enter label value for MPLS record type
                ''',
                'label',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('record-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Flow record format (Either 'ipv4-raw'
                ,'ipv4-peer-as', 'ipv6', 'mpls', 'mpls-ipv4',
                'mpls-ipv6', 'mpls-ipv4-ipv6', 'ipv6-peer-as')
                ''',
                'record_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'record',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapTable.FlowMonitorMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapTable.FlowMonitorMap',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('cache-active-aging-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Specify the active flow cache aging timeout
                ''',
                'cache_active_aging_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-aging-mode', REFERENCE_ENUM_CLASS, 'NfCacheAgingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NfCacheAgingModeEnum', 
                [], [], 
                '''                Specify the flow cache aging mode
                ''',
                'cache_aging_mode',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-entries', ATTRIBUTE, 'int' , None, None, 
                [('4096', '1000000')], [], 
                '''                Specify the number of entries in the flow cache
                ''',
                'cache_entries',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-inactive-aging-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specify the inactive flow cache aging timeout
                ''',
                'cache_inactive_aging_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-timeout-rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000000')], [], 
                '''                Specify the maximum number of entries to age
                each second
                ''',
                'cache_timeout_rate_limit',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-update-aging-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Specify the update flow cache aging timeout
                ''',
                'cache_update_aging_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('exporters', REFERENCE_CLASS, 'Exporters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters', 
                [], [], 
                '''                Configure exporters to be used by the
                monitor-map
                ''',
                'exporters',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option', 
                [], [], 
                '''                Specify an option for the flow cache
                ''',
                'option',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('record', REFERENCE_CLASS, 'Record' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record', 
                [], [], 
                '''                Specify a flow record format
                ''',
                'record',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapTable' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapTable',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-map', REFERENCE_LIST, 'FlowMonitorMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapTable.FlowMonitorMap', 
                [], [], 
                '''                Monitor map name
                ''',
                'flow_monitor_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map-table',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option',
            False, 
            [
            _MetaInfoClassMember('bgp-attr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify if BGP Attributes AS_PATH STD_COMM
                should be exported
                ''',
                'bgp_attr',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('filtered', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify whether data should be filtered
                ''',
                'filtered',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('out-bundle-member', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify whether to export physical ifh for
                bundle interface
                ''',
                'out_bundle_member',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('out-phys-int', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify whether it exports the physical output
                interface
                ''',
                'out_phys_int',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'option',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter',
            False, 
            [
            _MetaInfoClassMember('exporter-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Exporter name
                ''',
                'exporter_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'exporter',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters',
            False, 
            [
            _MetaInfoClassMember('exporter', REFERENCE_LIST, 'Exporter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter', 
                [], [], 
                '''                Configure exporter to be used by the
                monitor-map
                ''',
                'exporter',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'exporters',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                Enter label value for MPLS record type
                ''',
                'label',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('record-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Flow record format (Either 'ipv4-raw'
                ,'ipv4-peer-as', 'ipv6', 'mpls', 'mpls-ipv4',
                'mpls-ipv6', 'mpls-ipv4-ipv6', 'ipv6-peer-as')
                ''',
                'record_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'record',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap',
            False, 
            [
            _MetaInfoClassMember('monitor-map-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Monitor map name
                ''',
                'monitor_map_name',
                'Cisco-IOS-XR-traffmon-netflow-cfg', True),
            _MetaInfoClassMember('cache-active-aging-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Specify the active flow cache aging timeout
                ''',
                'cache_active_aging_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-aging-mode', REFERENCE_ENUM_CLASS, 'NfCacheAgingModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NfCacheAgingModeEnum', 
                [], [], 
                '''                Specify the flow cache aging mode
                ''',
                'cache_aging_mode',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-entries', ATTRIBUTE, 'int' , None, None, 
                [('4096', '1000000')], [], 
                '''                Specify the number of entries in the flow cache
                ''',
                'cache_entries',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-inactive-aging-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '604800')], [], 
                '''                Specify the inactive flow cache aging timeout
                ''',
                'cache_inactive_aging_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-timeout-rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000000')], [], 
                '''                Specify the maximum number of entries to age
                each second
                ''',
                'cache_timeout_rate_limit',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('cache-update-aging-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '604800')], [], 
                '''                Specify the update flow cache aging timeout
                ''',
                'cache_update_aging_timeout',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('exporters', REFERENCE_CLASS, 'Exporters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters', 
                [], [], 
                '''                Configure exporters to be used by the
                monitor-map
                ''',
                'exporters',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('option', REFERENCE_CLASS, 'Option' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option', 
                [], [], 
                '''                Specify an option for the flow cache
                ''',
                'option',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('record', REFERENCE_CLASS, 'Record' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record', 
                [], [], 
                '''                Specify a flow record format
                ''',
                'record',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow.FlowMonitorMapPerformanceTable' : {
        'meta_info' : _MetaInfoClass('NetFlow.FlowMonitorMapPerformanceTable',
            False, 
            [
            _MetaInfoClassMember('flow-monitor-map', REFERENCE_LIST, 'FlowMonitorMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap', 
                [], [], 
                '''                Monitor map name
                ''',
                'flow_monitor_map',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'flow-monitor-map-performance-table',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
    'NetFlow' : {
        'meta_info' : _MetaInfoClass('NetFlow',
            False, 
            [
            _MetaInfoClassMember('flow-exporter-maps', REFERENCE_CLASS, 'FlowExporterMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowExporterMaps', 
                [], [], 
                '''                Configure a flow exporter map
                ''',
                'flow_exporter_maps',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('flow-monitor-map-performance-table', REFERENCE_CLASS, 'FlowMonitorMapPerformanceTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapPerformanceTable', 
                [], [], 
                '''                Configure a performance traffic flow monitor map
                ''',
                'flow_monitor_map_performance_table',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('flow-monitor-map-table', REFERENCE_CLASS, 'FlowMonitorMapTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowMonitorMapTable', 
                [], [], 
                '''                Flow monitor map configuration
                ''',
                'flow_monitor_map_table',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            _MetaInfoClassMember('flow-sampler-maps', REFERENCE_CLASS, 'FlowSamplerMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg', 'NetFlow.FlowSamplerMaps', 
                [], [], 
                '''                Flow sampler map configuration
                ''',
                'flow_sampler_maps',
                'Cisco-IOS-XR-traffmon-netflow-cfg', False),
            ],
            'Cisco-IOS-XR-traffmon-netflow-cfg',
            'net-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-traffmon-netflow-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg'
        ),
    },
}
_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options']['meta_info'].parent =_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version']['meta_info']
_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version']['meta_info'].parent =_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions']['meta_info']
_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Udp']['meta_info'].parent =_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap']['meta_info']
_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Versions']['meta_info'].parent =_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap']['meta_info']
_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap.Destination']['meta_info'].parent =_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap']['meta_info']
_meta_table['NetFlow.FlowExporterMaps.FlowExporterMap']['meta_info'].parent =_meta_table['NetFlow.FlowExporterMaps']['meta_info']
_meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode']['meta_info'].parent =_meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes']['meta_info']
_meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes']['meta_info'].parent =_meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap']['meta_info']
_meta_table['NetFlow.FlowSamplerMaps.FlowSamplerMap']['meta_info'].parent =_meta_table['NetFlow.FlowSamplerMaps']['meta_info']
_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters']['meta_info']
_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.FlowMonitorMapTable.FlowMonitorMap']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapTable']['meta_info']
_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters']['meta_info']
_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap']['meta_info']
_meta_table['NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap']['meta_info'].parent =_meta_table['NetFlow.FlowMonitorMapPerformanceTable']['meta_info']
_meta_table['NetFlow.FlowExporterMaps']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
_meta_table['NetFlow.FlowSamplerMaps']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
_meta_table['NetFlow.FlowMonitorMapTable']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
_meta_table['NetFlow.FlowMonitorMapPerformanceTable']['meta_info'].parent =_meta_table['NetFlow']['meta_info']
