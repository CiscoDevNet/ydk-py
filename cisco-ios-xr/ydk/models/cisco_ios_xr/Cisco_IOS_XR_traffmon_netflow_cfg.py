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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class NfCacheAgingMode(Enum):
    """
    NfCacheAgingMode (Enum Class)

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
    NfSamplingMode (Enum Class)

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
    	**type**\:  :py:class:`FlowExporterMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps>`
    
    .. attribute:: flow_sampler_maps
    
    	Flow sampler map configuration
    	**type**\:  :py:class:`FlowSamplerMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps>`
    
    .. attribute:: flow_monitor_map_table
    
    	Flow monitor map configuration
    	**type**\:  :py:class:`FlowMonitorMapTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable>`
    
    .. attribute:: flow_monitor_map_performance_table
    
    	Configure a performance traffic flow monitor map
    	**type**\:  :py:class:`FlowMonitorMapPerformanceTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable>`
    
    

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
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("flow-exporter-maps", ("flow_exporter_maps", NetFlow.FlowExporterMaps)), ("flow-sampler-maps", ("flow_sampler_maps", NetFlow.FlowSamplerMaps)), ("flow-monitor-map-table", ("flow_monitor_map_table", NetFlow.FlowMonitorMapTable)), ("flow-monitor-map-performance-table", ("flow_monitor_map_performance_table", NetFlow.FlowMonitorMapPerformanceTable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.flow_exporter_maps = NetFlow.FlowExporterMaps()
        self.flow_exporter_maps.parent = self
        self._children_name_map["flow_exporter_maps"] = "flow-exporter-maps"
        self._children_yang_names.add("flow-exporter-maps")

        self.flow_sampler_maps = NetFlow.FlowSamplerMaps()
        self.flow_sampler_maps.parent = self
        self._children_name_map["flow_sampler_maps"] = "flow-sampler-maps"
        self._children_yang_names.add("flow-sampler-maps")

        self.flow_monitor_map_table = NetFlow.FlowMonitorMapTable()
        self.flow_monitor_map_table.parent = self
        self._children_name_map["flow_monitor_map_table"] = "flow-monitor-map-table"
        self._children_yang_names.add("flow-monitor-map-table")

        self.flow_monitor_map_performance_table = NetFlow.FlowMonitorMapPerformanceTable()
        self.flow_monitor_map_performance_table.parent = self
        self._children_name_map["flow_monitor_map_performance_table"] = "flow-monitor-map-performance-table"
        self._children_yang_names.add("flow-monitor-map-performance-table")
        self._segment_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow"


    class FlowExporterMaps(Entity):
        """
        Configure a flow exporter map
        
        .. attribute:: flow_exporter_map
        
        	Exporter map name
        	**type**\: list of  		 :py:class:`FlowExporterMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowExporterMaps, self).__init__()

            self.yang_name = "flow-exporter-maps"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("flow-exporter-map", ("flow_exporter_map", NetFlow.FlowExporterMaps.FlowExporterMap))])
            self._leafs = OrderedDict()

            self.flow_exporter_map = YList(self)
            self._segment_path = lambda: "flow-exporter-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowExporterMaps, [], name, value)


        class FlowExporterMap(Entity):
            """
            Exporter map name
            
            .. attribute:: exporter_map_name  (key)
            
            	Exporter map name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: udp
            
            	Use UDP as transport protocol
            	**type**\:  :py:class:`Udp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Udp>`
            
            .. attribute:: destination
            
            	Configure export destination (collector)
            	**type**\:  :py:class:`Destination <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Destination>`
            
            .. attribute:: version
            
            	Specify export version parameters
            	**type**\:  :py:class:`Version <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Version>`
            
            .. attribute:: source_interface
            
            	Configure source interface for collector
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: dscp
            
            	Specify DSCP value for export packets
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: packet_length
            
            	Configure Maximum Value for Export Packet size
            	**type**\: int
            
            	**range:** 512..1468
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowExporterMaps.FlowExporterMap, self).__init__()

                self.yang_name = "flow-exporter-map"
                self.yang_parent_name = "flow-exporter-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['exporter_map_name']
                self._child_container_classes = OrderedDict([("udp", ("udp", NetFlow.FlowExporterMaps.FlowExporterMap.Udp)), ("destination", ("destination", NetFlow.FlowExporterMaps.FlowExporterMap.Destination)), ("version", ("version", NetFlow.FlowExporterMaps.FlowExporterMap.Version))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('exporter_map_name', YLeaf(YType.str, 'exporter-map-name')),
                    ('source_interface', YLeaf(YType.str, 'source-interface')),
                    ('dscp', YLeaf(YType.uint32, 'dscp')),
                    ('packet_length', YLeaf(YType.uint32, 'packet-length')),
                ])
                self.exporter_map_name = None
                self.source_interface = None
                self.dscp = None
                self.packet_length = None

                self.udp = NetFlow.FlowExporterMaps.FlowExporterMap.Udp()
                self.udp.parent = self
                self._children_name_map["udp"] = "udp"
                self._children_yang_names.add("udp")

                self.destination = NetFlow.FlowExporterMaps.FlowExporterMap.Destination()
                self.destination.parent = self
                self._children_name_map["destination"] = "destination"
                self._children_yang_names.add("destination")

                self.version = NetFlow.FlowExporterMaps.FlowExporterMap.Version()
                self.version.parent = self
                self._children_name_map["version"] = "version"
                self._children_yang_names.add("version")
                self._segment_path = lambda: "flow-exporter-map" + "[exporter-map-name='" + str(self.exporter_map_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-exporter-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap, ['exporter_map_name', 'source_interface', 'dscp', 'packet_length'], name, value)


            class Udp(Entity):
                """
                Use UDP as transport protocol
                
                .. attribute:: destination_port
                
                	Configure Destination UDP port
                	**type**\: int
                
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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('destination_port', YLeaf(YType.uint32, 'destination-port')),
                    ])
                    self.destination_port = None
                    self._segment_path = lambda: "udp"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Udp, ['destination_port'], name, value)


            class Destination(Entity):
                """
                Configure export destination (collector)
                
                .. attribute:: ip_address
                
                	Destination IPv4 address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_address
                
                	IPV6 address of the tunnel destination
                	**type**\: str
                
                .. attribute:: vrf_name
                
                	VRF name
                	**type**\: str
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, self).__init__()

                    self.yang_name = "destination"
                    self.yang_parent_name = "flow-exporter-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('ip_address', YLeaf(YType.str, 'ip-address')),
                        ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                        ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ])
                    self.ip_address = None
                    self.ipv6_address = None
                    self.vrf_name = None
                    self._segment_path = lambda: "destination"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Destination, ['ip_address', 'ipv6_address', 'vrf_name'], name, value)


            class Version(Entity):
                """
                Specify export version parameters
                
                .. attribute:: options
                
                	Specify options for exporting templates
                	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowExporterMaps.FlowExporterMap.Version.Options>`
                
                .. attribute:: version_type
                
                	Export version number
                	**type**\: int
                
                	**range:** 9..10
                
                .. attribute:: options_template_timeout
                
                	Option template configuration options
                	**type**\: int
                
                	**range:** 1..604800
                
                	**units**\: second
                
                	**default value**\: 1800
                
                .. attribute:: common_template_timeout
                
                	Specify custom timeout for the template
                	**type**\: int
                
                	**range:** 1..604800
                
                	**units**\: second
                
                	**default value**\: 1800
                
                .. attribute:: data_template_timeout
                
                	Data template configuration options
                	**type**\: int
                
                	**range:** 1..604800
                
                	**units**\: second
                
                	**default value**\: 1800
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowExporterMaps.FlowExporterMap.Version, self).__init__()

                    self.yang_name = "version"
                    self.yang_parent_name = "flow-exporter-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("options", ("options", NetFlow.FlowExporterMaps.FlowExporterMap.Version.Options))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('version_type', YLeaf(YType.uint32, 'version-type')),
                        ('options_template_timeout', YLeaf(YType.uint32, 'options-template-timeout')),
                        ('common_template_timeout', YLeaf(YType.uint32, 'common-template-timeout')),
                        ('data_template_timeout', YLeaf(YType.uint32, 'data-template-timeout')),
                    ])
                    self.version_type = None
                    self.options_template_timeout = None
                    self.common_template_timeout = None
                    self.data_template_timeout = None

                    self.options = NetFlow.FlowExporterMaps.FlowExporterMap.Version.Options()
                    self.options.parent = self
                    self._children_name_map["options"] = "options"
                    self._children_yang_names.add("options")
                    self._segment_path = lambda: "version"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Version, ['version_type', 'options_template_timeout', 'common_template_timeout', 'data_template_timeout'], name, value)


                class Options(Entity):
                    """
                    Specify options for exporting templates
                    
                    .. attribute:: interface_table_export_timeout
                    
                    	Specify timeout for exporting interface table
                    	**type**\: int
                    
                    	**range:** 0..604800
                    
                    	**units**\: second
                    
                    .. attribute:: sampler_table_export_timeout
                    
                    	Specify timeout for exporting sampler table
                    	**type**\: int
                    
                    	**range:** 0..604800
                    
                    	**units**\: second
                    
                    .. attribute:: vrf_table_export_timeout
                    
                    	Specify timeout for exporting vrf table
                    	**type**\: int
                    
                    	**range:** 0..604800
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'traffmon-netflow-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(NetFlow.FlowExporterMaps.FlowExporterMap.Version.Options, self).__init__()

                        self.yang_name = "options"
                        self.yang_parent_name = "version"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_table_export_timeout', YLeaf(YType.uint32, 'interface-table-export-timeout')),
                            ('sampler_table_export_timeout', YLeaf(YType.uint32, 'sampler-table-export-timeout')),
                            ('vrf_table_export_timeout', YLeaf(YType.uint32, 'vrf-table-export-timeout')),
                        ])
                        self.interface_table_export_timeout = None
                        self.sampler_table_export_timeout = None
                        self.vrf_table_export_timeout = None
                        self._segment_path = lambda: "options"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowExporterMaps.FlowExporterMap.Version.Options, ['interface_table_export_timeout', 'sampler_table_export_timeout', 'vrf_table_export_timeout'], name, value)


    class FlowSamplerMaps(Entity):
        """
        Flow sampler map configuration
        
        .. attribute:: flow_sampler_map
        
        	Sampler map name
        	**type**\: list of  		 :py:class:`FlowSamplerMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowSamplerMaps, self).__init__()

            self.yang_name = "flow-sampler-maps"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("flow-sampler-map", ("flow_sampler_map", NetFlow.FlowSamplerMaps.FlowSamplerMap))])
            self._leafs = OrderedDict()

            self.flow_sampler_map = YList(self)
            self._segment_path = lambda: "flow-sampler-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowSamplerMaps, [], name, value)


        class FlowSamplerMap(Entity):
            """
            Sampler map name
            
            .. attribute:: sampler_map_name  (key)
            
            	Sampler map name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: sampling_modes
            
            	Configure packet sampling mode
            	**type**\:  :py:class:`SamplingModes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes>`
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowSamplerMaps.FlowSamplerMap, self).__init__()

                self.yang_name = "flow-sampler-map"
                self.yang_parent_name = "flow-sampler-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['sampler_map_name']
                self._child_container_classes = OrderedDict([("sampling-modes", ("sampling_modes", NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('sampler_map_name', YLeaf(YType.str, 'sampler-map-name')),
                ])
                self.sampler_map_name = None

                self.sampling_modes = NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes()
                self.sampling_modes.parent = self
                self._children_name_map["sampling_modes"] = "sampling-modes"
                self._children_yang_names.add("sampling-modes")
                self._segment_path = lambda: "flow-sampler-map" + "[sampler-map-name='" + str(self.sampler_map_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-sampler-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowSamplerMaps.FlowSamplerMap, ['sampler_map_name'], name, value)


            class SamplingModes(Entity):
                """
                Configure packet sampling mode
                
                .. attribute:: sampling_mode
                
                	Configure sampling mode
                	**type**\: list of  		 :py:class:`SamplingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, self).__init__()

                    self.yang_name = "sampling-modes"
                    self.yang_parent_name = "flow-sampler-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("sampling-mode", ("sampling_mode", NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode))])
                    self._leafs = OrderedDict()

                    self.sampling_mode = YList(self)
                    self._segment_path = lambda: "sampling-modes"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes, [], name, value)


                class SamplingMode(Entity):
                    """
                    Configure sampling mode
                    
                    .. attribute:: mode  (key)
                    
                    	Sampling mode
                    	**type**\:  :py:class:`NfSamplingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfSamplingMode>`
                    
                    .. attribute:: sample_number
                    
                    	Number of packets to be sampled in the sampling interval
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: interval
                    
                    	Sampling interval in units of packets
                    	**type**\: int
                    
                    	**range:** 1..65535
                    
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
                        self.ylist_key_names = ['mode']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('mode', YLeaf(YType.enumeration, 'mode')),
                            ('sample_number', YLeaf(YType.uint32, 'sample-number')),
                            ('interval', YLeaf(YType.uint32, 'interval')),
                        ])
                        self.mode = None
                        self.sample_number = None
                        self.interval = None
                        self._segment_path = lambda: "sampling-mode" + "[mode='" + str(self.mode) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowSamplerMaps.FlowSamplerMap.SamplingModes.SamplingMode, ['mode', 'sample_number', 'interval'], name, value)


    class FlowMonitorMapTable(Entity):
        """
        Flow monitor map configuration
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of  		 :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowMonitorMapTable, self).__init__()

            self.yang_name = "flow-monitor-map-table"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("flow-monitor-map", ("flow_monitor_map", NetFlow.FlowMonitorMapTable.FlowMonitorMap))])
            self._leafs = OrderedDict()

            self.flow_monitor_map = YList(self)
            self._segment_path = lambda: "flow-monitor-map-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowMonitorMapTable, [], name, value)


        class FlowMonitorMap(Entity):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name  (key)
            
            	Monitor map name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option>`
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\:  :py:class:`Exporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\:  :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record>`
            
            	**presence node**\: True
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\: int
            
            	**range:** 4096..1000000
            
            	**default value**\: 65535
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: second
            
            	**default value**\: 15
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\: int
            
            	**range:** 1..1000000
            
            	**default value**\: 2000
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\:  :py:class:`NfCacheAgingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingMode>`
            
            	**default value**\: normal
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowMonitorMapTable.FlowMonitorMap, self).__init__()

                self.yang_name = "flow-monitor-map"
                self.yang_parent_name = "flow-monitor-map-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['monitor_map_name']
                self._child_container_classes = OrderedDict([("option", ("option", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option)), ("exporters", ("exporters", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters)), ("record", ("record", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('monitor_map_name', YLeaf(YType.str, 'monitor-map-name')),
                    ('cache_update_aging_timeout', YLeaf(YType.uint32, 'cache-update-aging-timeout')),
                    ('cache_entries', YLeaf(YType.uint32, 'cache-entries')),
                    ('cache_inactive_aging_timeout', YLeaf(YType.uint32, 'cache-inactive-aging-timeout')),
                    ('cache_active_aging_timeout', YLeaf(YType.uint32, 'cache-active-aging-timeout')),
                    ('cache_timeout_rate_limit', YLeaf(YType.uint32, 'cache-timeout-rate-limit')),
                    ('cache_aging_mode', YLeaf(YType.enumeration, 'cache-aging-mode')),
                ])
                self.monitor_map_name = None
                self.cache_update_aging_timeout = None
                self.cache_entries = None
                self.cache_inactive_aging_timeout = None
                self.cache_active_aging_timeout = None
                self.cache_timeout_rate_limit = None
                self.cache_aging_mode = None

                self.option = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option()
                self.option.parent = self
                self._children_name_map["option"] = "option"
                self._children_yang_names.add("option")

                self.exporters = NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self._children_name_map["exporters"] = "exporters"
                self._children_yang_names.add("exporters")

                self.record = None
                self._children_name_map["record"] = "record"
                self._children_yang_names.add("record")
                self._segment_path = lambda: "flow-monitor-map" + "[monitor-map-name='" + str(self.monitor_map_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-monitor-map-table/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap, ['monitor_map_name', 'cache_update_aging_timeout', 'cache_entries', 'cache_inactive_aging_timeout', 'cache_active_aging_timeout', 'cache_timeout_rate_limit', 'cache_aging_mode'], name, value)


            class Option(Entity):
                """
                Specify an option for the flow cache
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_bundle_member
                
                	Specify whether to export physical ifh for bundle interface
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bgp_attr
                
                	Specify if BGP Attributes AS\_PATH STD\_COMM should be exported
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, self).__init__()

                    self.yang_name = "option"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('filtered', YLeaf(YType.empty, 'filtered')),
                        ('out_bundle_member', YLeaf(YType.empty, 'out-bundle-member')),
                        ('out_phys_int', YLeaf(YType.empty, 'out-phys-int')),
                        ('bgp_attr', YLeaf(YType.empty, 'bgp-attr')),
                    ])
                    self.filtered = None
                    self.out_bundle_member = None
                    self.out_phys_int = None
                    self.bgp_attr = None
                    self._segment_path = lambda: "option"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Option, ['filtered', 'out_bundle_member', 'out_phys_int', 'bgp_attr'], name, value)


            class Exporters(Entity):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of  		 :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, self).__init__()

                    self.yang_name = "exporters"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("exporter", ("exporter", NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter))])
                    self._leafs = OrderedDict()

                    self.exporter = YList(self)
                    self._segment_path = lambda: "exporters"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters, [], name, value)


                class Exporter(Entity):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name  (key)
                    
                    	Exporter name
                    	**type**\: str
                    
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
                        self.ylist_key_names = ['exporter_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('exporter_name', YLeaf(YType.str, 'exporter-name')),
                        ])
                        self.exporter_name = None
                        self._segment_path = lambda: "exporter" + "[exporter-name='" + str(self.exporter_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Exporters.Exporter, ['exporter_name'], name, value)


            class Record(Entity):
                """
                Specify a flow record format
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\: str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\: int
                
                	**range:** 1..6
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('record_name', YLeaf(YType.str, 'record-name')),
                        ('label', YLeaf(YType.uint32, 'label')),
                    ])
                    self.record_name = None
                    self.label = None
                    self._segment_path = lambda: "record"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapTable.FlowMonitorMap.Record, ['record_name', 'label'], name, value)


    class FlowMonitorMapPerformanceTable(Entity):
        """
        Configure a performance traffic flow monitor map
        
        .. attribute:: flow_monitor_map
        
        	Monitor map name
        	**type**\: list of  		 :py:class:`FlowMonitorMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap>`
        
        

        """

        _prefix = 'traffmon-netflow-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(NetFlow.FlowMonitorMapPerformanceTable, self).__init__()

            self.yang_name = "flow-monitor-map-performance-table"
            self.yang_parent_name = "net-flow"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("flow-monitor-map", ("flow_monitor_map", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap))])
            self._leafs = OrderedDict()

            self.flow_monitor_map = YList(self)
            self._segment_path = lambda: "flow-monitor-map-performance-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable, [], name, value)


        class FlowMonitorMap(Entity):
            """
            Monitor map name
            
            .. attribute:: monitor_map_name  (key)
            
            	Monitor map name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: option
            
            	Specify an option for the flow cache
            	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option>`
            
            .. attribute:: exporters
            
            	Configure exporters to be used by the monitor\-map
            	**type**\:  :py:class:`Exporters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters>`
            
            .. attribute:: record
            
            	Specify a flow record format
            	**type**\:  :py:class:`Record <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record>`
            
            	**presence node**\: True
            
            .. attribute:: cache_update_aging_timeout
            
            	Specify the update flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_entries
            
            	Specify the number of entries in the flow cache
            	**type**\: int
            
            	**range:** 4096..1000000
            
            	**default value**\: 65535
            
            .. attribute:: cache_inactive_aging_timeout
            
            	Specify the inactive flow cache aging timeout
            	**type**\: int
            
            	**range:** 0..604800
            
            	**units**\: second
            
            	**default value**\: 15
            
            .. attribute:: cache_active_aging_timeout
            
            	Specify the active flow cache aging timeout
            	**type**\: int
            
            	**range:** 1..604800
            
            	**units**\: second
            
            	**default value**\: 1800
            
            .. attribute:: cache_timeout_rate_limit
            
            	Specify the maximum number of entries to age each second
            	**type**\: int
            
            	**range:** 1..1000000
            
            	**default value**\: 2000
            
            .. attribute:: cache_aging_mode
            
            	Specify the flow cache aging mode
            	**type**\:  :py:class:`NfCacheAgingMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NfCacheAgingMode>`
            
            	**default value**\: normal
            
            

            """

            _prefix = 'traffmon-netflow-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, self).__init__()

                self.yang_name = "flow-monitor-map"
                self.yang_parent_name = "flow-monitor-map-performance-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['monitor_map_name']
                self._child_container_classes = OrderedDict([("option", ("option", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option)), ("exporters", ("exporters", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters)), ("record", ("record", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('monitor_map_name', YLeaf(YType.str, 'monitor-map-name')),
                    ('cache_update_aging_timeout', YLeaf(YType.uint32, 'cache-update-aging-timeout')),
                    ('cache_entries', YLeaf(YType.uint32, 'cache-entries')),
                    ('cache_inactive_aging_timeout', YLeaf(YType.uint32, 'cache-inactive-aging-timeout')),
                    ('cache_active_aging_timeout', YLeaf(YType.uint32, 'cache-active-aging-timeout')),
                    ('cache_timeout_rate_limit', YLeaf(YType.uint32, 'cache-timeout-rate-limit')),
                    ('cache_aging_mode', YLeaf(YType.enumeration, 'cache-aging-mode')),
                ])
                self.monitor_map_name = None
                self.cache_update_aging_timeout = None
                self.cache_entries = None
                self.cache_inactive_aging_timeout = None
                self.cache_active_aging_timeout = None
                self.cache_timeout_rate_limit = None
                self.cache_aging_mode = None

                self.option = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option()
                self.option.parent = self
                self._children_name_map["option"] = "option"
                self._children_yang_names.add("option")

                self.exporters = NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters()
                self.exporters.parent = self
                self._children_name_map["exporters"] = "exporters"
                self._children_yang_names.add("exporters")

                self.record = None
                self._children_name_map["record"] = "record"
                self._children_yang_names.add("record")
                self._segment_path = lambda: "flow-monitor-map" + "[monitor-map-name='" + str(self.monitor_map_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-traffmon-netflow-cfg:net-flow/flow-monitor-map-performance-table/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap, ['monitor_map_name', 'cache_update_aging_timeout', 'cache_entries', 'cache_inactive_aging_timeout', 'cache_active_aging_timeout', 'cache_timeout_rate_limit', 'cache_aging_mode'], name, value)


            class Option(Entity):
                """
                Specify an option for the flow cache
                
                .. attribute:: filtered
                
                	Specify whether data should be filtered
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_bundle_member
                
                	Specify whether to export physical ifh for bundle interface
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: out_phys_int
                
                	Specify whether it exports the physical output interface
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bgp_attr
                
                	Specify if BGP Attributes AS\_PATH STD\_COMM should be exported
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, self).__init__()

                    self.yang_name = "option"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('filtered', YLeaf(YType.empty, 'filtered')),
                        ('out_bundle_member', YLeaf(YType.empty, 'out-bundle-member')),
                        ('out_phys_int', YLeaf(YType.empty, 'out-phys-int')),
                        ('bgp_attr', YLeaf(YType.empty, 'bgp-attr')),
                    ])
                    self.filtered = None
                    self.out_bundle_member = None
                    self.out_phys_int = None
                    self.bgp_attr = None
                    self._segment_path = lambda: "option"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Option, ['filtered', 'out_bundle_member', 'out_phys_int', 'bgp_attr'], name, value)


            class Exporters(Entity):
                """
                Configure exporters to be used by the
                monitor\-map
                
                .. attribute:: exporter
                
                	Configure exporter to be used by the monitor\-map
                	**type**\: list of  		 :py:class:`Exporter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_traffmon_netflow_cfg.NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter>`
                
                

                """

                _prefix = 'traffmon-netflow-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, self).__init__()

                    self.yang_name = "exporters"
                    self.yang_parent_name = "flow-monitor-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("exporter", ("exporter", NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter))])
                    self._leafs = OrderedDict()

                    self.exporter = YList(self)
                    self._segment_path = lambda: "exporters"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters, [], name, value)


                class Exporter(Entity):
                    """
                    Configure exporter to be used by the
                    monitor\-map
                    
                    .. attribute:: exporter_name  (key)
                    
                    	Exporter name
                    	**type**\: str
                    
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
                        self.ylist_key_names = ['exporter_name']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('exporter_name', YLeaf(YType.str, 'exporter-name')),
                        ])
                        self.exporter_name = None
                        self._segment_path = lambda: "exporter" + "[exporter-name='" + str(self.exporter_name) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Exporters.Exporter, ['exporter_name'], name, value)


            class Record(Entity):
                """
                Specify a flow record format
                
                .. attribute:: record_name
                
                	Flow record format (Either 'ipv4\-raw' ,'ipv4\-peer\-as', 'ipv6', 'mpls', 'mpls\-ipv4', 'mpls\-ipv6', 'mpls\-ipv4\-ipv6', 'ipv6\-peer\-as')
                	**type**\: str
                
                	**length:** 1..32
                
                	**mandatory**\: True
                
                .. attribute:: label
                
                	Enter label value for MPLS record type
                	**type**\: int
                
                	**range:** 1..6
                
                

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
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('record_name', YLeaf(YType.str, 'record-name')),
                        ('label', YLeaf(YType.uint32, 'label')),
                    ])
                    self.record_name = None
                    self.label = None
                    self._segment_path = lambda: "record"

                def __setattr__(self, name, value):
                    self._perform_setattr(NetFlow.FlowMonitorMapPerformanceTable.FlowMonitorMap.Record, ['record_name', 'label'], name, value)

    def clone_ptr(self):
        self._top_entity = NetFlow()
        return self._top_entity

