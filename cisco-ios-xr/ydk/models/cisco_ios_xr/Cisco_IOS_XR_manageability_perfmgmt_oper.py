""" Cisco_IOS_XR_manageability_perfmgmt_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-perfmgmt package operational data.

This module contains definitions
for the following management objects\:
  perf\-mgmt\: Performance Management agent operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PerfMgmt(Entity):
    """
    Performance Management agent operational data
    
    .. attribute:: monitor
    
    	Data from monitor (one history period) requests
    	**type**\:   :py:class:`Monitor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor>`
    
    .. attribute:: periodic
    
    	Data from periodic requests
    	**type**\:   :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic>`
    
    

    """

    _prefix = 'manageability-perfmgmt-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(PerfMgmt, self).__init__()
        self._top_entity = None

        self.yang_name = "perf-mgmt"
        self.yang_parent_name = "Cisco-IOS-XR-manageability-perfmgmt-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"monitor" : ("monitor", PerfMgmt.Monitor), "periodic" : ("periodic", PerfMgmt.Periodic)}
        self._child_list_classes = {}

        self.monitor = PerfMgmt.Monitor()
        self.monitor.parent = self
        self._children_name_map["monitor"] = "monitor"
        self._children_yang_names.add("monitor")

        self.periodic = PerfMgmt.Periodic()
        self.periodic.parent = self
        self._children_name_map["periodic"] = "periodic"
        self._children_yang_names.add("periodic")
        self._segment_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt"


    class Monitor(Entity):
        """
        Data from monitor (one history period) requests
        
        .. attribute:: bgp
        
        	Collected BGP data
        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp>`
        
        .. attribute:: interface
        
        	Collected Interface data
        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface>`
        
        .. attribute:: mpls
        
        	Collected MPLS data
        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls>`
        
        .. attribute:: nodes
        
        	Nodes for which data is collected
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes>`
        
        .. attribute:: ospf
        
        	Collected OSPF data
        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf>`
        
        

        """

        _prefix = 'manageability-perfmgmt-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PerfMgmt.Monitor, self).__init__()

            self.yang_name = "monitor"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"bgp" : ("bgp", PerfMgmt.Monitor.Bgp), "interface" : ("interface", PerfMgmt.Monitor.Interface), "mpls" : ("mpls", PerfMgmt.Monitor.Mpls), "nodes" : ("nodes", PerfMgmt.Monitor.Nodes), "ospf" : ("ospf", PerfMgmt.Monitor.Ospf)}
            self._child_list_classes = {}

            self.bgp = PerfMgmt.Monitor.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"
            self._children_yang_names.add("bgp")

            self.interface = PerfMgmt.Monitor.Interface()
            self.interface.parent = self
            self._children_name_map["interface"] = "interface"
            self._children_yang_names.add("interface")

            self.mpls = PerfMgmt.Monitor.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"
            self._children_yang_names.add("mpls")

            self.nodes = PerfMgmt.Monitor.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")

            self.ospf = PerfMgmt.Monitor.Ospf()
            self.ospf.parent = self
            self._children_name_map["ospf"] = "ospf"
            self._children_yang_names.add("ospf")
            self._segment_path = lambda: "monitor"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/%s" % self._segment_path()


        class Bgp(Entity):
            """
            Collected BGP data
            
            .. attribute:: bgp_neighbors
            
            	Neighbors for which statistics are collected
            	**type**\:   :py:class:`BgpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Monitor.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bgp-neighbors" : ("bgp_neighbors", PerfMgmt.Monitor.Bgp.BgpNeighbors)}
                self._child_list_classes = {}

                self.bgp_neighbors = PerfMgmt.Monitor.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self
                self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                self._children_yang_names.add("bgp-neighbors")
                self._segment_path = lambda: "bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()


            class BgpNeighbors(Entity):
                """
                Neighbors for which statistics are collected
                
                .. attribute:: bgp_neighbor
                
                	Samples for particular neighbor
                	**type**\: list of    :py:class:`BgpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Bgp.BgpNeighbors, self).__init__()

                    self.yang_name = "bgp-neighbors"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"bgp-neighbor" : ("bgp_neighbor", PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor)}

                    self.bgp_neighbor = YList(self)
                    self._segment_path = lambda: "bgp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/bgp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors, [], name, value)


                class BgpNeighbor(Entity):
                    """
                    Samples for particular neighbor
                    
                    .. attribute:: ip_address  <key>
                    
                    	BGP Neighbor Identifier
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Sample Table for a BGP neighbor
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor, self).__init__()

                        self.yang_name = "bgp-neighbor"
                        self.yang_parent_name = "bgp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples)}
                        self._child_list_classes = {}

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.samples = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "bgp-neighbor" + "[ip-address='" + self.ip_address.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/bgp/bgp-neighbors/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor, ['ip_address'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for a BGP neighbor
                        
                        .. attribute:: sample
                        
                        	Neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "bgp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Neighbor statistics sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: conn_dropped
                            
                            	Number of times connection was dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: conn_established
                            
                            	Number of times the connection was established
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_received
                            
                            	Number of error notifications received on the connection
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_sent
                            
                            	Number of error notifications sent on the connection
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_messages
                            
                            	Number of messages received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_update_messages
                            
                            	Number of update messages received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_messages
                            
                            	Number of messages sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_update_messages
                            
                            	Number of update messages sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.conn_dropped = YLeaf(YType.uint32, "conn-dropped")

                                self.conn_established = YLeaf(YType.uint32, "conn-established")

                                self.errors_received = YLeaf(YType.uint32, "errors-received")

                                self.errors_sent = YLeaf(YType.uint32, "errors-sent")

                                self.input_messages = YLeaf(YType.uint32, "input-messages")

                                self.input_update_messages = YLeaf(YType.uint32, "input-update-messages")

                                self.output_messages = YLeaf(YType.uint32, "output-messages")

                                self.output_update_messages = YLeaf(YType.uint32, "output-update-messages")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, ['sample_id', 'conn_dropped', 'conn_established', 'errors_received', 'errors_sent', 'input_messages', 'input_update_messages', 'output_messages', 'output_update_messages', 'time_stamp'], name, value)


        class Interface(Entity):
            """
            Collected Interface data
            
            .. attribute:: basic_counter_interfaces
            
            	Interfaces for which Basic Counters are collected
            	**type**\:   :py:class:`BasicCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces>`
            
            .. attribute:: data_rate_interfaces
            
            	Interfaces for which Data Rates are collected
            	**type**\:   :py:class:`DataRateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces>`
            
            .. attribute:: generic_counter_interfaces
            
            	Interfaces for which Generic Counters are collected
            	**type**\:   :py:class:`GenericCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Monitor.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"basic-counter-interfaces" : ("basic_counter_interfaces", PerfMgmt.Monitor.Interface.BasicCounterInterfaces), "data-rate-interfaces" : ("data_rate_interfaces", PerfMgmt.Monitor.Interface.DataRateInterfaces), "generic-counter-interfaces" : ("generic_counter_interfaces", PerfMgmt.Monitor.Interface.GenericCounterInterfaces)}
                self._child_list_classes = {}

                self.basic_counter_interfaces = PerfMgmt.Monitor.Interface.BasicCounterInterfaces()
                self.basic_counter_interfaces.parent = self
                self._children_name_map["basic_counter_interfaces"] = "basic-counter-interfaces"
                self._children_yang_names.add("basic-counter-interfaces")

                self.data_rate_interfaces = PerfMgmt.Monitor.Interface.DataRateInterfaces()
                self.data_rate_interfaces.parent = self
                self._children_name_map["data_rate_interfaces"] = "data-rate-interfaces"
                self._children_yang_names.add("data-rate-interfaces")

                self.generic_counter_interfaces = PerfMgmt.Monitor.Interface.GenericCounterInterfaces()
                self.generic_counter_interfaces.parent = self
                self._children_name_map["generic_counter_interfaces"] = "generic-counter-interfaces"
                self._children_yang_names.add("generic-counter-interfaces")
                self._segment_path = lambda: "interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()


            class BasicCounterInterfaces(Entity):
                """
                Interfaces for which Basic Counters are
                collected
                
                .. attribute:: basic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces, self).__init__()

                    self.yang_name = "basic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"basic-counter-interface" : ("basic_counter_interface", PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface)}

                    self.basic_counter_interface = YList(self)
                    self._segment_path = lambda: "basic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces, [], name, value)


                class BasicCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: samples
                    
                    	Basic Counter samples for an interface
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__init__()

                        self.yang_name = "basic-counter-interface"
                        self.yang_parent_name = "basic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "basic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/basic-counter-interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Basic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Basic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "basic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Basic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_queue_drops
                            
                            	Output queue drops
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds from UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.in_octets = YLeaf(YType.uint64, "in-octets")

                                self.in_packets = YLeaf(YType.uint64, "in-packets")

                                self.input_queue_drops = YLeaf(YType.uint64, "input-queue-drops")

                                self.input_total_drops = YLeaf(YType.uint64, "input-total-drops")

                                self.input_total_errors = YLeaf(YType.uint64, "input-total-errors")

                                self.out_octets = YLeaf(YType.uint64, "out-octets")

                                self.out_packets = YLeaf(YType.uint64, "out-packets")

                                self.output_queue_drops = YLeaf(YType.uint64, "output-queue-drops")

                                self.output_total_drops = YLeaf(YType.uint64, "output-total-drops")

                                self.output_total_errors = YLeaf(YType.uint64, "output-total-errors")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, ['sample_id', 'in_octets', 'in_packets', 'input_queue_drops', 'input_total_drops', 'input_total_errors', 'out_octets', 'out_packets', 'output_queue_drops', 'output_total_drops', 'output_total_errors', 'time_stamp'], name, value)


            class DataRateInterfaces(Entity):
                """
                Interfaces for which Data Rates are collected
                
                .. attribute:: data_rate_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Interface.DataRateInterfaces, self).__init__()

                    self.yang_name = "data-rate-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"data-rate-interface" : ("data_rate_interface", PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface)}

                    self.data_rate_interface = YList(self)
                    self._segment_path = lambda: "data-rate-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces, [], name, value)


                class DataRateInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: samples
                    
                    	Data Rate samples for an interface
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface, self).__init__()

                        self.yang_name = "data-rate-interface"
                        self.yang_parent_name = "data-rate-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "data-rate-interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/data-rate-interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Data Rate samples for an interface
                        
                        .. attribute:: sample
                        
                        	Data Rates sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "data-rate-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Data Rates sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: bandwidth
                            
                            	Bandwidth (in kbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: input_data_rate
                            
                            	Input datarate in 1000's of bps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: input_packet_rate
                            
                            	Input packets per second
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: input_peak_pkts
                            
                            	Peak input packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_peak_rate
                            
                            	Peak input datarate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_data_rate
                            
                            	Output datarate in 1000's of bps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: output_packet_rate
                            
                            	Output packets per second
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: output_peak_pkts
                            
                            	Peak output packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_peak_rate
                            
                            	Peak output datarate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                                self.input_data_rate = YLeaf(YType.uint32, "input-data-rate")

                                self.input_packet_rate = YLeaf(YType.uint32, "input-packet-rate")

                                self.input_peak_pkts = YLeaf(YType.uint32, "input-peak-pkts")

                                self.input_peak_rate = YLeaf(YType.uint32, "input-peak-rate")

                                self.output_data_rate = YLeaf(YType.uint32, "output-data-rate")

                                self.output_packet_rate = YLeaf(YType.uint32, "output-packet-rate")

                                self.output_peak_pkts = YLeaf(YType.uint32, "output-peak-pkts")

                                self.output_peak_rate = YLeaf(YType.uint32, "output-peak-rate")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, ['sample_id', 'bandwidth', 'input_data_rate', 'input_packet_rate', 'input_peak_pkts', 'input_peak_rate', 'output_data_rate', 'output_packet_rate', 'output_peak_pkts', 'output_peak_rate', 'time_stamp'], name, value)


            class GenericCounterInterfaces(Entity):
                """
                Interfaces for which Generic Counters are
                collected
                
                .. attribute:: generic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces, self).__init__()

                    self.yang_name = "generic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"generic-counter-interface" : ("generic_counter_interface", PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface)}

                    self.generic_counter_interface = YList(self)
                    self._segment_path = lambda: "generic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces, [], name, value)


                class GenericCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: samples
                    
                    	Generic Counter samples for an interface
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__init__()

                        self.yang_name = "generic-counter-interface"
                        self.yang_parent_name = "generic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "generic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/generic-counter-interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Generic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "generic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: in_broadcast_pkts
                            
                            	Broadcast packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_multicast_pkts
                            
                            	Multicast packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_ucast_pkts
                            
                            	Unicast packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_crc
                            
                            	Inbound packets discarded with incorrect CRC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_frame
                            
                            	Inbound framing errors
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_overrun
                            
                            	Input overruns
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_unknown_proto
                            
                            	Inbound packets discarded with unknown proto
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_broadcast_pkts
                            
                            	Broadcast packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_multicast_pkts
                            
                            	Multicast packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_ucast_pkts
                            
                            	Unicast packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_underrun
                            
                            	Output underruns
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.in_broadcast_pkts = YLeaf(YType.uint64, "in-broadcast-pkts")

                                self.in_multicast_pkts = YLeaf(YType.uint64, "in-multicast-pkts")

                                self.in_octets = YLeaf(YType.uint64, "in-octets")

                                self.in_packets = YLeaf(YType.uint64, "in-packets")

                                self.in_ucast_pkts = YLeaf(YType.uint64, "in-ucast-pkts")

                                self.input_crc = YLeaf(YType.uint32, "input-crc")

                                self.input_frame = YLeaf(YType.uint32, "input-frame")

                                self.input_overrun = YLeaf(YType.uint32, "input-overrun")

                                self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                                self.input_total_drops = YLeaf(YType.uint32, "input-total-drops")

                                self.input_total_errors = YLeaf(YType.uint32, "input-total-errors")

                                self.input_unknown_proto = YLeaf(YType.uint32, "input-unknown-proto")

                                self.out_broadcast_pkts = YLeaf(YType.uint64, "out-broadcast-pkts")

                                self.out_multicast_pkts = YLeaf(YType.uint64, "out-multicast-pkts")

                                self.out_octets = YLeaf(YType.uint64, "out-octets")

                                self.out_packets = YLeaf(YType.uint64, "out-packets")

                                self.out_ucast_pkts = YLeaf(YType.uint64, "out-ucast-pkts")

                                self.output_total_drops = YLeaf(YType.uint32, "output-total-drops")

                                self.output_total_errors = YLeaf(YType.uint32, "output-total-errors")

                                self.output_underrun = YLeaf(YType.uint32, "output-underrun")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, ['sample_id', 'in_broadcast_pkts', 'in_multicast_pkts', 'in_octets', 'in_packets', 'in_ucast_pkts', 'input_crc', 'input_frame', 'input_overrun', 'input_queue_drops', 'input_total_drops', 'input_total_errors', 'input_unknown_proto', 'out_broadcast_pkts', 'out_multicast_pkts', 'out_octets', 'out_packets', 'out_ucast_pkts', 'output_total_drops', 'output_total_errors', 'output_underrun', 'time_stamp'], name, value)


        class Mpls(Entity):
            """
            Collected MPLS data
            
            .. attribute:: ldp_neighbors
            
            	LDP neighbors for which statistics are collected
            	**type**\:   :py:class:`LdpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Monitor.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ldp-neighbors" : ("ldp_neighbors", PerfMgmt.Monitor.Mpls.LdpNeighbors)}
                self._child_list_classes = {}

                self.ldp_neighbors = PerfMgmt.Monitor.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self
                self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                self._children_yang_names.add("ldp-neighbors")
                self._segment_path = lambda: "mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()


            class LdpNeighbors(Entity):
                """
                LDP neighbors for which statistics are
                collected
                
                .. attribute:: ldp_neighbor
                
                	Samples for a particular LDP neighbor
                	**type**\: list of    :py:class:`LdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Mpls.LdpNeighbors, self).__init__()

                    self.yang_name = "ldp-neighbors"
                    self.yang_parent_name = "mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ldp-neighbor" : ("ldp_neighbor", PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor)}

                    self.ldp_neighbor = YList(self)
                    self._segment_path = lambda: "ldp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/mpls/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors, [], name, value)


                class LdpNeighbor(Entity):
                    """
                    Samples for a particular LDP neighbor
                    
                    .. attribute:: nbr  <key>
                    
                    	Neighbor Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Samples for a particular LDP neighbor
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor, self).__init__()

                        self.yang_name = "ldp-neighbor"
                        self.yang_parent_name = "ldp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples)}
                        self._child_list_classes = {}

                        self.nbr = YLeaf(YType.str, "nbr")

                        self.samples = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "ldp-neighbor" + "[nbr='" + self.nbr.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/mpls/ldp-neighbors/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor, ['nbr'], name, value)


                    class Samples(Entity):
                        """
                        Samples for a particular LDP neighbor
                        
                        .. attribute:: sample
                        
                        	LDP neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ldp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            LDP neighbor statistics sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: address_msgs_rcvd
                            
                            	Address messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_msgs_sent
                            
                            	Address messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_rcvd
                            
                            	Address withdraw messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_sent
                            
                            	Address withdraw messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_rcvd
                            
                            	Tnit messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_sent
                            
                            	Init messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_rcvd
                            
                            	Keepalive messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_sent
                            
                            	Keepalive messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_rcvd
                            
                            	Label mapping messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_sent
                            
                            	Label mapping messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_rcvd
                            
                            	Label release messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_sent
                            
                            	Label release messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_rcvd
                            
                            	Label withdraw messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_sent
                            
                            	Label withdraw messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_rcvd
                            
                            	Notification messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_sent
                            
                            	Notification messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: total_msgs_rcvd
                            
                            	Total messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: total_msgs_sent
                            
                            	Total messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.address_msgs_rcvd = YLeaf(YType.uint16, "address-msgs-rcvd")

                                self.address_msgs_sent = YLeaf(YType.uint16, "address-msgs-sent")

                                self.address_withdraw_msgs_rcvd = YLeaf(YType.uint16, "address-withdraw-msgs-rcvd")

                                self.address_withdraw_msgs_sent = YLeaf(YType.uint16, "address-withdraw-msgs-sent")

                                self.init_msgs_rcvd = YLeaf(YType.uint16, "init-msgs-rcvd")

                                self.init_msgs_sent = YLeaf(YType.uint16, "init-msgs-sent")

                                self.keepalive_msgs_rcvd = YLeaf(YType.uint16, "keepalive-msgs-rcvd")

                                self.keepalive_msgs_sent = YLeaf(YType.uint16, "keepalive-msgs-sent")

                                self.label_mapping_msgs_rcvd = YLeaf(YType.uint16, "label-mapping-msgs-rcvd")

                                self.label_mapping_msgs_sent = YLeaf(YType.uint16, "label-mapping-msgs-sent")

                                self.label_release_msgs_rcvd = YLeaf(YType.uint16, "label-release-msgs-rcvd")

                                self.label_release_msgs_sent = YLeaf(YType.uint16, "label-release-msgs-sent")

                                self.label_withdraw_msgs_rcvd = YLeaf(YType.uint16, "label-withdraw-msgs-rcvd")

                                self.label_withdraw_msgs_sent = YLeaf(YType.uint16, "label-withdraw-msgs-sent")

                                self.notification_msgs_rcvd = YLeaf(YType.uint16, "notification-msgs-rcvd")

                                self.notification_msgs_sent = YLeaf(YType.uint16, "notification-msgs-sent")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                                self.total_msgs_rcvd = YLeaf(YType.uint16, "total-msgs-rcvd")

                                self.total_msgs_sent = YLeaf(YType.uint16, "total-msgs-sent")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, ['sample_id', 'address_msgs_rcvd', 'address_msgs_sent', 'address_withdraw_msgs_rcvd', 'address_withdraw_msgs_sent', 'init_msgs_rcvd', 'init_msgs_sent', 'keepalive_msgs_rcvd', 'keepalive_msgs_sent', 'label_mapping_msgs_rcvd', 'label_mapping_msgs_sent', 'label_release_msgs_rcvd', 'label_release_msgs_sent', 'label_withdraw_msgs_rcvd', 'label_withdraw_msgs_sent', 'notification_msgs_rcvd', 'notification_msgs_sent', 'time_stamp', 'total_msgs_rcvd', 'total_msgs_sent'], name, value)


        class Nodes(Entity):
            """
            Nodes for which data is collected
            
            .. attribute:: node
            
            	Node Instance
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Monitor.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"node" : ("node", PerfMgmt.Monitor.Nodes.Node)}

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Monitor.Nodes, [], name, value)


            class Node(Entity):
                """
                Node Instance
                
                .. attribute:: node_id  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: processes
                
                	Processes data
                	**type**\:   :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes>`
                
                .. attribute:: sample_xr
                
                	Node CPU data
                	**type**\:   :py:class:`SampleXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.SampleXr>`
                
                .. attribute:: samples
                
                	Node Memory data
                	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Samples>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"processes" : ("processes", PerfMgmt.Monitor.Nodes.Node.Processes), "sample-xr" : ("sample_xr", PerfMgmt.Monitor.Nodes.Node.SampleXr), "samples" : ("samples", PerfMgmt.Monitor.Nodes.Node.Samples)}
                    self._child_list_classes = {}

                    self.node_id = YLeaf(YType.str, "node-id")

                    self.processes = PerfMgmt.Monitor.Nodes.Node.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"
                    self._children_yang_names.add("processes")

                    self.sample_xr = PerfMgmt.Monitor.Nodes.Node.SampleXr()
                    self.sample_xr.parent = self
                    self._children_name_map["sample_xr"] = "sample-xr"
                    self._children_yang_names.add("sample-xr")

                    self.samples = PerfMgmt.Monitor.Nodes.Node.Samples()
                    self.samples.parent = self
                    self._children_name_map["samples"] = "samples"
                    self._children_yang_names.add("samples")
                    self._segment_path = lambda: "node" + "[node-id='" + self.node_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Nodes.Node, ['node_id'], name, value)


                class Processes(Entity):
                    """
                    Processes data
                    
                    .. attribute:: process
                    
                    	Process data
                    	**type**\: list of    :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Nodes.Node.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"process" : ("process", PerfMgmt.Monitor.Nodes.Node.Processes.Process)}

                        self.process = YList(self)
                        self._segment_path = lambda: "processes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes, [], name, value)


                    class Process(Entity):
                        """
                        Process data
                        
                        .. attribute:: process_id  <key>
                        
                        	Process ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: samples
                        
                        	Process data
                        	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Nodes.Node.Processes.Process, self).__init__()

                            self.yang_name = "process"
                            self.yang_parent_name = "processes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples)}
                            self._child_list_classes = {}

                            self.process_id = YLeaf(YType.int32, "process-id")

                            self.samples = PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                            self._children_yang_names.add("samples")
                            self._segment_path = lambda: "process" + "[process-id='" + self.process_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes.Process, ['process_id'], name, value)


                        class Samples(Entity):
                            """
                            Process data
                            
                            .. attribute:: sample
                            
                            	Process data sample
                            	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples, self).__init__()

                                self.yang_name = "samples"
                                self.yang_parent_name = "process"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample)}

                                self.sample = YList(self)
                                self._segment_path = lambda: "samples"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples, [], name, value)


                            class Sample(Entity):
                                """
                                Process data sample
                                
                                .. attribute:: sample_id  <key>
                                
                                	Sample ID
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: average_cpu_used
                                
                                	Average %CPU utilization
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: no_threads
                                
                                	Number of threads
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: peak_memory
                                
                                	Max. dynamic memory (KBytes) used since startup time
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kilobyte
                                
                                .. attribute:: time_stamp
                                
                                	Timestamp of sample in seconds drom UCT
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'manageability-perfmgmt-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample, self).__init__()

                                    self.yang_name = "sample"
                                    self.yang_parent_name = "samples"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.sample_id = YLeaf(YType.int32, "sample-id")

                                    self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                                    self.no_threads = YLeaf(YType.uint32, "no-threads")

                                    self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                                    self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                    self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample, ['sample_id', 'average_cpu_used', 'no_threads', 'peak_memory', 'time_stamp'], name, value)


                class SampleXr(Entity):
                    """
                    Node CPU data
                    
                    .. attribute:: sample
                    
                    	Node CPU data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Nodes.Node.SampleXr, self).__init__()

                        self.yang_name = "sample-xr"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample)}

                        self.sample = YList(self)
                        self._segment_path = lambda: "sample-xr"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.SampleXr, [], name, value)


                    class Sample(Entity):
                        """
                        Node CPU data sample
                        
                        .. attribute:: sample_id  <key>
                        
                        	Sample ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: average_cpu_used
                        
                        	Average system %CPU utilization
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_processes
                        
                        	Number of processes in the system
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "sample-xr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                            self.no_processes = YLeaf(YType.uint32, "no-processes")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                            self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample, ['sample_id', 'average_cpu_used', 'no_processes', 'time_stamp'], name, value)


                class Samples(Entity):
                    """
                    Node Memory data
                    
                    .. attribute:: sample
                    
                    	Node Memory data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Samples.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Nodes.Node.Samples, self).__init__()

                        self.yang_name = "samples"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Nodes.Node.Samples.Sample)}

                        self.sample = YList(self)
                        self._segment_path = lambda: "samples"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Samples, [], name, value)


                    class Sample(Entity):
                        """
                        Node Memory data sample
                        
                        .. attribute:: sample_id  <key>
                        
                        	Sample ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: curr_memory
                        
                        	Current application memory (Bytes) in use
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: peak_memory
                        
                        	Max. system memory (MBytes) used since bootup
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: megabyte
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Nodes.Node.Samples.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "samples"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.curr_memory = YLeaf(YType.uint32, "curr-memory")

                            self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                            self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Samples.Sample, ['sample_id', 'curr_memory', 'peak_memory', 'time_stamp'], name, value)


        class Ospf(Entity):
            """
            Collected OSPF data
            
            .. attribute:: ospfv2_protocol_instances
            
            	OSPF v2 instances for which protocol statistics are collected
            	**type**\:   :py:class:`Ospfv2ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances>`
            
            .. attribute:: ospfv3_protocol_instances
            
            	OSPF v3 instances for which protocol statistics are collected
            	**type**\:   :py:class:`Ospfv3ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Monitor.Ospf, self).__init__()

                self.yang_name = "ospf"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ospfv2-protocol-instances" : ("ospfv2_protocol_instances", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances), "ospfv3-protocol-instances" : ("ospfv3_protocol_instances", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances)}
                self._child_list_classes = {}

                self.ospfv2_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"
                self._children_yang_names.add("ospfv2-protocol-instances")

                self.ospfv3_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self
                self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                self._children_yang_names.add("ospfv3-protocol-instances")
                self._segment_path = lambda: "ospf"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()


            class Ospfv2ProtocolInstances(Entity):
                """
                OSPF v2 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv2_protocol_instance
                
                	Protocol samples for a particular OSPF v2 instance
                	**type**\: list of    :py:class:`Ospfv2ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv2-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ospfv2-protocol-instance" : ("ospfv2_protocol_instance", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance)}

                    self.ospfv2_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv2-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances, [], name, value)


                class Ospfv2ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v2
                    instance
                    
                    .. attribute:: instance_name  <key>
                    
                    	OSPF Instance Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v2 instance
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv2-protocol-instance"
                        self.yang_parent_name = "ospfv2-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples)}
                        self._child_list_classes = {}

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "ospfv2-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/ospfv2-protocol-instances/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v2 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv2-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: checksum_errors
                            
                            	Number of packets received with checksum errors
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.checksum_errors = YLeaf(YType.uint32, "checksum-errors")

                                self.input_db_ds = YLeaf(YType.uint32, "input-db-ds")

                                self.input_db_ds_lsa = YLeaf(YType.uint32, "input-db-ds-lsa")

                                self.input_hello_packets = YLeaf(YType.uint32, "input-hello-packets")

                                self.input_ls_requests = YLeaf(YType.uint32, "input-ls-requests")

                                self.input_ls_requests_lsa = YLeaf(YType.uint32, "input-ls-requests-lsa")

                                self.input_lsa_acks = YLeaf(YType.uint32, "input-lsa-acks")

                                self.input_lsa_acks_lsa = YLeaf(YType.uint32, "input-lsa-acks-lsa")

                                self.input_lsa_updates = YLeaf(YType.uint32, "input-lsa-updates")

                                self.input_lsa_updates_lsa = YLeaf(YType.uint32, "input-lsa-updates-lsa")

                                self.input_packets = YLeaf(YType.uint32, "input-packets")

                                self.output_db_ds = YLeaf(YType.uint32, "output-db-ds")

                                self.output_db_ds_lsa = YLeaf(YType.uint32, "output-db-ds-lsa")

                                self.output_hello_packets = YLeaf(YType.uint32, "output-hello-packets")

                                self.output_ls_requests = YLeaf(YType.uint32, "output-ls-requests")

                                self.output_ls_requests_lsa = YLeaf(YType.uint32, "output-ls-requests-lsa")

                                self.output_lsa_acks = YLeaf(YType.uint32, "output-lsa-acks")

                                self.output_lsa_acks_lsa = YLeaf(YType.uint32, "output-lsa-acks-lsa")

                                self.output_lsa_updates = YLeaf(YType.uint32, "output-lsa-updates")

                                self.output_lsa_updates_lsa = YLeaf(YType.uint32, "output-lsa-updates-lsa")

                                self.output_packets = YLeaf(YType.uint32, "output-packets")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, ['sample_id', 'checksum_errors', 'input_db_ds', 'input_db_ds_lsa', 'input_hello_packets', 'input_ls_requests', 'input_ls_requests_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'input_packets', 'output_db_ds', 'output_db_ds_lsa', 'output_hello_packets', 'output_ls_requests', 'output_ls_requests_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'output_packets', 'time_stamp'], name, value)


            class Ospfv3ProtocolInstances(Entity):
                """
                OSPF v3 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv3_protocol_instance
                
                	Protocol samples for a particular OSPF v3 instance
                	**type**\: list of    :py:class:`Ospfv3ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv3-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ospfv3-protocol-instance" : ("ospfv3_protocol_instance", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance)}

                    self.ospfv3_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv3-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances, [], name, value)


                class Ospfv3ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v3
                    instance
                    
                    .. attribute:: instance_name  <key>
                    
                    	OSPF Instance Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v3 instance
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv3-protocol-instance"
                        self.yang_parent_name = "ospfv3-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples)}
                        self._child_list_classes = {}

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "ospfv3-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/ospfv3-protocol-instances/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v3 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv3-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.input_db_ds = YLeaf(YType.uint32, "input-db-ds")

                                self.input_db_ds_lsa = YLeaf(YType.uint32, "input-db-ds-lsa")

                                self.input_hello_packets = YLeaf(YType.uint32, "input-hello-packets")

                                self.input_ls_requests = YLeaf(YType.uint32, "input-ls-requests")

                                self.input_ls_requests_lsa = YLeaf(YType.uint32, "input-ls-requests-lsa")

                                self.input_lsa_acks = YLeaf(YType.uint32, "input-lsa-acks")

                                self.input_lsa_acks_lsa = YLeaf(YType.uint32, "input-lsa-acks-lsa")

                                self.input_lsa_updates = YLeaf(YType.uint32, "input-lsa-updates")

                                self.input_lsa_updates_lsa = YLeaf(YType.uint32, "input-lsa-updates-lsa")

                                self.input_packets = YLeaf(YType.uint32, "input-packets")

                                self.output_db_ds = YLeaf(YType.uint32, "output-db-ds")

                                self.output_db_ds_lsa = YLeaf(YType.uint32, "output-db-ds-lsa")

                                self.output_hello_packets = YLeaf(YType.uint32, "output-hello-packets")

                                self.output_ls_requests = YLeaf(YType.uint32, "output-ls-requests")

                                self.output_ls_requests_lsa = YLeaf(YType.uint32, "output-ls-requests-lsa")

                                self.output_lsa_acks = YLeaf(YType.uint32, "output-lsa-acks")

                                self.output_lsa_acks_lsa = YLeaf(YType.uint32, "output-lsa-acks-lsa")

                                self.output_lsa_updates = YLeaf(YType.uint32, "output-lsa-updates")

                                self.output_lsa_updates_lsa = YLeaf(YType.uint32, "output-lsa-updates-lsa")

                                self.output_packets = YLeaf(YType.uint32, "output-packets")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, ['sample_id', 'input_db_ds', 'input_db_ds_lsa', 'input_hello_packets', 'input_ls_requests', 'input_ls_requests_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'input_packets', 'output_db_ds', 'output_db_ds_lsa', 'output_hello_packets', 'output_ls_requests', 'output_ls_requests_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'output_packets', 'time_stamp'], name, value)


    class Periodic(Entity):
        """
        Data from periodic requests
        
        .. attribute:: bgp
        
        	Collected BGP data
        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp>`
        
        .. attribute:: interface
        
        	Collected Interface data
        	**type**\:   :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface>`
        
        .. attribute:: mpls
        
        	Collected MPLS data
        	**type**\:   :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls>`
        
        .. attribute:: nodes
        
        	Nodes for which data is collected
        	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes>`
        
        .. attribute:: ospf
        
        	Collected OSPF data
        	**type**\:   :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf>`
        
        

        """

        _prefix = 'manageability-perfmgmt-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(PerfMgmt.Periodic, self).__init__()

            self.yang_name = "periodic"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"bgp" : ("bgp", PerfMgmt.Periodic.Bgp), "interface" : ("interface", PerfMgmt.Periodic.Interface), "mpls" : ("mpls", PerfMgmt.Periodic.Mpls), "nodes" : ("nodes", PerfMgmt.Periodic.Nodes), "ospf" : ("ospf", PerfMgmt.Periodic.Ospf)}
            self._child_list_classes = {}

            self.bgp = PerfMgmt.Periodic.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"
            self._children_yang_names.add("bgp")

            self.interface = PerfMgmt.Periodic.Interface()
            self.interface.parent = self
            self._children_name_map["interface"] = "interface"
            self._children_yang_names.add("interface")

            self.mpls = PerfMgmt.Periodic.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"
            self._children_yang_names.add("mpls")

            self.nodes = PerfMgmt.Periodic.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"
            self._children_yang_names.add("nodes")

            self.ospf = PerfMgmt.Periodic.Ospf()
            self.ospf.parent = self
            self._children_name_map["ospf"] = "ospf"
            self._children_yang_names.add("ospf")
            self._segment_path = lambda: "periodic"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/%s" % self._segment_path()


        class Bgp(Entity):
            """
            Collected BGP data
            
            .. attribute:: bgp_neighbors
            
            	Neighbors for which statistics are collected
            	**type**\:   :py:class:`BgpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Periodic.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bgp-neighbors" : ("bgp_neighbors", PerfMgmt.Periodic.Bgp.BgpNeighbors)}
                self._child_list_classes = {}

                self.bgp_neighbors = PerfMgmt.Periodic.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self
                self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                self._children_yang_names.add("bgp-neighbors")
                self._segment_path = lambda: "bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()


            class BgpNeighbors(Entity):
                """
                Neighbors for which statistics are collected
                
                .. attribute:: bgp_neighbor
                
                	Samples for particular neighbor
                	**type**\: list of    :py:class:`BgpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Bgp.BgpNeighbors, self).__init__()

                    self.yang_name = "bgp-neighbors"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"bgp-neighbor" : ("bgp_neighbor", PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor)}

                    self.bgp_neighbor = YList(self)
                    self._segment_path = lambda: "bgp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/bgp/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors, [], name, value)


                class BgpNeighbor(Entity):
                    """
                    Samples for particular neighbor
                    
                    .. attribute:: ip_address  <key>
                    
                    	BGP Neighbor Identifier
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Sample Table for a BGP neighbor
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor, self).__init__()

                        self.yang_name = "bgp-neighbor"
                        self.yang_parent_name = "bgp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples)}
                        self._child_list_classes = {}

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.samples = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "bgp-neighbor" + "[ip-address='" + self.ip_address.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/bgp/bgp-neighbors/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor, ['ip_address'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for a BGP neighbor
                        
                        .. attribute:: sample
                        
                        	Neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "bgp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Neighbor statistics sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: conn_dropped
                            
                            	Number of times connection was dropped
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: conn_established
                            
                            	Number of times the connection was established
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_received
                            
                            	Number of error notifications received on the connection
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_sent
                            
                            	Number of error notifications sent on the connection
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_messages
                            
                            	Number of messages received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_update_messages
                            
                            	Number of update messages received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_messages
                            
                            	Number of messages sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_update_messages
                            
                            	Number of update messages sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.conn_dropped = YLeaf(YType.uint32, "conn-dropped")

                                self.conn_established = YLeaf(YType.uint32, "conn-established")

                                self.errors_received = YLeaf(YType.uint32, "errors-received")

                                self.errors_sent = YLeaf(YType.uint32, "errors-sent")

                                self.input_messages = YLeaf(YType.uint32, "input-messages")

                                self.input_update_messages = YLeaf(YType.uint32, "input-update-messages")

                                self.output_messages = YLeaf(YType.uint32, "output-messages")

                                self.output_update_messages = YLeaf(YType.uint32, "output-update-messages")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, ['sample_id', 'conn_dropped', 'conn_established', 'errors_received', 'errors_sent', 'input_messages', 'input_update_messages', 'output_messages', 'output_update_messages', 'time_stamp'], name, value)


        class Interface(Entity):
            """
            Collected Interface data
            
            .. attribute:: basic_counter_interfaces
            
            	Interfaces for which Basic Counters are collected
            	**type**\:   :py:class:`BasicCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces>`
            
            .. attribute:: data_rate_interfaces
            
            	Interfaces for which Data Rates are collected
            	**type**\:   :py:class:`DataRateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces>`
            
            .. attribute:: generic_counter_interfaces
            
            	Interfaces for which Generic Counters are collected
            	**type**\:   :py:class:`GenericCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Periodic.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"basic-counter-interfaces" : ("basic_counter_interfaces", PerfMgmt.Periodic.Interface.BasicCounterInterfaces), "data-rate-interfaces" : ("data_rate_interfaces", PerfMgmt.Periodic.Interface.DataRateInterfaces), "generic-counter-interfaces" : ("generic_counter_interfaces", PerfMgmt.Periodic.Interface.GenericCounterInterfaces)}
                self._child_list_classes = {}

                self.basic_counter_interfaces = PerfMgmt.Periodic.Interface.BasicCounterInterfaces()
                self.basic_counter_interfaces.parent = self
                self._children_name_map["basic_counter_interfaces"] = "basic-counter-interfaces"
                self._children_yang_names.add("basic-counter-interfaces")

                self.data_rate_interfaces = PerfMgmt.Periodic.Interface.DataRateInterfaces()
                self.data_rate_interfaces.parent = self
                self._children_name_map["data_rate_interfaces"] = "data-rate-interfaces"
                self._children_yang_names.add("data-rate-interfaces")

                self.generic_counter_interfaces = PerfMgmt.Periodic.Interface.GenericCounterInterfaces()
                self.generic_counter_interfaces.parent = self
                self._children_name_map["generic_counter_interfaces"] = "generic-counter-interfaces"
                self._children_yang_names.add("generic-counter-interfaces")
                self._segment_path = lambda: "interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()


            class BasicCounterInterfaces(Entity):
                """
                Interfaces for which Basic Counters are
                collected
                
                .. attribute:: basic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces, self).__init__()

                    self.yang_name = "basic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"basic-counter-interface" : ("basic_counter_interface", PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface)}

                    self.basic_counter_interface = YList(self)
                    self._segment_path = lambda: "basic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces, [], name, value)


                class BasicCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: samples
                    
                    	Basic Counter samples for an interface
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__init__()

                        self.yang_name = "basic-counter-interface"
                        self.yang_parent_name = "basic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "basic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/basic-counter-interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Basic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Basic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "basic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Basic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_queue_drops
                            
                            	Output queue drops
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds from UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.in_octets = YLeaf(YType.uint64, "in-octets")

                                self.in_packets = YLeaf(YType.uint64, "in-packets")

                                self.input_queue_drops = YLeaf(YType.uint64, "input-queue-drops")

                                self.input_total_drops = YLeaf(YType.uint64, "input-total-drops")

                                self.input_total_errors = YLeaf(YType.uint64, "input-total-errors")

                                self.out_octets = YLeaf(YType.uint64, "out-octets")

                                self.out_packets = YLeaf(YType.uint64, "out-packets")

                                self.output_queue_drops = YLeaf(YType.uint64, "output-queue-drops")

                                self.output_total_drops = YLeaf(YType.uint64, "output-total-drops")

                                self.output_total_errors = YLeaf(YType.uint64, "output-total-errors")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, ['sample_id', 'in_octets', 'in_packets', 'input_queue_drops', 'input_total_drops', 'input_total_errors', 'out_octets', 'out_packets', 'output_queue_drops', 'output_total_drops', 'output_total_errors', 'time_stamp'], name, value)


            class DataRateInterfaces(Entity):
                """
                Interfaces for which Data Rates are collected
                
                .. attribute:: data_rate_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Interface.DataRateInterfaces, self).__init__()

                    self.yang_name = "data-rate-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"data-rate-interface" : ("data_rate_interface", PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface)}

                    self.data_rate_interface = YList(self)
                    self._segment_path = lambda: "data-rate-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces, [], name, value)


                class DataRateInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: samples
                    
                    	Data Rate samples for an interface
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface, self).__init__()

                        self.yang_name = "data-rate-interface"
                        self.yang_parent_name = "data-rate-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "data-rate-interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/data-rate-interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Data Rate samples for an interface
                        
                        .. attribute:: sample
                        
                        	Data Rates sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "data-rate-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Data Rates sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: bandwidth
                            
                            	Bandwidth (in kbps)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: input_data_rate
                            
                            	Input datarate in 1000's of bps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: input_packet_rate
                            
                            	Input packets per second
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: input_peak_pkts
                            
                            	Peak input packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_peak_rate
                            
                            	Peak input datarate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_data_rate
                            
                            	Output datarate in 1000's of bps
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: output_packet_rate
                            
                            	Output packets per second
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: output_peak_pkts
                            
                            	Peak output packet rate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_peak_rate
                            
                            	Peak output datarate
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.bandwidth = YLeaf(YType.uint32, "bandwidth")

                                self.input_data_rate = YLeaf(YType.uint32, "input-data-rate")

                                self.input_packet_rate = YLeaf(YType.uint32, "input-packet-rate")

                                self.input_peak_pkts = YLeaf(YType.uint32, "input-peak-pkts")

                                self.input_peak_rate = YLeaf(YType.uint32, "input-peak-rate")

                                self.output_data_rate = YLeaf(YType.uint32, "output-data-rate")

                                self.output_packet_rate = YLeaf(YType.uint32, "output-packet-rate")

                                self.output_peak_pkts = YLeaf(YType.uint32, "output-peak-pkts")

                                self.output_peak_rate = YLeaf(YType.uint32, "output-peak-rate")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, ['sample_id', 'bandwidth', 'input_data_rate', 'input_packet_rate', 'input_peak_pkts', 'input_peak_rate', 'output_data_rate', 'output_packet_rate', 'output_peak_pkts', 'output_peak_rate', 'time_stamp'], name, value)


            class GenericCounterInterfaces(Entity):
                """
                Interfaces for which Generic Counters are
                collected
                
                .. attribute:: generic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces, self).__init__()

                    self.yang_name = "generic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"generic-counter-interface" : ("generic_counter_interface", PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface)}

                    self.generic_counter_interface = YList(self)
                    self._segment_path = lambda: "generic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces, [], name, value)


                class GenericCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: samples
                    
                    	Generic Counter samples for an interface
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__init__()

                        self.yang_name = "generic-counter-interface"
                        self.yang_parent_name = "generic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples)}
                        self._child_list_classes = {}

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "generic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/generic-counter-interfaces/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Generic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "generic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: in_broadcast_pkts
                            
                            	Broadcast packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_multicast_pkts
                            
                            	Multicast packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_ucast_pkts
                            
                            	Unicast packets received
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_crc
                            
                            	Inbound packets discarded with incorrect CRC
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_frame
                            
                            	Inbound framing errors
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_overrun
                            
                            	Input overruns
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_unknown_proto
                            
                            	Inbound packets discarded with unknown proto
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: out_broadcast_pkts
                            
                            	Broadcast packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_multicast_pkts
                            
                            	Multicast packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_ucast_pkts
                            
                            	Unicast packets sent
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_underrun
                            
                            	Output underruns
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.in_broadcast_pkts = YLeaf(YType.uint64, "in-broadcast-pkts")

                                self.in_multicast_pkts = YLeaf(YType.uint64, "in-multicast-pkts")

                                self.in_octets = YLeaf(YType.uint64, "in-octets")

                                self.in_packets = YLeaf(YType.uint64, "in-packets")

                                self.in_ucast_pkts = YLeaf(YType.uint64, "in-ucast-pkts")

                                self.input_crc = YLeaf(YType.uint32, "input-crc")

                                self.input_frame = YLeaf(YType.uint32, "input-frame")

                                self.input_overrun = YLeaf(YType.uint32, "input-overrun")

                                self.input_queue_drops = YLeaf(YType.uint32, "input-queue-drops")

                                self.input_total_drops = YLeaf(YType.uint32, "input-total-drops")

                                self.input_total_errors = YLeaf(YType.uint32, "input-total-errors")

                                self.input_unknown_proto = YLeaf(YType.uint32, "input-unknown-proto")

                                self.out_broadcast_pkts = YLeaf(YType.uint64, "out-broadcast-pkts")

                                self.out_multicast_pkts = YLeaf(YType.uint64, "out-multicast-pkts")

                                self.out_octets = YLeaf(YType.uint64, "out-octets")

                                self.out_packets = YLeaf(YType.uint64, "out-packets")

                                self.out_ucast_pkts = YLeaf(YType.uint64, "out-ucast-pkts")

                                self.output_total_drops = YLeaf(YType.uint32, "output-total-drops")

                                self.output_total_errors = YLeaf(YType.uint32, "output-total-errors")

                                self.output_underrun = YLeaf(YType.uint32, "output-underrun")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, ['sample_id', 'in_broadcast_pkts', 'in_multicast_pkts', 'in_octets', 'in_packets', 'in_ucast_pkts', 'input_crc', 'input_frame', 'input_overrun', 'input_queue_drops', 'input_total_drops', 'input_total_errors', 'input_unknown_proto', 'out_broadcast_pkts', 'out_multicast_pkts', 'out_octets', 'out_packets', 'out_ucast_pkts', 'output_total_drops', 'output_total_errors', 'output_underrun', 'time_stamp'], name, value)


        class Mpls(Entity):
            """
            Collected MPLS data
            
            .. attribute:: ldp_neighbors
            
            	LDP neighbors for which statistics are collected
            	**type**\:   :py:class:`LdpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Periodic.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ldp-neighbors" : ("ldp_neighbors", PerfMgmt.Periodic.Mpls.LdpNeighbors)}
                self._child_list_classes = {}

                self.ldp_neighbors = PerfMgmt.Periodic.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self
                self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                self._children_yang_names.add("ldp-neighbors")
                self._segment_path = lambda: "mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()


            class LdpNeighbors(Entity):
                """
                LDP neighbors for which statistics are
                collected
                
                .. attribute:: ldp_neighbor
                
                	Samples for a particular LDP neighbor
                	**type**\: list of    :py:class:`LdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Mpls.LdpNeighbors, self).__init__()

                    self.yang_name = "ldp-neighbors"
                    self.yang_parent_name = "mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ldp-neighbor" : ("ldp_neighbor", PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor)}

                    self.ldp_neighbor = YList(self)
                    self._segment_path = lambda: "ldp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/mpls/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors, [], name, value)


                class LdpNeighbor(Entity):
                    """
                    Samples for a particular LDP neighbor
                    
                    .. attribute:: nbr  <key>
                    
                    	Neighbor Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Samples for a particular LDP neighbor
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor, self).__init__()

                        self.yang_name = "ldp-neighbor"
                        self.yang_parent_name = "ldp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples)}
                        self._child_list_classes = {}

                        self.nbr = YLeaf(YType.str, "nbr")

                        self.samples = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "ldp-neighbor" + "[nbr='" + self.nbr.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/mpls/ldp-neighbors/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor, ['nbr'], name, value)


                    class Samples(Entity):
                        """
                        Samples for a particular LDP neighbor
                        
                        .. attribute:: sample
                        
                        	LDP neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ldp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            LDP neighbor statistics sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: address_msgs_rcvd
                            
                            	Address messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_msgs_sent
                            
                            	Address messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_rcvd
                            
                            	Address withdraw messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_sent
                            
                            	Address withdraw messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_rcvd
                            
                            	Tnit messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_sent
                            
                            	Init messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_rcvd
                            
                            	Keepalive messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_sent
                            
                            	Keepalive messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_rcvd
                            
                            	Label mapping messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_sent
                            
                            	Label mapping messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_rcvd
                            
                            	Label release messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_sent
                            
                            	Label release messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_rcvd
                            
                            	Label withdraw messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_sent
                            
                            	Label withdraw messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_rcvd
                            
                            	Notification messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_sent
                            
                            	Notification messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: total_msgs_rcvd
                            
                            	Total messages received
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: total_msgs_sent
                            
                            	Total messages sent
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.address_msgs_rcvd = YLeaf(YType.uint16, "address-msgs-rcvd")

                                self.address_msgs_sent = YLeaf(YType.uint16, "address-msgs-sent")

                                self.address_withdraw_msgs_rcvd = YLeaf(YType.uint16, "address-withdraw-msgs-rcvd")

                                self.address_withdraw_msgs_sent = YLeaf(YType.uint16, "address-withdraw-msgs-sent")

                                self.init_msgs_rcvd = YLeaf(YType.uint16, "init-msgs-rcvd")

                                self.init_msgs_sent = YLeaf(YType.uint16, "init-msgs-sent")

                                self.keepalive_msgs_rcvd = YLeaf(YType.uint16, "keepalive-msgs-rcvd")

                                self.keepalive_msgs_sent = YLeaf(YType.uint16, "keepalive-msgs-sent")

                                self.label_mapping_msgs_rcvd = YLeaf(YType.uint16, "label-mapping-msgs-rcvd")

                                self.label_mapping_msgs_sent = YLeaf(YType.uint16, "label-mapping-msgs-sent")

                                self.label_release_msgs_rcvd = YLeaf(YType.uint16, "label-release-msgs-rcvd")

                                self.label_release_msgs_sent = YLeaf(YType.uint16, "label-release-msgs-sent")

                                self.label_withdraw_msgs_rcvd = YLeaf(YType.uint16, "label-withdraw-msgs-rcvd")

                                self.label_withdraw_msgs_sent = YLeaf(YType.uint16, "label-withdraw-msgs-sent")

                                self.notification_msgs_rcvd = YLeaf(YType.uint16, "notification-msgs-rcvd")

                                self.notification_msgs_sent = YLeaf(YType.uint16, "notification-msgs-sent")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                                self.total_msgs_rcvd = YLeaf(YType.uint16, "total-msgs-rcvd")

                                self.total_msgs_sent = YLeaf(YType.uint16, "total-msgs-sent")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, ['sample_id', 'address_msgs_rcvd', 'address_msgs_sent', 'address_withdraw_msgs_rcvd', 'address_withdraw_msgs_sent', 'init_msgs_rcvd', 'init_msgs_sent', 'keepalive_msgs_rcvd', 'keepalive_msgs_sent', 'label_mapping_msgs_rcvd', 'label_mapping_msgs_sent', 'label_release_msgs_rcvd', 'label_release_msgs_sent', 'label_withdraw_msgs_rcvd', 'label_withdraw_msgs_sent', 'notification_msgs_rcvd', 'notification_msgs_sent', 'time_stamp', 'total_msgs_rcvd', 'total_msgs_sent'], name, value)


        class Nodes(Entity):
            """
            Nodes for which data is collected
            
            .. attribute:: node
            
            	Node Instance
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Periodic.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"node" : ("node", PerfMgmt.Periodic.Nodes.Node)}

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Periodic.Nodes, [], name, value)


            class Node(Entity):
                """
                Node Instance
                
                .. attribute:: node_id  <key>
                
                	Node ID
                	**type**\:  str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: processes
                
                	Processes data
                	**type**\:   :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes>`
                
                .. attribute:: sample_xr
                
                	Node CPU data
                	**type**\:   :py:class:`SampleXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.SampleXr>`
                
                .. attribute:: samples
                
                	Node Memory data
                	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Samples>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"processes" : ("processes", PerfMgmt.Periodic.Nodes.Node.Processes), "sample-xr" : ("sample_xr", PerfMgmt.Periodic.Nodes.Node.SampleXr), "samples" : ("samples", PerfMgmt.Periodic.Nodes.Node.Samples)}
                    self._child_list_classes = {}

                    self.node_id = YLeaf(YType.str, "node-id")

                    self.processes = PerfMgmt.Periodic.Nodes.Node.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"
                    self._children_yang_names.add("processes")

                    self.sample_xr = PerfMgmt.Periodic.Nodes.Node.SampleXr()
                    self.sample_xr.parent = self
                    self._children_name_map["sample_xr"] = "sample-xr"
                    self._children_yang_names.add("sample-xr")

                    self.samples = PerfMgmt.Periodic.Nodes.Node.Samples()
                    self.samples.parent = self
                    self._children_name_map["samples"] = "samples"
                    self._children_yang_names.add("samples")
                    self._segment_path = lambda: "node" + "[node-id='" + self.node_id.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/nodes/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Nodes.Node, ['node_id'], name, value)


                class Processes(Entity):
                    """
                    Processes data
                    
                    .. attribute:: process
                    
                    	Process data
                    	**type**\: list of    :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Nodes.Node.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"process" : ("process", PerfMgmt.Periodic.Nodes.Node.Processes.Process)}

                        self.process = YList(self)
                        self._segment_path = lambda: "processes"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes, [], name, value)


                    class Process(Entity):
                        """
                        Process data
                        
                        .. attribute:: process_id  <key>
                        
                        	Process ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: samples
                        
                        	Process data
                        	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Nodes.Node.Processes.Process, self).__init__()

                            self.yang_name = "process"
                            self.yang_parent_name = "processes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples)}
                            self._child_list_classes = {}

                            self.process_id = YLeaf(YType.int32, "process-id")

                            self.samples = PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                            self._children_yang_names.add("samples")
                            self._segment_path = lambda: "process" + "[process-id='" + self.process_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes.Process, ['process_id'], name, value)


                        class Samples(Entity):
                            """
                            Process data
                            
                            .. attribute:: sample
                            
                            	Process data sample
                            	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples, self).__init__()

                                self.yang_name = "samples"
                                self.yang_parent_name = "process"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample)}

                                self.sample = YList(self)
                                self._segment_path = lambda: "samples"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples, [], name, value)


                            class Sample(Entity):
                                """
                                Process data sample
                                
                                .. attribute:: sample_id  <key>
                                
                                	Sample ID
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: average_cpu_used
                                
                                	Average %CPU utilization
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: no_threads
                                
                                	Number of threads
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: peak_memory
                                
                                	Max. dynamic memory (KBytes) used since startup time
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kilobyte
                                
                                .. attribute:: time_stamp
                                
                                	Timestamp of sample in seconds drom UCT
                                	**type**\:  int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'manageability-perfmgmt-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample, self).__init__()

                                    self.yang_name = "sample"
                                    self.yang_parent_name = "samples"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.sample_id = YLeaf(YType.int32, "sample-id")

                                    self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                                    self.no_threads = YLeaf(YType.uint32, "no-threads")

                                    self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                                    self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                    self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample, ['sample_id', 'average_cpu_used', 'no_threads', 'peak_memory', 'time_stamp'], name, value)


                class SampleXr(Entity):
                    """
                    Node CPU data
                    
                    .. attribute:: sample
                    
                    	Node CPU data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Nodes.Node.SampleXr, self).__init__()

                        self.yang_name = "sample-xr"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample)}

                        self.sample = YList(self)
                        self._segment_path = lambda: "sample-xr"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.SampleXr, [], name, value)


                    class Sample(Entity):
                        """
                        Node CPU data sample
                        
                        .. attribute:: sample_id  <key>
                        
                        	Sample ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: average_cpu_used
                        
                        	Average system %CPU utilization
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: no_processes
                        
                        	Number of processes in the system
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "sample-xr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                            self.no_processes = YLeaf(YType.uint32, "no-processes")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                            self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample, ['sample_id', 'average_cpu_used', 'no_processes', 'time_stamp'], name, value)


                class Samples(Entity):
                    """
                    Node Memory data
                    
                    .. attribute:: sample
                    
                    	Node Memory data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Samples.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Nodes.Node.Samples, self).__init__()

                        self.yang_name = "samples"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Nodes.Node.Samples.Sample)}

                        self.sample = YList(self)
                        self._segment_path = lambda: "samples"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Samples, [], name, value)


                    class Sample(Entity):
                        """
                        Node Memory data sample
                        
                        .. attribute:: sample_id  <key>
                        
                        	Sample ID
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: curr_memory
                        
                        	Current application memory (Bytes) in use
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: peak_memory
                        
                        	Max. system memory (MBytes) used since bootup
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: megabyte
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Nodes.Node.Samples.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "samples"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.curr_memory = YLeaf(YType.uint32, "curr-memory")

                            self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                            self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Samples.Sample, ['sample_id', 'curr_memory', 'peak_memory', 'time_stamp'], name, value)


        class Ospf(Entity):
            """
            Collected OSPF data
            
            .. attribute:: ospfv2_protocol_instances
            
            	OSPF v2 instances for which protocol statistics are collected
            	**type**\:   :py:class:`Ospfv2ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances>`
            
            .. attribute:: ospfv3_protocol_instances
            
            	OSPF v3 instances for which protocol statistics are collected
            	**type**\:   :py:class:`Ospfv3ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(PerfMgmt.Periodic.Ospf, self).__init__()

                self.yang_name = "ospf"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ospfv2-protocol-instances" : ("ospfv2_protocol_instances", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances), "ospfv3-protocol-instances" : ("ospfv3_protocol_instances", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances)}
                self._child_list_classes = {}

                self.ospfv2_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"
                self._children_yang_names.add("ospfv2-protocol-instances")

                self.ospfv3_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self
                self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                self._children_yang_names.add("ospfv3-protocol-instances")
                self._segment_path = lambda: "ospf"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()


            class Ospfv2ProtocolInstances(Entity):
                """
                OSPF v2 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv2_protocol_instance
                
                	Protocol samples for a particular OSPF v2 instance
                	**type**\: list of    :py:class:`Ospfv2ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv2-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ospfv2-protocol-instance" : ("ospfv2_protocol_instance", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance)}

                    self.ospfv2_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv2-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances, [], name, value)


                class Ospfv2ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v2
                    instance
                    
                    .. attribute:: instance_name  <key>
                    
                    	OSPF Instance Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v2 instance
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv2-protocol-instance"
                        self.yang_parent_name = "ospfv2-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples)}
                        self._child_list_classes = {}

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "ospfv2-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/ospfv2-protocol-instances/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v2 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv2-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: checksum_errors
                            
                            	Number of packets received with checksum errors
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.checksum_errors = YLeaf(YType.uint32, "checksum-errors")

                                self.input_db_ds = YLeaf(YType.uint32, "input-db-ds")

                                self.input_db_ds_lsa = YLeaf(YType.uint32, "input-db-ds-lsa")

                                self.input_hello_packets = YLeaf(YType.uint32, "input-hello-packets")

                                self.input_ls_requests = YLeaf(YType.uint32, "input-ls-requests")

                                self.input_ls_requests_lsa = YLeaf(YType.uint32, "input-ls-requests-lsa")

                                self.input_lsa_acks = YLeaf(YType.uint32, "input-lsa-acks")

                                self.input_lsa_acks_lsa = YLeaf(YType.uint32, "input-lsa-acks-lsa")

                                self.input_lsa_updates = YLeaf(YType.uint32, "input-lsa-updates")

                                self.input_lsa_updates_lsa = YLeaf(YType.uint32, "input-lsa-updates-lsa")

                                self.input_packets = YLeaf(YType.uint32, "input-packets")

                                self.output_db_ds = YLeaf(YType.uint32, "output-db-ds")

                                self.output_db_ds_lsa = YLeaf(YType.uint32, "output-db-ds-lsa")

                                self.output_hello_packets = YLeaf(YType.uint32, "output-hello-packets")

                                self.output_ls_requests = YLeaf(YType.uint32, "output-ls-requests")

                                self.output_ls_requests_lsa = YLeaf(YType.uint32, "output-ls-requests-lsa")

                                self.output_lsa_acks = YLeaf(YType.uint32, "output-lsa-acks")

                                self.output_lsa_acks_lsa = YLeaf(YType.uint32, "output-lsa-acks-lsa")

                                self.output_lsa_updates = YLeaf(YType.uint32, "output-lsa-updates")

                                self.output_lsa_updates_lsa = YLeaf(YType.uint32, "output-lsa-updates-lsa")

                                self.output_packets = YLeaf(YType.uint32, "output-packets")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, ['sample_id', 'checksum_errors', 'input_db_ds', 'input_db_ds_lsa', 'input_hello_packets', 'input_ls_requests', 'input_ls_requests_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'input_packets', 'output_db_ds', 'output_db_ds_lsa', 'output_hello_packets', 'output_ls_requests', 'output_ls_requests_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'output_packets', 'time_stamp'], name, value)


            class Ospfv3ProtocolInstances(Entity):
                """
                OSPF v3 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv3_protocol_instance
                
                	Protocol samples for a particular OSPF v3 instance
                	**type**\: list of    :py:class:`Ospfv3ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv3-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ospfv3-protocol-instance" : ("ospfv3_protocol_instance", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance)}

                    self.ospfv3_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv3-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances, [], name, value)


                class Ospfv3ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v3
                    instance
                    
                    .. attribute:: instance_name  <key>
                    
                    	OSPF Instance Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v3 instance
                    	**type**\:   :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv3-protocol-instance"
                        self.yang_parent_name = "ospfv3-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"samples" : ("samples", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples)}
                        self._child_list_classes = {}

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")
                        self._segment_path = lambda: "ospfv3-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/ospfv3-protocol-instances/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v3 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv3-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"sample" : ("sample", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample)}

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  <key>
                            
                            	Sample ID
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.sample_id = YLeaf(YType.int32, "sample-id")

                                self.input_db_ds = YLeaf(YType.uint32, "input-db-ds")

                                self.input_db_ds_lsa = YLeaf(YType.uint32, "input-db-ds-lsa")

                                self.input_hello_packets = YLeaf(YType.uint32, "input-hello-packets")

                                self.input_ls_requests = YLeaf(YType.uint32, "input-ls-requests")

                                self.input_ls_requests_lsa = YLeaf(YType.uint32, "input-ls-requests-lsa")

                                self.input_lsa_acks = YLeaf(YType.uint32, "input-lsa-acks")

                                self.input_lsa_acks_lsa = YLeaf(YType.uint32, "input-lsa-acks-lsa")

                                self.input_lsa_updates = YLeaf(YType.uint32, "input-lsa-updates")

                                self.input_lsa_updates_lsa = YLeaf(YType.uint32, "input-lsa-updates-lsa")

                                self.input_packets = YLeaf(YType.uint32, "input-packets")

                                self.output_db_ds = YLeaf(YType.uint32, "output-db-ds")

                                self.output_db_ds_lsa = YLeaf(YType.uint32, "output-db-ds-lsa")

                                self.output_hello_packets = YLeaf(YType.uint32, "output-hello-packets")

                                self.output_ls_requests = YLeaf(YType.uint32, "output-ls-requests")

                                self.output_ls_requests_lsa = YLeaf(YType.uint32, "output-ls-requests-lsa")

                                self.output_lsa_acks = YLeaf(YType.uint32, "output-lsa-acks")

                                self.output_lsa_acks_lsa = YLeaf(YType.uint32, "output-lsa-acks-lsa")

                                self.output_lsa_updates = YLeaf(YType.uint32, "output-lsa-updates")

                                self.output_lsa_updates_lsa = YLeaf(YType.uint32, "output-lsa-updates-lsa")

                                self.output_packets = YLeaf(YType.uint32, "output-packets")

                                self.time_stamp = YLeaf(YType.uint64, "time-stamp")
                                self._segment_path = lambda: "sample" + "[sample-id='" + self.sample_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, ['sample_id', 'input_db_ds', 'input_db_ds_lsa', 'input_hello_packets', 'input_ls_requests', 'input_ls_requests_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'input_packets', 'output_db_ds', 'output_db_ds_lsa', 'output_hello_packets', 'output_ls_requests', 'output_ls_requests_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'output_packets', 'time_stamp'], name, value)

    def clone_ptr(self):
        self._top_entity = PerfMgmt()
        return self._top_entity

