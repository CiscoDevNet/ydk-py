""" Cisco_IOS_XR_traffmon_netflow_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR traffmon\-netflow package configuration.

This module contains definitions
for the following management objects\:
  net\-flow\: NetFlow Configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NfCacheAgingMode(Enum):
    """
    NfCacheAgingMode

    Nf cache aging mode

    .. data:: normal = 0

    	Normal, caches age

    .. data:: permanent = 1

    	Permanent, caches never age

    .. data:: immediate = 2

    	Immediate, caches age immediately

    """

    normal = Enum.YLeaf(0, "normal")

    permanent = Enum.YLeaf(1, "permanent")

    immediate = Enum.YLeaf(2, "immediate")


class NfSamplingMode(Enum):
    """
    NfSamplingMode

    Nf sampling mode

    .. data:: random = 2

    	Random sampling

    """

    random = Enum.YLeaf(2, "random")



class NetFlow(Entity):
    """
    NetFlow Configuration
    
    .. attribute:: flow_exporter_maps
    
    	Configure a flow exporter map
    	**type**\:   :py:class:`FlowExporterMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps>`
    
    .. attribute:: flow_monitor_map_performance_table
    
    	Configure a performance traffic flow monitor map
    	**type**\:   :py:class:`FlowMonitorMapPerformanceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable>`
    
    .. attribute:: flow_monitor_map_table
    
    	Flow monitor map configuration
    	**type**\:   :py:class:`FlowMonitorMapTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable>`
    
    .. attribute:: flow_sampler_maps
    
    	Flow sampler map configuration
    	**type**\:   :py:class:`FlowSamplerMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps>`
    
    

    """

    _prefix = 'traffmon-netflow-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(NetFlow, self).__init__()
        self._top_entity = None

        self.yang_name = "net-flow"
        self.yang_parent_name = "Cisco-IOS-XR-traffmon-netflow-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"flow-exporter-maps" : ("flow_exporter_maps", NetFlow.FlowExporterMaps), "flow-monitor-map-performance-table" : ("flow_monitor_map_performance_table", NetFlow.FlowMonitorMapPerformanceTable), "flow-monitor-map-table" : ("flow_monitor_map_table", NetFlow.FlowMonitorMapTable), "flow-sampler-maps" : ("flow_sampler_maps", NetFlow.FlowSamplerMaps)}
        self._child_list_classes = {}

        self.flow_exporter_maps = NetFlow.FlowExporterMaps()
        self.flow_exporter_maps.parent = self
        self._children_name_map["flow_exporter_maps"] = "flow-exporter-maps"
        self._children_yang_names.add("flow-exporter-maps")

        self.flow_monitor_map_performance_table = NetFlow.FlowMonitorMapPerformanceTable()
        self.flow_monitor_map_performance_table.parent = self
        self._children_name_map["flow_monitor_map_performance_table"] = "flow-monitor-map-performance-table"
        self._children_yang_names.add("flow-monitor-map-performance-table")

        self.flow_monitor_map_table = NetFlow.FlowMonitorMapTable()
        self.flow_monitor_map_table.parent = self
        self._children_name_map["flow_monitor_map_table"] = "flow-monitor-map-table"
        self._children_yang_names.add("flow-monitor-map-table")

        self.flow_sampler_maps = NetFlow.FlowSamplerMaps()
        self.flow_sampler_maps.parent = self
        self._children_name_map["flow_sampler_maps"] = "flow-sampler-maps"
        self._children_yang_names.add("flow-sampler-maps")
        self._segment_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow"


    class FlowExporterMaps(Entity):
        """
        Configure a flow exporter map
        
        .. attribute:: flow_exporter_map
        
        	Exporter map name
        	**type**\: list of    :py:class:`FlowExporterMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowExporterMaps, self).__init__()

            self.yang_name = "flow-exporter-maps"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"flow-exporter-map" : ("flow_exporter_map", NetFlow.FlowExporterMaps.FlowExporterMap)}

            self.flow_exporter_map = YList(self)
            self._segment_path = lambda: "flow-exporter-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowExporterMaps, [], name, value)


        class FlowExporterMap(Entity):
            """
            Exporter map name
            
            .. attribute:: exporter_map_name  <key>
            
            	Exporter map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: destination
            
            	Configure export destination (collector)
            	**type**\:   :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Destination>`
            
            .. attribute:: dscp
            
            	Specify DSCP value for export packets
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: packet_length
            
            	Configure Maximum Value for Export Packet size
            	**type**\:  int
            
            	**range:** 512..1468
            
            .. attribute:: source_interface
            
            	Configure source interface for collector
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: udp
            
            	Use UDP as transport protocol
            	**type**\:   :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Udp>`
            
            .. attribute:: versions
            
            	Specify export version parameters
            	**type**\:   :py:class:`Versions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowExporterMaps.FlowExporterMap, self).__init__()

                self.yang_name = "flow-exporter-map"
                self.yang_parent_name = "flow-exporter-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"destination" : ("destination", NetFlow.FlowExporterMaps.FlowExporterMap.Destination), "udp" : ("udp", NetFlow.FlowExporterMaps.FlowExporterMap.Udp), "versions" : ("versions", NetFlow.FlowExporterMaps.FlowExporterMap.Versions)}
                self._child_list_classes = {}

                self.exporter_map_name = YLeaf(YType.str, "exporter-map-name")

                self.dscp = YLeaf(YType.uint32, "dscp")

                self.packet_length = YLeaf(YType.uint32, "packet-length")

                self.source_interface = YLeaf(YType.str, "source-interface")

                self.destination = NetFlow.FlowExporterMaps.FlowExporterMap.Destination()
                self.destination.parent = self
                self._children_name_map["destination"] = "destination"
                self._children_yang_names.add("destination")

                self.udp = NetFlow.FlowExporterMaps.FlowExporterMap.Udp()
                self.udp.parent = self
                self._children_name_map["udp"] = "udp"
                self._children_yang_names.add("udp")

                self.versions = NetFlow.FlowExporterMaps.FlowExporterMap.Versions()
                self.versions.parent = self
                self._children_name_map["versions"] = "versions"
                self._children_yang_names.add("versions")
                self._segment_path = lambda: "flow-exporter-map" + "[exporter-map-name='" + self.exporter_map_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-exporter-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap, ['exporter_map_name', 'dscp', 'packet_length', 'source_interface'], name, value)


            class Destination(Entity):
                """
                Configure export destination (collector)
                
                .. attribute:: ip_address
                
                	Destination IPv4 address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPV6 address of the tunnel destination
                	**type**\:  str
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\:  str
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "flow-exporter-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ip_address = YLeaf(YType.str, "ip-address")

                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                    self._segment_path = lambda: "destination"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, ['ip_address', 'ipv6_address', 'vrf_name'], name, value)


            class Udp(Entity):
                """
                Use UDP as transport protocol
                
                .. attribute:: destination_port
                
                	Configure Destination UDP port
                	**type**\:  int
                
                	**range:** 1024..65535
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Udp, self).__init__()

                    self.yang_name = "udp"
                    self.yang_parent_name = "flow-exporter-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.destination_port = YLeaf(YType.uint32, "destination-port")
                    self._segment_path = lambda: "udp"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Udp, ['destination_port'], name, value)


            class Versions(Entity):
                """
                Specify export version parameters
                
                .. attribute:: version
                
                	Configure export version options
                	**type**\: list of    :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions, self).__init__()

                    self.yang_name = "versions"
                    self.yang_parent_name = "flow-exporter-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"version" : ("version", NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version)}

                    self.version = YList(self)
                    self._segment_path = lambda: "versions"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Versions, [], name, value)


                class Version(Entity):
                    """
                    Configure export version options
                    
                    .. attribute:: version_number  <key>
                    
                    	Export version number
                    	**type**\:  int
                    
                    	**range:** 9..10
                    
                    .. attribute:: common_template_timeout
                    
                    	Specify custom timeout for the template
                    	**type**\:  int
                    
                    	**range:** 1..604800
                    
                    	**units**\: second
                    
                    	**default value**\: 1800
                    
                    .. attribute:: data_template_timeout
                    
                    	Data template configuration options
                    	**type**\:  int
                    
                    	**range:** 1..604800
                    
                    	**units**\: second
                    
                    	**default value**\: 1800
                    
                    .. attribute:: options
                    
                    	Specify options for exporting templates
                    	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options>`
                    
                    .. attribute:: options_template_timeout
                    
                    	Option template configuration options
                    	**type**\:  int
                    
                    	**range:** 1..604800
                    
                    	**units**\: second
                    
                    	**default value**\: 1800
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version, self).__init__()

                        self.yang_name = "version"
                        self.yang_parent_name = "versions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"options" : ("options", NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options)}
                        self._child_list_classes = {}

                        self.version_number = YLeaf(YType.uint32, "version-number")

                        self.common_template_timeout = YLeaf(YType.uint32, "common-template-timeout")

                        self.data_template_timeout = YLeaf(YType.uint32, "data-template-timeout")

                        self.options_template_timeout = YLeaf(YType.uint32, "options-template-timeout")

                        self.options = NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options()
                        self.options.parent = self
                        self._children_name_map["options"] = "options"
                        self._children_yang_names.add("options")
                        self._segment_path = lambda: "version" + "[version-number='" + self.version_number.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version, ['version_number', 'common_template_timeout', 'data_template_timeout', 'options_template_timeout'], name, value)


                    class Options(Entity):
                        """
                        Specify options for exporting templates
                        
                        .. attribute:: interface_table_export_timeout
                        
                        	Specify timeout for exporting interface table
                        	**type**\:  int
                        
                        	**range:** 0..604800
                        
                        	**units**\: second
                        
                        .. attribute:: sampler_table_export_timeout
                        
                        	Specify timeout for exporting sampler table
                        	**type**\:  int
                        
                        	**range:** 0..604800
                        
                        	**units**\: second
                        
                        .. attribute:: vrf_table_export_timeout
                        
                        	Specify timeout for exporting vrf table
                        	**type**\:  int
                        
                        	**range:** 0..604800
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'traffmon-netflow-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options, self).__init__()

                            self.yang_name = "options"
                            self.yang_parent_name = "version"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_table_export_timeout = YLeaf(YType.uint32, "interface-table-export-timeout")

                            self.sampler_table_export_timeout = YLeaf(YType.uint32, "sampler-table-export-timeout")

                            self.vrf_table_export_timeout = YLeaf(YType.uint32, "vrf-table-export-timeout")
                            self._segment_path = lambda: "options"

                        def __setattr__(self, name, value):
                            self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Versions.Version.Options, ['interface_table_export_timeout', 'sampler_table_export_timeout', 'vrf_table_export_timeout'], name, value)


    class FlowMonitorMapPerformanceTable(Entity):
        """
        Configure a performance traffic flow monitor map
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of    :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowMonitorMapPerformanceTable, self).__init__()

            self.yang_name = "flow-monitor-map-performance-table"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"flow-monitor-map" : ("flow_monitor_map", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap)}

            self.flow_monitor_map = YList(self)
            self._segment_path = lambda: "flow-monitor-map-performance-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable, [], name, value)


        class FlowMonitorMap(Entity):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name  <key>
            
            	Monitor map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\:   :py:class:`NfCacheAgingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingMode>`
            
            	**default value**\: normal
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\:  int
            
            	**range:** 4096..1000000
            
            	**default value**\: 65535
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: second
            
            	**default value**\: 15
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\:  int
            
            	**range:** 1..1000000
            
            	**default value**\: 2000
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\:   :py:class:`Exporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\:   :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, self).__init__()

                self.yang_name = "flow-monitor-map"
                self.yang_parent_name = "flow-monitor-map-performance-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"exporters" : ("exporters", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters), "option" : ("option", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option), "record" : ("record", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record)}
                self._child_list_classes = {}

                self.monitor_map_name = YLeaf(YType.str, "monitor-map-name")

                self.cache_active_aging_timeout = YLeaf(YType.uint32, "cache-active-aging-timeout")

                self.cache_aging_mode = YLeaf(YType.enumeration, "cache-aging-mode")

                self.cache_entries = YLeaf(YType.uint32, "cache-entries")

                self.cache_inactive_aging_timeout = YLeaf(YType.uint32, "cache-inactive-aging-timeout")

                self.cache_timeout_rate_limit = YLeaf(YType.uint32, "cache-timeout-rate-limit")

                self.cache_update_aging_timeout = YLeaf(YType.uint32, "cache-update-aging-timeout")

                self.exporters = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self._children_name_map["exporters"] = "exporters"
                self._children_yang_names.add("exporters")

                self.option = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option()
                self.option.parent = self
                self._children_name_map["option"] = "option"
                self._children_yang_names.add("option")

                self.record = None
                self._children_name_map["record"] = "record"
                self._children_yang_names.add("record")
                self._segment_path = lambda: "flow-monitor-map" + "[monitor-map-name='" + self.monitor_map_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-monitor-map-performance-table/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, ['monitor_map_name', 'cache_active_aging_timeout', 'cache_aging_mode', 'cache_entries', 'cache_inactive_aging_timeout', 'cache_timeout_rate_limit', 'cache_update_aging_timeout'], name, value)


            class Exporters(Entity):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of    :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, self).__init__()

                    self.yang_name = "exporters"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"exporter" : ("exporter", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter)}

                    self.exporter = YList(self)
                    self._segment_path = lambda: "exporters"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, [], name, value)


                class Exporter(Entity):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name  <key>
                    
                    	Exporter name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter, self).__init__()

                        self.yang_name = "exporter"
                        self.yang_parent_name = "exporters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.exporter_name = YLeaf(YType.str, "exporter-name")
                        self._segment_path = lambda: "exporter" + "[exporter-name='" + self.exporter_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter, ['exporter_name'], name, value)


            class Option(Entity):
                """
                Specify an option for the flow cache
                
                .. attribute:: bgp_attr
                
                	Specify if BGP Attributes AS\_PATH STD\_COMM should be exported
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_bundle_member
                
                	Specify whether to export physical ifh for bundle interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, self).__init__()

                    self.yang_name = "option"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bgp_attr = YLeaf(YType.empty, "bgp-attr")

                    self.filtered = YLeaf(YType.empty, "filtered")

                    self.out_bundle_member = YLeaf(YType.empty, "out-bundle-member")

                    self.out_phys_int = YLeaf(YType.empty, "out-phys-int")
                    self._segment_path = lambda: "option"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, ['bgp_attr', 'filtered', 'out_bundle_member', 'out_phys_int'], name, value)


            class Record(Entity):
                """
                Specify a flow record format
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\:  int
                
                	**range:** 1..6
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\:  str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record, self).__init__()

                    self.yang_name = "record"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.label = YLeaf(YType.uint32, "label")

                    self.record_name = YLeaf(YType.str, "record-name")
                    self._segment_path = lambda: "record"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record, ['label', 'record_name'], name, value)


    class FlowMonitorMapTable(Entity):
        """
        Flow monitor map configuration
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of    :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowMonitorMapTable, self).__init__()

            self.yang_name = "flow-monitor-map-table"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"flow-monitor-map" : ("flow_monitor_map", NetFlow.FlowMonitorMapTable.FlowMonitorMap)}

            self.flow_monitor_map = YList(self)
            self._segment_path = lambda: "flow-monitor-map-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowMonitorMapTable, [], name, value)


        class FlowMonitorMap(Entity):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name  <key>
            
            	Monitor map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\:   :py:class:`NfCacheAgingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingMode>`
            
            	**default value**\: normal
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\:  int
            
            	**range:** 4096..1000000
            
            	**default value**\: 65535
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: second
            
            	**default value**\: 15
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\:  int
            
            	**range:** 1..1000000
            
            	**default value**\: 2000
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\:   :py:class:`Exporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\:   :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\:   :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap, self).__init__()

                self.yang_name = "flow-monitor-map"
                self.yang_parent_name = "flow-monitor-map-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"exporters" : ("exporters", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters), "option" : ("option", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option), "record" : ("record", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record)}
                self._child_list_classes = {}

                self.monitor_map_name = YLeaf(YType.str, "monitor-map-name")

                self.cache_active_aging_timeout = YLeaf(YType.uint32, "cache-active-aging-timeout")

                self.cache_aging_mode = YLeaf(YType.enumeration, "cache-aging-mode")

                self.cache_entries = YLeaf(YType.uint32, "cache-entries")

                self.cache_inactive_aging_timeout = YLeaf(YType.uint32, "cache-inactive-aging-timeout")

                self.cache_timeout_rate_limit = YLeaf(YType.uint32, "cache-timeout-rate-limit")

                self.cache_update_aging_timeout = YLeaf(YType.uint32, "cache-update-aging-timeout")

                self.exporters = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self._children_name_map["exporters"] = "exporters"
                self._children_yang_names.add("exporters")

                self.option = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option()
                self.option.parent = self
                self._children_name_map["option"] = "option"
                self._children_yang_names.add("option")

                self.record = None
                self._children_name_map["record"] = "record"
                self._children_yang_names.add("record")
                self._segment_path = lambda: "flow-monitor-map" + "[monitor-map-name='" + self.monitor_map_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-monitor-map-table/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap, ['monitor_map_name', 'cache_active_aging_timeout', 'cache_aging_mode', 'cache_entries', 'cache_inactive_aging_timeout', 'cache_timeout_rate_limit', 'cache_update_aging_timeout'], name, value)


            class Exporters(Entity):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of    :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, self).__init__()

                    self.yang_name = "exporters"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"exporter" : ("exporter", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter)}

                    self.exporter = YList(self)
                    self._segment_path = lambda: "exporters"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, [], name, value)


                class Exporter(Entity):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name  <key>
                    
                    	Exporter name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter, self).__init__()

                        self.yang_name = "exporter"
                        self.yang_parent_name = "exporters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.exporter_name = YLeaf(YType.str, "exporter-name")
                        self._segment_path = lambda: "exporter" + "[exporter-name='" + self.exporter_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter, ['exporter_name'], name, value)


            class Option(Entity):
                """
                Specify an option for the flow cache
                
                .. attribute:: bgp_attr
                
                	Specify if BGP Attributes AS\_PATH STD\_COMM should be exported
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_bundle_member
                
                	Specify whether to export physical ifh for bundle interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, self).__init__()

                    self.yang_name = "option"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.bgp_attr = YLeaf(YType.empty, "bgp-attr")

                    self.filtered = YLeaf(YType.empty, "filtered")

                    self.out_bundle_member = YLeaf(YType.empty, "out-bundle-member")

                    self.out_phys_int = YLeaf(YType.empty, "out-phys-int")
                    self._segment_path = lambda: "option"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, ['bgp_attr', 'filtered', 'out_bundle_member', 'out_phys_int'], name, value)


            class Record(Entity):
                """
                Specify a flow record format
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\:  int
                
                	**range:** 1..6
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\:  str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record, self).__init__()

                    self.yang_name = "record"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}
                    self.is_presence_container = True

                    self.label = YLeaf(YType.uint32, "label")

                    self.record_name = YLeaf(YType.str, "record-name")
                    self._segment_path = lambda: "record"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record, ['label', 'record_name'], name, value)


    class FlowSamplerMaps(Entity):
        """
        Flow sampler map configuration
        
        .. attribute:: flow_sampler_map
        
        	Sampler map name
        	**type**\: list of    :py:class:`FlowSamplerMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowSamplerMaps, self).__init__()

            self.yang_name = "flow-sampler-maps"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"flow-sampler-map" : ("flow_sampler_map", NetFlow.FlowSamplerMaps.FlowSamplerMap)}

            self.flow_sampler_map = YList(self)
            self._segment_path = lambda: "flow-sampler-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowSamplerMaps, [], name, value)


        class FlowSamplerMap(Entity):
            """
            Sampler map name
            
            .. attribute:: sampler_map_name  <key>
            
            	Sampler map name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: sampling_modes
            
            	Configure packet sampling mode
            	**type**\:   :py:class:`SamplingModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowSamplerMaps.FlowSamplerMap, self).__init__()

                self.yang_name = "flow-sampler-map"
                self.yang_parent_name = "flow-sampler-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"sampling-modes" : ("sampling_modes", NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes)}
                self._child_list_classes = {}

                self.sampler_map_name = YLeaf(YType.str, "sampler-map-name")

                self.sampling_modes = NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes()
                self.sampling_modes.parent = self
                self._children_name_map["sampling_modes"] = "sampling-modes"
                self._children_yang_names.add("sampling-modes")
                self._segment_path = lambda: "flow-sampler-map" + "[sampler-map-name='" + self.sampler_map_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-sampler-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowSamplerMaps.FlowSamplerMap, ['sampler_map_name'], name, value)


            class SamplingModes(Entity):
                """
                Configure packet sampling mode
                
                .. attribute:: sampling_mode
                
                	Configure sampling mode
                	**type**\: list of    :py:class:`SamplingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, self).__init__()

                    self.yang_name = "sampling-modes"
                    self.yang_parent_name = "flow-sampler-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"sampling-mode" : ("sampling_mode", NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode)}

                    self.sampling_mode = YList(self)
                    self._segment_path = lambda: "sampling-modes"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, [], name, value)


                class SamplingMode(Entity):
                    """
                    Configure sampling mode
                    
                    .. attribute:: mode  <key>
                    
                    	Sampling mode
                    	**type**\:   :py:class:`NfSamplingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfSamplingMode>`
                    
                    .. attribute:: interval
                    
                    	Sampling interval in units of packets
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    	**mandatory**\: True
                    
                    .. attribute:: sample_number
                    
                    	Number of packets to be sampled in the sampling interval
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode, self).__init__()

                        self.yang_name = "sampling-mode"
                        self.yang_parent_name = "sampling-modes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.mode = YLeaf(YType.enumeration, "mode")

                        self.interval = YLeaf(YType.uint32, "interval")

                        self.sample_number = YLeaf(YType.uint32, "sample-number")
                        self._segment_path = lambda: "sampling-mode" + "[mode='" + self.mode.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode, ['mode', 'interval', 'sample_number'], name, value)

    def clone_ptr(self):
        self._top_entity = NetFlow()
        return self._top_entity

