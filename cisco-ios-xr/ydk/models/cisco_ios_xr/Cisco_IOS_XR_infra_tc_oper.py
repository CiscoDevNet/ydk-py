""" Cisco_IOS_XR_infra_tc_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-tc package operational data.

This module contains definitions
for the following management objects\:
  traffic\-collector\: Global Traffic Collector configuration
    commands

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class TcOperAfName(Enum):
    """
    TcOperAfName

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
    
    .. attribute:: afs
    
    	Address Family specific operational data
    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs>`
    
    .. attribute:: external_interfaces
    
    	External Interface
    	**type**\:   :py:class:`ExternalInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces>`
    
    .. attribute:: summary
    
    	Traffic Collector summary
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary>`
    
    .. attribute:: vrf_table
    
    	VRF specific operational data
    	**type**\:   :py:class:`VrfTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable>`
    
    

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
        self._child_container_classes = {"afs" : ("afs", TrafficCollector.Afs), "external-interfaces" : ("external_interfaces", TrafficCollector.ExternalInterfaces), "summary" : ("summary", TrafficCollector.Summary), "vrf-table" : ("vrf_table", TrafficCollector.VrfTable)}
        self._child_list_classes = {}

        self.afs = TrafficCollector.Afs()
        self.afs.parent = self
        self._children_name_map["afs"] = "afs"
        self._children_yang_names.add("afs")

        self.external_interfaces = TrafficCollector.ExternalInterfaces()
        self.external_interfaces.parent = self
        self._children_name_map["external_interfaces"] = "external-interfaces"
        self._children_yang_names.add("external-interfaces")

        self.summary = TrafficCollector.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.vrf_table = TrafficCollector.VrfTable()
        self.vrf_table.parent = self
        self._children_name_map["vrf_table"] = "vrf-table"
        self._children_yang_names.add("vrf-table")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector"


    class Afs(Entity):
        """
        Address Family specific operational data
        
        .. attribute:: af
        
        	Operational data for given Address Family
        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Afs, self).__init__()

            self.yang_name = "afs"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"af" : ("af", TrafficCollector.Afs.Af)}

            self.af = YList(self)
            self._segment_path = lambda: "afs"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.Afs, [], name, value)


        class Af(Entity):
            """
            Operational data for given Address Family
            
            .. attribute:: af_name  <key>
            
            	Address Family name
            	**type**\:   :py:class:`TcOperAfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfName>`
            
            .. attribute:: counters
            
            	Show Counters
            	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Afs.Af, self).__init__()

                self.yang_name = "af"
                self.yang_parent_name = "afs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"counters" : ("counters", TrafficCollector.Afs.Af.Counters)}
                self._child_list_classes = {}

                self.af_name = YLeaf(YType.enumeration, "af-name")

                self.counters = TrafficCollector.Afs.Af.Counters()
                self.counters.parent = self
                self._children_name_map["counters"] = "counters"
                self._children_yang_names.add("counters")
                self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/afs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Afs.Af, ['af_name'], name, value)


            class Counters(Entity):
                """
                Show Counters
                
                .. attribute:: prefixes
                
                	Prefix Database
                	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes>`
                
                .. attribute:: tunnels
                
                	Tunnels
                	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Afs.Af.Counters, self).__init__()

                    self.yang_name = "counters"
                    self.yang_parent_name = "af"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"prefixes" : ("prefixes", TrafficCollector.Afs.Af.Counters.Prefixes), "tunnels" : ("tunnels", TrafficCollector.Afs.Af.Counters.Tunnels)}
                    self._child_list_classes = {}

                    self.prefixes = TrafficCollector.Afs.Af.Counters.Prefixes()
                    self.prefixes.parent = self
                    self._children_name_map["prefixes"] = "prefixes"
                    self._children_yang_names.add("prefixes")

                    self.tunnels = TrafficCollector.Afs.Af.Counters.Tunnels()
                    self.tunnels.parent = self
                    self._children_name_map["tunnels"] = "tunnels"
                    self._children_yang_names.add("tunnels")
                    self._segment_path = lambda: "counters"


                class Prefixes(Entity):
                    """
                    Prefix Database
                    
                    .. attribute:: prefix
                    
                    	Show Prefix Counter
                    	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.Afs.Af.Counters.Prefixes, self).__init__()

                        self.yang_name = "prefixes"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"prefix" : ("prefix", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix)}

                        self.prefix = YList(self)
                        self._segment_path = lambda: "prefixes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes, [], name, value)


                    class Prefix(Entity):
                        """
                        Show Prefix Counter
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                        
                        .. attribute:: ipaddr
                        
                        	IP Address
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: is_active
                        
                        	Prefix is Active and collecting new Statistics
                        	**type**\:  bool
                        
                        .. attribute:: label
                        
                        	Local Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_xr
                        
                        	Label
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mask
                        
                        	Prefix Mask
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: prefix
                        
                        	Prefix Address (V4 or V6 Format)
                        	**type**\:  str
                        
                        .. attribute:: traffic_matrix_counter_statistics
                        
                        	Traffic Matrix (TM) counter statistics
                        	**type**\:   :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "prefixes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"base-counter-statistics" : ("base_counter_statistics", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics), "traffic-matrix-counter-statistics" : ("traffic_matrix_counter_statistics", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics)}
                            self._child_list_classes = {}

                            self.ipaddr = YLeaf(YType.str, "ipaddr")

                            self.is_active = YLeaf(YType.boolean, "is-active")

                            self.label = YLeaf(YType.uint32, "label")

                            self.label_xr = YLeaf(YType.uint32, "label-xr")

                            self.mask = YLeaf(YType.str, "mask")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                            self._children_yang_names.add("base-counter-statistics")

                            self.traffic_matrix_counter_statistics = TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                            self.traffic_matrix_counter_statistics.parent = self
                            self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                            self._children_yang_names.add("traffic-matrix-counter-statistics")
                            self._segment_path = lambda: "prefix"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix, ['ipaddr', 'is_active', 'label', 'label_xr', 'mask', 'prefix'], name, value)


                        class BaseCounterStatistics(Entity):
                            """
                            Base counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__init__()

                                self.yang_name = "base-counter-statistics"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"count-history" : ("count_history", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory)}

                                self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                self.count_history = YList(self)
                                self._segment_path = lambda: "base-counter-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, ['transmit_bytes_per_second_switched', 'transmit_packets_per_second_switched'], name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "base-counter-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                    self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                    self.is_valid = YLeaf(YType.boolean, "is-valid")

                                    self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                    self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")
                                    self._segment_path = lambda: "count-history"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, ['event_end_timestamp', 'event_start_timestamp', 'is_valid', 'transmit_number_of_bytes_switched', 'transmit_number_of_packets_switched'], name, value)


                        class TrafficMatrixCounterStatistics(Entity):
                            """
                            Traffic Matrix (TM) counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__init__()

                                self.yang_name = "traffic-matrix-counter-statistics"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"count-history" : ("count_history", TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory)}

                                self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                self.count_history = YList(self)
                                self._segment_path = lambda: "traffic-matrix-counter-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, ['transmit_bytes_per_second_switched', 'transmit_packets_per_second_switched'], name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "traffic-matrix-counter-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                    self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                    self.is_valid = YLeaf(YType.boolean, "is-valid")

                                    self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                    self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")
                                    self._segment_path = lambda: "count-history"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, ['event_end_timestamp', 'event_start_timestamp', 'is_valid', 'transmit_number_of_bytes_switched', 'transmit_number_of_packets_switched'], name, value)


                class Tunnels(Entity):
                    """
                    Tunnels
                    
                    .. attribute:: tunnel
                    
                    	Tunnel information
                    	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.Afs.Af.Counters.Tunnels, self).__init__()

                        self.yang_name = "tunnels"
                        self.yang_parent_name = "counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"tunnel" : ("tunnel", TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel)}

                        self.tunnel = YList(self)
                        self._segment_path = lambda: "tunnels"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels, [], name, value)


                    class Tunnel(Entity):
                        """
                        Tunnel information
                        
                        .. attribute:: interface_name  <key>
                        
                        	The Interface Name
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: base_counter_statistics
                        
                        	Base counter statistics
                        	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface name in Display format
                        	**type**\:  str
                        
                        .. attribute:: is_active
                        
                        	Interface is Active and collecting new Statistics
                        	**type**\:  bool
                        
                        .. attribute:: vrfid
                        
                        	Interface VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, self).__init__()

                            self.yang_name = "tunnel"
                            self.yang_parent_name = "tunnels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"base-counter-statistics" : ("base_counter_statistics", TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics)}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                            self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                            self.is_active = YLeaf(YType.boolean, "is-active")

                            self.vrfid = YLeaf(YType.uint32, "vrfid")

                            self.base_counter_statistics = TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                            self.base_counter_statistics.parent = self
                            self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                            self._children_yang_names.add("base-counter-statistics")
                            self._segment_path = lambda: "tunnel" + "[interface-name='" + self.interface_name.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel, ['interface_name', 'interface_handle', 'interface_name_xr', 'is_active', 'vrfid'], name, value)


                        class BaseCounterStatistics(Entity):
                            """
                            Base counter statistics
                            
                            .. attribute:: count_history
                            
                            	Counter History
                            	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                            
                            .. attribute:: transmit_bytes_per_second_switched
                            
                            	Average Rate of Bytes/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte/s
                            
                            .. attribute:: transmit_packets_per_second_switched
                            
                            	Average Rate of Packets/second switched
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: packet/s
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__init__()

                                self.yang_name = "base-counter-statistics"
                                self.yang_parent_name = "tunnel"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"count-history" : ("count_history", TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory)}

                                self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                self.count_history = YList(self)
                                self._segment_path = lambda: "base-counter-statistics"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, ['transmit_bytes_per_second_switched', 'transmit_packets_per_second_switched'], name, value)


                            class CountHistory(Entity):
                                """
                                Counter History
                                
                                .. attribute:: event_end_timestamp
                                
                                	Event End timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: event_start_timestamp
                                
                                	Event Start timestamp
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: is_valid
                                
                                	Flag to indicate if this history entry is valid
                                	**type**\:  bool
                                
                                .. attribute:: transmit_number_of_bytes_switched
                                
                                	Number of Bytes switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                .. attribute:: transmit_number_of_packets_switched
                                
                                	Number of packets switched in this interval
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__init__()

                                    self.yang_name = "count-history"
                                    self.yang_parent_name = "base-counter-statistics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                    self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                    self.is_valid = YLeaf(YType.boolean, "is-valid")

                                    self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                    self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")
                                    self._segment_path = lambda: "count-history"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, ['event_end_timestamp', 'event_start_timestamp', 'is_valid', 'transmit_number_of_bytes_switched', 'transmit_number_of_packets_switched'], name, value)


    class ExternalInterfaces(Entity):
        """
        External Interface
        
        .. attribute:: external_interface
        
        	External Interface 
        	**type**\: list of    :py:class:`ExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.ExternalInterfaces.ExternalInterface>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.ExternalInterfaces, self).__init__()

            self.yang_name = "external-interfaces"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"external-interface" : ("external_interface", TrafficCollector.ExternalInterfaces.ExternalInterface)}

            self.external_interface = YList(self)
            self._segment_path = lambda: "external-interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.ExternalInterfaces, [], name, value)


        class ExternalInterface(Entity):
            """
            External Interface 
            
            .. attribute:: interface_name  <key>
            
            	The Interface Name
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            .. attribute:: interface_handle
            
            	Interface handle
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: interface_name_xr
            
            	Interface name in Display format
            	**type**\:  str
            
            .. attribute:: is_interface_enabled
            
            	Flag to indicate interface enabled or not
            	**type**\:  bool
            
            .. attribute:: vrfid
            
            	Interface VRF ID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.ExternalInterfaces.ExternalInterface, self).__init__()

                self.yang_name = "external-interface"
                self.yang_parent_name = "external-interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                self.is_interface_enabled = YLeaf(YType.boolean, "is-interface-enabled")

                self.vrfid = YLeaf(YType.uint32, "vrfid")
                self._segment_path = lambda: "external-interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/external-interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.ExternalInterfaces.ExternalInterface, ['interface_name', 'interface_handle', 'interface_name_xr', 'is_interface_enabled', 'vrfid'], name, value)


    class Summary(Entity):
        """
        Traffic Collector summary
        
        .. attribute:: checkpoint_message_statistic
        
        	Statistics per message type for Chkpt
        	**type**\: list of    :py:class:`CheckpointMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CheckpointMessageStatistic>`
        
        .. attribute:: collection_interval
        
        	Statistic collection interval in minutes
        	**type**\:  int
        
        	**range:** 0..255
        
        	**units**\: minute
        
        .. attribute:: collection_message_statistic
        
        	Statistics per message type for STAT collector
        	**type**\: list of    :py:class:`CollectionMessageStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.CollectionMessageStatistic>`
        
        .. attribute:: collection_timer_is_running
        
        	TRUE if collection timer is running
        	**type**\:  bool
        
        .. attribute:: database_statistics_external_interface
        
        	Database statistics for External Interface
        	**type**\:   :py:class:`DatabaseStatisticsExternalInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.DatabaseStatisticsExternalInterface>`
        
        .. attribute:: history_size
        
        	Statistics history size
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: timeout_interval
        
        	Statistic history timeout interval in hours
        	**type**\:  int
        
        	**range:** 0..65535
        
        	**units**\: hour
        
        .. attribute:: timeout_timer_is_running
        
        	TRUE if history timeout timer is running
        	**type**\:  bool
        
        .. attribute:: vrf_statistic
        
        	VRF table statistics
        	**type**\: list of    :py:class:`VrfStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"database-statistics-external-interface" : ("database_statistics_external_interface", TrafficCollector.Summary.DatabaseStatisticsExternalInterface)}
            self._child_list_classes = {"checkpoint-message-statistic" : ("checkpoint_message_statistic", TrafficCollector.Summary.CheckpointMessageStatistic), "collection-message-statistic" : ("collection_message_statistic", TrafficCollector.Summary.CollectionMessageStatistic), "vrf-statistic" : ("vrf_statistic", TrafficCollector.Summary.VrfStatistic)}

            self.collection_interval = YLeaf(YType.uint8, "collection-interval")

            self.collection_timer_is_running = YLeaf(YType.boolean, "collection-timer-is-running")

            self.history_size = YLeaf(YType.uint8, "history-size")

            self.timeout_interval = YLeaf(YType.uint16, "timeout-interval")

            self.timeout_timer_is_running = YLeaf(YType.boolean, "timeout-timer-is-running")

            self.database_statistics_external_interface = TrafficCollector.Summary.DatabaseStatisticsExternalInterface()
            self.database_statistics_external_interface.parent = self
            self._children_name_map["database_statistics_external_interface"] = "database-statistics-external-interface"
            self._children_yang_names.add("database-statistics-external-interface")

            self.checkpoint_message_statistic = YList(self)
            self.collection_message_statistic = YList(self)
            self.vrf_statistic = YList(self)
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TrafficCollector.Summary, ['collection_interval', 'collection_timer_is_running', 'history_size', 'timeout_interval', 'timeout_timer_is_running'], name, value)


        class CheckpointMessageStatistic(Entity):
            """
            Statistics per message type for Chkpt
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\:  int
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.byte_received = YLeaf(YType.uint64, "byte-received")

                self.byte_sent = YLeaf(YType.uint64, "byte-sent")

                self.maimum_latency_timestamp = YLeaf(YType.uint64, "maimum-latency-timestamp")

                self.maximum_roundtrip_latency = YLeaf(YType.uint32, "maximum-roundtrip-latency")

                self.packet_received = YLeaf(YType.uint64, "packet-received")

                self.packet_sent = YLeaf(YType.uint64, "packet-sent")
                self._segment_path = lambda: "checkpoint-message-statistic"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.CheckpointMessageStatistic, ['byte_received', 'byte_sent', 'maimum_latency_timestamp', 'maximum_roundtrip_latency', 'packet_received', 'packet_sent'], name, value)


        class CollectionMessageStatistic(Entity):
            """
            Statistics per message type for STAT collector
            
            .. attribute:: byte_received
            
            	Number of bytes received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: byte_sent
            
            	Number of bytes sent
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: byte
            
            .. attribute:: maimum_latency_timestamp
            
            	Timestamp of maximum latency
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: maximum_roundtrip_latency
            
            	Maximum roundtrip latency in msec
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: packet_received
            
            	Number of packets received
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: packet_sent
            
            	Number of packets sent
            	**type**\:  int
            
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
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.byte_received = YLeaf(YType.uint64, "byte-received")

                self.byte_sent = YLeaf(YType.uint64, "byte-sent")

                self.maimum_latency_timestamp = YLeaf(YType.uint64, "maimum-latency-timestamp")

                self.maximum_roundtrip_latency = YLeaf(YType.uint32, "maximum-roundtrip-latency")

                self.packet_received = YLeaf(YType.uint64, "packet-received")

                self.packet_sent = YLeaf(YType.uint64, "packet-sent")
                self._segment_path = lambda: "collection-message-statistic"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.CollectionMessageStatistic, ['byte_received', 'byte_sent', 'maimum_latency_timestamp', 'maximum_roundtrip_latency', 'packet_received', 'packet_sent'], name, value)


        class DatabaseStatisticsExternalInterface(Entity):
            """
            Database statistics for External Interface
            
            .. attribute:: number_of_add_o_perations
            
            	Number of add operations
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_delete_o_perations
            
            	Number of delete operations
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: number_of_entries
            
            	Number of DB entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: number_of_stale_entries
            
            	Number of stale  entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, self).__init__()

                self.yang_name = "database-statistics-external-interface"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.number_of_add_o_perations = YLeaf(YType.uint64, "number-of-add-o-perations")

                self.number_of_delete_o_perations = YLeaf(YType.uint64, "number-of-delete-o-perations")

                self.number_of_entries = YLeaf(YType.uint32, "number-of-entries")

                self.number_of_stale_entries = YLeaf(YType.uint32, "number-of-stale-entries")
                self._segment_path = lambda: "database-statistics-external-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.DatabaseStatisticsExternalInterface, ['number_of_add_o_perations', 'number_of_delete_o_perations', 'number_of_entries', 'number_of_stale_entries'], name, value)


        class VrfStatistic(Entity):
            """
            VRF table statistics
            
            .. attribute:: database_statistics_ipv4
            
            	Database statistics for IPv4 table
            	**type**\:   :py:class:`DatabaseStatisticsIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4>`
            
            .. attribute:: database_statistics_tunnel
            
            	Database statistics for Tunnel table
            	**type**\:   :py:class:`DatabaseStatisticsTunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.Summary.VrfStatistic, self).__init__()

                self.yang_name = "vrf-statistic"
                self.yang_parent_name = "summary"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"database-statistics-ipv4" : ("database_statistics_ipv4", TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4), "database-statistics-tunnel" : ("database_statistics_tunnel", TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.database_statistics_ipv4 = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4()
                self.database_statistics_ipv4.parent = self
                self._children_name_map["database_statistics_ipv4"] = "database-statistics-ipv4"
                self._children_yang_names.add("database-statistics-ipv4")

                self.database_statistics_tunnel = TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel()
                self.database_statistics_tunnel.parent = self
                self._children_name_map["database_statistics_tunnel"] = "database-statistics-tunnel"
                self._children_yang_names.add("database-statistics-tunnel")
                self._segment_path = lambda: "vrf-statistic"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TrafficCollector.Summary.VrfStatistic, ['vrf_name'], name, value)


            class DatabaseStatisticsIpv4(Entity):
                """
                Database statistics for IPv4 table
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, self).__init__()

                    self.yang_name = "database-statistics-ipv4"
                    self.yang_parent_name = "vrf-statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.number_of_add_o_perations = YLeaf(YType.uint64, "number-of-add-o-perations")

                    self.number_of_delete_o_perations = YLeaf(YType.uint64, "number-of-delete-o-perations")

                    self.number_of_entries = YLeaf(YType.uint32, "number-of-entries")

                    self.number_of_stale_entries = YLeaf(YType.uint32, "number-of-stale-entries")
                    self._segment_path = lambda: "database-statistics-ipv4"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/vrf-statistic/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsIpv4, ['number_of_add_o_perations', 'number_of_delete_o_perations', 'number_of_entries', 'number_of_stale_entries'], name, value)


            class DatabaseStatisticsTunnel(Entity):
                """
                Database statistics for Tunnel table
                
                .. attribute:: number_of_add_o_perations
                
                	Number of add operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_delete_o_perations
                
                	Number of delete operations
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: number_of_entries
                
                	Number of DB entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: number_of_stale_entries
                
                	Number of stale  entries
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, self).__init__()

                    self.yang_name = "database-statistics-tunnel"
                    self.yang_parent_name = "vrf-statistic"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.number_of_add_o_perations = YLeaf(YType.uint64, "number-of-add-o-perations")

                    self.number_of_delete_o_perations = YLeaf(YType.uint64, "number-of-delete-o-perations")

                    self.number_of_entries = YLeaf(YType.uint32, "number-of-entries")

                    self.number_of_stale_entries = YLeaf(YType.uint32, "number-of-stale-entries")
                    self._segment_path = lambda: "database-statistics-tunnel"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/summary/vrf-statistic/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.Summary.VrfStatistic.DatabaseStatisticsTunnel, ['number_of_add_o_perations', 'number_of_delete_o_perations', 'number_of_entries', 'number_of_stale_entries'], name, value)


    class VrfTable(Entity):
        """
        VRF specific operational data
        
        .. attribute:: default_vrf
        
        	DefaultVRF specific operational data
        	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf>`
        
        

        """

        _prefix = 'infra-tc-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(TrafficCollector.VrfTable, self).__init__()

            self.yang_name = "vrf-table"
            self.yang_parent_name = "traffic-collector"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"default-vrf" : ("default_vrf", TrafficCollector.VrfTable.DefaultVrf)}
            self._child_list_classes = {}

            self.default_vrf = TrafficCollector.VrfTable.DefaultVrf()
            self.default_vrf.parent = self
            self._children_name_map["default_vrf"] = "default-vrf"
            self._children_yang_names.add("default-vrf")
            self._segment_path = lambda: "vrf-table"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/%s" % self._segment_path()


        class DefaultVrf(Entity):
            """
            DefaultVRF specific operational data
            
            .. attribute:: afs
            
            	Address Family specific operational data
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs>`
            
            

            """

            _prefix = 'infra-tc-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(TrafficCollector.VrfTable.DefaultVrf, self).__init__()

                self.yang_name = "default-vrf"
                self.yang_parent_name = "vrf-table"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"afs" : ("afs", TrafficCollector.VrfTable.DefaultVrf.Afs)}
                self._child_list_classes = {}

                self.afs = TrafficCollector.VrfTable.DefaultVrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._children_yang_names.add("afs")
                self._segment_path = lambda: "default-vrf"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/%s" % self._segment_path()


            class Afs(Entity):
                """
                Address Family specific operational data
                
                .. attribute:: af
                
                	Operational data for given Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af>`
                
                

                """

                _prefix = 'infra-tc-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(TrafficCollector.VrfTable.DefaultVrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "default-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"af" : ("af", TrafficCollector.VrfTable.DefaultVrf.Afs.Af)}

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/default-vrf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    Operational data for given Address Family
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`TcOperAfName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TcOperAfName>`
                    
                    .. attribute:: counters
                    
                    	Show Counters
                    	**type**\:   :py:class:`Counters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters>`
                    
                    

                    """

                    _prefix = 'infra-tc-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"counters" : ("counters", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters)}
                        self._child_list_classes = {}

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.counters = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters()
                        self.counters.parent = self
                        self._children_name_map["counters"] = "counters"
                        self._children_yang_names.add("counters")
                        self._segment_path = lambda: "af" + "[af-name='" + self.af_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-infra-tc-oper:traffic-collector/vrf-table/default-vrf/afs/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af, ['af_name'], name, value)


                    class Counters(Entity):
                        """
                        Show Counters
                        
                        .. attribute:: prefixes
                        
                        	Prefix Database
                        	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes>`
                        
                        .. attribute:: tunnels
                        
                        	Tunnels
                        	**type**\:   :py:class:`Tunnels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels>`
                        
                        

                        """

                        _prefix = 'infra-tc-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters, self).__init__()

                            self.yang_name = "counters"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"prefixes" : ("prefixes", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes), "tunnels" : ("tunnels", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels)}
                            self._child_list_classes = {}

                            self.prefixes = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes()
                            self.prefixes.parent = self
                            self._children_name_map["prefixes"] = "prefixes"
                            self._children_yang_names.add("prefixes")

                            self.tunnels = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels()
                            self.tunnels.parent = self
                            self._children_name_map["tunnels"] = "tunnels"
                            self._children_yang_names.add("tunnels")
                            self._segment_path = lambda: "counters"


                        class Prefixes(Entity):
                            """
                            Prefix Database
                            
                            .. attribute:: prefix
                            
                            	Show Prefix Counter
                            	**type**\: list of    :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, self).__init__()

                                self.yang_name = "prefixes"
                                self.yang_parent_name = "counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"prefix" : ("prefix", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix)}

                                self.prefix = YList(self)
                                self._segment_path = lambda: "prefixes"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes, [], name, value)


                            class Prefix(Entity):
                                """
                                Show Prefix Counter
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics>`
                                
                                .. attribute:: ipaddr
                                
                                	IP Address
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: is_active
                                
                                	Prefix is Active and collecting new Statistics
                                	**type**\:  bool
                                
                                .. attribute:: label
                                
                                	Local Label
                                	**type**\:  int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: label_xr
                                
                                	Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mask
                                
                                	Prefix Mask
                                	**type**\:  str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: prefix
                                
                                	Prefix Address (V4 or V6 Format)
                                	**type**\:  str
                                
                                .. attribute:: traffic_matrix_counter_statistics
                                
                                	Traffic Matrix (TM) counter statistics
                                	**type**\:   :py:class:`TrafficMatrixCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics>`
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "prefixes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"base-counter-statistics" : ("base_counter_statistics", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics), "traffic-matrix-counter-statistics" : ("traffic_matrix_counter_statistics", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics)}
                                    self._child_list_classes = {}

                                    self.ipaddr = YLeaf(YType.str, "ipaddr")

                                    self.is_active = YLeaf(YType.boolean, "is-active")

                                    self.label = YLeaf(YType.uint32, "label")

                                    self.label_xr = YLeaf(YType.uint32, "label-xr")

                                    self.mask = YLeaf(YType.str, "mask")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                    self._children_yang_names.add("base-counter-statistics")

                                    self.traffic_matrix_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics()
                                    self.traffic_matrix_counter_statistics.parent = self
                                    self._children_name_map["traffic_matrix_counter_statistics"] = "traffic-matrix-counter-statistics"
                                    self._children_yang_names.add("traffic-matrix-counter-statistics")
                                    self._segment_path = lambda: "prefix"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix, ['ipaddr', 'is_active', 'label', 'label_xr', 'mask', 'prefix'], name, value)


                                class BaseCounterStatistics(Entity):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, self).__init__()

                                        self.yang_name = "base-counter-statistics"
                                        self.yang_parent_name = "prefix"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"count-history" : ("count_history", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory)}

                                        self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                        self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                        self.count_history = YList(self)
                                        self._segment_path = lambda: "base-counter-statistics"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics, ['transmit_bytes_per_second_switched', 'transmit_packets_per_second_switched'], name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "base-counter-statistics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                            self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                            self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")
                                            self._segment_path = lambda: "count-history"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.BaseCounterStatistics.CountHistory, ['event_end_timestamp', 'event_start_timestamp', 'is_valid', 'transmit_number_of_bytes_switched', 'transmit_number_of_packets_switched'], name, value)


                                class TrafficMatrixCounterStatistics(Entity):
                                    """
                                    Traffic Matrix (TM) counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, self).__init__()

                                        self.yang_name = "traffic-matrix-counter-statistics"
                                        self.yang_parent_name = "prefix"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"count-history" : ("count_history", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory)}

                                        self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                        self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                        self.count_history = YList(self)
                                        self._segment_path = lambda: "traffic-matrix-counter-statistics"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics, ['transmit_bytes_per_second_switched', 'transmit_packets_per_second_switched'], name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "traffic-matrix-counter-statistics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                            self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                            self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")
                                            self._segment_path = lambda: "count-history"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Prefixes.Prefix.TrafficMatrixCounterStatistics.CountHistory, ['event_end_timestamp', 'event_start_timestamp', 'is_valid', 'transmit_number_of_bytes_switched', 'transmit_number_of_packets_switched'], name, value)


                        class Tunnels(Entity):
                            """
                            Tunnels
                            
                            .. attribute:: tunnel
                            
                            	Tunnel information
                            	**type**\: list of    :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel>`
                            
                            

                            """

                            _prefix = 'infra-tc-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, self).__init__()

                                self.yang_name = "tunnels"
                                self.yang_parent_name = "counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"tunnel" : ("tunnel", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel)}

                                self.tunnel = YList(self)
                                self._segment_path = lambda: "tunnels"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels, [], name, value)


                            class Tunnel(Entity):
                                """
                                Tunnel information
                                
                                .. attribute:: interface_name  <key>
                                
                                	The Interface Name
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: base_counter_statistics
                                
                                	Base counter statistics
                                	**type**\:   :py:class:`BaseCounterStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics>`
                                
                                .. attribute:: interface_handle
                                
                                	Interface handle
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name_xr
                                
                                	Interface name in Display format
                                	**type**\:  str
                                
                                .. attribute:: is_active
                                
                                	Interface is Active and collecting new Statistics
                                	**type**\:  bool
                                
                                .. attribute:: vrfid
                                
                                	Interface VRF ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'infra-tc-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, self).__init__()

                                    self.yang_name = "tunnel"
                                    self.yang_parent_name = "tunnels"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"base-counter-statistics" : ("base_counter_statistics", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics)}
                                    self._child_list_classes = {}

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.interface_handle = YLeaf(YType.uint32, "interface-handle")

                                    self.interface_name_xr = YLeaf(YType.str, "interface-name-xr")

                                    self.is_active = YLeaf(YType.boolean, "is-active")

                                    self.vrfid = YLeaf(YType.uint32, "vrfid")

                                    self.base_counter_statistics = TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics()
                                    self.base_counter_statistics.parent = self
                                    self._children_name_map["base_counter_statistics"] = "base-counter-statistics"
                                    self._children_yang_names.add("base-counter-statistics")
                                    self._segment_path = lambda: "tunnel" + "[interface-name='" + self.interface_name.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel, ['interface_name', 'interface_handle', 'interface_name_xr', 'is_active', 'vrfid'], name, value)


                                class BaseCounterStatistics(Entity):
                                    """
                                    Base counter statistics
                                    
                                    .. attribute:: count_history
                                    
                                    	Counter History
                                    	**type**\: list of    :py:class:`CountHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_tc_oper.TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory>`
                                    
                                    .. attribute:: transmit_bytes_per_second_switched
                                    
                                    	Average Rate of Bytes/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: byte/s
                                    
                                    .. attribute:: transmit_packets_per_second_switched
                                    
                                    	Average Rate of Packets/second switched
                                    	**type**\:  int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    	**units**\: packet/s
                                    
                                    

                                    """

                                    _prefix = 'infra-tc-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, self).__init__()

                                        self.yang_name = "base-counter-statistics"
                                        self.yang_parent_name = "tunnel"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"count-history" : ("count_history", TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory)}

                                        self.transmit_bytes_per_second_switched = YLeaf(YType.uint64, "transmit-bytes-per-second-switched")

                                        self.transmit_packets_per_second_switched = YLeaf(YType.uint64, "transmit-packets-per-second-switched")

                                        self.count_history = YList(self)
                                        self._segment_path = lambda: "base-counter-statistics"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics, ['transmit_bytes_per_second_switched', 'transmit_packets_per_second_switched'], name, value)


                                    class CountHistory(Entity):
                                        """
                                        Counter History
                                        
                                        .. attribute:: event_end_timestamp
                                        
                                        	Event End timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: event_start_timestamp
                                        
                                        	Event Start timestamp
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: is_valid
                                        
                                        	Flag to indicate if this history entry is valid
                                        	**type**\:  bool
                                        
                                        .. attribute:: transmit_number_of_bytes_switched
                                        
                                        	Number of Bytes switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        	**units**\: byte
                                        
                                        .. attribute:: transmit_number_of_packets_switched
                                        
                                        	Number of packets switched in this interval
                                        	**type**\:  int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'infra-tc-oper'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, self).__init__()

                                            self.yang_name = "count-history"
                                            self.yang_parent_name = "base-counter-statistics"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.event_end_timestamp = YLeaf(YType.uint64, "event-end-timestamp")

                                            self.event_start_timestamp = YLeaf(YType.uint64, "event-start-timestamp")

                                            self.is_valid = YLeaf(YType.boolean, "is-valid")

                                            self.transmit_number_of_bytes_switched = YLeaf(YType.uint64, "transmit-number-of-bytes-switched")

                                            self.transmit_number_of_packets_switched = YLeaf(YType.uint64, "transmit-number-of-packets-switched")
                                            self._segment_path = lambda: "count-history"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TrafficCollector.VrfTable.DefaultVrf.Afs.Af.Counters.Tunnels.Tunnel.BaseCounterStatistics.CountHistory, ['event_end_timestamp', 'event_start_timestamp', 'is_valid', 'transmit_number_of_bytes_switched', 'transmit_number_of_packets_switched'], name, value)

    def clone_ptr(self):
        self._top_entity = TrafficCollector()
        return self._top_entity

