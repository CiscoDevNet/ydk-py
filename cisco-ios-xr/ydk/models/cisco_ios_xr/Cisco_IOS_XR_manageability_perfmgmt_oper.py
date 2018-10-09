""" Cisco_IOS_XR_manageability_perfmgmt_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-perfmgmt package operational data.

This module contains definitions
for the following management objects\:
  perf\-mgmt\: Performance Management agent operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class PerfMgmt(Entity):
    """
    Performance Management agent operational data
    
    .. attribute:: periodic
    
    	Data from periodic requests
    	**type**\:  :py:class:`Periodic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic>`
    
    .. attribute:: monitor
    
    	Data from monitor (one history period) requests
    	**type**\:  :py:class:`Monitor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor>`
    
    

    """

    _prefix = 'manageability-perfmgmt-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(PerfMgmt, self).__init__()
        self._top_entity = None

        self.yang_name = "perf-mgmt"
        self.yang_parent_name = "Cisco-IOS-XR-manageability-perfmgmt-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("periodic", ("periodic", PerfMgmt.Periodic)), ("monitor", ("monitor", PerfMgmt.Monitor))])
        self._leafs = OrderedDict()

        self.periodic = PerfMgmt.Periodic()
        self.periodic.parent = self
        self._children_name_map["periodic"] = "periodic"

        self.monitor = PerfMgmt.Monitor()
        self.monitor.parent = self
        self._children_name_map["monitor"] = "monitor"
        self._segment_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PerfMgmt, [], name, value)


    class Periodic(Entity):
        """
        Data from periodic requests
        
        .. attribute:: ospf
        
        	Collected OSPF data
        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf>`
        
        .. attribute:: mpls
        
        	Collected MPLS data
        	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls>`
        
        .. attribute:: nodes
        
        	Nodes for which data is collected
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes>`
        
        .. attribute:: bgp
        
        	Collected BGP data
        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp>`
        
        .. attribute:: interface
        
        	Collected Interface data
        	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface>`
        
        

        """

        _prefix = 'manageability-perfmgmt-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.Periodic, self).__init__()

            self.yang_name = "periodic"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospf", ("ospf", PerfMgmt.Periodic.Ospf)), ("mpls", ("mpls", PerfMgmt.Periodic.Mpls)), ("nodes", ("nodes", PerfMgmt.Periodic.Nodes)), ("bgp", ("bgp", PerfMgmt.Periodic.Bgp)), ("interface", ("interface", PerfMgmt.Periodic.Interface))])
            self._leafs = OrderedDict()

            self.ospf = PerfMgmt.Periodic.Ospf()
            self.ospf.parent = self
            self._children_name_map["ospf"] = "ospf"

            self.mpls = PerfMgmt.Periodic.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"

            self.nodes = PerfMgmt.Periodic.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"

            self.bgp = PerfMgmt.Periodic.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"

            self.interface = PerfMgmt.Periodic.Interface()
            self.interface.parent = self
            self._children_name_map["interface"] = "interface"
            self._segment_path = lambda: "periodic"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.Periodic, [], name, value)


        class Ospf(Entity):
            """
            Collected OSPF data
            
            .. attribute:: ospfv2_protocol_instances
            
            	OSPF v2 instances for which protocol statistics are collected
            	**type**\:  :py:class:`Ospfv2ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances>`
            
            .. attribute:: ospfv3_protocol_instances
            
            	OSPF v3 instances for which protocol statistics are collected
            	**type**\:  :py:class:`Ospfv3ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Periodic.Ospf, self).__init__()

                self.yang_name = "ospf"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ospfv2-protocol-instances", ("ospfv2_protocol_instances", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances)), ("ospfv3-protocol-instances", ("ospfv3_protocol_instances", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances))])
                self._leafs = OrderedDict()

                self.ospfv2_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"

                self.ospfv3_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self
                self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                self._segment_path = lambda: "ospf"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Periodic.Ospf, [], name, value)


            class Ospfv2ProtocolInstances(Entity):
                """
                OSPF v2 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv2_protocol_instance
                
                	Protocol samples for a particular OSPF v2 instance
                	**type**\: list of  		 :py:class:`Ospfv2ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv2-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospfv2-protocol-instance", ("ospfv2_protocol_instance", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance))])
                    self._leafs = OrderedDict()

                    self.ospfv2_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv2-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances, [], name, value)


                class Ospfv2ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v2
                    instance
                    
                    .. attribute:: instance_name  (key)
                    
                    	OSPF Instance Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v2 instance
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv2-protocol-instance"
                        self.yang_parent_name = "ospfv2-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['instance_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples))])
                        self._leafs = OrderedDict([
                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                        ])
                        self.instance_name = None

                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "ospfv2-protocol-instance" + "[instance-name='" + str(self.instance_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/ospfv2-protocol-instances/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v2 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv2-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: checksum_errors
                            
                            	Number of packets received with checksum errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_packets', (YLeaf(YType.uint32, 'input-packets'), ['int'])),
                                    ('output_packets', (YLeaf(YType.uint32, 'output-packets'), ['int'])),
                                    ('input_hello_packets', (YLeaf(YType.uint32, 'input-hello-packets'), ['int'])),
                                    ('output_hello_packets', (YLeaf(YType.uint32, 'output-hello-packets'), ['int'])),
                                    ('input_db_ds', (YLeaf(YType.uint32, 'input-db-ds'), ['int'])),
                                    ('input_db_ds_lsa', (YLeaf(YType.uint32, 'input-db-ds-lsa'), ['int'])),
                                    ('output_db_ds', (YLeaf(YType.uint32, 'output-db-ds'), ['int'])),
                                    ('output_db_ds_lsa', (YLeaf(YType.uint32, 'output-db-ds-lsa'), ['int'])),
                                    ('input_ls_requests', (YLeaf(YType.uint32, 'input-ls-requests'), ['int'])),
                                    ('input_ls_requests_lsa', (YLeaf(YType.uint32, 'input-ls-requests-lsa'), ['int'])),
                                    ('output_ls_requests', (YLeaf(YType.uint32, 'output-ls-requests'), ['int'])),
                                    ('output_ls_requests_lsa', (YLeaf(YType.uint32, 'output-ls-requests-lsa'), ['int'])),
                                    ('input_lsa_updates', (YLeaf(YType.uint32, 'input-lsa-updates'), ['int'])),
                                    ('input_lsa_updates_lsa', (YLeaf(YType.uint32, 'input-lsa-updates-lsa'), ['int'])),
                                    ('output_lsa_updates', (YLeaf(YType.uint32, 'output-lsa-updates'), ['int'])),
                                    ('output_lsa_updates_lsa', (YLeaf(YType.uint32, 'output-lsa-updates-lsa'), ['int'])),
                                    ('input_lsa_acks', (YLeaf(YType.uint32, 'input-lsa-acks'), ['int'])),
                                    ('input_lsa_acks_lsa', (YLeaf(YType.uint32, 'input-lsa-acks-lsa'), ['int'])),
                                    ('output_lsa_acks', (YLeaf(YType.uint32, 'output-lsa-acks'), ['int'])),
                                    ('output_lsa_acks_lsa', (YLeaf(YType.uint32, 'output-lsa-acks-lsa'), ['int'])),
                                    ('checksum_errors', (YLeaf(YType.uint32, 'checksum-errors'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_packets = None
                                self.output_packets = None
                                self.input_hello_packets = None
                                self.output_hello_packets = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self.checksum_errors = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, ['sample_id', 'time_stamp', 'input_packets', 'output_packets', 'input_hello_packets', 'output_hello_packets', 'input_db_ds', 'input_db_ds_lsa', 'output_db_ds', 'output_db_ds_lsa', 'input_ls_requests', 'input_ls_requests_lsa', 'output_ls_requests', 'output_ls_requests_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa', 'checksum_errors'], name, value)


            class Ospfv3ProtocolInstances(Entity):
                """
                OSPF v3 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv3_protocol_instance
                
                	Protocol samples for a particular OSPF v3 instance
                	**type**\: list of  		 :py:class:`Ospfv3ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv3-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospfv3-protocol-instance", ("ospfv3_protocol_instance", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance))])
                    self._leafs = OrderedDict()

                    self.ospfv3_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv3-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances, [], name, value)


                class Ospfv3ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v3
                    instance
                    
                    .. attribute:: instance_name  (key)
                    
                    	OSPF Instance Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v3 instance
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv3-protocol-instance"
                        self.yang_parent_name = "ospfv3-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['instance_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples))])
                        self._leafs = OrderedDict([
                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                        ])
                        self.instance_name = None

                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "ospfv3-protocol-instance" + "[instance-name='" + str(self.instance_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/ospfv3-protocol-instances/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v3 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv3-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_packets', (YLeaf(YType.uint32, 'input-packets'), ['int'])),
                                    ('output_packets', (YLeaf(YType.uint32, 'output-packets'), ['int'])),
                                    ('input_hello_packets', (YLeaf(YType.uint32, 'input-hello-packets'), ['int'])),
                                    ('output_hello_packets', (YLeaf(YType.uint32, 'output-hello-packets'), ['int'])),
                                    ('input_db_ds', (YLeaf(YType.uint32, 'input-db-ds'), ['int'])),
                                    ('input_db_ds_lsa', (YLeaf(YType.uint32, 'input-db-ds-lsa'), ['int'])),
                                    ('output_db_ds', (YLeaf(YType.uint32, 'output-db-ds'), ['int'])),
                                    ('output_db_ds_lsa', (YLeaf(YType.uint32, 'output-db-ds-lsa'), ['int'])),
                                    ('input_ls_requests', (YLeaf(YType.uint32, 'input-ls-requests'), ['int'])),
                                    ('input_ls_requests_lsa', (YLeaf(YType.uint32, 'input-ls-requests-lsa'), ['int'])),
                                    ('output_ls_requests', (YLeaf(YType.uint32, 'output-ls-requests'), ['int'])),
                                    ('output_ls_requests_lsa', (YLeaf(YType.uint32, 'output-ls-requests-lsa'), ['int'])),
                                    ('input_lsa_updates', (YLeaf(YType.uint32, 'input-lsa-updates'), ['int'])),
                                    ('input_lsa_updates_lsa', (YLeaf(YType.uint32, 'input-lsa-updates-lsa'), ['int'])),
                                    ('output_lsa_updates', (YLeaf(YType.uint32, 'output-lsa-updates'), ['int'])),
                                    ('output_lsa_updates_lsa', (YLeaf(YType.uint32, 'output-lsa-updates-lsa'), ['int'])),
                                    ('input_lsa_acks', (YLeaf(YType.uint32, 'input-lsa-acks'), ['int'])),
                                    ('input_lsa_acks_lsa', (YLeaf(YType.uint32, 'input-lsa-acks-lsa'), ['int'])),
                                    ('output_lsa_acks', (YLeaf(YType.uint32, 'output-lsa-acks'), ['int'])),
                                    ('output_lsa_acks_lsa', (YLeaf(YType.uint32, 'output-lsa-acks-lsa'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_packets = None
                                self.output_packets = None
                                self.input_hello_packets = None
                                self.output_hello_packets = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, ['sample_id', 'time_stamp', 'input_packets', 'output_packets', 'input_hello_packets', 'output_hello_packets', 'input_db_ds', 'input_db_ds_lsa', 'output_db_ds', 'output_db_ds_lsa', 'input_ls_requests', 'input_ls_requests_lsa', 'output_ls_requests', 'output_ls_requests_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa'], name, value)


        class Mpls(Entity):
            """
            Collected MPLS data
            
            .. attribute:: ldp_neighbors
            
            	LDP neighbors for which statistics are collected
            	**type**\:  :py:class:`LdpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Periodic.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ldp-neighbors", ("ldp_neighbors", PerfMgmt.Periodic.Mpls.LdpNeighbors))])
                self._leafs = OrderedDict()

                self.ldp_neighbors = PerfMgmt.Periodic.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self
                self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                self._segment_path = lambda: "mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Periodic.Mpls, [], name, value)


            class LdpNeighbors(Entity):
                """
                LDP neighbors for which statistics are
                collected
                
                .. attribute:: ldp_neighbor
                
                	Samples for a particular LDP neighbor
                	**type**\: list of  		 :py:class:`LdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Mpls.LdpNeighbors, self).__init__()

                    self.yang_name = "ldp-neighbors"
                    self.yang_parent_name = "mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ldp-neighbor", ("ldp_neighbor", PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor))])
                    self._leafs = OrderedDict()

                    self.ldp_neighbor = YList(self)
                    self._segment_path = lambda: "ldp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/mpls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors, [], name, value)


                class LdpNeighbor(Entity):
                    """
                    Samples for a particular LDP neighbor
                    
                    .. attribute:: nbr  (key)
                    
                    	Neighbor Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Samples for a particular LDP neighbor
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor, self).__init__()

                        self.yang_name = "ldp-neighbor"
                        self.yang_parent_name = "ldp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['nbr']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples))])
                        self._leafs = OrderedDict([
                            ('nbr', (YLeaf(YType.str, 'nbr'), ['str'])),
                        ])
                        self.nbr = None

                        self.samples = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "ldp-neighbor" + "[nbr='" + str(self.nbr) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/mpls/ldp-neighbors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor, ['nbr'], name, value)


                    class Samples(Entity):
                        """
                        Samples for a particular LDP neighbor
                        
                        .. attribute:: sample
                        
                        	LDP neighbor statistics sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ldp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            LDP neighbor statistics sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: total_msgs_sent
                            
                            	Total messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: total_msgs_rcvd
                            
                            	Total messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_sent
                            
                            	Init messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_rcvd
                            
                            	Tnit messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_msgs_sent
                            
                            	Address messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_msgs_rcvd
                            
                            	Address messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_sent
                            
                            	Address withdraw messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_rcvd
                            
                            	Address withdraw messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_sent
                            
                            	Label mapping messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_rcvd
                            
                            	Label mapping messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_sent
                            
                            	Label withdraw messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_rcvd
                            
                            	Label withdraw messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_sent
                            
                            	Label release messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_rcvd
                            
                            	Label release messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_sent
                            
                            	Notification messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_rcvd
                            
                            	Notification messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_sent
                            
                            	Keepalive messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_rcvd
                            
                            	Keepalive messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('total_msgs_sent', (YLeaf(YType.uint16, 'total-msgs-sent'), ['int'])),
                                    ('total_msgs_rcvd', (YLeaf(YType.uint16, 'total-msgs-rcvd'), ['int'])),
                                    ('init_msgs_sent', (YLeaf(YType.uint16, 'init-msgs-sent'), ['int'])),
                                    ('init_msgs_rcvd', (YLeaf(YType.uint16, 'init-msgs-rcvd'), ['int'])),
                                    ('address_msgs_sent', (YLeaf(YType.uint16, 'address-msgs-sent'), ['int'])),
                                    ('address_msgs_rcvd', (YLeaf(YType.uint16, 'address-msgs-rcvd'), ['int'])),
                                    ('address_withdraw_msgs_sent', (YLeaf(YType.uint16, 'address-withdraw-msgs-sent'), ['int'])),
                                    ('address_withdraw_msgs_rcvd', (YLeaf(YType.uint16, 'address-withdraw-msgs-rcvd'), ['int'])),
                                    ('label_mapping_msgs_sent', (YLeaf(YType.uint16, 'label-mapping-msgs-sent'), ['int'])),
                                    ('label_mapping_msgs_rcvd', (YLeaf(YType.uint16, 'label-mapping-msgs-rcvd'), ['int'])),
                                    ('label_withdraw_msgs_sent', (YLeaf(YType.uint16, 'label-withdraw-msgs-sent'), ['int'])),
                                    ('label_withdraw_msgs_rcvd', (YLeaf(YType.uint16, 'label-withdraw-msgs-rcvd'), ['int'])),
                                    ('label_release_msgs_sent', (YLeaf(YType.uint16, 'label-release-msgs-sent'), ['int'])),
                                    ('label_release_msgs_rcvd', (YLeaf(YType.uint16, 'label-release-msgs-rcvd'), ['int'])),
                                    ('notification_msgs_sent', (YLeaf(YType.uint16, 'notification-msgs-sent'), ['int'])),
                                    ('notification_msgs_rcvd', (YLeaf(YType.uint16, 'notification-msgs-rcvd'), ['int'])),
                                    ('keepalive_msgs_sent', (YLeaf(YType.uint16, 'keepalive-msgs-sent'), ['int'])),
                                    ('keepalive_msgs_rcvd', (YLeaf(YType.uint16, 'keepalive-msgs-rcvd'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.total_msgs_sent = None
                                self.total_msgs_rcvd = None
                                self.init_msgs_sent = None
                                self.init_msgs_rcvd = None
                                self.address_msgs_sent = None
                                self.address_msgs_rcvd = None
                                self.address_withdraw_msgs_sent = None
                                self.address_withdraw_msgs_rcvd = None
                                self.label_mapping_msgs_sent = None
                                self.label_mapping_msgs_rcvd = None
                                self.label_withdraw_msgs_sent = None
                                self.label_withdraw_msgs_rcvd = None
                                self.label_release_msgs_sent = None
                                self.label_release_msgs_rcvd = None
                                self.notification_msgs_sent = None
                                self.notification_msgs_rcvd = None
                                self.keepalive_msgs_sent = None
                                self.keepalive_msgs_rcvd = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, ['sample_id', 'time_stamp', 'total_msgs_sent', 'total_msgs_rcvd', 'init_msgs_sent', 'init_msgs_rcvd', 'address_msgs_sent', 'address_msgs_rcvd', 'address_withdraw_msgs_sent', 'address_withdraw_msgs_rcvd', 'label_mapping_msgs_sent', 'label_mapping_msgs_rcvd', 'label_withdraw_msgs_sent', 'label_withdraw_msgs_rcvd', 'label_release_msgs_sent', 'label_release_msgs_rcvd', 'notification_msgs_sent', 'notification_msgs_rcvd', 'keepalive_msgs_sent', 'keepalive_msgs_rcvd'], name, value)


        class Nodes(Entity):
            """
            Nodes for which data is collected
            
            .. attribute:: node
            
            	Node Instance
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Periodic.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Periodic.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Periodic.Nodes, [], name, value)


            class Node(Entity):
                """
                Node Instance
                
                .. attribute:: node_id  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: sample_xr
                
                	Node CPU data
                	**type**\:  :py:class:`SampleXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.SampleXr>`
                
                .. attribute:: processes
                
                	Processes data
                	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes>`
                
                .. attribute:: samples
                
                	Node Memory data
                	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Samples>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_id']
                    self._child_classes = OrderedDict([("sample-xr", ("sample_xr", PerfMgmt.Periodic.Nodes.Node.SampleXr)), ("processes", ("processes", PerfMgmt.Periodic.Nodes.Node.Processes)), ("samples", ("samples", PerfMgmt.Periodic.Nodes.Node.Samples))])
                    self._leafs = OrderedDict([
                        ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                    ])
                    self.node_id = None

                    self.sample_xr = PerfMgmt.Periodic.Nodes.Node.SampleXr()
                    self.sample_xr.parent = self
                    self._children_name_map["sample_xr"] = "sample-xr"

                    self.processes = PerfMgmt.Periodic.Nodes.Node.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"

                    self.samples = PerfMgmt.Periodic.Nodes.Node.Samples()
                    self.samples.parent = self
                    self._children_name_map["samples"] = "samples"
                    self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Nodes.Node, ['node_id'], name, value)


                class SampleXr(Entity):
                    """
                    Node CPU data
                    
                    .. attribute:: sample
                    
                    	Node CPU data sample
                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Nodes.Node.SampleXr, self).__init__()

                        self.yang_name = "sample-xr"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample))])
                        self._leafs = OrderedDict()

                        self.sample = YList(self)
                        self._segment_path = lambda: "sample-xr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.SampleXr, [], name, value)


                    class Sample(Entity):
                        """
                        Node CPU data sample
                        
                        .. attribute:: sample_id  (key)
                        
                        	Sample ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: no_processes
                        
                        	Number of processes in the system
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: average_cpu_used
                        
                        	Average system %CPU utilization
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "sample-xr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sample_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                ('no_processes', (YLeaf(YType.uint32, 'no-processes'), ['int'])),
                                ('average_cpu_used', (YLeaf(YType.uint32, 'average-cpu-used'), ['int'])),
                            ])
                            self.sample_id = None
                            self.time_stamp = None
                            self.no_processes = None
                            self.average_cpu_used = None
                            self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample, ['sample_id', 'time_stamp', 'no_processes', 'average_cpu_used'], name, value)


                class Processes(Entity):
                    """
                    Processes data
                    
                    .. attribute:: process
                    
                    	Process data
                    	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Nodes.Node.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process", ("process", PerfMgmt.Periodic.Nodes.Node.Processes.Process))])
                        self._leafs = OrderedDict()

                        self.process = YList(self)
                        self._segment_path = lambda: "processes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes, [], name, value)


                    class Process(Entity):
                        """
                        Process data
                        
                        .. attribute:: process_id  (key)
                        
                        	Process ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: samples
                        
                        	Process data
                        	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Nodes.Node.Processes.Process, self).__init__()

                            self.yang_name = "process"
                            self.yang_parent_name = "processes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['process_id']
                            self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples))])
                            self._leafs = OrderedDict([
                                ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                            ])
                            self.process_id = None

                            self.samples = PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                            self._segment_path = lambda: "process" + "[process-id='" + str(self.process_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes.Process, ['process_id'], name, value)


                        class Samples(Entity):
                            """
                            Process data
                            
                            .. attribute:: sample
                            
                            	Process data sample
                            	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples, self).__init__()

                                self.yang_name = "samples"
                                self.yang_parent_name = "process"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample))])
                                self._leafs = OrderedDict()

                                self.sample = YList(self)
                                self._segment_path = lambda: "samples"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples, [], name, value)


                            class Sample(Entity):
                                """
                                Process data sample
                                
                                .. attribute:: sample_id  (key)
                                
                                	Sample ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_stamp
                                
                                	Timestamp of sample in seconds drom UCT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: second
                                
                                .. attribute:: peak_memory
                                
                                	Max. dynamic memory (KBytes) used since startup time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kilobyte
                                
                                .. attribute:: average_cpu_used
                                
                                	Average %CPU utilization
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: no_threads
                                
                                	Number of threads
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'manageability-perfmgmt-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample, self).__init__()

                                    self.yang_name = "sample"
                                    self.yang_parent_name = "samples"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['sample_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                        ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                        ('peak_memory', (YLeaf(YType.uint32, 'peak-memory'), ['int'])),
                                        ('average_cpu_used', (YLeaf(YType.uint32, 'average-cpu-used'), ['int'])),
                                        ('no_threads', (YLeaf(YType.uint32, 'no-threads'), ['int'])),
                                    ])
                                    self.sample_id = None
                                    self.time_stamp = None
                                    self.peak_memory = None
                                    self.average_cpu_used = None
                                    self.no_threads = None
                                    self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample, ['sample_id', 'time_stamp', 'peak_memory', 'average_cpu_used', 'no_threads'], name, value)


                class Samples(Entity):
                    """
                    Node Memory data
                    
                    .. attribute:: sample
                    
                    	Node Memory data sample
                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Samples.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Nodes.Node.Samples, self).__init__()

                        self.yang_name = "samples"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Nodes.Node.Samples.Sample))])
                        self._leafs = OrderedDict()

                        self.sample = YList(self)
                        self._segment_path = lambda: "samples"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Samples, [], name, value)


                    class Sample(Entity):
                        """
                        Node Memory data sample
                        
                        .. attribute:: sample_id  (key)
                        
                        	Sample ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: curr_memory
                        
                        	Current application memory (Bytes) in use
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: peak_memory
                        
                        	Max. system memory (MBytes) used since bootup
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: megabyte
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Nodes.Node.Samples.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "samples"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sample_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                ('curr_memory', (YLeaf(YType.uint32, 'curr-memory'), ['int'])),
                                ('peak_memory', (YLeaf(YType.uint32, 'peak-memory'), ['int'])),
                            ])
                            self.sample_id = None
                            self.time_stamp = None
                            self.curr_memory = None
                            self.peak_memory = None
                            self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Nodes.Node.Samples.Sample, ['sample_id', 'time_stamp', 'curr_memory', 'peak_memory'], name, value)


        class Bgp(Entity):
            """
            Collected BGP data
            
            .. attribute:: bgp_neighbors
            
            	Neighbors for which statistics are collected
            	**type**\:  :py:class:`BgpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Periodic.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bgp-neighbors", ("bgp_neighbors", PerfMgmt.Periodic.Bgp.BgpNeighbors))])
                self._leafs = OrderedDict()

                self.bgp_neighbors = PerfMgmt.Periodic.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self
                self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                self._segment_path = lambda: "bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Periodic.Bgp, [], name, value)


            class BgpNeighbors(Entity):
                """
                Neighbors for which statistics are collected
                
                .. attribute:: bgp_neighbor
                
                	Samples for particular neighbor
                	**type**\: list of  		 :py:class:`BgpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Bgp.BgpNeighbors, self).__init__()

                    self.yang_name = "bgp-neighbors"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bgp-neighbor", ("bgp_neighbor", PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor))])
                    self._leafs = OrderedDict()

                    self.bgp_neighbor = YList(self)
                    self._segment_path = lambda: "bgp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/bgp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors, [], name, value)


                class BgpNeighbor(Entity):
                    """
                    Samples for particular neighbor
                    
                    .. attribute:: ip_address  (key)
                    
                    	BGP Neighbor Identifier
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Sample Table for a BGP neighbor
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor, self).__init__()

                        self.yang_name = "bgp-neighbor"
                        self.yang_parent_name = "bgp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['ip_address']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples))])
                        self._leafs = OrderedDict([
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                        ])
                        self.ip_address = None

                        self.samples = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "bgp-neighbor" + "[ip-address='" + str(self.ip_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/bgp/bgp-neighbors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor, ['ip_address'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for a BGP neighbor
                        
                        .. attribute:: sample
                        
                        	Neighbor statistics sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "bgp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Neighbor statistics sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_messages
                            
                            	Number of messages received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_messages
                            
                            	Number of messages sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_update_messages
                            
                            	Number of update messages received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_update_messages
                            
                            	Number of update messages sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: conn_established
                            
                            	Number of times the connection was established
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: conn_dropped
                            
                            	Number of times connection was dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_received
                            
                            	Number of error notifications received on the connection
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_sent
                            
                            	Number of error notifications sent on the connection
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_messages', (YLeaf(YType.uint32, 'input-messages'), ['int'])),
                                    ('output_messages', (YLeaf(YType.uint32, 'output-messages'), ['int'])),
                                    ('input_update_messages', (YLeaf(YType.uint32, 'input-update-messages'), ['int'])),
                                    ('output_update_messages', (YLeaf(YType.uint32, 'output-update-messages'), ['int'])),
                                    ('conn_established', (YLeaf(YType.uint32, 'conn-established'), ['int'])),
                                    ('conn_dropped', (YLeaf(YType.uint32, 'conn-dropped'), ['int'])),
                                    ('errors_received', (YLeaf(YType.uint32, 'errors-received'), ['int'])),
                                    ('errors_sent', (YLeaf(YType.uint32, 'errors-sent'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_messages = None
                                self.output_messages = None
                                self.input_update_messages = None
                                self.output_update_messages = None
                                self.conn_established = None
                                self.conn_dropped = None
                                self.errors_received = None
                                self.errors_sent = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, ['sample_id', 'time_stamp', 'input_messages', 'output_messages', 'input_update_messages', 'output_update_messages', 'conn_established', 'conn_dropped', 'errors_received', 'errors_sent'], name, value)


        class Interface(Entity):
            """
            Collected Interface data
            
            .. attribute:: generic_counter_interfaces
            
            	Interfaces for which Generic Counters are collected
            	**type**\:  :py:class:`GenericCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces>`
            
            .. attribute:: basic_counter_interfaces
            
            	Interfaces for which Basic Counters are collected
            	**type**\:  :py:class:`BasicCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces>`
            
            .. attribute:: data_rate_interfaces
            
            	Interfaces for which Data Rates are collected
            	**type**\:  :py:class:`DataRateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Periodic.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "periodic"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("generic-counter-interfaces", ("generic_counter_interfaces", PerfMgmt.Periodic.Interface.GenericCounterInterfaces)), ("basic-counter-interfaces", ("basic_counter_interfaces", PerfMgmt.Periodic.Interface.BasicCounterInterfaces)), ("data-rate-interfaces", ("data_rate_interfaces", PerfMgmt.Periodic.Interface.DataRateInterfaces))])
                self._leafs = OrderedDict()

                self.generic_counter_interfaces = PerfMgmt.Periodic.Interface.GenericCounterInterfaces()
                self.generic_counter_interfaces.parent = self
                self._children_name_map["generic_counter_interfaces"] = "generic-counter-interfaces"

                self.basic_counter_interfaces = PerfMgmt.Periodic.Interface.BasicCounterInterfaces()
                self.basic_counter_interfaces.parent = self
                self._children_name_map["basic_counter_interfaces"] = "basic-counter-interfaces"

                self.data_rate_interfaces = PerfMgmt.Periodic.Interface.DataRateInterfaces()
                self.data_rate_interfaces.parent = self
                self._children_name_map["data_rate_interfaces"] = "data-rate-interfaces"
                self._segment_path = lambda: "interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Periodic.Interface, [], name, value)


            class GenericCounterInterfaces(Entity):
                """
                Interfaces for which Generic Counters are
                collected
                
                .. attribute:: generic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of  		 :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces, self).__init__()

                    self.yang_name = "generic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("generic-counter-interface", ("generic_counter_interface", PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface))])
                    self._leafs = OrderedDict()

                    self.generic_counter_interface = YList(self)
                    self._segment_path = lambda: "generic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces, [], name, value)


                class GenericCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: samples
                    
                    	Generic Counter samples for an interface
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__init__()

                        self.yang_name = "generic-counter-interface"
                        self.yang_parent_name = "generic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.samples = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "generic-counter-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/generic-counter-interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Generic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "generic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: in_ucast_pkts
                            
                            	Unicast packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_multicast_pkts
                            
                            	Multicast packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_broadcast_pkts
                            
                            	Broadcast packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_ucast_pkts
                            
                            	Unicast packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_multicast_pkts
                            
                            	Multicast packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_broadcast_pkts
                            
                            	Broadcast packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_unknown_proto
                            
                            	Inbound packets discarded with unknown proto
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_underrun
                            
                            	Output underruns
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_crc
                            
                            	Inbound packets discarded with incorrect CRC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_overrun
                            
                            	Input overruns
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_frame
                            
                            	Inbound framing errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('in_packets', (YLeaf(YType.uint64, 'in-packets'), ['int'])),
                                    ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                    ('out_packets', (YLeaf(YType.uint64, 'out-packets'), ['int'])),
                                    ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                                    ('in_ucast_pkts', (YLeaf(YType.uint64, 'in-ucast-pkts'), ['int'])),
                                    ('in_multicast_pkts', (YLeaf(YType.uint64, 'in-multicast-pkts'), ['int'])),
                                    ('in_broadcast_pkts', (YLeaf(YType.uint64, 'in-broadcast-pkts'), ['int'])),
                                    ('out_ucast_pkts', (YLeaf(YType.uint64, 'out-ucast-pkts'), ['int'])),
                                    ('out_multicast_pkts', (YLeaf(YType.uint64, 'out-multicast-pkts'), ['int'])),
                                    ('out_broadcast_pkts', (YLeaf(YType.uint64, 'out-broadcast-pkts'), ['int'])),
                                    ('output_total_drops', (YLeaf(YType.uint32, 'output-total-drops'), ['int'])),
                                    ('input_total_drops', (YLeaf(YType.uint32, 'input-total-drops'), ['int'])),
                                    ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                                    ('input_unknown_proto', (YLeaf(YType.uint32, 'input-unknown-proto'), ['int'])),
                                    ('output_total_errors', (YLeaf(YType.uint32, 'output-total-errors'), ['int'])),
                                    ('output_underrun', (YLeaf(YType.uint32, 'output-underrun'), ['int'])),
                                    ('input_total_errors', (YLeaf(YType.uint32, 'input-total-errors'), ['int'])),
                                    ('input_crc', (YLeaf(YType.uint32, 'input-crc'), ['int'])),
                                    ('input_overrun', (YLeaf(YType.uint32, 'input-overrun'), ['int'])),
                                    ('input_frame', (YLeaf(YType.uint32, 'input-frame'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.in_packets = None
                                self.in_octets = None
                                self.out_packets = None
                                self.out_octets = None
                                self.in_ucast_pkts = None
                                self.in_multicast_pkts = None
                                self.in_broadcast_pkts = None
                                self.out_ucast_pkts = None
                                self.out_multicast_pkts = None
                                self.out_broadcast_pkts = None
                                self.output_total_drops = None
                                self.input_total_drops = None
                                self.input_queue_drops = None
                                self.input_unknown_proto = None
                                self.output_total_errors = None
                                self.output_underrun = None
                                self.input_total_errors = None
                                self.input_crc = None
                                self.input_overrun = None
                                self.input_frame = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, ['sample_id', 'time_stamp', 'in_packets', 'in_octets', 'out_packets', 'out_octets', 'in_ucast_pkts', 'in_multicast_pkts', 'in_broadcast_pkts', 'out_ucast_pkts', 'out_multicast_pkts', 'out_broadcast_pkts', 'output_total_drops', 'input_total_drops', 'input_queue_drops', 'input_unknown_proto', 'output_total_errors', 'output_underrun', 'input_total_errors', 'input_crc', 'input_overrun', 'input_frame'], name, value)


            class BasicCounterInterfaces(Entity):
                """
                Interfaces for which Basic Counters are
                collected
                
                .. attribute:: basic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of  		 :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces, self).__init__()

                    self.yang_name = "basic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("basic-counter-interface", ("basic_counter_interface", PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface))])
                    self._leafs = OrderedDict()

                    self.basic_counter_interface = YList(self)
                    self._segment_path = lambda: "basic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces, [], name, value)


                class BasicCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: samples
                    
                    	Basic Counter samples for an interface
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__init__()

                        self.yang_name = "basic-counter-interface"
                        self.yang_parent_name = "basic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.samples = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "basic-counter-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/basic-counter-interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Basic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Basic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "basic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Basic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds from UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_queue_drops
                            
                            	Output queue drops
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('in_packets', (YLeaf(YType.uint64, 'in-packets'), ['int'])),
                                    ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                    ('out_packets', (YLeaf(YType.uint64, 'out-packets'), ['int'])),
                                    ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                                    ('input_total_drops', (YLeaf(YType.uint64, 'input-total-drops'), ['int'])),
                                    ('input_queue_drops', (YLeaf(YType.uint64, 'input-queue-drops'), ['int'])),
                                    ('input_total_errors', (YLeaf(YType.uint64, 'input-total-errors'), ['int'])),
                                    ('output_total_drops', (YLeaf(YType.uint64, 'output-total-drops'), ['int'])),
                                    ('output_queue_drops', (YLeaf(YType.uint64, 'output-queue-drops'), ['int'])),
                                    ('output_total_errors', (YLeaf(YType.uint64, 'output-total-errors'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.in_packets = None
                                self.in_octets = None
                                self.out_packets = None
                                self.out_octets = None
                                self.input_total_drops = None
                                self.input_queue_drops = None
                                self.input_total_errors = None
                                self.output_total_drops = None
                                self.output_queue_drops = None
                                self.output_total_errors = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, ['sample_id', 'time_stamp', 'in_packets', 'in_octets', 'out_packets', 'out_octets', 'input_total_drops', 'input_queue_drops', 'input_total_errors', 'output_total_drops', 'output_queue_drops', 'output_total_errors'], name, value)


            class DataRateInterfaces(Entity):
                """
                Interfaces for which Data Rates are collected
                
                .. attribute:: data_rate_interface
                
                	Samples for a particular interface
                	**type**\: list of  		 :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Periodic.Interface.DataRateInterfaces, self).__init__()

                    self.yang_name = "data-rate-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("data-rate-interface", ("data_rate_interface", PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface))])
                    self._leafs = OrderedDict()

                    self.data_rate_interface = YList(self)
                    self._segment_path = lambda: "data-rate-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces, [], name, value)


                class DataRateInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: samples
                    
                    	Data Rate samples for an interface
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface, self).__init__()

                        self.yang_name = "data-rate-interface"
                        self.yang_parent_name = "data-rate-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.samples = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "data-rate-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/data-rate-interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Data Rate samples for an interface
                        
                        .. attribute:: sample
                        
                        	Data Rates sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "data-rate-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Data Rates sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_data_rate
                            
                            	Input datarate in 1000's of bps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: input_packet_rate
                            
                            	Input packets per second
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: output_data_rate
                            
                            	Output datarate in 1000's of bps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: output_packet_rate
                            
                            	Output packets per second
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: input_peak_rate
                            
                            	Peak input datarate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_peak_pkts
                            
                            	Peak input packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_peak_rate
                            
                            	Peak output datarate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_peak_pkts
                            
                            	Peak output packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bandwidth
                            
                            	Bandwidth (in kbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_data_rate', (YLeaf(YType.uint32, 'input-data-rate'), ['int'])),
                                    ('input_packet_rate', (YLeaf(YType.uint32, 'input-packet-rate'), ['int'])),
                                    ('output_data_rate', (YLeaf(YType.uint32, 'output-data-rate'), ['int'])),
                                    ('output_packet_rate', (YLeaf(YType.uint32, 'output-packet-rate'), ['int'])),
                                    ('input_peak_rate', (YLeaf(YType.uint32, 'input-peak-rate'), ['int'])),
                                    ('input_peak_pkts', (YLeaf(YType.uint32, 'input-peak-pkts'), ['int'])),
                                    ('output_peak_rate', (YLeaf(YType.uint32, 'output-peak-rate'), ['int'])),
                                    ('output_peak_pkts', (YLeaf(YType.uint32, 'output-peak-pkts'), ['int'])),
                                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_data_rate = None
                                self.input_packet_rate = None
                                self.output_data_rate = None
                                self.output_packet_rate = None
                                self.input_peak_rate = None
                                self.input_peak_pkts = None
                                self.output_peak_rate = None
                                self.output_peak_pkts = None
                                self.bandwidth = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, ['sample_id', 'time_stamp', 'input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'input_peak_rate', 'input_peak_pkts', 'output_peak_rate', 'output_peak_pkts', 'bandwidth'], name, value)


    class Monitor(Entity):
        """
        Data from monitor (one history period) requests
        
        .. attribute:: ospf
        
        	Collected OSPF data
        	**type**\:  :py:class:`Ospf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf>`
        
        .. attribute:: mpls
        
        	Collected MPLS data
        	**type**\:  :py:class:`Mpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls>`
        
        .. attribute:: nodes
        
        	Nodes for which data is collected
        	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes>`
        
        .. attribute:: bgp
        
        	Collected BGP data
        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp>`
        
        .. attribute:: interface
        
        	Collected Interface data
        	**type**\:  :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface>`
        
        

        """

        _prefix = 'manageability-perfmgmt-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.Monitor, self).__init__()

            self.yang_name = "monitor"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ospf", ("ospf", PerfMgmt.Monitor.Ospf)), ("mpls", ("mpls", PerfMgmt.Monitor.Mpls)), ("nodes", ("nodes", PerfMgmt.Monitor.Nodes)), ("bgp", ("bgp", PerfMgmt.Monitor.Bgp)), ("interface", ("interface", PerfMgmt.Monitor.Interface))])
            self._leafs = OrderedDict()

            self.ospf = PerfMgmt.Monitor.Ospf()
            self.ospf.parent = self
            self._children_name_map["ospf"] = "ospf"

            self.mpls = PerfMgmt.Monitor.Mpls()
            self.mpls.parent = self
            self._children_name_map["mpls"] = "mpls"

            self.nodes = PerfMgmt.Monitor.Nodes()
            self.nodes.parent = self
            self._children_name_map["nodes"] = "nodes"

            self.bgp = PerfMgmt.Monitor.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"

            self.interface = PerfMgmt.Monitor.Interface()
            self.interface.parent = self
            self._children_name_map["interface"] = "interface"
            self._segment_path = lambda: "monitor"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.Monitor, [], name, value)


        class Ospf(Entity):
            """
            Collected OSPF data
            
            .. attribute:: ospfv2_protocol_instances
            
            	OSPF v2 instances for which protocol statistics are collected
            	**type**\:  :py:class:`Ospfv2ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances>`
            
            .. attribute:: ospfv3_protocol_instances
            
            	OSPF v3 instances for which protocol statistics are collected
            	**type**\:  :py:class:`Ospfv3ProtocolInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Monitor.Ospf, self).__init__()

                self.yang_name = "ospf"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ospfv2-protocol-instances", ("ospfv2_protocol_instances", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances)), ("ospfv3-protocol-instances", ("ospfv3_protocol_instances", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances))])
                self._leafs = OrderedDict()

                self.ospfv2_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"

                self.ospfv3_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self
                self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                self._segment_path = lambda: "ospf"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Monitor.Ospf, [], name, value)


            class Ospfv2ProtocolInstances(Entity):
                """
                OSPF v2 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv2_protocol_instance
                
                	Protocol samples for a particular OSPF v2 instance
                	**type**\: list of  		 :py:class:`Ospfv2ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv2-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospfv2-protocol-instance", ("ospfv2_protocol_instance", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance))])
                    self._leafs = OrderedDict()

                    self.ospfv2_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv2-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances, [], name, value)


                class Ospfv2ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v2
                    instance
                    
                    .. attribute:: instance_name  (key)
                    
                    	OSPF Instance Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v2 instance
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv2-protocol-instance"
                        self.yang_parent_name = "ospfv2-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['instance_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples))])
                        self._leafs = OrderedDict([
                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                        ])
                        self.instance_name = None

                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "ospfv2-protocol-instance" + "[instance-name='" + str(self.instance_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/ospfv2-protocol-instances/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v2 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv2-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: checksum_errors
                            
                            	Number of packets received with checksum errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_packets', (YLeaf(YType.uint32, 'input-packets'), ['int'])),
                                    ('output_packets', (YLeaf(YType.uint32, 'output-packets'), ['int'])),
                                    ('input_hello_packets', (YLeaf(YType.uint32, 'input-hello-packets'), ['int'])),
                                    ('output_hello_packets', (YLeaf(YType.uint32, 'output-hello-packets'), ['int'])),
                                    ('input_db_ds', (YLeaf(YType.uint32, 'input-db-ds'), ['int'])),
                                    ('input_db_ds_lsa', (YLeaf(YType.uint32, 'input-db-ds-lsa'), ['int'])),
                                    ('output_db_ds', (YLeaf(YType.uint32, 'output-db-ds'), ['int'])),
                                    ('output_db_ds_lsa', (YLeaf(YType.uint32, 'output-db-ds-lsa'), ['int'])),
                                    ('input_ls_requests', (YLeaf(YType.uint32, 'input-ls-requests'), ['int'])),
                                    ('input_ls_requests_lsa', (YLeaf(YType.uint32, 'input-ls-requests-lsa'), ['int'])),
                                    ('output_ls_requests', (YLeaf(YType.uint32, 'output-ls-requests'), ['int'])),
                                    ('output_ls_requests_lsa', (YLeaf(YType.uint32, 'output-ls-requests-lsa'), ['int'])),
                                    ('input_lsa_updates', (YLeaf(YType.uint32, 'input-lsa-updates'), ['int'])),
                                    ('input_lsa_updates_lsa', (YLeaf(YType.uint32, 'input-lsa-updates-lsa'), ['int'])),
                                    ('output_lsa_updates', (YLeaf(YType.uint32, 'output-lsa-updates'), ['int'])),
                                    ('output_lsa_updates_lsa', (YLeaf(YType.uint32, 'output-lsa-updates-lsa'), ['int'])),
                                    ('input_lsa_acks', (YLeaf(YType.uint32, 'input-lsa-acks'), ['int'])),
                                    ('input_lsa_acks_lsa', (YLeaf(YType.uint32, 'input-lsa-acks-lsa'), ['int'])),
                                    ('output_lsa_acks', (YLeaf(YType.uint32, 'output-lsa-acks'), ['int'])),
                                    ('output_lsa_acks_lsa', (YLeaf(YType.uint32, 'output-lsa-acks-lsa'), ['int'])),
                                    ('checksum_errors', (YLeaf(YType.uint32, 'checksum-errors'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_packets = None
                                self.output_packets = None
                                self.input_hello_packets = None
                                self.output_hello_packets = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self.checksum_errors = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, ['sample_id', 'time_stamp', 'input_packets', 'output_packets', 'input_hello_packets', 'output_hello_packets', 'input_db_ds', 'input_db_ds_lsa', 'output_db_ds', 'output_db_ds_lsa', 'input_ls_requests', 'input_ls_requests_lsa', 'output_ls_requests', 'output_ls_requests_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa', 'checksum_errors'], name, value)


            class Ospfv3ProtocolInstances(Entity):
                """
                OSPF v3 instances for which protocol statistics
                are collected
                
                .. attribute:: ospfv3_protocol_instance
                
                	Protocol samples for a particular OSPF v3 instance
                	**type**\: list of  		 :py:class:`Ospfv3ProtocolInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances, self).__init__()

                    self.yang_name = "ospfv3-protocol-instances"
                    self.yang_parent_name = "ospf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospfv3-protocol-instance", ("ospfv3_protocol_instance", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance))])
                    self._leafs = OrderedDict()

                    self.ospfv3_protocol_instance = YList(self)
                    self._segment_path = lambda: "ospfv3-protocol-instances"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances, [], name, value)


                class Ospfv3ProtocolInstance(Entity):
                    """
                    Protocol samples for a particular OSPF v3
                    instance
                    
                    .. attribute:: instance_name  (key)
                    
                    	OSPF Instance Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: samples
                    
                    	Sample Table for an OSPV v3 instance
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__init__()

                        self.yang_name = "ospfv3-protocol-instance"
                        self.yang_parent_name = "ospfv3-protocol-instances"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['instance_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples))])
                        self._leafs = OrderedDict([
                            ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                        ])
                        self.instance_name = None

                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "ospfv3-protocol-instance" + "[instance-name='" + str(self.instance_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/ospfv3-protocol-instances/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, ['instance_name'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for an OSPV v3 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ospfv3-protocol-instance"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_packets
                            
                            	Total number of packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_packets
                            
                            	Total number of packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_hello_packets
                            
                            	Number of Hello packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_hello_packets
                            
                            	Number of Hello packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds
                            
                            	Number of DBD packets received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_db_ds_lsa
                            
                            	Number of LSA received in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds
                            
                            	Number of DBD packets sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_db_ds_lsa
                            
                            	Number of LSA sent in DBD packets
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests
                            
                            	Number of LS Requests received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_ls_requests_lsa
                            
                            	Number of LSA received in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests
                            
                            	Number of LS Requests sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_ls_requests_lsa
                            
                            	Number of LSA sent in LS Requests
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates
                            
                            	Number of LSA Updates received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_updates_lsa
                            
                            	Number of LSA received in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates
                            
                            	Number of LSA Updates sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_updates_lsa
                            
                            	Number of LSA sent in LSA Updates
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks
                            
                            	Number of LSA Acknowledgements received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_lsa_acks_lsa
                            
                            	Number of LSA received in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks
                            
                            	Number of LSA Acknowledgements sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_lsa_acks_lsa
                            
                            	Number of LSA sent in LSA Acknowledgements
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_packets', (YLeaf(YType.uint32, 'input-packets'), ['int'])),
                                    ('output_packets', (YLeaf(YType.uint32, 'output-packets'), ['int'])),
                                    ('input_hello_packets', (YLeaf(YType.uint32, 'input-hello-packets'), ['int'])),
                                    ('output_hello_packets', (YLeaf(YType.uint32, 'output-hello-packets'), ['int'])),
                                    ('input_db_ds', (YLeaf(YType.uint32, 'input-db-ds'), ['int'])),
                                    ('input_db_ds_lsa', (YLeaf(YType.uint32, 'input-db-ds-lsa'), ['int'])),
                                    ('output_db_ds', (YLeaf(YType.uint32, 'output-db-ds'), ['int'])),
                                    ('output_db_ds_lsa', (YLeaf(YType.uint32, 'output-db-ds-lsa'), ['int'])),
                                    ('input_ls_requests', (YLeaf(YType.uint32, 'input-ls-requests'), ['int'])),
                                    ('input_ls_requests_lsa', (YLeaf(YType.uint32, 'input-ls-requests-lsa'), ['int'])),
                                    ('output_ls_requests', (YLeaf(YType.uint32, 'output-ls-requests'), ['int'])),
                                    ('output_ls_requests_lsa', (YLeaf(YType.uint32, 'output-ls-requests-lsa'), ['int'])),
                                    ('input_lsa_updates', (YLeaf(YType.uint32, 'input-lsa-updates'), ['int'])),
                                    ('input_lsa_updates_lsa', (YLeaf(YType.uint32, 'input-lsa-updates-lsa'), ['int'])),
                                    ('output_lsa_updates', (YLeaf(YType.uint32, 'output-lsa-updates'), ['int'])),
                                    ('output_lsa_updates_lsa', (YLeaf(YType.uint32, 'output-lsa-updates-lsa'), ['int'])),
                                    ('input_lsa_acks', (YLeaf(YType.uint32, 'input-lsa-acks'), ['int'])),
                                    ('input_lsa_acks_lsa', (YLeaf(YType.uint32, 'input-lsa-acks-lsa'), ['int'])),
                                    ('output_lsa_acks', (YLeaf(YType.uint32, 'output-lsa-acks'), ['int'])),
                                    ('output_lsa_acks_lsa', (YLeaf(YType.uint32, 'output-lsa-acks-lsa'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_packets = None
                                self.output_packets = None
                                self.input_hello_packets = None
                                self.output_hello_packets = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, ['sample_id', 'time_stamp', 'input_packets', 'output_packets', 'input_hello_packets', 'output_hello_packets', 'input_db_ds', 'input_db_ds_lsa', 'output_db_ds', 'output_db_ds_lsa', 'input_ls_requests', 'input_ls_requests_lsa', 'output_ls_requests', 'output_ls_requests_lsa', 'input_lsa_updates', 'input_lsa_updates_lsa', 'output_lsa_updates', 'output_lsa_updates_lsa', 'input_lsa_acks', 'input_lsa_acks_lsa', 'output_lsa_acks', 'output_lsa_acks_lsa'], name, value)


        class Mpls(Entity):
            """
            Collected MPLS data
            
            .. attribute:: ldp_neighbors
            
            	LDP neighbors for which statistics are collected
            	**type**\:  :py:class:`LdpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Monitor.Mpls, self).__init__()

                self.yang_name = "mpls"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ldp-neighbors", ("ldp_neighbors", PerfMgmt.Monitor.Mpls.LdpNeighbors))])
                self._leafs = OrderedDict()

                self.ldp_neighbors = PerfMgmt.Monitor.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self
                self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                self._segment_path = lambda: "mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Monitor.Mpls, [], name, value)


            class LdpNeighbors(Entity):
                """
                LDP neighbors for which statistics are
                collected
                
                .. attribute:: ldp_neighbor
                
                	Samples for a particular LDP neighbor
                	**type**\: list of  		 :py:class:`LdpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Mpls.LdpNeighbors, self).__init__()

                    self.yang_name = "ldp-neighbors"
                    self.yang_parent_name = "mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ldp-neighbor", ("ldp_neighbor", PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor))])
                    self._leafs = OrderedDict()

                    self.ldp_neighbor = YList(self)
                    self._segment_path = lambda: "ldp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/mpls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors, [], name, value)


                class LdpNeighbor(Entity):
                    """
                    Samples for a particular LDP neighbor
                    
                    .. attribute:: nbr  (key)
                    
                    	Neighbor Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Samples for a particular LDP neighbor
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor, self).__init__()

                        self.yang_name = "ldp-neighbor"
                        self.yang_parent_name = "ldp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['nbr']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples))])
                        self._leafs = OrderedDict([
                            ('nbr', (YLeaf(YType.str, 'nbr'), ['str'])),
                        ])
                        self.nbr = None

                        self.samples = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "ldp-neighbor" + "[nbr='" + str(self.nbr) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/mpls/ldp-neighbors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor, ['nbr'], name, value)


                    class Samples(Entity):
                        """
                        Samples for a particular LDP neighbor
                        
                        .. attribute:: sample
                        
                        	LDP neighbor statistics sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "ldp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            LDP neighbor statistics sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: total_msgs_sent
                            
                            	Total messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: total_msgs_rcvd
                            
                            	Total messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_sent
                            
                            	Init messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: init_msgs_rcvd
                            
                            	Tnit messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_msgs_sent
                            
                            	Address messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_msgs_rcvd
                            
                            	Address messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_sent
                            
                            	Address withdraw messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: address_withdraw_msgs_rcvd
                            
                            	Address withdraw messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_sent
                            
                            	Label mapping messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_mapping_msgs_rcvd
                            
                            	Label mapping messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_sent
                            
                            	Label withdraw messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_withdraw_msgs_rcvd
                            
                            	Label withdraw messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_sent
                            
                            	Label release messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: label_release_msgs_rcvd
                            
                            	Label release messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_sent
                            
                            	Notification messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: notification_msgs_rcvd
                            
                            	Notification messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_sent
                            
                            	Keepalive messages sent
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: keepalive_msgs_rcvd
                            
                            	Keepalive messages received
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('total_msgs_sent', (YLeaf(YType.uint16, 'total-msgs-sent'), ['int'])),
                                    ('total_msgs_rcvd', (YLeaf(YType.uint16, 'total-msgs-rcvd'), ['int'])),
                                    ('init_msgs_sent', (YLeaf(YType.uint16, 'init-msgs-sent'), ['int'])),
                                    ('init_msgs_rcvd', (YLeaf(YType.uint16, 'init-msgs-rcvd'), ['int'])),
                                    ('address_msgs_sent', (YLeaf(YType.uint16, 'address-msgs-sent'), ['int'])),
                                    ('address_msgs_rcvd', (YLeaf(YType.uint16, 'address-msgs-rcvd'), ['int'])),
                                    ('address_withdraw_msgs_sent', (YLeaf(YType.uint16, 'address-withdraw-msgs-sent'), ['int'])),
                                    ('address_withdraw_msgs_rcvd', (YLeaf(YType.uint16, 'address-withdraw-msgs-rcvd'), ['int'])),
                                    ('label_mapping_msgs_sent', (YLeaf(YType.uint16, 'label-mapping-msgs-sent'), ['int'])),
                                    ('label_mapping_msgs_rcvd', (YLeaf(YType.uint16, 'label-mapping-msgs-rcvd'), ['int'])),
                                    ('label_withdraw_msgs_sent', (YLeaf(YType.uint16, 'label-withdraw-msgs-sent'), ['int'])),
                                    ('label_withdraw_msgs_rcvd', (YLeaf(YType.uint16, 'label-withdraw-msgs-rcvd'), ['int'])),
                                    ('label_release_msgs_sent', (YLeaf(YType.uint16, 'label-release-msgs-sent'), ['int'])),
                                    ('label_release_msgs_rcvd', (YLeaf(YType.uint16, 'label-release-msgs-rcvd'), ['int'])),
                                    ('notification_msgs_sent', (YLeaf(YType.uint16, 'notification-msgs-sent'), ['int'])),
                                    ('notification_msgs_rcvd', (YLeaf(YType.uint16, 'notification-msgs-rcvd'), ['int'])),
                                    ('keepalive_msgs_sent', (YLeaf(YType.uint16, 'keepalive-msgs-sent'), ['int'])),
                                    ('keepalive_msgs_rcvd', (YLeaf(YType.uint16, 'keepalive-msgs-rcvd'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.total_msgs_sent = None
                                self.total_msgs_rcvd = None
                                self.init_msgs_sent = None
                                self.init_msgs_rcvd = None
                                self.address_msgs_sent = None
                                self.address_msgs_rcvd = None
                                self.address_withdraw_msgs_sent = None
                                self.address_withdraw_msgs_rcvd = None
                                self.label_mapping_msgs_sent = None
                                self.label_mapping_msgs_rcvd = None
                                self.label_withdraw_msgs_sent = None
                                self.label_withdraw_msgs_rcvd = None
                                self.label_release_msgs_sent = None
                                self.label_release_msgs_rcvd = None
                                self.notification_msgs_sent = None
                                self.notification_msgs_rcvd = None
                                self.keepalive_msgs_sent = None
                                self.keepalive_msgs_rcvd = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, ['sample_id', 'time_stamp', 'total_msgs_sent', 'total_msgs_rcvd', 'init_msgs_sent', 'init_msgs_rcvd', 'address_msgs_sent', 'address_msgs_rcvd', 'address_withdraw_msgs_sent', 'address_withdraw_msgs_rcvd', 'label_mapping_msgs_sent', 'label_mapping_msgs_rcvd', 'label_withdraw_msgs_sent', 'label_withdraw_msgs_rcvd', 'label_release_msgs_sent', 'label_release_msgs_rcvd', 'notification_msgs_sent', 'notification_msgs_rcvd', 'keepalive_msgs_sent', 'keepalive_msgs_rcvd'], name, value)


        class Nodes(Entity):
            """
            Nodes for which data is collected
            
            .. attribute:: node
            
            	Node Instance
            	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Monitor.Nodes, self).__init__()

                self.yang_name = "nodes"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Monitor.Nodes.Node))])
                self._leafs = OrderedDict()

                self.node = YList(self)
                self._segment_path = lambda: "nodes"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Monitor.Nodes, [], name, value)


            class Node(Entity):
                """
                Node Instance
                
                .. attribute:: node_id  (key)
                
                	Node ID
                	**type**\: str
                
                	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                
                .. attribute:: sample_xr
                
                	Node CPU data
                	**type**\:  :py:class:`SampleXr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.SampleXr>`
                
                .. attribute:: processes
                
                	Processes data
                	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes>`
                
                .. attribute:: samples
                
                	Node Memory data
                	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Samples>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Nodes.Node, self).__init__()

                    self.yang_name = "node"
                    self.yang_parent_name = "nodes"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['node_id']
                    self._child_classes = OrderedDict([("sample-xr", ("sample_xr", PerfMgmt.Monitor.Nodes.Node.SampleXr)), ("processes", ("processes", PerfMgmt.Monitor.Nodes.Node.Processes)), ("samples", ("samples", PerfMgmt.Monitor.Nodes.Node.Samples))])
                    self._leafs = OrderedDict([
                        ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                    ])
                    self.node_id = None

                    self.sample_xr = PerfMgmt.Monitor.Nodes.Node.SampleXr()
                    self.sample_xr.parent = self
                    self._children_name_map["sample_xr"] = "sample-xr"

                    self.processes = PerfMgmt.Monitor.Nodes.Node.Processes()
                    self.processes.parent = self
                    self._children_name_map["processes"] = "processes"

                    self.samples = PerfMgmt.Monitor.Nodes.Node.Samples()
                    self.samples.parent = self
                    self._children_name_map["samples"] = "samples"
                    self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/nodes/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Nodes.Node, ['node_id'], name, value)


                class SampleXr(Entity):
                    """
                    Node CPU data
                    
                    .. attribute:: sample
                    
                    	Node CPU data sample
                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Nodes.Node.SampleXr, self).__init__()

                        self.yang_name = "sample-xr"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample))])
                        self._leafs = OrderedDict()

                        self.sample = YList(self)
                        self._segment_path = lambda: "sample-xr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.SampleXr, [], name, value)


                    class Sample(Entity):
                        """
                        Node CPU data sample
                        
                        .. attribute:: sample_id  (key)
                        
                        	Sample ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: no_processes
                        
                        	Number of processes in the system
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: average_cpu_used
                        
                        	Average system %CPU utilization
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "sample-xr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sample_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                ('no_processes', (YLeaf(YType.uint32, 'no-processes'), ['int'])),
                                ('average_cpu_used', (YLeaf(YType.uint32, 'average-cpu-used'), ['int'])),
                            ])
                            self.sample_id = None
                            self.time_stamp = None
                            self.no_processes = None
                            self.average_cpu_used = None
                            self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample, ['sample_id', 'time_stamp', 'no_processes', 'average_cpu_used'], name, value)


                class Processes(Entity):
                    """
                    Processes data
                    
                    .. attribute:: process
                    
                    	Process data
                    	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Nodes.Node.Processes, self).__init__()

                        self.yang_name = "processes"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process", ("process", PerfMgmt.Monitor.Nodes.Node.Processes.Process))])
                        self._leafs = OrderedDict()

                        self.process = YList(self)
                        self._segment_path = lambda: "processes"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes, [], name, value)


                    class Process(Entity):
                        """
                        Process data
                        
                        .. attribute:: process_id  (key)
                        
                        	Process ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: samples
                        
                        	Process data
                        	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Nodes.Node.Processes.Process, self).__init__()

                            self.yang_name = "process"
                            self.yang_parent_name = "processes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['process_id']
                            self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples))])
                            self._leafs = OrderedDict([
                                ('process_id', (YLeaf(YType.uint32, 'process-id'), ['int'])),
                            ])
                            self.process_id = None

                            self.samples = PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                            self._segment_path = lambda: "process" + "[process-id='" + str(self.process_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes.Process, ['process_id'], name, value)


                        class Samples(Entity):
                            """
                            Process data
                            
                            .. attribute:: sample
                            
                            	Process data sample
                            	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples, self).__init__()

                                self.yang_name = "samples"
                                self.yang_parent_name = "process"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample))])
                                self._leafs = OrderedDict()

                                self.sample = YList(self)
                                self._segment_path = lambda: "samples"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples, [], name, value)


                            class Sample(Entity):
                                """
                                Process data sample
                                
                                .. attribute:: sample_id  (key)
                                
                                	Sample ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: time_stamp
                                
                                	Timestamp of sample in seconds drom UCT
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: second
                                
                                .. attribute:: peak_memory
                                
                                	Max. dynamic memory (KBytes) used since startup time
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: kilobyte
                                
                                .. attribute:: average_cpu_used
                                
                                	Average %CPU utilization
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: no_threads
                                
                                	Number of threads
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'manageability-perfmgmt-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample, self).__init__()

                                    self.yang_name = "sample"
                                    self.yang_parent_name = "samples"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['sample_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                        ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                        ('peak_memory', (YLeaf(YType.uint32, 'peak-memory'), ['int'])),
                                        ('average_cpu_used', (YLeaf(YType.uint32, 'average-cpu-used'), ['int'])),
                                        ('no_threads', (YLeaf(YType.uint32, 'no-threads'), ['int'])),
                                    ])
                                    self.sample_id = None
                                    self.time_stamp = None
                                    self.peak_memory = None
                                    self.average_cpu_used = None
                                    self.no_threads = None
                                    self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample, ['sample_id', 'time_stamp', 'peak_memory', 'average_cpu_used', 'no_threads'], name, value)


                class Samples(Entity):
                    """
                    Node Memory data
                    
                    .. attribute:: sample
                    
                    	Node Memory data sample
                    	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Samples.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Nodes.Node.Samples, self).__init__()

                        self.yang_name = "samples"
                        self.yang_parent_name = "node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Nodes.Node.Samples.Sample))])
                        self._leafs = OrderedDict()

                        self.sample = YList(self)
                        self._segment_path = lambda: "samples"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Samples, [], name, value)


                    class Sample(Entity):
                        """
                        Node Memory data sample
                        
                        .. attribute:: sample_id  (key)
                        
                        	Sample ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: time_stamp
                        
                        	Timestamp of sample in seconds drom UCT
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        	**units**\: second
                        
                        .. attribute:: curr_memory
                        
                        	Current application memory (Bytes) in use
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: peak_memory
                        
                        	Max. system memory (MBytes) used since bootup
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: megabyte
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Nodes.Node.Samples.Sample, self).__init__()

                            self.yang_name = "sample"
                            self.yang_parent_name = "samples"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['sample_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                ('curr_memory', (YLeaf(YType.uint32, 'curr-memory'), ['int'])),
                                ('peak_memory', (YLeaf(YType.uint32, 'peak-memory'), ['int'])),
                            ])
                            self.sample_id = None
                            self.time_stamp = None
                            self.curr_memory = None
                            self.peak_memory = None
                            self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Nodes.Node.Samples.Sample, ['sample_id', 'time_stamp', 'curr_memory', 'peak_memory'], name, value)


        class Bgp(Entity):
            """
            Collected BGP data
            
            .. attribute:: bgp_neighbors
            
            	Neighbors for which statistics are collected
            	**type**\:  :py:class:`BgpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Monitor.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bgp-neighbors", ("bgp_neighbors", PerfMgmt.Monitor.Bgp.BgpNeighbors))])
                self._leafs = OrderedDict()

                self.bgp_neighbors = PerfMgmt.Monitor.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self
                self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                self._segment_path = lambda: "bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Monitor.Bgp, [], name, value)


            class BgpNeighbors(Entity):
                """
                Neighbors for which statistics are collected
                
                .. attribute:: bgp_neighbor
                
                	Samples for particular neighbor
                	**type**\: list of  		 :py:class:`BgpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Bgp.BgpNeighbors, self).__init__()

                    self.yang_name = "bgp-neighbors"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bgp-neighbor", ("bgp_neighbor", PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor))])
                    self._leafs = OrderedDict()

                    self.bgp_neighbor = YList(self)
                    self._segment_path = lambda: "bgp-neighbors"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/bgp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors, [], name, value)


                class BgpNeighbor(Entity):
                    """
                    Samples for particular neighbor
                    
                    .. attribute:: ip_address  (key)
                    
                    	BGP Neighbor Identifier
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: samples
                    
                    	Sample Table for a BGP neighbor
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor, self).__init__()

                        self.yang_name = "bgp-neighbor"
                        self.yang_parent_name = "bgp-neighbors"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['ip_address']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples))])
                        self._leafs = OrderedDict([
                            ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                        ])
                        self.ip_address = None

                        self.samples = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "bgp-neighbor" + "[ip-address='" + str(self.ip_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/bgp/bgp-neighbors/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor, ['ip_address'], name, value)


                    class Samples(Entity):
                        """
                        Sample Table for a BGP neighbor
                        
                        .. attribute:: sample
                        
                        	Neighbor statistics sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "bgp-neighbor"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Neighbor statistics sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_messages
                            
                            	Number of messages received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_messages
                            
                            	Number of messages sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_update_messages
                            
                            	Number of update messages received
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_update_messages
                            
                            	Number of update messages sent
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: conn_established
                            
                            	Number of times the connection was established
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: conn_dropped
                            
                            	Number of times connection was dropped
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_received
                            
                            	Number of error notifications received on the connection
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: errors_sent
                            
                            	Number of error notifications sent on the connection
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_messages', (YLeaf(YType.uint32, 'input-messages'), ['int'])),
                                    ('output_messages', (YLeaf(YType.uint32, 'output-messages'), ['int'])),
                                    ('input_update_messages', (YLeaf(YType.uint32, 'input-update-messages'), ['int'])),
                                    ('output_update_messages', (YLeaf(YType.uint32, 'output-update-messages'), ['int'])),
                                    ('conn_established', (YLeaf(YType.uint32, 'conn-established'), ['int'])),
                                    ('conn_dropped', (YLeaf(YType.uint32, 'conn-dropped'), ['int'])),
                                    ('errors_received', (YLeaf(YType.uint32, 'errors-received'), ['int'])),
                                    ('errors_sent', (YLeaf(YType.uint32, 'errors-sent'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_messages = None
                                self.output_messages = None
                                self.input_update_messages = None
                                self.output_update_messages = None
                                self.conn_established = None
                                self.conn_dropped = None
                                self.errors_received = None
                                self.errors_sent = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, ['sample_id', 'time_stamp', 'input_messages', 'output_messages', 'input_update_messages', 'output_update_messages', 'conn_established', 'conn_dropped', 'errors_received', 'errors_sent'], name, value)


        class Interface(Entity):
            """
            Collected Interface data
            
            .. attribute:: generic_counter_interfaces
            
            	Interfaces for which Generic Counters are collected
            	**type**\:  :py:class:`GenericCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces>`
            
            .. attribute:: basic_counter_interfaces
            
            	Interfaces for which Basic Counters are collected
            	**type**\:  :py:class:`BasicCounterInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces>`
            
            .. attribute:: data_rate_interfaces
            
            	Interfaces for which Data Rates are collected
            	**type**\:  :py:class:`DataRateInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Monitor.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "monitor"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("generic-counter-interfaces", ("generic_counter_interfaces", PerfMgmt.Monitor.Interface.GenericCounterInterfaces)), ("basic-counter-interfaces", ("basic_counter_interfaces", PerfMgmt.Monitor.Interface.BasicCounterInterfaces)), ("data-rate-interfaces", ("data_rate_interfaces", PerfMgmt.Monitor.Interface.DataRateInterfaces))])
                self._leafs = OrderedDict()

                self.generic_counter_interfaces = PerfMgmt.Monitor.Interface.GenericCounterInterfaces()
                self.generic_counter_interfaces.parent = self
                self._children_name_map["generic_counter_interfaces"] = "generic-counter-interfaces"

                self.basic_counter_interfaces = PerfMgmt.Monitor.Interface.BasicCounterInterfaces()
                self.basic_counter_interfaces.parent = self
                self._children_name_map["basic_counter_interfaces"] = "basic-counter-interfaces"

                self.data_rate_interfaces = PerfMgmt.Monitor.Interface.DataRateInterfaces()
                self.data_rate_interfaces.parent = self
                self._children_name_map["data_rate_interfaces"] = "data-rate-interfaces"
                self._segment_path = lambda: "interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Monitor.Interface, [], name, value)


            class GenericCounterInterfaces(Entity):
                """
                Interfaces for which Generic Counters are
                collected
                
                .. attribute:: generic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of  		 :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces, self).__init__()

                    self.yang_name = "generic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("generic-counter-interface", ("generic_counter_interface", PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface))])
                    self._leafs = OrderedDict()

                    self.generic_counter_interface = YList(self)
                    self._segment_path = lambda: "generic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces, [], name, value)


                class GenericCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: samples
                    
                    	Generic Counter samples for an interface
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__init__()

                        self.yang_name = "generic-counter-interface"
                        self.yang_parent_name = "generic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.samples = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "generic-counter-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/generic-counter-interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Generic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "generic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Generic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: in_ucast_pkts
                            
                            	Unicast packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_multicast_pkts
                            
                            	Multicast packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_broadcast_pkts
                            
                            	Broadcast packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_ucast_pkts
                            
                            	Unicast packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_multicast_pkts
                            
                            	Multicast packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_broadcast_pkts
                            
                            	Broadcast packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_unknown_proto
                            
                            	Inbound packets discarded with unknown proto
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_underrun
                            
                            	Output underruns
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_crc
                            
                            	Inbound packets discarded with incorrect CRC
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_overrun
                            
                            	Input overruns
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_frame
                            
                            	Inbound framing errors
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('in_packets', (YLeaf(YType.uint64, 'in-packets'), ['int'])),
                                    ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                    ('out_packets', (YLeaf(YType.uint64, 'out-packets'), ['int'])),
                                    ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                                    ('in_ucast_pkts', (YLeaf(YType.uint64, 'in-ucast-pkts'), ['int'])),
                                    ('in_multicast_pkts', (YLeaf(YType.uint64, 'in-multicast-pkts'), ['int'])),
                                    ('in_broadcast_pkts', (YLeaf(YType.uint64, 'in-broadcast-pkts'), ['int'])),
                                    ('out_ucast_pkts', (YLeaf(YType.uint64, 'out-ucast-pkts'), ['int'])),
                                    ('out_multicast_pkts', (YLeaf(YType.uint64, 'out-multicast-pkts'), ['int'])),
                                    ('out_broadcast_pkts', (YLeaf(YType.uint64, 'out-broadcast-pkts'), ['int'])),
                                    ('output_total_drops', (YLeaf(YType.uint32, 'output-total-drops'), ['int'])),
                                    ('input_total_drops', (YLeaf(YType.uint32, 'input-total-drops'), ['int'])),
                                    ('input_queue_drops', (YLeaf(YType.uint32, 'input-queue-drops'), ['int'])),
                                    ('input_unknown_proto', (YLeaf(YType.uint32, 'input-unknown-proto'), ['int'])),
                                    ('output_total_errors', (YLeaf(YType.uint32, 'output-total-errors'), ['int'])),
                                    ('output_underrun', (YLeaf(YType.uint32, 'output-underrun'), ['int'])),
                                    ('input_total_errors', (YLeaf(YType.uint32, 'input-total-errors'), ['int'])),
                                    ('input_crc', (YLeaf(YType.uint32, 'input-crc'), ['int'])),
                                    ('input_overrun', (YLeaf(YType.uint32, 'input-overrun'), ['int'])),
                                    ('input_frame', (YLeaf(YType.uint32, 'input-frame'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.in_packets = None
                                self.in_octets = None
                                self.out_packets = None
                                self.out_octets = None
                                self.in_ucast_pkts = None
                                self.in_multicast_pkts = None
                                self.in_broadcast_pkts = None
                                self.out_ucast_pkts = None
                                self.out_multicast_pkts = None
                                self.out_broadcast_pkts = None
                                self.output_total_drops = None
                                self.input_total_drops = None
                                self.input_queue_drops = None
                                self.input_unknown_proto = None
                                self.output_total_errors = None
                                self.output_underrun = None
                                self.input_total_errors = None
                                self.input_crc = None
                                self.input_overrun = None
                                self.input_frame = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, ['sample_id', 'time_stamp', 'in_packets', 'in_octets', 'out_packets', 'out_octets', 'in_ucast_pkts', 'in_multicast_pkts', 'in_broadcast_pkts', 'out_ucast_pkts', 'out_multicast_pkts', 'out_broadcast_pkts', 'output_total_drops', 'input_total_drops', 'input_queue_drops', 'input_unknown_proto', 'output_total_errors', 'output_underrun', 'input_total_errors', 'input_crc', 'input_overrun', 'input_frame'], name, value)


            class BasicCounterInterfaces(Entity):
                """
                Interfaces for which Basic Counters are
                collected
                
                .. attribute:: basic_counter_interface
                
                	Samples for a particular interface
                	**type**\: list of  		 :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces, self).__init__()

                    self.yang_name = "basic-counter-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("basic-counter-interface", ("basic_counter_interface", PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface))])
                    self._leafs = OrderedDict()

                    self.basic_counter_interface = YList(self)
                    self._segment_path = lambda: "basic-counter-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces, [], name, value)


                class BasicCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: samples
                    
                    	Basic Counter samples for an interface
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__init__()

                        self.yang_name = "basic-counter-interface"
                        self.yang_parent_name = "basic-counter-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.samples = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "basic-counter-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/basic-counter-interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Basic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Basic Counters sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "basic-counter-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Basic Counters sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds from UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: in_packets
                            
                            	Packets received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: in_octets
                            
                            	Bytes received
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: out_packets
                            
                            	Packets sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: out_octets
                            
                            	Bytes sent
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: input_total_drops
                            
                            	Inbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_queue_drops
                            
                            	Input queue drops
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: input_total_errors
                            
                            	Inbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_drops
                            
                            	Outbound correct packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_queue_drops
                            
                            	Output queue drops
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: output_total_errors
                            
                            	Outbound incorrect packets discarded
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('in_packets', (YLeaf(YType.uint64, 'in-packets'), ['int'])),
                                    ('in_octets', (YLeaf(YType.uint64, 'in-octets'), ['int'])),
                                    ('out_packets', (YLeaf(YType.uint64, 'out-packets'), ['int'])),
                                    ('out_octets', (YLeaf(YType.uint64, 'out-octets'), ['int'])),
                                    ('input_total_drops', (YLeaf(YType.uint64, 'input-total-drops'), ['int'])),
                                    ('input_queue_drops', (YLeaf(YType.uint64, 'input-queue-drops'), ['int'])),
                                    ('input_total_errors', (YLeaf(YType.uint64, 'input-total-errors'), ['int'])),
                                    ('output_total_drops', (YLeaf(YType.uint64, 'output-total-drops'), ['int'])),
                                    ('output_queue_drops', (YLeaf(YType.uint64, 'output-queue-drops'), ['int'])),
                                    ('output_total_errors', (YLeaf(YType.uint64, 'output-total-errors'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.in_packets = None
                                self.in_octets = None
                                self.out_packets = None
                                self.out_octets = None
                                self.input_total_drops = None
                                self.input_queue_drops = None
                                self.input_total_errors = None
                                self.output_total_drops = None
                                self.output_queue_drops = None
                                self.output_total_errors = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, ['sample_id', 'time_stamp', 'in_packets', 'in_octets', 'out_packets', 'out_octets', 'input_total_drops', 'input_queue_drops', 'input_total_errors', 'output_total_drops', 'output_queue_drops', 'output_total_errors'], name, value)


            class DataRateInterfaces(Entity):
                """
                Interfaces for which Data Rates are collected
                
                .. attribute:: data_rate_interface
                
                	Samples for a particular interface
                	**type**\: list of  		 :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Monitor.Interface.DataRateInterfaces, self).__init__()

                    self.yang_name = "data-rate-interfaces"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("data-rate-interface", ("data_rate_interface", PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface))])
                    self._leafs = OrderedDict()

                    self.data_rate_interface = YList(self)
                    self._segment_path = lambda: "data-rate-interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces, [], name, value)


                class DataRateInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface Name
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: samples
                    
                    	Data Rate samples for an interface
                    	**type**\:  :py:class:`Samples <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface, self).__init__()

                        self.yang_name = "data-rate-interface"
                        self.yang_parent_name = "data-rate-interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("samples", ("samples", PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                        ])
                        self.interface_name = None

                        self.samples = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._segment_path = lambda: "data-rate-interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/data-rate-interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface, ['interface_name'], name, value)


                    class Samples(Entity):
                        """
                        Data Rate samples for an interface
                        
                        .. attribute:: sample
                        
                        	Data Rates sample
                        	**type**\: list of  		 :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__init__()

                            self.yang_name = "samples"
                            self.yang_parent_name = "data-rate-interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("sample", ("sample", PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample))])
                            self._leafs = OrderedDict()

                            self.sample = YList(self)
                            self._segment_path = lambda: "samples"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples, [], name, value)


                        class Sample(Entity):
                            """
                            Data Rates sample
                            
                            .. attribute:: sample_id  (key)
                            
                            	Sample ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: time_stamp
                            
                            	Timestamp of sample in seconds drom UCT
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: second
                            
                            .. attribute:: input_data_rate
                            
                            	Input datarate in 1000's of bps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: input_packet_rate
                            
                            	Input packets per second
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: output_data_rate
                            
                            	Output datarate in 1000's of bps
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: bit/s
                            
                            .. attribute:: output_packet_rate
                            
                            	Output packets per second
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: packet/s
                            
                            .. attribute:: input_peak_rate
                            
                            	Peak input datarate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: input_peak_pkts
                            
                            	Peak input packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_peak_rate
                            
                            	Peak output datarate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: output_peak_pkts
                            
                            	Peak output packet rate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bandwidth
                            
                            	Bandwidth (in kbps)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: kbit/s
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__init__()

                                self.yang_name = "sample"
                                self.yang_parent_name = "samples"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['sample_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sample_id', (YLeaf(YType.uint32, 'sample-id'), ['int'])),
                                    ('time_stamp', (YLeaf(YType.uint64, 'time-stamp'), ['int'])),
                                    ('input_data_rate', (YLeaf(YType.uint32, 'input-data-rate'), ['int'])),
                                    ('input_packet_rate', (YLeaf(YType.uint32, 'input-packet-rate'), ['int'])),
                                    ('output_data_rate', (YLeaf(YType.uint32, 'output-data-rate'), ['int'])),
                                    ('output_packet_rate', (YLeaf(YType.uint32, 'output-packet-rate'), ['int'])),
                                    ('input_peak_rate', (YLeaf(YType.uint32, 'input-peak-rate'), ['int'])),
                                    ('input_peak_pkts', (YLeaf(YType.uint32, 'input-peak-pkts'), ['int'])),
                                    ('output_peak_rate', (YLeaf(YType.uint32, 'output-peak-rate'), ['int'])),
                                    ('output_peak_pkts', (YLeaf(YType.uint32, 'output-peak-pkts'), ['int'])),
                                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                ])
                                self.sample_id = None
                                self.time_stamp = None
                                self.input_data_rate = None
                                self.input_packet_rate = None
                                self.output_data_rate = None
                                self.output_packet_rate = None
                                self.input_peak_rate = None
                                self.input_peak_pkts = None
                                self.output_peak_rate = None
                                self.output_peak_pkts = None
                                self.bandwidth = None
                                self._segment_path = lambda: "sample" + "[sample-id='" + str(self.sample_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, ['sample_id', 'time_stamp', 'input_data_rate', 'input_packet_rate', 'output_data_rate', 'output_packet_rate', 'input_peak_rate', 'input_peak_pkts', 'output_peak_rate', 'output_peak_pkts', 'bandwidth'], name, value)

    def clone_ptr(self):
        self._top_entity = PerfMgmt()
        return self._top_entity

