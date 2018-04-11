""" Cisco_IOS_XE_flow_monitor_oper 

This module contains a collection of YANG definitions
for Flexible NetFlow Operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class FlowExporterIpwriteStatsType(Enum):
    """
    FlowExporterIpwriteStatsType (Enum Class)

    The Netflow export statistics

    .. data:: flow_exporter_ipwrite_stats_ok = 0

    	Normal Statistics event

    .. data:: flow_exporter_ipwrite_stats_no_fib = 1

    	No Forwarding Information Base event

    .. data:: flow_exporter_ipwrite_stats_fail_event = 2

    	Adjacency failed event

    .. data:: flow_exporter_ipwrite_stats_process = 3

    	Process switch event

    .. data:: flow_exporter_ipwrite_stats_enqueue_failed = 4

    	Enqueue Failed event

    .. data:: flow_exporter_ipwrite_stats_ipc_failed = 5

    	IPC failed event

    .. data:: flow_exporter_ipwrite_stats_output_failed = 6

    	Output failed event

    .. data:: flow_exporter_ipwrite_stats_mtu_failed = 7

    	Maximum Transmission Unit failed event

    .. data:: flow_exporter_ipwrite_stats_encapfix_failed = 8

    	Encapsulation Fixup failed event

    .. data:: flow_exporter_ipwrite_stats_cef_off = 9

    	Cisco Express Forwarding off event

    .. data:: flow_exporter_ipwrite_stats_other = 10

    	Other event

    .. data:: flow_exporter_ipwrite_stats_rate_limit = 11

    	Rate Limit event

    .. data:: flow_exporter_ipwrite_stats_no_destination = 12

    	No destination event

    """

    flow_exporter_ipwrite_stats_ok = Enum.YLeaf(0, "flow-exporter-ipwrite-stats-ok")

    flow_exporter_ipwrite_stats_no_fib = Enum.YLeaf(1, "flow-exporter-ipwrite-stats-no-fib")

    flow_exporter_ipwrite_stats_fail_event = Enum.YLeaf(2, "flow-exporter-ipwrite-stats-fail-event")

    flow_exporter_ipwrite_stats_process = Enum.YLeaf(3, "flow-exporter-ipwrite-stats-process")

    flow_exporter_ipwrite_stats_enqueue_failed = Enum.YLeaf(4, "flow-exporter-ipwrite-stats-enqueue-failed")

    flow_exporter_ipwrite_stats_ipc_failed = Enum.YLeaf(5, "flow-exporter-ipwrite-stats-ipc-failed")

    flow_exporter_ipwrite_stats_output_failed = Enum.YLeaf(6, "flow-exporter-ipwrite-stats-output-failed")

    flow_exporter_ipwrite_stats_mtu_failed = Enum.YLeaf(7, "flow-exporter-ipwrite-stats-mtu-failed")

    flow_exporter_ipwrite_stats_encapfix_failed = Enum.YLeaf(8, "flow-exporter-ipwrite-stats-encapfix-failed")

    flow_exporter_ipwrite_stats_cef_off = Enum.YLeaf(9, "flow-exporter-ipwrite-stats-cef-off")

    flow_exporter_ipwrite_stats_other = Enum.YLeaf(10, "flow-exporter-ipwrite-stats-other")

    flow_exporter_ipwrite_stats_rate_limit = Enum.YLeaf(11, "flow-exporter-ipwrite-stats-rate-limit")

    flow_exporter_ipwrite_stats_no_destination = Enum.YLeaf(12, "flow-exporter-ipwrite-stats-no-destination")


class FlowMonitorCacheState(Enum):
    """
    FlowMonitorCacheState (Enum Class)

    Flow monitor cache state

    .. data:: flow_monitor_cache_state_being_deleted = 0

    	Flow monitor cache is being deleted

    .. data:: flow_monitor_cache_state_being_allocated = 1

    	Flow monitor cache is being allocated

    .. data:: flow_monitor_cache_state_not_allocated = 2

    	Flow monitor cache is not allocated

    """

    flow_monitor_cache_state_being_deleted = Enum.YLeaf(0, "flow-monitor-cache-state-being-deleted")

    flow_monitor_cache_state_being_allocated = Enum.YLeaf(1, "flow-monitor-cache-state-being-allocated")

    flow_monitor_cache_state_not_allocated = Enum.YLeaf(2, "flow-monitor-cache-state-not-allocated")


class FlowMonitorCacheType(Enum):
    """
    FlowMonitorCacheType (Enum Class)

    The flow monitor cache type

    .. data:: flow_monitor_cache_type_normal = 0

    	Normal Flow monitor cache

    .. data:: flow_monitor_cache_type_permanent = 1

    	Permanent cache type

    .. data:: flow_monitor_cache_type_synchronized = 2

    	Synchronized Flow monitor cache type

    .. data:: flow_monitor_cache_type_immediate = 3

    	Immediate Flow monitor cache type

    """

    flow_monitor_cache_type_normal = Enum.YLeaf(0, "flow-monitor-cache-type-normal")

    flow_monitor_cache_type_permanent = Enum.YLeaf(1, "flow-monitor-cache-type-permanent")

    flow_monitor_cache_type_synchronized = Enum.YLeaf(2, "flow-monitor-cache-type-synchronized")

    flow_monitor_cache_type_immediate = Enum.YLeaf(3, "flow-monitor-cache-type-immediate")



class FlowMonitors(Entity):
    """
    All of the flow monitors
    
    .. attribute:: flow_monitor
    
    	List of Flow monitors
    	**type**\: list of  		 :py:class:`FlowMonitor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor>`
    
    .. attribute:: flow_export_statistics
    
    	List of statistics per exporter
    	**type**\: list of  		 :py:class:`FlowExportStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowExportStatistics>`
    
    .. attribute:: flow_cache_statistics
    
    	List of statistics per flow cache
    	**type**\: list of  		 :py:class:`FlowCacheStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowCacheStatistics>`
    
    .. attribute:: flow_monitor_statistics
    
    	List of statistics per flow monitor
    	**type**\: list of  		 :py:class:`FlowMonitorStatistics <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitorStatistics>`
    
    

    """

    _prefix = 'flow-monitor-ios-xe-oper'
    _revision = '2017-11-30'

    def __init__(self):
        super(FlowMonitors, self).__init__()
        self._top_entity = None

        self.yang_name = "flow-monitors"
        self.yang_parent_name = "Cisco-IOS-XE-flow-monitor-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("flow-monitor", ("flow_monitor", FlowMonitors.FlowMonitor)), ("flow-export-statistics", ("flow_export_statistics", FlowMonitors.FlowExportStatistics)), ("flow-cache-statistics", ("flow_cache_statistics", FlowMonitors.FlowCacheStatistics)), ("flow-monitor-statistics", ("flow_monitor_statistics", FlowMonitors.FlowMonitorStatistics))])
        self._leafs = OrderedDict()

        self.flow_monitor = YList(self)
        self.flow_export_statistics = YList(self)
        self.flow_cache_statistics = YList(self)
        self.flow_monitor_statistics = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors"

    def __setattr__(self, name, value):
        self._perform_setattr(FlowMonitors, [], name, value)


    class FlowMonitor(Entity):
        """
        List of Flow monitors
        
        .. attribute:: name  (key)
        
        	Name of the flow monitor
        	**type**\: str
        
        .. attribute:: time_collected
        
        	Time the flow monitor data was collected in seconds
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flows
        
        	All the flows for this flow monitor
        	**type**\:  :py:class:`Flows <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows>`
        
        

        """

        _prefix = 'flow-monitor-ios-xe-oper'
        _revision = '2017-11-30'

        def __init__(self):
            super(FlowMonitors.FlowMonitor, self).__init__()

            self.yang_name = "flow-monitor"
            self.yang_parent_name = "flow-monitors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([("flows", ("flows", FlowMonitors.FlowMonitor.Flows))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('time_collected', YLeaf(YType.uint64, 'time-collected')),
            ])
            self.name = None
            self.time_collected = None

            self.flows = FlowMonitors.FlowMonitor.Flows()
            self.flows.parent = self
            self._children_name_map["flows"] = "flows"
            self._children_yang_names.add("flows")
            self._segment_path = lambda: "flow-monitor" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FlowMonitors.FlowMonitor, ['name', 'time_collected'], name, value)


        class Flows(Entity):
            """
            All the flows for this flow monitor
            
            .. attribute:: flow
            
            	List of flows
            	**type**\: list of  		 :py:class:`Flow <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitor.Flows.Flow>`
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-11-30'

            def __init__(self):
                super(FlowMonitors.FlowMonitor.Flows, self).__init__()

                self.yang_name = "flows"
                self.yang_parent_name = "flow-monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("flow", ("flow", FlowMonitors.FlowMonitor.Flows.Flow))])
                self._leafs = OrderedDict()

                self.flow = YList(self)
                self._segment_path = lambda: "flows"

            def __setattr__(self, name, value):
                self._perform_setattr(FlowMonitors.FlowMonitor.Flows, [], name, value)


            class Flow(Entity):
                """
                List of flows
                
                .. attribute:: source_address  (key)
                
                	Source address of the flow
                	**type**\: str
                
                .. attribute:: destination_address  (key)
                
                	Destination address of the flow
                	**type**\: str
                
                .. attribute:: interface_input  (key)
                
                	Input interface of the flow
                	**type**\: str
                
                .. attribute:: is_multicast  (key)
                
                	Multicast flow
                	**type**\: str
                
                .. attribute:: vrf_id_input  (key)
                
                	VRF ID input
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: source_port  (key)
                
                	Source port number
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: destination_port  (key)
                
                	Destination port number
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: ip_tos  (key)
                
                	ip\-tos value
                	**type**\: str
                
                .. attribute:: ip_protocol  (key)
                
                	IP protocol number
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: interface_output
                
                	Output interface of the flow
                	**type**\: str
                
                .. attribute:: bytes
                
                	Number of bytes passed through
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                .. attribute:: packets
                
                	Number of packets passed through
                	**type**\: int
                
                	**range:** \-9223372036854775808..9223372036854775807
                
                

                """

                _prefix = 'flow-monitor-ios-xe-oper'
                _revision = '2017-11-30'

                def __init__(self):
                    super(FlowMonitors.FlowMonitor.Flows.Flow, self).__init__()

                    self.yang_name = "flow"
                    self.yang_parent_name = "flows"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['source_address','destination_address','interface_input','is_multicast','vrf_id_input','source_port','destination_port','ip_tos','ip_protocol']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('source_address', YLeaf(YType.str, 'source-address')),
                        ('destination_address', YLeaf(YType.str, 'destination-address')),
                        ('interface_input', YLeaf(YType.str, 'interface-input')),
                        ('is_multicast', YLeaf(YType.str, 'is-multicast')),
                        ('vrf_id_input', YLeaf(YType.int64, 'vrf-id-input')),
                        ('source_port', YLeaf(YType.int64, 'source-port')),
                        ('destination_port', YLeaf(YType.int64, 'destination-port')),
                        ('ip_tos', YLeaf(YType.str, 'ip-tos')),
                        ('ip_protocol', YLeaf(YType.int64, 'ip-protocol')),
                        ('interface_output', YLeaf(YType.str, 'interface-output')),
                        ('bytes', YLeaf(YType.int64, 'bytes')),
                        ('packets', YLeaf(YType.int64, 'packets')),
                    ])
                    self.source_address = None
                    self.destination_address = None
                    self.interface_input = None
                    self.is_multicast = None
                    self.vrf_id_input = None
                    self.source_port = None
                    self.destination_port = None
                    self.ip_tos = None
                    self.ip_protocol = None
                    self.interface_output = None
                    self.bytes = None
                    self.packets = None
                    self._segment_path = lambda: "flow" + "[source-address='" + str(self.source_address) + "']" + "[destination-address='" + str(self.destination_address) + "']" + "[interface-input='" + str(self.interface_input) + "']" + "[is-multicast='" + str(self.is_multicast) + "']" + "[vrf-id-input='" + str(self.vrf_id_input) + "']" + "[source-port='" + str(self.source_port) + "']" + "[destination-port='" + str(self.destination_port) + "']" + "[ip-tos='" + str(self.ip_tos) + "']" + "[ip-protocol='" + str(self.ip_protocol) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowMonitors.FlowMonitor.Flows.Flow, ['source_address', 'destination_address', 'interface_input', 'is_multicast', 'vrf_id_input', 'source_port', 'destination_port', 'ip_tos', 'ip_protocol', 'interface_output', 'bytes', 'packets'], name, value)


    class FlowExportStatistics(Entity):
        """
        List of statistics per exporter
        
        .. attribute:: name  (key)
        
        	The name of the flow exporter
        	**type**\: str
        
        .. attribute:: transport_stats
        
        	The coontainer for the transport statistics
        	**type**\:  :py:class:`TransportStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowExportStatistics.TransportStats>`
        
        .. attribute:: export_client
        
        	The container for the export client information
        	**type**\: list of  		 :py:class:`ExportClient <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowExportStatistics.ExportClient>`
        
        

        """

        _prefix = 'flow-monitor-ios-xe-oper'
        _revision = '2017-11-30'

        def __init__(self):
            super(FlowMonitors.FlowExportStatistics, self).__init__()

            self.yang_name = "flow-export-statistics"
            self.yang_parent_name = "flow-monitors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([("transport-stats", ("transport_stats", FlowMonitors.FlowExportStatistics.TransportStats))])
            self._child_list_classes = OrderedDict([("export-client", ("export_client", FlowMonitors.FlowExportStatistics.ExportClient))])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
            ])
            self.name = None

            self.transport_stats = FlowMonitors.FlowExportStatistics.TransportStats()
            self.transport_stats.parent = self
            self._children_name_map["transport_stats"] = "transport-stats"
            self._children_yang_names.add("transport-stats")

            self.export_client = YList(self)
            self._segment_path = lambda: "flow-export-statistics" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FlowMonitors.FlowExportStatistics, ['name'], name, value)


        class TransportStats(Entity):
            """
            The coontainer for the transport statistics
            
            .. attribute:: last_cleared
            
            	Time when the statistics were last cleared
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: flow_exporter_stats
            
            	Container of the exporter statistics
            	**type**\: list of  		 :py:class:`FlowExporterStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowExportStatistics.TransportStats.FlowExporterStats>`
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-11-30'

            def __init__(self):
                super(FlowMonitors.FlowExportStatistics.TransportStats, self).__init__()

                self.yang_name = "transport-stats"
                self.yang_parent_name = "flow-export-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("flow-exporter-stats", ("flow_exporter_stats", FlowMonitors.FlowExportStatistics.TransportStats.FlowExporterStats))])
                self._leafs = OrderedDict([
                    ('last_cleared', YLeaf(YType.str, 'last-cleared')),
                ])
                self.last_cleared = None

                self.flow_exporter_stats = YList(self)
                self._segment_path = lambda: "transport-stats"

            def __setattr__(self, name, value):
                self._perform_setattr(FlowMonitors.FlowExportStatistics.TransportStats, ['last_cleared'], name, value)


            class FlowExporterStats(Entity):
                """
                Container of the exporter statistics
                
                .. attribute:: type
                
                	The type of the export statistics
                	**type**\:  :py:class:`FlowExporterIpwriteStatsType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowExporterIpwriteStatsType>`
                
                .. attribute:: pkt_counts
                
                	The packet counts that have been exported
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: byte_counts
                
                	The byte counts that have been exported
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'flow-monitor-ios-xe-oper'
                _revision = '2017-11-30'

                def __init__(self):
                    super(FlowMonitors.FlowExportStatistics.TransportStats.FlowExporterStats, self).__init__()

                    self.yang_name = "flow-exporter-stats"
                    self.yang_parent_name = "transport-stats"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('type', YLeaf(YType.enumeration, 'type')),
                        ('pkt_counts', YLeaf(YType.uint64, 'pkt-counts')),
                        ('byte_counts', YLeaf(YType.uint64, 'byte-counts')),
                    ])
                    self.type = None
                    self.pkt_counts = None
                    self.byte_counts = None
                    self._segment_path = lambda: "flow-exporter-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowMonitors.FlowExportStatistics.TransportStats.FlowExporterStats, ['type', 'pkt_counts', 'byte_counts'], name, value)


        class ExportClient(Entity):
            """
            The container for the export client information
            
            .. attribute:: name
            
            	The name of the flow export client
            	**type**\: str
            
            .. attribute:: group
            
            	The group that this exporter client belongs to
            	**type**\: str
            
            .. attribute:: protocol_stats
            
            	The container with the protocol statistics
            	**type**\:  :py:class:`ProtocolStats <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowExportStatistics.ExportClient.ProtocolStats>`
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-11-30'

            def __init__(self):
                super(FlowMonitors.FlowExportStatistics.ExportClient, self).__init__()

                self.yang_name = "export-client"
                self.yang_parent_name = "flow-export-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([("protocol-stats", ("protocol_stats", FlowMonitors.FlowExportStatistics.ExportClient.ProtocolStats))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('group', YLeaf(YType.str, 'group')),
                ])
                self.name = None
                self.group = None

                self.protocol_stats = FlowMonitors.FlowExportStatistics.ExportClient.ProtocolStats()
                self.protocol_stats.parent = self
                self._children_name_map["protocol_stats"] = "protocol-stats"
                self._children_yang_names.add("protocol-stats")
                self._segment_path = lambda: "export-client"

            def __setattr__(self, name, value):
                self._perform_setattr(FlowMonitors.FlowExportStatistics.ExportClient, ['name', 'group'], name, value)


            class ProtocolStats(Entity):
                """
                The container with the protocol statistics
                
                .. attribute:: bytes_added
                
                	Number of byte added to the exporter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_sent
                
                	Bytes sent on this exporter
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: bytes_dropped
                
                	Bytes dropped 
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_added
                
                	Number of records added
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_sent
                
                	Number of records sent
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: records_dropped
                
                	Number of records dropped
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'flow-monitor-ios-xe-oper'
                _revision = '2017-11-30'

                def __init__(self):
                    super(FlowMonitors.FlowExportStatistics.ExportClient.ProtocolStats, self).__init__()

                    self.yang_name = "protocol-stats"
                    self.yang_parent_name = "export-client"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('bytes_added', YLeaf(YType.uint64, 'bytes-added')),
                        ('bytes_sent', YLeaf(YType.uint64, 'bytes-sent')),
                        ('bytes_dropped', YLeaf(YType.uint64, 'bytes-dropped')),
                        ('records_added', YLeaf(YType.uint64, 'records-added')),
                        ('records_sent', YLeaf(YType.uint64, 'records-sent')),
                        ('records_dropped', YLeaf(YType.uint64, 'records-dropped')),
                    ])
                    self.bytes_added = None
                    self.bytes_sent = None
                    self.bytes_dropped = None
                    self.records_added = None
                    self.records_sent = None
                    self.records_dropped = None
                    self._segment_path = lambda: "protocol-stats"

                def __setattr__(self, name, value):
                    self._perform_setattr(FlowMonitors.FlowExportStatistics.ExportClient.ProtocolStats, ['bytes_added', 'bytes_sent', 'bytes_dropped', 'records_added', 'records_sent', 'records_dropped'], name, value)


    class FlowCacheStatistics(Entity):
        """
        List of statistics per flow cache
        
        .. attribute:: name  (key)
        
        	The name of the flow cache
        	**type**\: str
        
        .. attribute:: cache_size
        
        	The size of the cache
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: current_entries
        
        	The current number of entries
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: high_watermark
        
        	The high watermark of flows
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flows_added
        
        	The number of flows added
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: flows_aged
        
        	The number of flows that have been aged
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: active_flows_timed_out
        
        	The number of flows that have been timed out  whilst still active
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: inactive_flows_timed_out
        
        	The number of flows that have been timed out for inactivity
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'flow-monitor-ios-xe-oper'
        _revision = '2017-11-30'

        def __init__(self):
            super(FlowMonitors.FlowCacheStatistics, self).__init__()

            self.yang_name = "flow-cache-statistics"
            self.yang_parent_name = "flow-monitors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['name']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('name', YLeaf(YType.str, 'name')),
                ('cache_size', YLeaf(YType.uint64, 'cache-size')),
                ('current_entries', YLeaf(YType.uint64, 'current-entries')),
                ('high_watermark', YLeaf(YType.uint64, 'high-watermark')),
                ('flows_added', YLeaf(YType.uint64, 'flows-added')),
                ('flows_aged', YLeaf(YType.uint64, 'flows-aged')),
                ('active_flows_timed_out', YLeaf(YType.uint64, 'active-flows-timed-out')),
                ('inactive_flows_timed_out', YLeaf(YType.uint64, 'inactive-flows-timed-out')),
            ])
            self.name = None
            self.cache_size = None
            self.current_entries = None
            self.high_watermark = None
            self.flows_added = None
            self.flows_aged = None
            self.active_flows_timed_out = None
            self.inactive_flows_timed_out = None
            self._segment_path = lambda: "flow-cache-statistics" + "[name='" + str(self.name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FlowMonitors.FlowCacheStatistics, ['name', 'cache_size', 'current_entries', 'high_watermark', 'flows_added', 'flows_aged', 'active_flows_timed_out', 'inactive_flows_timed_out'], name, value)


    class FlowMonitorStatistics(Entity):
        """
        List of statistics per flow monitor
        
        .. attribute:: monitor_name  (key)
        
        	The name of the flow monitor
        	**type**\: str
        
        .. attribute:: description
        
        	The description of the flow monitor
        	**type**\: str
        
        .. attribute:: record_name
        
        	The name of the record
        	**type**\: str
        
        .. attribute:: active_flow_exporter
        
        	The active flow exporters
        	**type**\: list of str
        
        .. attribute:: inactive_flow_exporter
        
        	The inactive flow exporters
        	**type**\: list of str
        
        .. attribute:: invalid_packet_counts
        
        	The number of invalid packet counts
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: cache_data
        
        	The grouping of the cache data
        	**type**\:  :py:class:`CacheData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitors.FlowMonitorStatistics.CacheData>`
        
        .. attribute:: transaction_end_ager_enabled
        
        	Indicate whether the transaction end ager is enabled
        	**type**\: bool
        
        .. attribute:: protocol_dist_configured
        
        	The protocol distribution is configured
        	**type**\: str
        
        .. attribute:: size_dist_configured
        
        	The size distribution is configured
        	**type**\: str
        
        .. attribute:: inactive_timer
        
        	The inactive timer on the normal cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: active_timer
        
        	The active time on the normal cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: update_timeout
        
        	The update timeout of the permanent type
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: synchronized_timeout
        
        	The timeout of the synchronized cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: export_spread_interval
        
        	The export spread interval
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: immediate_timeout
        
        	The timeout for the immediate cache
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'flow-monitor-ios-xe-oper'
        _revision = '2017-11-30'

        def __init__(self):
            super(FlowMonitors.FlowMonitorStatistics, self).__init__()

            self.yang_name = "flow-monitor-statistics"
            self.yang_parent_name = "flow-monitors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['monitor_name']
            self._child_container_classes = OrderedDict([("cache-data", ("cache_data", FlowMonitors.FlowMonitorStatistics.CacheData))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('monitor_name', YLeaf(YType.str, 'monitor-name')),
                ('description', YLeaf(YType.str, 'description')),
                ('record_name', YLeaf(YType.str, 'record-name')),
                ('active_flow_exporter', YLeafList(YType.str, 'active-flow-exporter')),
                ('inactive_flow_exporter', YLeafList(YType.str, 'inactive-flow-exporter')),
                ('invalid_packet_counts', YLeaf(YType.uint64, 'invalid-packet-counts')),
                ('transaction_end_ager_enabled', YLeaf(YType.boolean, 'transaction-end-ager-enabled')),
                ('protocol_dist_configured', YLeaf(YType.str, 'protocol-dist-configured')),
                ('size_dist_configured', YLeaf(YType.str, 'size-dist-configured')),
                ('inactive_timer', YLeaf(YType.uint32, 'inactive-timer')),
                ('active_timer', YLeaf(YType.uint32, 'active-timer')),
                ('update_timeout', YLeaf(YType.uint32, 'update-timeout')),
                ('synchronized_timeout', YLeaf(YType.uint32, 'synchronized-timeout')),
                ('export_spread_interval', YLeaf(YType.uint32, 'export-spread-interval')),
                ('immediate_timeout', YLeaf(YType.uint32, 'immediate-timeout')),
            ])
            self.monitor_name = None
            self.description = None
            self.record_name = None
            self.active_flow_exporter = []
            self.inactive_flow_exporter = []
            self.invalid_packet_counts = None
            self.transaction_end_ager_enabled = None
            self.protocol_dist_configured = None
            self.size_dist_configured = None
            self.inactive_timer = None
            self.active_timer = None
            self.update_timeout = None
            self.synchronized_timeout = None
            self.export_spread_interval = None
            self.immediate_timeout = None

            self.cache_data = FlowMonitors.FlowMonitorStatistics.CacheData()
            self.cache_data.parent = self
            self._children_name_map["cache_data"] = "cache-data"
            self._children_yang_names.add("cache-data")
            self._segment_path = lambda: "flow-monitor-statistics" + "[monitor-name='" + str(self.monitor_name) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-flow-monitor-oper:flow-monitors/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(FlowMonitors.FlowMonitorStatistics, ['monitor_name', 'description', 'record_name', 'active_flow_exporter', 'inactive_flow_exporter', 'invalid_packet_counts', 'transaction_end_ager_enabled', 'protocol_dist_configured', 'size_dist_configured', 'inactive_timer', 'active_timer', 'update_timeout', 'synchronized_timeout', 'export_spread_interval', 'immediate_timeout'], name, value)


        class CacheData(Entity):
            """
            The grouping of the cache data
            
            .. attribute:: state
            
            	The state of the flow cache
            	**type**\:  :py:class:`FlowMonitorCacheState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_flow_monitor_oper.FlowMonitorCacheState>`
            
            .. attribute:: type
            
            	The type of the flow cache
            	**type**\: str
            
            .. attribute:: cache_name
            
            	The name of the cache
            	**type**\: str
            
            .. attribute:: status
            
            	The status of the cache
            	**type**\: str
            
            .. attribute:: num_entries
            
            	The number of entries permissible in the cache
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: num_bytes
            
            	The number of bytes in the cache
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'flow-monitor-ios-xe-oper'
            _revision = '2017-11-30'

            def __init__(self):
                super(FlowMonitors.FlowMonitorStatistics.CacheData, self).__init__()

                self.yang_name = "cache-data"
                self.yang_parent_name = "flow-monitor-statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('state', YLeaf(YType.enumeration, 'state')),
                    ('type', YLeaf(YType.str, 'type')),
                    ('cache_name', YLeaf(YType.str, 'cache-name')),
                    ('status', YLeaf(YType.str, 'status')),
                    ('num_entries', YLeaf(YType.uint64, 'num-entries')),
                    ('num_bytes', YLeaf(YType.uint64, 'num-bytes')),
                ])
                self.state = None
                self.type = None
                self.cache_name = None
                self.status = None
                self.num_entries = None
                self.num_bytes = None
                self._segment_path = lambda: "cache-data"

            def __setattr__(self, name, value):
                self._perform_setattr(FlowMonitors.FlowMonitorStatistics.CacheData, ['state', 'type', 'cache_name', 'status', 'num_entries', 'num_bytes'], name, value)

    def clone_ptr(self):
        self._top_entity = FlowMonitors()
        return self._top_entity

