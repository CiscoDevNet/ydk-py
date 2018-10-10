""" Cisco_IOS_XR_infra_tc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package operational data.

This module contains definitions
for the following management objects\:
  traffic\-collector\: Global Traffic Collector configuration
    commands

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class TcOperAfName(Enum):
    """
    TcOperAfName (Enum Class)

    Tc oper af name

    .. data:: ipv4 = 0

    	IPv4

    .. data:: ipv6 = 1

    	IPv6

    """

    ipv4 = Enum.YLeaf(0, "ipv4")

    ipv6 = Enum.YLeaf(1, "ipv6")



class TrafficCollector(Entity):
    """
    Global Traffic Collector configuration commands
    
    .. attribute:: external_interfaces
    
    	External Interface
    	**type**\:  :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: summary
    
    	Traffic Collector summary
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary>`
    
    .. attribute:: vrf_table
    
    	VRF specific operational data
    	**type**\:  :py:class:`VrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable>`
    
    .. attribute:: afs
    
    	Address Family specific operational data
    	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs>`
    
    

    """

    _prefix = 'infra-tc-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(TrafficCollector, self).__init__()
        self._top_entity = None

        self.yang_name = "traffic-collector"
        self.yang_parent_name = "Cisco-IOS-XR-infra-tc-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("external-interfaces", ("external_interfaces", TrafficCollector.ExternalInterfaces)), ("summary", ("summary", TrafficCollector.Summary)), ("vrf-table", ("vrf_table", TrafficCollector.VrfTable)), ("afs", ("afs", TrafficCollector.Afs))])
        self._leafs = OrderedDict()

        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self._children_name_map["external_interfaces"] = "external-interfaces"

        self.summary = TrafficCollector.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.vrf_table = TrafficCollector.VrfTable()
        self.vrf_table.parent = self
        self._children_name_map["vrf_table"] = "vrf-table"

        self.afs = TrafficCollector.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(TrafficCollector, [], name, value)


    class ExternalInterfaces(Entity):
        """
        External Interface
        
        .. attribute:: external_interface
        
        	External Interface 
        	**type**\: list of  		 :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.ExternalInterfaces, self).__init__()

            self.yang_name = "external-interfaces"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("external-interface", ("external_interface", TrafficCollector.ExternalInterfaces.ExternalInterface))])
            self._leafs = OrderedDict()

            self.external_interface = YList(self)
            self._segment_path = lambda: "external-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.ExternalInterfaces, [], name, value)


        class ExternalInterface(Entity):
            """
            External Interface 
            
            .. attribute:: interface_name  (key)
            
            	The Interface Name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: interface_name_xr
            
            	Interface name in Display format
            	**type**\: str
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: vrfid
            
            	Interface VRF ID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: is_interface_enabled
            
            	Flag to indicate interface enabled or not
            	**type**\: bool
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__init__()

                self.yang_name = "external-interface"
                self.yang_parent_name = "external-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                    ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                    ('vrfid', (YLeaf(YType.uint32, 'vrfid'), ['int'])),
                    ('is_interface_enabled', (YLeaf(YType.boolean, 'is-interface-enabled'), ['bool'])),
                ])
                self.interface_name = None
                self.interface_name_xr = None
                self.interface_handle = None
                self.vrfid = None
                self.is_interface_enabled = None
                self._segment_path = lambda: "external-interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/external-interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.ExternalInterfaces.ExternalInterface, ['interface_name', 'interface_name_xr', 'interface_handle', 'vrfid', 'is_interface_enabled'], name, value)


    class Summary(Entity):
        """
        Traffic Collector summary
        
        .. attribute:: database_statistics_external_interface
        
        	Database statistics for External Interface
        	**type**\:  :py:class:`DatabaseStatisticsExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.DatabaseStatisticsExternalInterface>`
        
        .. attribute:: collection_interval
        
        	Statistic collection interval in minutes
        	**type**\: int
        
        	**range:** 0..255
        
        	**units**\: minute
        
        .. attribute:: collection_timer_is_running
        
        	TRUE if collection timer is running
        	**type**\: bool
        
        .. attribute:: timeout_interval
        
        	Statistic history timeout interval in hours
        	**type**\: int
        
        	**range:** 0..65535
        
        	**units**\: hour
        
        .. attribute:: timeout_timer_is_running
        
        	TRUE if history timeout timer is running
        	**type**\: bool
        
        .. attribute:: history_size
        
        	Statistics history size
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: vrf_statistic
        
        	VRF table statistics
        	**type**\: list of  		 :py:class:`VrfStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic>`
        
        .. attribute:: collection_message_statistic
        
        	Statistics per message type for STAT collector
        	**type**\: list of  		 :py:class:`CollectionMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CollectionMessageStatistic>`
        
        .. attribute:: checkpoint_message_statistic
        
        	Statistics per message type for Chkpt
        	**type**\: list of  		 :py:class:`CheckpointMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CheckpointMessageStatistic>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("database-statistics-external-interface", ("database_statistics_external_interface", TrafficCollector.Summary.DatabaseStatisticsExternalInterface)), ("vrf-statistic", ("vrf_statistic", TrafficCollector.Summary.VrfStatistic)), ("collection-message-statistic", ("collection_message_statistic", TrafficCollector.Summary.CollectionMessageStatistic)), ("checkpoint-message-statistic", ("checkpoint_message_statistic", TrafficCollector.Summary.CheckpointMessageStatistic))])
            self._leafs = OrderedDict([
                ('collection_interval', (YLeaf(YType.uint8, 'collection-interval'), ['int'])),
                ('collection_timer_is_running', (YLeaf(YType.boolean, 'collection-timer-is-running'), ['bool'])),
                ('timeout_interval', (YLeaf(YType.uint16, 'timeout-interval'), ['int'])),
                ('timeout_timer_is_running', (YLeaf(YType.boolean, 'timeout-timer-is-running'), ['bool'])),
                ('history_size', (YLeaf(YType.uint8, 'history-size'), ['int'])),
            ])
            self.collection_interval = None
            self.collection_timer_is_running = None
            self.timeout_interval = None
            self.timeout_timer_is_running = None
            self.history_size = None

            self.database_statistics_external_interface = TrafficCollector.Summary.DatabaseStatisticsExternalInterface()
            self.database_statistics_external_interface.parent = self
            self._children_name_map["database_statistics_external_interface"] = "database-statistics-external-interface"

            self.vrf_statistic = YList(self)
            self.collection_message_statistic = YList(self)
            self.checkpoint_message_statistic = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.Summary, ['collection_interval', 'collection_timer_is_running', 'timeout_interval', 'timeout_timer_is_running', 'history_size'], name, value)


        class DatabaseStatisticsExternalInterface(Entity):
            """
            Database statistics for External Interface
            
            .. attribute:: number_of_entries
            
            	Number of DB entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_stale_entries
            
            	Number of stale  entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_add_o_perations
            
            	Number of add operations
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_delete_o_perations
            
            	Number of delete operations
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, self).__init__()

                self.yang_name = "database-statistics-external-interface"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('number_of_entries', (YLeaf(YType.uint32, 'number-of-entries'), ['int'])),
                    ('number_of_stale_entries', (YLeaf(YType.uint32, 'number-of-stale-entries'), ['int'])),
                    ('number_of_add_o_perations', (YLeaf(YType.uint64, 'number-of-add-o-perations'), ['int'])),
                    ('number_of_delete_o_perations', (YLeaf(YType.uint64, 'number-of-delete-o-perations'), ['int'])),
                ])
                self.number_of_entries = None
                self.number_of_stale_entries = None
                self.number_of_add_o_perations = None
                self.number_of_delete_o_perations = None
                self._segment_path = lambda: "database-statistics-external-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, ['number_of_entries', 'number_of_stale_entries', 'number_of_add_o_perations', 'number_of_delete_o_perations'], name, value)


        class VrfStatistic(Entity):
            """
            VRF table statistics
            
            .. attribute:: database_statistics_ipv4
            
            	Database statistics for IPv4 table
            	**type**\:  :py:class:`DatabaseStatisticsIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4>`
            
            .. attribute:: database_statistics_tunnel
            
            	Database statistics for Tunnel table
            	**type**\:  :py:class:`DatabaseStatisticsTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.VrfStatistic, self).__init__()

                self.yang_name = "vrf-statistic"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("database-statistics-ipv4", ("database_statistics_ipv4", TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4)), ("database-statistics-tunnel", ("database_statistics_tunnel", TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.database_statistics_ipv4 = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4()
                self.database_statistics_ipv4.parent = self
                self._children_name_map["database_statistics_ipv4"] = "database-statistics-ipv4"

                self.database_statistics_tunnel = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel()
                self.database_statistics_tunnel.parent = self
                self._children_name_map["database_statistics_tunnel"] = "database-statistics-tunnel"
                self._segment_path = lambda: "vrf-statistic"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.VrfStatistic, ['vrf_name'], name, value)


            class DatabaseStatisticsIpv4(Entity):
                """
                Database statistics for IPv4 table
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, self).__init__()

                    self.yang_name = "database-statistics-ipv4"
                    self.yang_parent_name = "vrf-statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('number_of_entries', (YLeaf(YType.uint32, 'number-of-entries'), ['int'])),
                        ('number_of_stale_entries', (YLeaf(YType.uint32, 'number-of-stale-entries'), ['int'])),
                        ('number_of_add_o_perations', (YLeaf(YType.uint64, 'number-of-add-o-perations'), ['int'])),
                        ('number_of_delete_o_perations', (YLeaf(YType.uint64, 'number-of-delete-o-perations'), ['int'])),
                    ])
                    self.number_of_entries = None
                    self.number_of_stale_entries = None
                    self.number_of_add_o_perations = None
                    self.number_of_delete_o_perations = None
                    self._segment_path = lambda: "database-statistics-ipv4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/vrf-statistic/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, ['number_of_entries', 'number_of_stale_entries', 'number_of_add_o_perations', 'number_of_delete_o_perations'], name, value)


            class DatabaseStatisticsTunnel(Entity):
                """
                Database statistics for Tunnel table
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, self).__init__()

                    self.yang_name = "database-statistics-tunnel"
                    self.yang_parent_name = "vrf-statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('number_of_entries', (YLeaf(YType.uint32, 'number-of-entries'), ['int'])),
                        ('number_of_stale_entries', (YLeaf(YType.uint32, 'number-of-stale-entries'), ['int'])),
                        ('number_of_add_o_perations', (YLeaf(YType.uint64, 'number-of-add-o-perations'), ['int'])),
                        ('number_of_delete_o_perations', (YLeaf(YType.uint64, 'number-of-delete-o-perations'), ['int'])),
                    ])
                    self.number_of_entries = None
                    self.number_of_stale_entries = None
                    self.number_of_add_o_perations = None
                    self.number_of_delete_o_perations = None
                    self._segment_path = lambda: "database-statistics-tunnel"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/vrf-statistic/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, ['number_of_entries', 'number_of_stale_entries', 'number_of_add_o_perations', 'number_of_delete_o_perations'], name, value)


        class CollectionMessageStatistic(Entity):
            """
            Statistics per message type for STAT collector
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.CollectionMessageStatistic, self).__init__()

                self.yang_name = "collection-message-statistic"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packet_sent', (YLeaf(YType.uint64, 'packet-sent'), ['int'])),
                    ('byte_sent', (YLeaf(YType.uint64, 'byte-sent'), ['int'])),
                    ('packet_received', (YLeaf(YType.uint64, 'packet-received'), ['int'])),
                    ('byte_received', (YLeaf(YType.uint64, 'byte-received'), ['int'])),
                    ('maximum_roundtrip_latency', (YLeaf(YType.uint32, 'maximum-roundtrip-latency'), ['int'])),
                    ('maimum_latency_timestamp', (YLeaf(YType.uint64, 'maimum-latency-timestamp'), ['int'])),
                ])
                self.packet_sent = None
                self.byte_sent = None
                self.packet_received = None
                self.byte_received = None
                self.maximum_roundtrip_latency = None
                self.maimum_latency_timestamp = None
                self._segment_path = lambda: "collection-message-statistic"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.CollectionMessageStatistic, ['packet_sent', 'byte_sent', 'packet_received', 'byte_received', 'maximum_roundtrip_latency', 'maimum_latency_timestamp'], name, value)


        class CheckpointMessageStatistic(Entity):
            """
            Statistics per message type for Chkpt
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.CheckpointMessageStatistic, self).__init__()

                self.yang_name = "checkpoint-message-statistic"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('packet_sent', (YLeaf(YType.uint64, 'packet-sent'), ['int'])),
                    ('byte_sent', (YLeaf(YType.uint64, 'byte-sent'), ['int'])),
                    ('packet_received', (YLeaf(YType.uint64, 'packet-received'), ['int'])),
                    ('byte_received', (YLeaf(YType.uint64, 'byte-received'), ['int'])),
                    ('maximum_roundtrip_latency', (YLeaf(YType.uint32, 'maximum-roundtrip-latency'), ['int'])),
                    ('maimum_latency_timestamp', (YLeaf(YType.uint64, 'maimum-latency-timestamp'), ['int'])),
                ])
                self.packet_sent = None
                self.byte_sent = None
                self.packet_received = None
                self.byte_received = None
                self.maximum_roundtrip_latency = None
                self.maimum_latency_timestamp = None
                self._segment_path = lambda: "checkpoint-message-statistic"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.CheckpointMessageStatistic, ['packet_sent', 'byte_sent', 'packet_received', 'byte_received', 'maximum_roundtrip_latency', 'maimum_latency_timestamp'], name, value)


    class VrfTable(Entity):
        """
        VRF specific operational data
        
        .. attribute:: default_vrf
        
        	DefaultVRF specific operational data
        	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.VrfTable, self).__init__()

            self.yang_name = "vrf-table"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("default-vrf", ("default_vrf", TrafficCollector.VrfTable.DefaultVrf))])
            self._leafs = OrderedDict()

            self.default_vrf = TrafficCollector.VrfTable.DefaultVrf()
            self.default_vrf.parent = self
            self._children_name_map["default_vrf"] = "default-vrf"
            self._segment_path = lambda: "vrf-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.VrfTable, [], name, value)


        class DefaultVrf(Entity):
            """
            DefaultVRF specific operational data
            
            .. attribute:: afs
            
            	Address Family specific operational data
            	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.VrfTable.DefaultVrf, self).__init__()

                self.yang_name = "default-vrf"
                self.yang_parent_name = "vrf-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("afs", ("afs", TrafficCollector.VrfTable.DefaultVrf.Afs))])
                self._leafs = OrderedDict()

                self.afs = TrafficCollector.VrfTable.DefaultVrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._segment_path = lambda: "default-vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf, [], name, value)


            class Afs(Entity):
                """
                Address Family specific operational data
                
                .. attribute:: af
                
                	Operational data for given Address Family
                	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.VrfTable.DefaultVrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("af", ("af", TrafficCollector.VrfTable.DefaultVrf.Afs.Af))])
                    self._leafs = OrderedDict()

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/default-vrf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    Operational data for given Address Family
                    
                    .. attribute:: af_name  (key)
                    
                    	Address Family name
                    	**type**\:  :py:class:`TcOperAfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfName>`
                    
                    .. attribute:: counters
                    
                    	Show Counters
                    	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['af_name']
                        self._child_classes = OrderedDict([("counters", ("counters", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters))])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TcOperAfName', '')])),
                        ])
                        self.af_name = None

                        self.counters = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/default-vrf/afs/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, ['af_name'], name, value)


                    class Counters(Entity):
                        """
                        Show Counters
                        
                        .. attribute:: prefixes
                        
                        	Prefix Database
                        	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes>`
                        
                        .. attribute:: tunnels
                        
                        	Tunnels
                        	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("prefixes", ("prefixes", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes)), ("tunnels", ("tunnels", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels))])
                            self._leafs = OrderedDict()

                            self.prefixes = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes()
                            self.prefixes.parent = self
                            self._children_name_map["prefixes"] = "prefixes"

                            self.tunnels = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels()
                            self.tunnels.parent = self
                            self._children_name_map["tunnels"] = "tunnels"
                            self._segment_path = lambda: "counters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters, [], name, value)


                        class Prefixes(Entity):
                            """
                            Prefix Database
                            
                            .. attribute:: prefix
                            
                            	Show Prefix Counter
                            	**type**\: list of  		 :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, self).__init__()

                                self.yang_name = "prefixes"
                                self.yang_parent_name = "counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("prefix", ("prefix", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix))])
                                self._leafs = OrderedDict()

                                self.prefix = YList(self)
                                self._segment_path = lambda: "prefixes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, [], name, value)


                            class Prefix(Entity):
                                """
                                Show Prefix Counter
                                
                                .. attribute:: ipaddr
                                
                                	IP Address
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: mask
                                
                                	Prefix Mask
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: label
                                
                                	Local Label
                                	**type**\: int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:  :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                                
                                .. attribute:: traffic_matrix_counter_statistics
                                
                                	Traffic Matrix (TM) counter statistics
                                	**type**\:  :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                                
                                .. attribute:: prefix
                                
                                	Prefix Address (V4 or V6 Format)
                                	**type**\: str
                                
                                .. attribute:: label_xr
                                
                                	SR Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ldp_label
                                
                                	LDP Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_active
                                
                                	Prefix is Active and collecting new Statistics
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("base-counter-statistics", ("base_counter_statistics", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics)), ("traffic-matrix-counter-statistics", ("traffic_matrix_counter_statistics", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics))])
                                    self._leafs = OrderedDict([
                                        ('ipaddr', (YLeaf(YType.str, 'ipaddr'), ['str'])),
                                        ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                        ('label_xr', (YLeaf(YType.uint32, 'label-xr'), ['int'])),
                                        ('ldp_label', (YLeaf(YType.uint32, 'ldp-label'), ['int'])),
                                        ('is_active', (YLeaf(YType.boolean, 'is-active'), ['bool'])),
                                    ])
                                    self.ipaddr = None
                                    self.mask = None
                                    self.label = None
                                    self.prefix = None
                                    self.label_xr = None
                                    self.ldp_label = None
                                    self.is_active = None

                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"

                                    self.traffic_matrix_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                                    self.traffic_matrix_counter_statistics.parent = self
                                    self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                                    self._segment_path = lambda: "prefix"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, ['ipaddr', 'mask', 'label', 'prefix', 'label_xr', 'ldp_label', 'is_active'], name, value)


                                class BaseCounterStatistics(Entity):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of  		 :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__init__()

                                        self.yang_name = "base-counter-statistics"
                                        self.yang_parent_name = "prefix"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("count-history", ("count_history", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory))])
                                        self._leafs = OrderedDict([
                                            ('transmit_packets_per_second_switched', (YLeaf(YType.uint64, 'transmit-packets-per-second-switched'), ['int'])),
                                            ('transmit_bytes_per_second_switched', (YLeaf(YType.uint64, 'transmit-bytes-per-second-switched'), ['int'])),
                                        ])
                                        self.transmit_packets_per_second_switched = None
                                        self.transmit_bytes_per_second_switched = None

                                        self.count_history = YList(self)
                                        self._segment_path = lambda: "base-counter-statistics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, ['transmit_packets_per_second_switched', 'transmit_bytes_per_second_switched'], name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "base-counter-statistics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('event_start_timestamp', (YLeaf(YType.uint64, 'event-start-timestamp'), ['int'])),
                                                ('event_end_timestamp', (YLeaf(YType.uint64, 'event-end-timestamp'), ['int'])),
                                                ('transmit_number_of_packets_switched', (YLeaf(YType.uint64, 'transmit-number-of-packets-switched'), ['int'])),
                                                ('transmit_number_of_bytes_switched', (YLeaf(YType.uint64, 'transmit-number-of-bytes-switched'), ['int'])),
                                                ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                            ])
                                            self.event_start_timestamp = None
                                            self.event_end_timestamp = None
                                            self.transmit_number_of_packets_switched = None
                                            self.transmit_number_of_bytes_switched = None
                                            self.is_valid = None
                                            self._segment_path = lambda: "count-history"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, ['event_start_timestamp', 'event_end_timestamp', 'transmit_number_of_packets_switched', 'transmit_number_of_bytes_switched', 'is_valid'], name, value)


                                class TrafficMatrixCounterStatistics(Entity):
                                    """
                                    Traffic Matrix (TM) counter statistics
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of  		 :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__init__()

                                        self.yang_name = "traffic-matrix-counter-statistics"
                                        self.yang_parent_name = "prefix"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("count-history", ("count_history", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory))])
                                        self._leafs = OrderedDict([
                                            ('transmit_packets_per_second_switched', (YLeaf(YType.uint64, 'transmit-packets-per-second-switched'), ['int'])),
                                            ('transmit_bytes_per_second_switched', (YLeaf(YType.uint64, 'transmit-bytes-per-second-switched'), ['int'])),
                                        ])
                                        self.transmit_packets_per_second_switched = None
                                        self.transmit_bytes_per_second_switched = None

                                        self.count_history = YList(self)
                                        self._segment_path = lambda: "traffic-matrix-counter-statistics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, ['transmit_packets_per_second_switched', 'transmit_bytes_per_second_switched'], name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "traffic-matrix-counter-statistics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('event_start_timestamp', (YLeaf(YType.uint64, 'event-start-timestamp'), ['int'])),
                                                ('event_end_timestamp', (YLeaf(YType.uint64, 'event-end-timestamp'), ['int'])),
                                                ('transmit_number_of_packets_switched', (YLeaf(YType.uint64, 'transmit-number-of-packets-switched'), ['int'])),
                                                ('transmit_number_of_bytes_switched', (YLeaf(YType.uint64, 'transmit-number-of-bytes-switched'), ['int'])),
                                                ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                            ])
                                            self.event_start_timestamp = None
                                            self.event_end_timestamp = None
                                            self.transmit_number_of_packets_switched = None
                                            self.transmit_number_of_bytes_switched = None
                                            self.is_valid = None
                                            self._segment_path = lambda: "count-history"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, ['event_start_timestamp', 'event_end_timestamp', 'transmit_number_of_packets_switched', 'transmit_number_of_bytes_switched', 'is_valid'], name, value)


                        class Tunnels(Entity):
                            """
                            Tunnels
                            
                            .. attribute:: tunnel
                            
                            	Tunnel information
                            	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, self).__init__()

                                self.yang_name = "tunnels"
                                self.yang_parent_name = "counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("tunnel", ("tunnel", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel))])
                                self._leafs = OrderedDict()

                                self.tunnel = YList(self)
                                self._segment_path = lambda: "tunnels"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, [], name, value)


                            class Tunnel(Entity):
                                """
                                Tunnel information
                                
                                .. attribute:: interface_name  (key)
                                
                                	The Interface Name
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:  :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                                
                                .. attribute:: interface_name_xr
                                
                                	Interface name in Display format
                                	**type**\: str
                                
                                .. attribute:: interface_handle
                                
                                	Interface handle
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: vrfid
                                
                                	Interface VRF ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: is_active
                                
                                	Interface is Active and collecting new Statistics
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, self).__init__()

                                    self.yang_name = "tunnel"
                                    self.yang_parent_name = "tunnels"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("base-counter-statistics", ("base_counter_statistics", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                                        ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                        ('vrfid', (YLeaf(YType.uint32, 'vrfid'), ['int'])),
                                        ('is_active', (YLeaf(YType.boolean, 'is-active'), ['bool'])),
                                    ])
                                    self.interface_name = None
                                    self.interface_name_xr = None
                                    self.interface_handle = None
                                    self.vrfid = None
                                    self.is_active = None

                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                    self._segment_path = lambda: "tunnel" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, ['interface_name', 'interface_name_xr', 'interface_handle', 'vrfid', 'is_active'], name, value)


                                class BaseCounterStatistics(Entity):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of  		 :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__init__()

                                        self.yang_name = "base-counter-statistics"
                                        self.yang_parent_name = "tunnel"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("count-history", ("count_history", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory))])
                                        self._leafs = OrderedDict([
                                            ('transmit_packets_per_second_switched', (YLeaf(YType.uint64, 'transmit-packets-per-second-switched'), ['int'])),
                                            ('transmit_bytes_per_second_switched', (YLeaf(YType.uint64, 'transmit-bytes-per-second-switched'), ['int'])),
                                        ])
                                        self.transmit_packets_per_second_switched = None
                                        self.transmit_bytes_per_second_switched = None

                                        self.count_history = YList(self)
                                        self._segment_path = lambda: "base-counter-statistics"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, ['transmit_packets_per_second_switched', 'transmit_bytes_per_second_switched'], name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\: bool
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "base-counter-statistics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('event_start_timestamp', (YLeaf(YType.uint64, 'event-start-timestamp'), ['int'])),
                                                ('event_end_timestamp', (YLeaf(YType.uint64, 'event-end-timestamp'), ['int'])),
                                                ('transmit_number_of_packets_switched', (YLeaf(YType.uint64, 'transmit-number-of-packets-switched'), ['int'])),
                                                ('transmit_number_of_bytes_switched', (YLeaf(YType.uint64, 'transmit-number-of-bytes-switched'), ['int'])),
                                                ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                            ])
                                            self.event_start_timestamp = None
                                            self.event_end_timestamp = None
                                            self.transmit_number_of_packets_switched = None
                                            self.transmit_number_of_bytes_switched = None
                                            self.is_valid = None
                                            self._segment_path = lambda: "count-history"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, ['event_start_timestamp', 'event_end_timestamp', 'transmit_number_of_packets_switched', 'transmit_number_of_bytes_switched', 'is_valid'], name, value)


    class Afs(Entity):
        """
        Address Family specific operational data
        
        .. attribute:: af
        
        	Operational data for given Address Family
        	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("af", ("af", TrafficCollector.Afs.Af))])
            self._leafs = OrderedDict()

            self.af = YList(self)
            self._segment_path = lambda: "afs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.Afs, [], name, value)


        class Af(Entity):
            """
            Operational data for given Address Family
            
            .. attribute:: af_name  (key)
            
            	Address Family name
            	**type**\:  :py:class:`TcOperAfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfName>`
            
            .. attribute:: counters
            
            	Show Counters
            	**type**\:  :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['af_name']
                self._child_classes = OrderedDict([("counters", ("counters", TrafficCollector.Afs.Af.Counters))])
                self._leafs = OrderedDict([
                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper', 'TcOperAfName', '')])),
                ])
                self.af_name = None

                self.counters = TrafficCollector.Afs.Af.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"
                self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/afs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Afs.Af, ['af_name'], name, value)


            class Counters(Entity):
                """
                Show Counters
                
                .. attribute:: prefixes
                
                	Prefix Database
                	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes>`
                
                .. attribute:: tunnels
                
                	Tunnels
                	**type**\:  :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Afs.Af.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "af"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("prefixes", ("prefixes", TrafficCollector.Afs.Af.Counters.Prefixes)), ("tunnels", ("tunnels", TrafficCollector.Afs.Af.Counters.Tunnels))])
                    self._leafs = OrderedDict()

                    self.prefixes = TrafficCollector.Afs.Af.Counters.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"

                    self.tunnels = TrafficCollector.Afs.Af.Counters.Tunnels()
                    self.tunnels.parent = self
                    self._children_name_map["tunnels"] = "tunnels"
                    self._segment_path = lambda: "counters"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.Afs.Af.Counters, [], name, value)


                class Prefixes(Entity):
                    """
                    Prefix Database
                    
                    .. attribute:: prefix
                    
                    	Show Prefix Counter
                    	**type**\: list of  		 :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.Afs.Af.Counters.Prefixes, self).__init__()

                        self.yang_name = "prefixes"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("prefix", ("prefix", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix))])
                        self._leafs = OrderedDict()

                        self.prefix = YList(self)
                        self._segment_path = lambda: "prefixes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes, [], name, value)


                    class Prefix(Entity):
                        """
                        Show Prefix Counter
                        
                        .. attribute:: ipaddr
                        
                        	IP Address
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: mask
                        
                        	Prefix Mask
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: label
                        
                        	Local Label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:  :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                        
                        .. attribute:: traffic_matrix_counter_statistics
                        
                        	Traffic Matrix (TM) counter statistics
                        	**type**\:  :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                        
                        .. attribute:: prefix
                        
                        	Prefix Address (V4 or V6 Format)
                        	**type**\: str
                        
                        .. attribute:: label_xr
                        
                        	SR Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ldp_label
                        
                        	LDP Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_active
                        
                        	Prefix is Active and collecting new Statistics
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "prefixes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("base-counter-statistics", ("base_counter_statistics", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics)), ("traffic-matrix-counter-statistics", ("traffic_matrix_counter_statistics", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics))])
                            self._leafs = OrderedDict([
                                ('ipaddr', (YLeaf(YType.str, 'ipaddr'), ['str'])),
                                ('mask', (YLeaf(YType.str, 'mask'), ['str'])),
                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str'])),
                                ('label_xr', (YLeaf(YType.uint32, 'label-xr'), ['int'])),
                                ('ldp_label', (YLeaf(YType.uint32, 'ldp-label'), ['int'])),
                                ('is_active', (YLeaf(YType.boolean, 'is-active'), ['bool'])),
                            ])
                            self.ipaddr = None
                            self.mask = None
                            self.label = None
                            self.prefix = None
                            self.label_xr = None
                            self.ldp_label = None
                            self.is_active = None

                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"

                            self.traffic_matrix_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                            self.traffic_matrix_counter_statistics.parent = self
                            self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                            self._segment_path = lambda: "prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, ['ipaddr', 'mask', 'label', 'prefix', 'label_xr', 'ldp_label', 'is_active'], name, value)


                        class BaseCounterStatistics(Entity):
                            """
                            Base counter statistics
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of  		 :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__init__()

                                self.yang_name = "base-counter-statistics"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("count-history", ("count_history", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory))])
                                self._leafs = OrderedDict([
                                    ('transmit_packets_per_second_switched', (YLeaf(YType.uint64, 'transmit-packets-per-second-switched'), ['int'])),
                                    ('transmit_bytes_per_second_switched', (YLeaf(YType.uint64, 'transmit-bytes-per-second-switched'), ['int'])),
                                ])
                                self.transmit_packets_per_second_switched = None
                                self.transmit_bytes_per_second_switched = None

                                self.count_history = YList(self)
                                self._segment_path = lambda: "base-counter-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, ['transmit_packets_per_second_switched', 'transmit_bytes_per_second_switched'], name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "base-counter-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('event_start_timestamp', (YLeaf(YType.uint64, 'event-start-timestamp'), ['int'])),
                                        ('event_end_timestamp', (YLeaf(YType.uint64, 'event-end-timestamp'), ['int'])),
                                        ('transmit_number_of_packets_switched', (YLeaf(YType.uint64, 'transmit-number-of-packets-switched'), ['int'])),
                                        ('transmit_number_of_bytes_switched', (YLeaf(YType.uint64, 'transmit-number-of-bytes-switched'), ['int'])),
                                        ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                    ])
                                    self.event_start_timestamp = None
                                    self.event_end_timestamp = None
                                    self.transmit_number_of_packets_switched = None
                                    self.transmit_number_of_bytes_switched = None
                                    self.is_valid = None
                                    self._segment_path = lambda: "count-history"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, ['event_start_timestamp', 'event_end_timestamp', 'transmit_number_of_packets_switched', 'transmit_number_of_bytes_switched', 'is_valid'], name, value)


                        class TrafficMatrixCounterStatistics(Entity):
                            """
                            Traffic Matrix (TM) counter statistics
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of  		 :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__init__()

                                self.yang_name = "traffic-matrix-counter-statistics"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("count-history", ("count_history", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory))])
                                self._leafs = OrderedDict([
                                    ('transmit_packets_per_second_switched', (YLeaf(YType.uint64, 'transmit-packets-per-second-switched'), ['int'])),
                                    ('transmit_bytes_per_second_switched', (YLeaf(YType.uint64, 'transmit-bytes-per-second-switched'), ['int'])),
                                ])
                                self.transmit_packets_per_second_switched = None
                                self.transmit_bytes_per_second_switched = None

                                self.count_history = YList(self)
                                self._segment_path = lambda: "traffic-matrix-counter-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, ['transmit_packets_per_second_switched', 'transmit_bytes_per_second_switched'], name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "traffic-matrix-counter-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('event_start_timestamp', (YLeaf(YType.uint64, 'event-start-timestamp'), ['int'])),
                                        ('event_end_timestamp', (YLeaf(YType.uint64, 'event-end-timestamp'), ['int'])),
                                        ('transmit_number_of_packets_switched', (YLeaf(YType.uint64, 'transmit-number-of-packets-switched'), ['int'])),
                                        ('transmit_number_of_bytes_switched', (YLeaf(YType.uint64, 'transmit-number-of-bytes-switched'), ['int'])),
                                        ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                    ])
                                    self.event_start_timestamp = None
                                    self.event_end_timestamp = None
                                    self.transmit_number_of_packets_switched = None
                                    self.transmit_number_of_bytes_switched = None
                                    self.is_valid = None
                                    self._segment_path = lambda: "count-history"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, ['event_start_timestamp', 'event_end_timestamp', 'transmit_number_of_packets_switched', 'transmit_number_of_bytes_switched', 'is_valid'], name, value)


                class Tunnels(Entity):
                    """
                    Tunnels
                    
                    .. attribute:: tunnel
                    
                    	Tunnel information
                    	**type**\: list of  		 :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.Afs.Af.Counters.Tunnels, self).__init__()

                        self.yang_name = "tunnels"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("tunnel", ("tunnel", TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel))])
                        self._leafs = OrderedDict()

                        self.tunnel = YList(self)
                        self._segment_path = lambda: "tunnels"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels, [], name, value)


                    class Tunnel(Entity):
                        """
                        Tunnel information
                        
                        .. attribute:: interface_name  (key)
                        
                        	The Interface Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:  :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface name in Display format
                        	**type**\: str
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: vrfid
                        
                        	Interface VRF ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_active
                        
                        	Interface is Active and collecting new Statistics
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, self).__init__()

                            self.yang_name = "tunnel"
                            self.yang_parent_name = "tunnels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([("base-counter-statistics", ("base_counter_statistics", TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                                ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ('vrfid', (YLeaf(YType.uint32, 'vrfid'), ['int'])),
                                ('is_active', (YLeaf(YType.boolean, 'is-active'), ['bool'])),
                            ])
                            self.interface_name = None
                            self.interface_name_xr = None
                            self.interface_handle = None
                            self.vrfid = None
                            self.is_active = None

                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                            self._segment_path = lambda: "tunnel" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, ['interface_name', 'interface_name_xr', 'interface_handle', 'vrfid', 'is_active'], name, value)


                        class BaseCounterStatistics(Entity):
                            """
                            Base counter statistics
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of  		 :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__init__()

                                self.yang_name = "base-counter-statistics"
                                self.yang_parent_name = "tunnel"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("count-history", ("count_history", TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory))])
                                self._leafs = OrderedDict([
                                    ('transmit_packets_per_second_switched', (YLeaf(YType.uint64, 'transmit-packets-per-second-switched'), ['int'])),
                                    ('transmit_bytes_per_second_switched', (YLeaf(YType.uint64, 'transmit-bytes-per-second-switched'), ['int'])),
                                ])
                                self.transmit_packets_per_second_switched = None
                                self.transmit_bytes_per_second_switched = None

                                self.count_history = YList(self)
                                self._segment_path = lambda: "base-counter-statistics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, ['transmit_packets_per_second_switched', 'transmit_bytes_per_second_switched'], name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "base-counter-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('event_start_timestamp', (YLeaf(YType.uint64, 'event-start-timestamp'), ['int'])),
                                        ('event_end_timestamp', (YLeaf(YType.uint64, 'event-end-timestamp'), ['int'])),
                                        ('transmit_number_of_packets_switched', (YLeaf(YType.uint64, 'transmit-number-of-packets-switched'), ['int'])),
                                        ('transmit_number_of_bytes_switched', (YLeaf(YType.uint64, 'transmit-number-of-bytes-switched'), ['int'])),
                                        ('is_valid', (YLeaf(YType.boolean, 'is-valid'), ['bool'])),
                                    ])
                                    self.event_start_timestamp = None
                                    self.event_end_timestamp = None
                                    self.transmit_number_of_packets_switched = None
                                    self.transmit_number_of_bytes_switched = None
                                    self.is_valid = None
                                    self._segment_path = lambda: "count-history"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, ['event_start_timestamp', 'event_end_timestamp', 'transmit_number_of_packets_switched', 'transmit_number_of_bytes_switched', 'is_valid'], name, value)

    def clone_ptr(self):
        self._top_entity = TrafficCollector()
        return self._top_entity

