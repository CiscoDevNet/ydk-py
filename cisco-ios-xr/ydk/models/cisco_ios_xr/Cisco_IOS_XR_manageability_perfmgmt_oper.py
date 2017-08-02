""" Cisco_IOS_XR_manageability_perfmgmt_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-perfmgmt package operational data.

This module contains definitions
for the following management objects\:
  perf\-mgmt\: Performance Management agent operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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

        self.monitor = PerfMgmt.Monitor()
        self.monitor.parent = self
        self._children_name_map["monitor"] = "monitor"
        self._children_yang_names.add("monitor")

        self.periodic = PerfMgmt.Periodic()
        self.periodic.parent = self
        self._children_name_map["periodic"] = "periodic"
        self._children_yang_names.add("periodic")


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

                self.ospfv2_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"
                self._children_yang_names.add("ospfv2-protocol-instances")

                self.ospfv3_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self
                self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                self._children_yang_names.add("ospfv3-protocol-instances")


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

                    self.ospfv2_protocol_instance = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances, self).__setattr__(name, value)


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

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("instance_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "checksum_errors",
                                                "input_db_ds",
                                                "input_db_ds_lsa",
                                                "input_hello_packets",
                                                "input_ls_requests",
                                                "input_ls_requests_lsa",
                                                "input_lsa_acks",
                                                "input_lsa_acks_lsa",
                                                "input_lsa_updates",
                                                "input_lsa_updates_lsa",
                                                "input_packets",
                                                "output_db_ds",
                                                "output_db_ds_lsa",
                                                "output_hello_packets",
                                                "output_ls_requests",
                                                "output_ls_requests_lsa",
                                                "output_lsa_acks",
                                                "output_lsa_acks_lsa",
                                                "output_lsa_updates",
                                                "output_lsa_updates_lsa",
                                                "output_packets",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.checksum_errors.is_set or
                                    self.input_db_ds.is_set or
                                    self.input_db_ds_lsa.is_set or
                                    self.input_hello_packets.is_set or
                                    self.input_ls_requests.is_set or
                                    self.input_ls_requests_lsa.is_set or
                                    self.input_lsa_acks.is_set or
                                    self.input_lsa_acks_lsa.is_set or
                                    self.input_lsa_updates.is_set or
                                    self.input_lsa_updates_lsa.is_set or
                                    self.input_packets.is_set or
                                    self.output_db_ds.is_set or
                                    self.output_db_ds_lsa.is_set or
                                    self.output_hello_packets.is_set or
                                    self.output_ls_requests.is_set or
                                    self.output_ls_requests_lsa.is_set or
                                    self.output_lsa_acks.is_set or
                                    self.output_lsa_acks_lsa.is_set or
                                    self.output_lsa_updates.is_set or
                                    self.output_lsa_updates_lsa.is_set or
                                    self.output_packets.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.checksum_errors.yfilter != YFilter.not_set or
                                    self.input_db_ds.yfilter != YFilter.not_set or
                                    self.input_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.input_hello_packets.yfilter != YFilter.not_set or
                                    self.input_ls_requests.yfilter != YFilter.not_set or
                                    self.input_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_acks.yfilter != YFilter.not_set or
                                    self.input_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_updates.yfilter != YFilter.not_set or
                                    self.input_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.input_packets.yfilter != YFilter.not_set or
                                    self.output_db_ds.yfilter != YFilter.not_set or
                                    self.output_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.output_hello_packets.yfilter != YFilter.not_set or
                                    self.output_ls_requests.yfilter != YFilter.not_set or
                                    self.output_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_acks.yfilter != YFilter.not_set or
                                    self.output_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_updates.yfilter != YFilter.not_set or
                                    self.output_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.output_packets.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.checksum_errors.is_set or self.checksum_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.checksum_errors.get_name_leafdata())
                                if (self.input_db_ds.is_set or self.input_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds.get_name_leafdata())
                                if (self.input_db_ds_lsa.is_set or self.input_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds_lsa.get_name_leafdata())
                                if (self.input_hello_packets.is_set or self.input_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_hello_packets.get_name_leafdata())
                                if (self.input_ls_requests.is_set or self.input_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests.get_name_leafdata())
                                if (self.input_ls_requests_lsa.is_set or self.input_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests_lsa.get_name_leafdata())
                                if (self.input_lsa_acks.is_set or self.input_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks.get_name_leafdata())
                                if (self.input_lsa_acks_lsa.is_set or self.input_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks_lsa.get_name_leafdata())
                                if (self.input_lsa_updates.is_set or self.input_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates.get_name_leafdata())
                                if (self.input_lsa_updates_lsa.is_set or self.input_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates_lsa.get_name_leafdata())
                                if (self.input_packets.is_set or self.input_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_packets.get_name_leafdata())
                                if (self.output_db_ds.is_set or self.output_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds.get_name_leafdata())
                                if (self.output_db_ds_lsa.is_set or self.output_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds_lsa.get_name_leafdata())
                                if (self.output_hello_packets.is_set or self.output_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_hello_packets.get_name_leafdata())
                                if (self.output_ls_requests.is_set or self.output_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests.get_name_leafdata())
                                if (self.output_ls_requests_lsa.is_set or self.output_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests_lsa.get_name_leafdata())
                                if (self.output_lsa_acks.is_set or self.output_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks.get_name_leafdata())
                                if (self.output_lsa_acks_lsa.is_set or self.output_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks_lsa.get_name_leafdata())
                                if (self.output_lsa_updates.is_set or self.output_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates.get_name_leafdata())
                                if (self.output_lsa_updates_lsa.is_set or self.output_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates_lsa.get_name_leafdata())
                                if (self.output_packets.is_set or self.output_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_packets.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "checksum-errors" or name == "input-db-ds" or name == "input-db-ds-lsa" or name == "input-hello-packets" or name == "input-ls-requests" or name == "input-ls-requests-lsa" or name == "input-lsa-acks" or name == "input-lsa-acks-lsa" or name == "input-lsa-updates" or name == "input-lsa-updates-lsa" or name == "input-packets" or name == "output-db-ds" or name == "output-db-ds-lsa" or name == "output-hello-packets" or name == "output-ls-requests" or name == "output-ls-requests-lsa" or name == "output-lsa-acks" or name == "output-lsa-acks-lsa" or name == "output-lsa-updates" or name == "output-lsa-updates-lsa" or name == "output-packets" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "checksum-errors"):
                                    self.checksum_errors = value
                                    self.checksum_errors.value_namespace = name_space
                                    self.checksum_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds"):
                                    self.input_db_ds = value
                                    self.input_db_ds.value_namespace = name_space
                                    self.input_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds-lsa"):
                                    self.input_db_ds_lsa = value
                                    self.input_db_ds_lsa.value_namespace = name_space
                                    self.input_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-hello-packets"):
                                    self.input_hello_packets = value
                                    self.input_hello_packets.value_namespace = name_space
                                    self.input_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests"):
                                    self.input_ls_requests = value
                                    self.input_ls_requests.value_namespace = name_space
                                    self.input_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests-lsa"):
                                    self.input_ls_requests_lsa = value
                                    self.input_ls_requests_lsa.value_namespace = name_space
                                    self.input_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks"):
                                    self.input_lsa_acks = value
                                    self.input_lsa_acks.value_namespace = name_space
                                    self.input_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks-lsa"):
                                    self.input_lsa_acks_lsa = value
                                    self.input_lsa_acks_lsa.value_namespace = name_space
                                    self.input_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates"):
                                    self.input_lsa_updates = value
                                    self.input_lsa_updates.value_namespace = name_space
                                    self.input_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates-lsa"):
                                    self.input_lsa_updates_lsa = value
                                    self.input_lsa_updates_lsa.value_namespace = name_space
                                    self.input_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-packets"):
                                    self.input_packets = value
                                    self.input_packets.value_namespace = name_space
                                    self.input_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds"):
                                    self.output_db_ds = value
                                    self.output_db_ds.value_namespace = name_space
                                    self.output_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds-lsa"):
                                    self.output_db_ds_lsa = value
                                    self.output_db_ds_lsa.value_namespace = name_space
                                    self.output_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-hello-packets"):
                                    self.output_hello_packets = value
                                    self.output_hello_packets.value_namespace = name_space
                                    self.output_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests"):
                                    self.output_ls_requests = value
                                    self.output_ls_requests.value_namespace = name_space
                                    self.output_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests-lsa"):
                                    self.output_ls_requests_lsa = value
                                    self.output_ls_requests_lsa.value_namespace = name_space
                                    self.output_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks"):
                                    self.output_lsa_acks = value
                                    self.output_lsa_acks.value_namespace = name_space
                                    self.output_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks-lsa"):
                                    self.output_lsa_acks_lsa = value
                                    self.output_lsa_acks_lsa.value_namespace = name_space
                                    self.output_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates"):
                                    self.output_lsa_updates = value
                                    self.output_lsa_updates.value_namespace = name_space
                                    self.output_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates-lsa"):
                                    self.output_lsa_updates_lsa = value
                                    self.output_lsa_updates_lsa.value_namespace = name_space
                                    self.output_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-packets"):
                                    self.output_packets = value
                                    self.output_packets.value_namespace = name_space
                                    self.output_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.instance_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.instance_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ospfv2-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/ospfv2-protocol-instances/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.instance_name.is_set or self.instance_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instance_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "instance-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "instance-name"):
                            self.instance_name = value
                            self.instance_name.value_namespace = name_space
                            self.instance_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ospfv2_protocol_instance:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ospfv2_protocol_instance:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ospfv2-protocol-instances" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ospfv2-protocol-instance"):
                        for c in self.ospfv2_protocol_instance:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ospfv2_protocol_instance.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ospfv2-protocol-instance"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.ospfv3_protocol_instance = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances, self).__setattr__(name, value)


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

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("instance_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "input_db_ds",
                                                "input_db_ds_lsa",
                                                "input_hello_packets",
                                                "input_ls_requests",
                                                "input_ls_requests_lsa",
                                                "input_lsa_acks",
                                                "input_lsa_acks_lsa",
                                                "input_lsa_updates",
                                                "input_lsa_updates_lsa",
                                                "input_packets",
                                                "output_db_ds",
                                                "output_db_ds_lsa",
                                                "output_hello_packets",
                                                "output_ls_requests",
                                                "output_ls_requests_lsa",
                                                "output_lsa_acks",
                                                "output_lsa_acks_lsa",
                                                "output_lsa_updates",
                                                "output_lsa_updates_lsa",
                                                "output_packets",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.input_db_ds.is_set or
                                    self.input_db_ds_lsa.is_set or
                                    self.input_hello_packets.is_set or
                                    self.input_ls_requests.is_set or
                                    self.input_ls_requests_lsa.is_set or
                                    self.input_lsa_acks.is_set or
                                    self.input_lsa_acks_lsa.is_set or
                                    self.input_lsa_updates.is_set or
                                    self.input_lsa_updates_lsa.is_set or
                                    self.input_packets.is_set or
                                    self.output_db_ds.is_set or
                                    self.output_db_ds_lsa.is_set or
                                    self.output_hello_packets.is_set or
                                    self.output_ls_requests.is_set or
                                    self.output_ls_requests_lsa.is_set or
                                    self.output_lsa_acks.is_set or
                                    self.output_lsa_acks_lsa.is_set or
                                    self.output_lsa_updates.is_set or
                                    self.output_lsa_updates_lsa.is_set or
                                    self.output_packets.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.input_db_ds.yfilter != YFilter.not_set or
                                    self.input_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.input_hello_packets.yfilter != YFilter.not_set or
                                    self.input_ls_requests.yfilter != YFilter.not_set or
                                    self.input_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_acks.yfilter != YFilter.not_set or
                                    self.input_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_updates.yfilter != YFilter.not_set or
                                    self.input_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.input_packets.yfilter != YFilter.not_set or
                                    self.output_db_ds.yfilter != YFilter.not_set or
                                    self.output_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.output_hello_packets.yfilter != YFilter.not_set or
                                    self.output_ls_requests.yfilter != YFilter.not_set or
                                    self.output_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_acks.yfilter != YFilter.not_set or
                                    self.output_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_updates.yfilter != YFilter.not_set or
                                    self.output_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.output_packets.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.input_db_ds.is_set or self.input_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds.get_name_leafdata())
                                if (self.input_db_ds_lsa.is_set or self.input_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds_lsa.get_name_leafdata())
                                if (self.input_hello_packets.is_set or self.input_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_hello_packets.get_name_leafdata())
                                if (self.input_ls_requests.is_set or self.input_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests.get_name_leafdata())
                                if (self.input_ls_requests_lsa.is_set or self.input_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests_lsa.get_name_leafdata())
                                if (self.input_lsa_acks.is_set or self.input_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks.get_name_leafdata())
                                if (self.input_lsa_acks_lsa.is_set or self.input_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks_lsa.get_name_leafdata())
                                if (self.input_lsa_updates.is_set or self.input_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates.get_name_leafdata())
                                if (self.input_lsa_updates_lsa.is_set or self.input_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates_lsa.get_name_leafdata())
                                if (self.input_packets.is_set or self.input_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_packets.get_name_leafdata())
                                if (self.output_db_ds.is_set or self.output_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds.get_name_leafdata())
                                if (self.output_db_ds_lsa.is_set or self.output_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds_lsa.get_name_leafdata())
                                if (self.output_hello_packets.is_set or self.output_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_hello_packets.get_name_leafdata())
                                if (self.output_ls_requests.is_set or self.output_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests.get_name_leafdata())
                                if (self.output_ls_requests_lsa.is_set or self.output_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests_lsa.get_name_leafdata())
                                if (self.output_lsa_acks.is_set or self.output_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks.get_name_leafdata())
                                if (self.output_lsa_acks_lsa.is_set or self.output_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks_lsa.get_name_leafdata())
                                if (self.output_lsa_updates.is_set or self.output_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates.get_name_leafdata())
                                if (self.output_lsa_updates_lsa.is_set or self.output_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates_lsa.get_name_leafdata())
                                if (self.output_packets.is_set or self.output_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_packets.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "input-db-ds" or name == "input-db-ds-lsa" or name == "input-hello-packets" or name == "input-ls-requests" or name == "input-ls-requests-lsa" or name == "input-lsa-acks" or name == "input-lsa-acks-lsa" or name == "input-lsa-updates" or name == "input-lsa-updates-lsa" or name == "input-packets" or name == "output-db-ds" or name == "output-db-ds-lsa" or name == "output-hello-packets" or name == "output-ls-requests" or name == "output-ls-requests-lsa" or name == "output-lsa-acks" or name == "output-lsa-acks-lsa" or name == "output-lsa-updates" or name == "output-lsa-updates-lsa" or name == "output-packets" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds"):
                                    self.input_db_ds = value
                                    self.input_db_ds.value_namespace = name_space
                                    self.input_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds-lsa"):
                                    self.input_db_ds_lsa = value
                                    self.input_db_ds_lsa.value_namespace = name_space
                                    self.input_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-hello-packets"):
                                    self.input_hello_packets = value
                                    self.input_hello_packets.value_namespace = name_space
                                    self.input_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests"):
                                    self.input_ls_requests = value
                                    self.input_ls_requests.value_namespace = name_space
                                    self.input_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests-lsa"):
                                    self.input_ls_requests_lsa = value
                                    self.input_ls_requests_lsa.value_namespace = name_space
                                    self.input_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks"):
                                    self.input_lsa_acks = value
                                    self.input_lsa_acks.value_namespace = name_space
                                    self.input_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks-lsa"):
                                    self.input_lsa_acks_lsa = value
                                    self.input_lsa_acks_lsa.value_namespace = name_space
                                    self.input_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates"):
                                    self.input_lsa_updates = value
                                    self.input_lsa_updates.value_namespace = name_space
                                    self.input_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates-lsa"):
                                    self.input_lsa_updates_lsa = value
                                    self.input_lsa_updates_lsa.value_namespace = name_space
                                    self.input_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-packets"):
                                    self.input_packets = value
                                    self.input_packets.value_namespace = name_space
                                    self.input_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds"):
                                    self.output_db_ds = value
                                    self.output_db_ds.value_namespace = name_space
                                    self.output_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds-lsa"):
                                    self.output_db_ds_lsa = value
                                    self.output_db_ds_lsa.value_namespace = name_space
                                    self.output_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-hello-packets"):
                                    self.output_hello_packets = value
                                    self.output_hello_packets.value_namespace = name_space
                                    self.output_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests"):
                                    self.output_ls_requests = value
                                    self.output_ls_requests.value_namespace = name_space
                                    self.output_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests-lsa"):
                                    self.output_ls_requests_lsa = value
                                    self.output_ls_requests_lsa.value_namespace = name_space
                                    self.output_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks"):
                                    self.output_lsa_acks = value
                                    self.output_lsa_acks.value_namespace = name_space
                                    self.output_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks-lsa"):
                                    self.output_lsa_acks_lsa = value
                                    self.output_lsa_acks_lsa.value_namespace = name_space
                                    self.output_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates"):
                                    self.output_lsa_updates = value
                                    self.output_lsa_updates.value_namespace = name_space
                                    self.output_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates-lsa"):
                                    self.output_lsa_updates_lsa = value
                                    self.output_lsa_updates_lsa.value_namespace = name_space
                                    self.output_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-packets"):
                                    self.output_packets = value
                                    self.output_packets.value_namespace = name_space
                                    self.output_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.instance_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.instance_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ospfv3-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/ospfv3-protocol-instances/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.instance_name.is_set or self.instance_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instance_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "instance-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "instance-name"):
                            self.instance_name = value
                            self.instance_name.value_namespace = name_space
                            self.instance_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ospfv3_protocol_instance:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ospfv3_protocol_instance:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ospfv3-protocol-instances" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/ospf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ospfv3-protocol-instance"):
                        for c in self.ospfv3_protocol_instance:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ospfv3_protocol_instance.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ospfv3-protocol-instance"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.ospfv2_protocol_instances is not None and self.ospfv2_protocol_instances.has_data()) or
                    (self.ospfv3_protocol_instances is not None and self.ospfv3_protocol_instances.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ospfv2_protocol_instances is not None and self.ospfv2_protocol_instances.has_operation()) or
                    (self.ospfv3_protocol_instances is not None and self.ospfv3_protocol_instances.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ospfv2-protocol-instances"):
                    if (self.ospfv2_protocol_instances is None):
                        self.ospfv2_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances()
                        self.ospfv2_protocol_instances.parent = self
                        self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"
                    return self.ospfv2_protocol_instances

                if (child_yang_name == "ospfv3-protocol-instances"):
                    if (self.ospfv3_protocol_instances is None):
                        self.ospfv3_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances()
                        self.ospfv3_protocol_instances.parent = self
                        self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                    return self.ospfv3_protocol_instances

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfv2-protocol-instances" or name == "ospfv3-protocol-instances"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.ldp_neighbors = PerfMgmt.Periodic.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self
                self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                self._children_yang_names.add("ldp-neighbors")


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

                    self.ldp_neighbor = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Mpls.LdpNeighbors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Mpls.LdpNeighbors, self).__setattr__(name, value)


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

                        self.nbr = YLeaf(YType.str, "nbr")

                        self.samples = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nbr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "address_msgs_rcvd",
                                                "address_msgs_sent",
                                                "address_withdraw_msgs_rcvd",
                                                "address_withdraw_msgs_sent",
                                                "init_msgs_rcvd",
                                                "init_msgs_sent",
                                                "keepalive_msgs_rcvd",
                                                "keepalive_msgs_sent",
                                                "label_mapping_msgs_rcvd",
                                                "label_mapping_msgs_sent",
                                                "label_release_msgs_rcvd",
                                                "label_release_msgs_sent",
                                                "label_withdraw_msgs_rcvd",
                                                "label_withdraw_msgs_sent",
                                                "notification_msgs_rcvd",
                                                "notification_msgs_sent",
                                                "time_stamp",
                                                "total_msgs_rcvd",
                                                "total_msgs_sent") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.address_msgs_rcvd.is_set or
                                    self.address_msgs_sent.is_set or
                                    self.address_withdraw_msgs_rcvd.is_set or
                                    self.address_withdraw_msgs_sent.is_set or
                                    self.init_msgs_rcvd.is_set or
                                    self.init_msgs_sent.is_set or
                                    self.keepalive_msgs_rcvd.is_set or
                                    self.keepalive_msgs_sent.is_set or
                                    self.label_mapping_msgs_rcvd.is_set or
                                    self.label_mapping_msgs_sent.is_set or
                                    self.label_release_msgs_rcvd.is_set or
                                    self.label_release_msgs_sent.is_set or
                                    self.label_withdraw_msgs_rcvd.is_set or
                                    self.label_withdraw_msgs_sent.is_set or
                                    self.notification_msgs_rcvd.is_set or
                                    self.notification_msgs_sent.is_set or
                                    self.time_stamp.is_set or
                                    self.total_msgs_rcvd.is_set or
                                    self.total_msgs_sent.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.address_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.address_msgs_sent.yfilter != YFilter.not_set or
                                    self.address_withdraw_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.address_withdraw_msgs_sent.yfilter != YFilter.not_set or
                                    self.init_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.init_msgs_sent.yfilter != YFilter.not_set or
                                    self.keepalive_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.keepalive_msgs_sent.yfilter != YFilter.not_set or
                                    self.label_mapping_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.label_mapping_msgs_sent.yfilter != YFilter.not_set or
                                    self.label_release_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.label_release_msgs_sent.yfilter != YFilter.not_set or
                                    self.label_withdraw_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.label_withdraw_msgs_sent.yfilter != YFilter.not_set or
                                    self.notification_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.notification_msgs_sent.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set or
                                    self.total_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.total_msgs_sent.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.address_msgs_rcvd.is_set or self.address_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_msgs_rcvd.get_name_leafdata())
                                if (self.address_msgs_sent.is_set or self.address_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_msgs_sent.get_name_leafdata())
                                if (self.address_withdraw_msgs_rcvd.is_set or self.address_withdraw_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_withdraw_msgs_rcvd.get_name_leafdata())
                                if (self.address_withdraw_msgs_sent.is_set or self.address_withdraw_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_withdraw_msgs_sent.get_name_leafdata())
                                if (self.init_msgs_rcvd.is_set or self.init_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.init_msgs_rcvd.get_name_leafdata())
                                if (self.init_msgs_sent.is_set or self.init_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.init_msgs_sent.get_name_leafdata())
                                if (self.keepalive_msgs_rcvd.is_set or self.keepalive_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.keepalive_msgs_rcvd.get_name_leafdata())
                                if (self.keepalive_msgs_sent.is_set or self.keepalive_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.keepalive_msgs_sent.get_name_leafdata())
                                if (self.label_mapping_msgs_rcvd.is_set or self.label_mapping_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_mapping_msgs_rcvd.get_name_leafdata())
                                if (self.label_mapping_msgs_sent.is_set or self.label_mapping_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_mapping_msgs_sent.get_name_leafdata())
                                if (self.label_release_msgs_rcvd.is_set or self.label_release_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_release_msgs_rcvd.get_name_leafdata())
                                if (self.label_release_msgs_sent.is_set or self.label_release_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_release_msgs_sent.get_name_leafdata())
                                if (self.label_withdraw_msgs_rcvd.is_set or self.label_withdraw_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_withdraw_msgs_rcvd.get_name_leafdata())
                                if (self.label_withdraw_msgs_sent.is_set or self.label_withdraw_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_withdraw_msgs_sent.get_name_leafdata())
                                if (self.notification_msgs_rcvd.is_set or self.notification_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.notification_msgs_rcvd.get_name_leafdata())
                                if (self.notification_msgs_sent.is_set or self.notification_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.notification_msgs_sent.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())
                                if (self.total_msgs_rcvd.is_set or self.total_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_msgs_rcvd.get_name_leafdata())
                                if (self.total_msgs_sent.is_set or self.total_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_msgs_sent.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "address-msgs-rcvd" or name == "address-msgs-sent" or name == "address-withdraw-msgs-rcvd" or name == "address-withdraw-msgs-sent" or name == "init-msgs-rcvd" or name == "init-msgs-sent" or name == "keepalive-msgs-rcvd" or name == "keepalive-msgs-sent" or name == "label-mapping-msgs-rcvd" or name == "label-mapping-msgs-sent" or name == "label-release-msgs-rcvd" or name == "label-release-msgs-sent" or name == "label-withdraw-msgs-rcvd" or name == "label-withdraw-msgs-sent" or name == "notification-msgs-rcvd" or name == "notification-msgs-sent" or name == "time-stamp" or name == "total-msgs-rcvd" or name == "total-msgs-sent"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-msgs-rcvd"):
                                    self.address_msgs_rcvd = value
                                    self.address_msgs_rcvd.value_namespace = name_space
                                    self.address_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-msgs-sent"):
                                    self.address_msgs_sent = value
                                    self.address_msgs_sent.value_namespace = name_space
                                    self.address_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-withdraw-msgs-rcvd"):
                                    self.address_withdraw_msgs_rcvd = value
                                    self.address_withdraw_msgs_rcvd.value_namespace = name_space
                                    self.address_withdraw_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-withdraw-msgs-sent"):
                                    self.address_withdraw_msgs_sent = value
                                    self.address_withdraw_msgs_sent.value_namespace = name_space
                                    self.address_withdraw_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "init-msgs-rcvd"):
                                    self.init_msgs_rcvd = value
                                    self.init_msgs_rcvd.value_namespace = name_space
                                    self.init_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "init-msgs-sent"):
                                    self.init_msgs_sent = value
                                    self.init_msgs_sent.value_namespace = name_space
                                    self.init_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "keepalive-msgs-rcvd"):
                                    self.keepalive_msgs_rcvd = value
                                    self.keepalive_msgs_rcvd.value_namespace = name_space
                                    self.keepalive_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "keepalive-msgs-sent"):
                                    self.keepalive_msgs_sent = value
                                    self.keepalive_msgs_sent.value_namespace = name_space
                                    self.keepalive_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-mapping-msgs-rcvd"):
                                    self.label_mapping_msgs_rcvd = value
                                    self.label_mapping_msgs_rcvd.value_namespace = name_space
                                    self.label_mapping_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-mapping-msgs-sent"):
                                    self.label_mapping_msgs_sent = value
                                    self.label_mapping_msgs_sent.value_namespace = name_space
                                    self.label_mapping_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-release-msgs-rcvd"):
                                    self.label_release_msgs_rcvd = value
                                    self.label_release_msgs_rcvd.value_namespace = name_space
                                    self.label_release_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-release-msgs-sent"):
                                    self.label_release_msgs_sent = value
                                    self.label_release_msgs_sent.value_namespace = name_space
                                    self.label_release_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-withdraw-msgs-rcvd"):
                                    self.label_withdraw_msgs_rcvd = value
                                    self.label_withdraw_msgs_rcvd.value_namespace = name_space
                                    self.label_withdraw_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-withdraw-msgs-sent"):
                                    self.label_withdraw_msgs_sent = value
                                    self.label_withdraw_msgs_sent.value_namespace = name_space
                                    self.label_withdraw_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "notification-msgs-rcvd"):
                                    self.notification_msgs_rcvd = value
                                    self.notification_msgs_rcvd.value_namespace = name_space
                                    self.notification_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "notification-msgs-sent"):
                                    self.notification_msgs_sent = value
                                    self.notification_msgs_sent.value_namespace = name_space
                                    self.notification_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-msgs-rcvd"):
                                    self.total_msgs_rcvd = value
                                    self.total_msgs_rcvd.value_namespace = name_space
                                    self.total_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-msgs-sent"):
                                    self.total_msgs_sent = value
                                    self.total_msgs_sent.value_namespace = name_space
                                    self.total_msgs_sent.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.nbr.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nbr.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ldp-neighbor" + "[nbr='" + self.nbr.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/mpls/ldp-neighbors/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nbr.is_set or self.nbr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nbr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "nbr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nbr"):
                            self.nbr = value
                            self.nbr.value_namespace = name_space
                            self.nbr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ldp_neighbor:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ldp_neighbor:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ldp-neighbors" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/mpls/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ldp-neighbor"):
                        for c in self.ldp_neighbor:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ldp_neighbor.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ldp-neighbor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.ldp_neighbors is not None and self.ldp_neighbors.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ldp_neighbors is not None and self.ldp_neighbors.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mpls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ldp-neighbors"):
                    if (self.ldp_neighbors is None):
                        self.ldp_neighbors = PerfMgmt.Periodic.Mpls.LdpNeighbors()
                        self.ldp_neighbors.parent = self
                        self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                    return self.ldp_neighbors

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ldp-neighbors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.node = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PerfMgmt.Periodic.Nodes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PerfMgmt.Periodic.Nodes, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("node_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Nodes.Node, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Nodes.Node, self).__setattr__(name, value)


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

                        self.sample = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Nodes.Node.SampleXr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Nodes.Node.SampleXr, self).__setattr__(name, value)


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

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                            self.no_processes = YLeaf(YType.uint32, "no-processes")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("sample_id",
                                            "average_cpu_used",
                                            "no_processes",
                                            "time_stamp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sample_id.is_set or
                                self.average_cpu_used.is_set or
                                self.no_processes.is_set or
                                self.time_stamp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sample_id.yfilter != YFilter.not_set or
                                self.average_cpu_used.yfilter != YFilter.not_set or
                                self.no_processes.yfilter != YFilter.not_set or
                                self.time_stamp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sample_id.get_name_leafdata())
                            if (self.average_cpu_used.is_set or self.average_cpu_used.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.average_cpu_used.get_name_leafdata())
                            if (self.no_processes.is_set or self.no_processes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_processes.get_name_leafdata())
                            if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample-id" or name == "average-cpu-used" or name == "no-processes" or name == "time-stamp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sample-id"):
                                self.sample_id = value
                                self.sample_id.value_namespace = name_space
                                self.sample_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "average-cpu-used"):
                                self.average_cpu_used = value
                                self.average_cpu_used.value_namespace = name_space
                                self.average_cpu_used.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-processes"):
                                self.no_processes = value
                                self.no_processes.value_namespace = name_space
                                self.no_processes.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-stamp"):
                                self.time_stamp = value
                                self.time_stamp.value_namespace = name_space
                                self.time_stamp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sample:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sample:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sample-xr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sample"):
                            for c in self.sample:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sample.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sample"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.process = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Nodes.Node.Processes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Nodes.Node.Processes, self).__setattr__(name, value)


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

                            self.process_id = YLeaf(YType.int32, "process-id")

                            self.samples = PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                            self._children_yang_names.add("samples")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("process_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Nodes.Node.Processes.Process, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Nodes.Node.Processes.Process, self).__setattr__(name, value)


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

                                self.sample = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples, self).__setattr__(name, value)


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

                                    self.sample_id = YLeaf(YType.int32, "sample-id")

                                    self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                                    self.no_threads = YLeaf(YType.uint32, "no-threads")

                                    self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                                    self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("sample_id",
                                                    "average_cpu_used",
                                                    "no_threads",
                                                    "peak_memory",
                                                    "time_stamp") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.sample_id.is_set or
                                        self.average_cpu_used.is_set or
                                        self.no_threads.is_set or
                                        self.peak_memory.is_set or
                                        self.time_stamp.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.sample_id.yfilter != YFilter.not_set or
                                        self.average_cpu_used.yfilter != YFilter.not_set or
                                        self.no_threads.yfilter != YFilter.not_set or
                                        self.peak_memory.yfilter != YFilter.not_set or
                                        self.time_stamp.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.sample_id.get_name_leafdata())
                                    if (self.average_cpu_used.is_set or self.average_cpu_used.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.average_cpu_used.get_name_leafdata())
                                    if (self.no_threads.is_set or self.no_threads.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.no_threads.get_name_leafdata())
                                    if (self.peak_memory.is_set or self.peak_memory.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peak_memory.get_name_leafdata())
                                    if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "sample-id" or name == "average-cpu-used" or name == "no-threads" or name == "peak-memory" or name == "time-stamp"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "sample-id"):
                                        self.sample_id = value
                                        self.sample_id.value_namespace = name_space
                                        self.sample_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "average-cpu-used"):
                                        self.average_cpu_used = value
                                        self.average_cpu_used.value_namespace = name_space
                                        self.average_cpu_used.value_namespace_prefix = name_space_prefix
                                    if(value_path == "no-threads"):
                                        self.no_threads = value
                                        self.no_threads.value_namespace = name_space
                                        self.no_threads.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peak-memory"):
                                        self.peak_memory = value
                                        self.peak_memory.value_namespace = name_space
                                        self.peak_memory.value_namespace_prefix = name_space_prefix
                                    if(value_path == "time-stamp"):
                                        self.time_stamp = value
                                        self.time_stamp.value_namespace = name_space
                                        self.time_stamp.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.sample:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.sample:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "samples" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "sample"):
                                    for c in self.sample:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.sample.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.process_id.is_set or
                                (self.samples is not None and self.samples.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.process_id.yfilter != YFilter.not_set or
                                (self.samples is not None and self.samples.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "process" + "[process-id='" + self.process_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.process_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "samples"):
                                if (self.samples is None):
                                    self.samples = PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples()
                                    self.samples.parent = self
                                    self._children_name_map["samples"] = "samples"
                                return self.samples

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "samples" or name == "process-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "process-id"):
                                self.process_id = value
                                self.process_id.value_namespace = name_space
                                self.process_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.process:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.process:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "processes" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "process"):
                            for c in self.process:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PerfMgmt.Periodic.Nodes.Node.Processes.Process()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.process.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "process"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.sample = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Nodes.Node.Samples, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Nodes.Node.Samples, self).__setattr__(name, value)


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

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.curr_memory = YLeaf(YType.uint32, "curr-memory")

                            self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("sample_id",
                                            "curr_memory",
                                            "peak_memory",
                                            "time_stamp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Nodes.Node.Samples.Sample, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Nodes.Node.Samples.Sample, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sample_id.is_set or
                                self.curr_memory.is_set or
                                self.peak_memory.is_set or
                                self.time_stamp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sample_id.yfilter != YFilter.not_set or
                                self.curr_memory.yfilter != YFilter.not_set or
                                self.peak_memory.yfilter != YFilter.not_set or
                                self.time_stamp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sample_id.get_name_leafdata())
                            if (self.curr_memory.is_set or self.curr_memory.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.curr_memory.get_name_leafdata())
                            if (self.peak_memory.is_set or self.peak_memory.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peak_memory.get_name_leafdata())
                            if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample-id" or name == "curr-memory" or name == "peak-memory" or name == "time-stamp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sample-id"):
                                self.sample_id = value
                                self.sample_id.value_namespace = name_space
                                self.sample_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "curr-memory"):
                                self.curr_memory = value
                                self.curr_memory.value_namespace = name_space
                                self.curr_memory.value_namespace_prefix = name_space_prefix
                            if(value_path == "peak-memory"):
                                self.peak_memory = value
                                self.peak_memory.value_namespace = name_space
                                self.peak_memory.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-stamp"):
                                self.time_stamp = value
                                self.time_stamp.value_namespace = name_space
                                self.time_stamp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sample:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sample:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "samples" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sample"):
                            for c in self.sample:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PerfMgmt.Periodic.Nodes.Node.Samples.Sample()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sample.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sample"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.node_id.is_set or
                        (self.processes is not None and self.processes.has_data()) or
                        (self.sample_xr is not None and self.sample_xr.has_data()) or
                        (self.samples is not None and self.samples.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.node_id.yfilter != YFilter.not_set or
                        (self.processes is not None and self.processes.has_operation()) or
                        (self.sample_xr is not None and self.sample_xr.has_operation()) or
                        (self.samples is not None and self.samples.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/nodes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "processes"):
                        if (self.processes is None):
                            self.processes = PerfMgmt.Periodic.Nodes.Node.Processes()
                            self.processes.parent = self
                            self._children_name_map["processes"] = "processes"
                        return self.processes

                    if (child_yang_name == "sample-xr"):
                        if (self.sample_xr is None):
                            self.sample_xr = PerfMgmt.Periodic.Nodes.Node.SampleXr()
                            self.sample_xr.parent = self
                            self._children_name_map["sample_xr"] = "sample-xr"
                        return self.sample_xr

                    if (child_yang_name == "samples"):
                        if (self.samples is None):
                            self.samples = PerfMgmt.Periodic.Nodes.Node.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                        return self.samples

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "processes" or name == "sample-xr" or name == "samples" or name == "node-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "node-id"):
                        self.node_id = value
                        self.node_id.value_namespace = name_space
                        self.node_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.node:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.node:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nodes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "node"):
                    for c in self.node:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = PerfMgmt.Periodic.Nodes.Node()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.node.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.bgp_neighbors = PerfMgmt.Periodic.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self
                self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                self._children_yang_names.add("bgp-neighbors")


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

                    self.bgp_neighbor = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Bgp.BgpNeighbors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Bgp.BgpNeighbors, self).__setattr__(name, value)


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

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.samples = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "conn_dropped",
                                                "conn_established",
                                                "errors_received",
                                                "errors_sent",
                                                "input_messages",
                                                "input_update_messages",
                                                "output_messages",
                                                "output_update_messages",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.conn_dropped.is_set or
                                    self.conn_established.is_set or
                                    self.errors_received.is_set or
                                    self.errors_sent.is_set or
                                    self.input_messages.is_set or
                                    self.input_update_messages.is_set or
                                    self.output_messages.is_set or
                                    self.output_update_messages.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.conn_dropped.yfilter != YFilter.not_set or
                                    self.conn_established.yfilter != YFilter.not_set or
                                    self.errors_received.yfilter != YFilter.not_set or
                                    self.errors_sent.yfilter != YFilter.not_set or
                                    self.input_messages.yfilter != YFilter.not_set or
                                    self.input_update_messages.yfilter != YFilter.not_set or
                                    self.output_messages.yfilter != YFilter.not_set or
                                    self.output_update_messages.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.conn_dropped.is_set or self.conn_dropped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.conn_dropped.get_name_leafdata())
                                if (self.conn_established.is_set or self.conn_established.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.conn_established.get_name_leafdata())
                                if (self.errors_received.is_set or self.errors_received.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.errors_received.get_name_leafdata())
                                if (self.errors_sent.is_set or self.errors_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.errors_sent.get_name_leafdata())
                                if (self.input_messages.is_set or self.input_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_messages.get_name_leafdata())
                                if (self.input_update_messages.is_set or self.input_update_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_update_messages.get_name_leafdata())
                                if (self.output_messages.is_set or self.output_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_messages.get_name_leafdata())
                                if (self.output_update_messages.is_set or self.output_update_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_update_messages.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "conn-dropped" or name == "conn-established" or name == "errors-received" or name == "errors-sent" or name == "input-messages" or name == "input-update-messages" or name == "output-messages" or name == "output-update-messages" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "conn-dropped"):
                                    self.conn_dropped = value
                                    self.conn_dropped.value_namespace = name_space
                                    self.conn_dropped.value_namespace_prefix = name_space_prefix
                                if(value_path == "conn-established"):
                                    self.conn_established = value
                                    self.conn_established.value_namespace = name_space
                                    self.conn_established.value_namespace_prefix = name_space_prefix
                                if(value_path == "errors-received"):
                                    self.errors_received = value
                                    self.errors_received.value_namespace = name_space
                                    self.errors_received.value_namespace_prefix = name_space_prefix
                                if(value_path == "errors-sent"):
                                    self.errors_sent = value
                                    self.errors_sent.value_namespace = name_space
                                    self.errors_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-messages"):
                                    self.input_messages = value
                                    self.input_messages.value_namespace = name_space
                                    self.input_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-update-messages"):
                                    self.input_update_messages = value
                                    self.input_update_messages.value_namespace = name_space
                                    self.input_update_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-messages"):
                                    self.output_messages = value
                                    self.output_messages.value_namespace = name_space
                                    self.output_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-update-messages"):
                                    self.output_update_messages = value
                                    self.output_update_messages.value_namespace = name_space
                                    self.output_update_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.ip_address.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bgp-neighbor" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/bgp/bgp-neighbors/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "ip-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bgp_neighbor:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bgp_neighbor:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bgp-neighbors" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/bgp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bgp-neighbor"):
                        for c in self.bgp_neighbor:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bgp_neighbor.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp-neighbor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.bgp_neighbors is not None and self.bgp_neighbors.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bgp_neighbors is not None and self.bgp_neighbors.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bgp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bgp-neighbors"):
                    if (self.bgp_neighbors is None):
                        self.bgp_neighbors = PerfMgmt.Periodic.Bgp.BgpNeighbors()
                        self.bgp_neighbors.parent = self
                        self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                    return self.bgp_neighbors

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgp-neighbors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                    self.generic_counter_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces, self).__setattr__(name, value)


                class GenericCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "in_broadcast_pkts",
                                                "in_multicast_pkts",
                                                "in_octets",
                                                "in_packets",
                                                "in_ucast_pkts",
                                                "input_crc",
                                                "input_frame",
                                                "input_overrun",
                                                "input_queue_drops",
                                                "input_total_drops",
                                                "input_total_errors",
                                                "input_unknown_proto",
                                                "out_broadcast_pkts",
                                                "out_multicast_pkts",
                                                "out_octets",
                                                "out_packets",
                                                "out_ucast_pkts",
                                                "output_total_drops",
                                                "output_total_errors",
                                                "output_underrun",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.in_broadcast_pkts.is_set or
                                    self.in_multicast_pkts.is_set or
                                    self.in_octets.is_set or
                                    self.in_packets.is_set or
                                    self.in_ucast_pkts.is_set or
                                    self.input_crc.is_set or
                                    self.input_frame.is_set or
                                    self.input_overrun.is_set or
                                    self.input_queue_drops.is_set or
                                    self.input_total_drops.is_set or
                                    self.input_total_errors.is_set or
                                    self.input_unknown_proto.is_set or
                                    self.out_broadcast_pkts.is_set or
                                    self.out_multicast_pkts.is_set or
                                    self.out_octets.is_set or
                                    self.out_packets.is_set or
                                    self.out_ucast_pkts.is_set or
                                    self.output_total_drops.is_set or
                                    self.output_total_errors.is_set or
                                    self.output_underrun.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.in_broadcast_pkts.yfilter != YFilter.not_set or
                                    self.in_multicast_pkts.yfilter != YFilter.not_set or
                                    self.in_octets.yfilter != YFilter.not_set or
                                    self.in_packets.yfilter != YFilter.not_set or
                                    self.in_ucast_pkts.yfilter != YFilter.not_set or
                                    self.input_crc.yfilter != YFilter.not_set or
                                    self.input_frame.yfilter != YFilter.not_set or
                                    self.input_overrun.yfilter != YFilter.not_set or
                                    self.input_queue_drops.yfilter != YFilter.not_set or
                                    self.input_total_drops.yfilter != YFilter.not_set or
                                    self.input_total_errors.yfilter != YFilter.not_set or
                                    self.input_unknown_proto.yfilter != YFilter.not_set or
                                    self.out_broadcast_pkts.yfilter != YFilter.not_set or
                                    self.out_multicast_pkts.yfilter != YFilter.not_set or
                                    self.out_octets.yfilter != YFilter.not_set or
                                    self.out_packets.yfilter != YFilter.not_set or
                                    self.out_ucast_pkts.yfilter != YFilter.not_set or
                                    self.output_total_drops.yfilter != YFilter.not_set or
                                    self.output_total_errors.yfilter != YFilter.not_set or
                                    self.output_underrun.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.in_broadcast_pkts.is_set or self.in_broadcast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_broadcast_pkts.get_name_leafdata())
                                if (self.in_multicast_pkts.is_set or self.in_multicast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_multicast_pkts.get_name_leafdata())
                                if (self.in_octets.is_set or self.in_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_octets.get_name_leafdata())
                                if (self.in_packets.is_set or self.in_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_packets.get_name_leafdata())
                                if (self.in_ucast_pkts.is_set or self.in_ucast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_ucast_pkts.get_name_leafdata())
                                if (self.input_crc.is_set or self.input_crc.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_crc.get_name_leafdata())
                                if (self.input_frame.is_set or self.input_frame.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_frame.get_name_leafdata())
                                if (self.input_overrun.is_set or self.input_overrun.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_overrun.get_name_leafdata())
                                if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                                if (self.input_total_drops.is_set or self.input_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_drops.get_name_leafdata())
                                if (self.input_total_errors.is_set or self.input_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_errors.get_name_leafdata())
                                if (self.input_unknown_proto.is_set or self.input_unknown_proto.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_unknown_proto.get_name_leafdata())
                                if (self.out_broadcast_pkts.is_set or self.out_broadcast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_broadcast_pkts.get_name_leafdata())
                                if (self.out_multicast_pkts.is_set or self.out_multicast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_multicast_pkts.get_name_leafdata())
                                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                                if (self.out_packets.is_set or self.out_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_packets.get_name_leafdata())
                                if (self.out_ucast_pkts.is_set or self.out_ucast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_ucast_pkts.get_name_leafdata())
                                if (self.output_total_drops.is_set or self.output_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_drops.get_name_leafdata())
                                if (self.output_total_errors.is_set or self.output_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_errors.get_name_leafdata())
                                if (self.output_underrun.is_set or self.output_underrun.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_underrun.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "in-broadcast-pkts" or name == "in-multicast-pkts" or name == "in-octets" or name == "in-packets" or name == "in-ucast-pkts" or name == "input-crc" or name == "input-frame" or name == "input-overrun" or name == "input-queue-drops" or name == "input-total-drops" or name == "input-total-errors" or name == "input-unknown-proto" or name == "out-broadcast-pkts" or name == "out-multicast-pkts" or name == "out-octets" or name == "out-packets" or name == "out-ucast-pkts" or name == "output-total-drops" or name == "output-total-errors" or name == "output-underrun" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-broadcast-pkts"):
                                    self.in_broadcast_pkts = value
                                    self.in_broadcast_pkts.value_namespace = name_space
                                    self.in_broadcast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-multicast-pkts"):
                                    self.in_multicast_pkts = value
                                    self.in_multicast_pkts.value_namespace = name_space
                                    self.in_multicast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-octets"):
                                    self.in_octets = value
                                    self.in_octets.value_namespace = name_space
                                    self.in_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-packets"):
                                    self.in_packets = value
                                    self.in_packets.value_namespace = name_space
                                    self.in_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-ucast-pkts"):
                                    self.in_ucast_pkts = value
                                    self.in_ucast_pkts.value_namespace = name_space
                                    self.in_ucast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-crc"):
                                    self.input_crc = value
                                    self.input_crc.value_namespace = name_space
                                    self.input_crc.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-frame"):
                                    self.input_frame = value
                                    self.input_frame.value_namespace = name_space
                                    self.input_frame.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-overrun"):
                                    self.input_overrun = value
                                    self.input_overrun.value_namespace = name_space
                                    self.input_overrun.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-queue-drops"):
                                    self.input_queue_drops = value
                                    self.input_queue_drops.value_namespace = name_space
                                    self.input_queue_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-drops"):
                                    self.input_total_drops = value
                                    self.input_total_drops.value_namespace = name_space
                                    self.input_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-errors"):
                                    self.input_total_errors = value
                                    self.input_total_errors.value_namespace = name_space
                                    self.input_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-unknown-proto"):
                                    self.input_unknown_proto = value
                                    self.input_unknown_proto.value_namespace = name_space
                                    self.input_unknown_proto.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-broadcast-pkts"):
                                    self.out_broadcast_pkts = value
                                    self.out_broadcast_pkts.value_namespace = name_space
                                    self.out_broadcast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-multicast-pkts"):
                                    self.out_multicast_pkts = value
                                    self.out_multicast_pkts.value_namespace = name_space
                                    self.out_multicast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-octets"):
                                    self.out_octets = value
                                    self.out_octets.value_namespace = name_space
                                    self.out_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-packets"):
                                    self.out_packets = value
                                    self.out_packets.value_namespace = name_space
                                    self.out_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-ucast-pkts"):
                                    self.out_ucast_pkts = value
                                    self.out_ucast_pkts.value_namespace = name_space
                                    self.out_ucast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-drops"):
                                    self.output_total_drops = value
                                    self.output_total_drops.value_namespace = name_space
                                    self.output_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-errors"):
                                    self.output_total_errors = value
                                    self.output_total_errors.value_namespace = name_space
                                    self.output_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-underrun"):
                                    self.output_underrun = value
                                    self.output_underrun.value_namespace = name_space
                                    self.output_underrun.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "generic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/generic-counter-interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.generic_counter_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.generic_counter_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "generic-counter-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "generic-counter-interface"):
                        for c in self.generic_counter_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.generic_counter_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "generic-counter-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.basic_counter_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces, self).__setattr__(name, value)


                class BasicCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "in_octets",
                                                "in_packets",
                                                "input_queue_drops",
                                                "input_total_drops",
                                                "input_total_errors",
                                                "out_octets",
                                                "out_packets",
                                                "output_queue_drops",
                                                "output_total_drops",
                                                "output_total_errors",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.in_octets.is_set or
                                    self.in_packets.is_set or
                                    self.input_queue_drops.is_set or
                                    self.input_total_drops.is_set or
                                    self.input_total_errors.is_set or
                                    self.out_octets.is_set or
                                    self.out_packets.is_set or
                                    self.output_queue_drops.is_set or
                                    self.output_total_drops.is_set or
                                    self.output_total_errors.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.in_octets.yfilter != YFilter.not_set or
                                    self.in_packets.yfilter != YFilter.not_set or
                                    self.input_queue_drops.yfilter != YFilter.not_set or
                                    self.input_total_drops.yfilter != YFilter.not_set or
                                    self.input_total_errors.yfilter != YFilter.not_set or
                                    self.out_octets.yfilter != YFilter.not_set or
                                    self.out_packets.yfilter != YFilter.not_set or
                                    self.output_queue_drops.yfilter != YFilter.not_set or
                                    self.output_total_drops.yfilter != YFilter.not_set or
                                    self.output_total_errors.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.in_octets.is_set or self.in_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_octets.get_name_leafdata())
                                if (self.in_packets.is_set or self.in_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_packets.get_name_leafdata())
                                if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                                if (self.input_total_drops.is_set or self.input_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_drops.get_name_leafdata())
                                if (self.input_total_errors.is_set or self.input_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_errors.get_name_leafdata())
                                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                                if (self.out_packets.is_set or self.out_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_packets.get_name_leafdata())
                                if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                                if (self.output_total_drops.is_set or self.output_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_drops.get_name_leafdata())
                                if (self.output_total_errors.is_set or self.output_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_errors.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "in-octets" or name == "in-packets" or name == "input-queue-drops" or name == "input-total-drops" or name == "input-total-errors" or name == "out-octets" or name == "out-packets" or name == "output-queue-drops" or name == "output-total-drops" or name == "output-total-errors" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-octets"):
                                    self.in_octets = value
                                    self.in_octets.value_namespace = name_space
                                    self.in_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-packets"):
                                    self.in_packets = value
                                    self.in_packets.value_namespace = name_space
                                    self.in_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-queue-drops"):
                                    self.input_queue_drops = value
                                    self.input_queue_drops.value_namespace = name_space
                                    self.input_queue_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-drops"):
                                    self.input_total_drops = value
                                    self.input_total_drops.value_namespace = name_space
                                    self.input_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-errors"):
                                    self.input_total_errors = value
                                    self.input_total_errors.value_namespace = name_space
                                    self.input_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-octets"):
                                    self.out_octets = value
                                    self.out_octets.value_namespace = name_space
                                    self.out_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-packets"):
                                    self.out_packets = value
                                    self.out_packets.value_namespace = name_space
                                    self.out_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-queue-drops"):
                                    self.output_queue_drops = value
                                    self.output_queue_drops.value_namespace = name_space
                                    self.output_queue_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-drops"):
                                    self.output_total_drops = value
                                    self.output_total_drops.value_namespace = name_space
                                    self.output_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-errors"):
                                    self.output_total_errors = value
                                    self.output_total_errors.value_namespace = name_space
                                    self.output_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "basic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/basic-counter-interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.basic_counter_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.basic_counter_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "basic-counter-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "basic-counter-interface"):
                        for c in self.basic_counter_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.basic_counter_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "basic-counter-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.data_rate_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Periodic.Interface.DataRateInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Periodic.Interface.DataRateInterfaces, self).__setattr__(name, value)


                class DataRateInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "bandwidth",
                                                "input_data_rate",
                                                "input_packet_rate",
                                                "input_peak_pkts",
                                                "input_peak_rate",
                                                "output_data_rate",
                                                "output_packet_rate",
                                                "output_peak_pkts",
                                                "output_peak_rate",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.bandwidth.is_set or
                                    self.input_data_rate.is_set or
                                    self.input_packet_rate.is_set or
                                    self.input_peak_pkts.is_set or
                                    self.input_peak_rate.is_set or
                                    self.output_data_rate.is_set or
                                    self.output_packet_rate.is_set or
                                    self.output_peak_pkts.is_set or
                                    self.output_peak_rate.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.bandwidth.yfilter != YFilter.not_set or
                                    self.input_data_rate.yfilter != YFilter.not_set or
                                    self.input_packet_rate.yfilter != YFilter.not_set or
                                    self.input_peak_pkts.yfilter != YFilter.not_set or
                                    self.input_peak_rate.yfilter != YFilter.not_set or
                                    self.output_data_rate.yfilter != YFilter.not_set or
                                    self.output_packet_rate.yfilter != YFilter.not_set or
                                    self.output_peak_pkts.yfilter != YFilter.not_set or
                                    self.output_peak_rate.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bandwidth.get_name_leafdata())
                                if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                                if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                                if (self.input_peak_pkts.is_set or self.input_peak_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_peak_pkts.get_name_leafdata())
                                if (self.input_peak_rate.is_set or self.input_peak_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_peak_rate.get_name_leafdata())
                                if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                                if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                                if (self.output_peak_pkts.is_set or self.output_peak_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_peak_pkts.get_name_leafdata())
                                if (self.output_peak_rate.is_set or self.output_peak_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_peak_rate.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "bandwidth" or name == "input-data-rate" or name == "input-packet-rate" or name == "input-peak-pkts" or name == "input-peak-rate" or name == "output-data-rate" or name == "output-packet-rate" or name == "output-peak-pkts" or name == "output-peak-rate" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "bandwidth"):
                                    self.bandwidth = value
                                    self.bandwidth.value_namespace = name_space
                                    self.bandwidth.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-data-rate"):
                                    self.input_data_rate = value
                                    self.input_data_rate.value_namespace = name_space
                                    self.input_data_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-packet-rate"):
                                    self.input_packet_rate = value
                                    self.input_packet_rate.value_namespace = name_space
                                    self.input_packet_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-peak-pkts"):
                                    self.input_peak_pkts = value
                                    self.input_peak_pkts.value_namespace = name_space
                                    self.input_peak_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-peak-rate"):
                                    self.input_peak_rate = value
                                    self.input_peak_rate.value_namespace = name_space
                                    self.input_peak_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-data-rate"):
                                    self.output_data_rate = value
                                    self.output_data_rate.value_namespace = name_space
                                    self.output_data_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-packet-rate"):
                                    self.output_packet_rate = value
                                    self.output_packet_rate.value_namespace = name_space
                                    self.output_packet_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-peak-pkts"):
                                    self.output_peak_pkts = value
                                    self.output_peak_pkts.value_namespace = name_space
                                    self.output_peak_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-peak-rate"):
                                    self.output_peak_rate = value
                                    self.output_peak_rate.value_namespace = name_space
                                    self.output_peak_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "data-rate-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/data-rate-interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.data_rate_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.data_rate_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "data-rate-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "data-rate-interface"):
                        for c in self.data_rate_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.data_rate_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "data-rate-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.basic_counter_interfaces is not None and self.basic_counter_interfaces.has_data()) or
                    (self.data_rate_interfaces is not None and self.data_rate_interfaces.has_data()) or
                    (self.generic_counter_interfaces is not None and self.generic_counter_interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.basic_counter_interfaces is not None and self.basic_counter_interfaces.has_operation()) or
                    (self.data_rate_interfaces is not None and self.data_rate_interfaces.has_operation()) or
                    (self.generic_counter_interfaces is not None and self.generic_counter_interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/periodic/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "basic-counter-interfaces"):
                    if (self.basic_counter_interfaces is None):
                        self.basic_counter_interfaces = PerfMgmt.Periodic.Interface.BasicCounterInterfaces()
                        self.basic_counter_interfaces.parent = self
                        self._children_name_map["basic_counter_interfaces"] = "basic-counter-interfaces"
                    return self.basic_counter_interfaces

                if (child_yang_name == "data-rate-interfaces"):
                    if (self.data_rate_interfaces is None):
                        self.data_rate_interfaces = PerfMgmt.Periodic.Interface.DataRateInterfaces()
                        self.data_rate_interfaces.parent = self
                        self._children_name_map["data_rate_interfaces"] = "data-rate-interfaces"
                    return self.data_rate_interfaces

                if (child_yang_name == "generic-counter-interfaces"):
                    if (self.generic_counter_interfaces is None):
                        self.generic_counter_interfaces = PerfMgmt.Periodic.Interface.GenericCounterInterfaces()
                        self.generic_counter_interfaces.parent = self
                        self._children_name_map["generic_counter_interfaces"] = "generic-counter-interfaces"
                    return self.generic_counter_interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "basic-counter-interfaces" or name == "data-rate-interfaces" or name == "generic-counter-interfaces"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.bgp is not None and self.bgp.has_data()) or
                (self.interface is not None and self.interface.has_data()) or
                (self.mpls is not None and self.mpls.has_data()) or
                (self.nodes is not None and self.nodes.has_data()) or
                (self.ospf is not None and self.ospf.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.bgp is not None and self.bgp.has_operation()) or
                (self.interface is not None and self.interface.has_operation()) or
                (self.mpls is not None and self.mpls.has_operation()) or
                (self.nodes is not None and self.nodes.has_operation()) or
                (self.ospf is not None and self.ospf.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "periodic" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgp"):
                if (self.bgp is None):
                    self.bgp = PerfMgmt.Periodic.Bgp()
                    self.bgp.parent = self
                    self._children_name_map["bgp"] = "bgp"
                return self.bgp

            if (child_yang_name == "interface"):
                if (self.interface is None):
                    self.interface = PerfMgmt.Periodic.Interface()
                    self.interface.parent = self
                    self._children_name_map["interface"] = "interface"
                return self.interface

            if (child_yang_name == "mpls"):
                if (self.mpls is None):
                    self.mpls = PerfMgmt.Periodic.Mpls()
                    self.mpls.parent = self
                    self._children_name_map["mpls"] = "mpls"
                return self.mpls

            if (child_yang_name == "nodes"):
                if (self.nodes is None):
                    self.nodes = PerfMgmt.Periodic.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                return self.nodes

            if (child_yang_name == "ospf"):
                if (self.ospf is None):
                    self.ospf = PerfMgmt.Periodic.Ospf()
                    self.ospf.parent = self
                    self._children_name_map["ospf"] = "ospf"
                return self.ospf

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgp" or name == "interface" or name == "mpls" or name == "nodes" or name == "ospf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

                self.ospfv2_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"
                self._children_yang_names.add("ospfv2-protocol-instances")

                self.ospfv3_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self
                self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                self._children_yang_names.add("ospfv3-protocol-instances")


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

                    self.ospfv2_protocol_instance = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances, self).__setattr__(name, value)


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

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("instance_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "checksum_errors",
                                                "input_db_ds",
                                                "input_db_ds_lsa",
                                                "input_hello_packets",
                                                "input_ls_requests",
                                                "input_ls_requests_lsa",
                                                "input_lsa_acks",
                                                "input_lsa_acks_lsa",
                                                "input_lsa_updates",
                                                "input_lsa_updates_lsa",
                                                "input_packets",
                                                "output_db_ds",
                                                "output_db_ds_lsa",
                                                "output_hello_packets",
                                                "output_ls_requests",
                                                "output_ls_requests_lsa",
                                                "output_lsa_acks",
                                                "output_lsa_acks_lsa",
                                                "output_lsa_updates",
                                                "output_lsa_updates_lsa",
                                                "output_packets",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.checksum_errors.is_set or
                                    self.input_db_ds.is_set or
                                    self.input_db_ds_lsa.is_set or
                                    self.input_hello_packets.is_set or
                                    self.input_ls_requests.is_set or
                                    self.input_ls_requests_lsa.is_set or
                                    self.input_lsa_acks.is_set or
                                    self.input_lsa_acks_lsa.is_set or
                                    self.input_lsa_updates.is_set or
                                    self.input_lsa_updates_lsa.is_set or
                                    self.input_packets.is_set or
                                    self.output_db_ds.is_set or
                                    self.output_db_ds_lsa.is_set or
                                    self.output_hello_packets.is_set or
                                    self.output_ls_requests.is_set or
                                    self.output_ls_requests_lsa.is_set or
                                    self.output_lsa_acks.is_set or
                                    self.output_lsa_acks_lsa.is_set or
                                    self.output_lsa_updates.is_set or
                                    self.output_lsa_updates_lsa.is_set or
                                    self.output_packets.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.checksum_errors.yfilter != YFilter.not_set or
                                    self.input_db_ds.yfilter != YFilter.not_set or
                                    self.input_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.input_hello_packets.yfilter != YFilter.not_set or
                                    self.input_ls_requests.yfilter != YFilter.not_set or
                                    self.input_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_acks.yfilter != YFilter.not_set or
                                    self.input_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_updates.yfilter != YFilter.not_set or
                                    self.input_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.input_packets.yfilter != YFilter.not_set or
                                    self.output_db_ds.yfilter != YFilter.not_set or
                                    self.output_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.output_hello_packets.yfilter != YFilter.not_set or
                                    self.output_ls_requests.yfilter != YFilter.not_set or
                                    self.output_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_acks.yfilter != YFilter.not_set or
                                    self.output_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_updates.yfilter != YFilter.not_set or
                                    self.output_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.output_packets.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.checksum_errors.is_set or self.checksum_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.checksum_errors.get_name_leafdata())
                                if (self.input_db_ds.is_set or self.input_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds.get_name_leafdata())
                                if (self.input_db_ds_lsa.is_set or self.input_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds_lsa.get_name_leafdata())
                                if (self.input_hello_packets.is_set or self.input_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_hello_packets.get_name_leafdata())
                                if (self.input_ls_requests.is_set or self.input_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests.get_name_leafdata())
                                if (self.input_ls_requests_lsa.is_set or self.input_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests_lsa.get_name_leafdata())
                                if (self.input_lsa_acks.is_set or self.input_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks.get_name_leafdata())
                                if (self.input_lsa_acks_lsa.is_set or self.input_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks_lsa.get_name_leafdata())
                                if (self.input_lsa_updates.is_set or self.input_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates.get_name_leafdata())
                                if (self.input_lsa_updates_lsa.is_set or self.input_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates_lsa.get_name_leafdata())
                                if (self.input_packets.is_set or self.input_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_packets.get_name_leafdata())
                                if (self.output_db_ds.is_set or self.output_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds.get_name_leafdata())
                                if (self.output_db_ds_lsa.is_set or self.output_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds_lsa.get_name_leafdata())
                                if (self.output_hello_packets.is_set or self.output_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_hello_packets.get_name_leafdata())
                                if (self.output_ls_requests.is_set or self.output_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests.get_name_leafdata())
                                if (self.output_ls_requests_lsa.is_set or self.output_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests_lsa.get_name_leafdata())
                                if (self.output_lsa_acks.is_set or self.output_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks.get_name_leafdata())
                                if (self.output_lsa_acks_lsa.is_set or self.output_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks_lsa.get_name_leafdata())
                                if (self.output_lsa_updates.is_set or self.output_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates.get_name_leafdata())
                                if (self.output_lsa_updates_lsa.is_set or self.output_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates_lsa.get_name_leafdata())
                                if (self.output_packets.is_set or self.output_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_packets.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "checksum-errors" or name == "input-db-ds" or name == "input-db-ds-lsa" or name == "input-hello-packets" or name == "input-ls-requests" or name == "input-ls-requests-lsa" or name == "input-lsa-acks" or name == "input-lsa-acks-lsa" or name == "input-lsa-updates" or name == "input-lsa-updates-lsa" or name == "input-packets" or name == "output-db-ds" or name == "output-db-ds-lsa" or name == "output-hello-packets" or name == "output-ls-requests" or name == "output-ls-requests-lsa" or name == "output-lsa-acks" or name == "output-lsa-acks-lsa" or name == "output-lsa-updates" or name == "output-lsa-updates-lsa" or name == "output-packets" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "checksum-errors"):
                                    self.checksum_errors = value
                                    self.checksum_errors.value_namespace = name_space
                                    self.checksum_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds"):
                                    self.input_db_ds = value
                                    self.input_db_ds.value_namespace = name_space
                                    self.input_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds-lsa"):
                                    self.input_db_ds_lsa = value
                                    self.input_db_ds_lsa.value_namespace = name_space
                                    self.input_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-hello-packets"):
                                    self.input_hello_packets = value
                                    self.input_hello_packets.value_namespace = name_space
                                    self.input_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests"):
                                    self.input_ls_requests = value
                                    self.input_ls_requests.value_namespace = name_space
                                    self.input_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests-lsa"):
                                    self.input_ls_requests_lsa = value
                                    self.input_ls_requests_lsa.value_namespace = name_space
                                    self.input_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks"):
                                    self.input_lsa_acks = value
                                    self.input_lsa_acks.value_namespace = name_space
                                    self.input_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks-lsa"):
                                    self.input_lsa_acks_lsa = value
                                    self.input_lsa_acks_lsa.value_namespace = name_space
                                    self.input_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates"):
                                    self.input_lsa_updates = value
                                    self.input_lsa_updates.value_namespace = name_space
                                    self.input_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates-lsa"):
                                    self.input_lsa_updates_lsa = value
                                    self.input_lsa_updates_lsa.value_namespace = name_space
                                    self.input_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-packets"):
                                    self.input_packets = value
                                    self.input_packets.value_namespace = name_space
                                    self.input_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds"):
                                    self.output_db_ds = value
                                    self.output_db_ds.value_namespace = name_space
                                    self.output_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds-lsa"):
                                    self.output_db_ds_lsa = value
                                    self.output_db_ds_lsa.value_namespace = name_space
                                    self.output_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-hello-packets"):
                                    self.output_hello_packets = value
                                    self.output_hello_packets.value_namespace = name_space
                                    self.output_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests"):
                                    self.output_ls_requests = value
                                    self.output_ls_requests.value_namespace = name_space
                                    self.output_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests-lsa"):
                                    self.output_ls_requests_lsa = value
                                    self.output_ls_requests_lsa.value_namespace = name_space
                                    self.output_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks"):
                                    self.output_lsa_acks = value
                                    self.output_lsa_acks.value_namespace = name_space
                                    self.output_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks-lsa"):
                                    self.output_lsa_acks_lsa = value
                                    self.output_lsa_acks_lsa.value_namespace = name_space
                                    self.output_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates"):
                                    self.output_lsa_updates = value
                                    self.output_lsa_updates.value_namespace = name_space
                                    self.output_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates-lsa"):
                                    self.output_lsa_updates_lsa = value
                                    self.output_lsa_updates_lsa.value_namespace = name_space
                                    self.output_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-packets"):
                                    self.output_packets = value
                                    self.output_packets.value_namespace = name_space
                                    self.output_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.instance_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.instance_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ospfv2-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/ospfv2-protocol-instances/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.instance_name.is_set or self.instance_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instance_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "instance-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "instance-name"):
                            self.instance_name = value
                            self.instance_name.value_namespace = name_space
                            self.instance_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ospfv2_protocol_instance:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ospfv2_protocol_instance:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ospfv2-protocol-instances" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ospfv2-protocol-instance"):
                        for c in self.ospfv2_protocol_instance:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ospfv2_protocol_instance.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ospfv2-protocol-instance"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.ospfv3_protocol_instance = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances, self).__setattr__(name, value)


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

                        self.instance_name = YLeaf(YType.str, "instance-name")

                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("instance_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "input_db_ds",
                                                "input_db_ds_lsa",
                                                "input_hello_packets",
                                                "input_ls_requests",
                                                "input_ls_requests_lsa",
                                                "input_lsa_acks",
                                                "input_lsa_acks_lsa",
                                                "input_lsa_updates",
                                                "input_lsa_updates_lsa",
                                                "input_packets",
                                                "output_db_ds",
                                                "output_db_ds_lsa",
                                                "output_hello_packets",
                                                "output_ls_requests",
                                                "output_ls_requests_lsa",
                                                "output_lsa_acks",
                                                "output_lsa_acks_lsa",
                                                "output_lsa_updates",
                                                "output_lsa_updates_lsa",
                                                "output_packets",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.input_db_ds.is_set or
                                    self.input_db_ds_lsa.is_set or
                                    self.input_hello_packets.is_set or
                                    self.input_ls_requests.is_set or
                                    self.input_ls_requests_lsa.is_set or
                                    self.input_lsa_acks.is_set or
                                    self.input_lsa_acks_lsa.is_set or
                                    self.input_lsa_updates.is_set or
                                    self.input_lsa_updates_lsa.is_set or
                                    self.input_packets.is_set or
                                    self.output_db_ds.is_set or
                                    self.output_db_ds_lsa.is_set or
                                    self.output_hello_packets.is_set or
                                    self.output_ls_requests.is_set or
                                    self.output_ls_requests_lsa.is_set or
                                    self.output_lsa_acks.is_set or
                                    self.output_lsa_acks_lsa.is_set or
                                    self.output_lsa_updates.is_set or
                                    self.output_lsa_updates_lsa.is_set or
                                    self.output_packets.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.input_db_ds.yfilter != YFilter.not_set or
                                    self.input_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.input_hello_packets.yfilter != YFilter.not_set or
                                    self.input_ls_requests.yfilter != YFilter.not_set or
                                    self.input_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_acks.yfilter != YFilter.not_set or
                                    self.input_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.input_lsa_updates.yfilter != YFilter.not_set or
                                    self.input_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.input_packets.yfilter != YFilter.not_set or
                                    self.output_db_ds.yfilter != YFilter.not_set or
                                    self.output_db_ds_lsa.yfilter != YFilter.not_set or
                                    self.output_hello_packets.yfilter != YFilter.not_set or
                                    self.output_ls_requests.yfilter != YFilter.not_set or
                                    self.output_ls_requests_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_acks.yfilter != YFilter.not_set or
                                    self.output_lsa_acks_lsa.yfilter != YFilter.not_set or
                                    self.output_lsa_updates.yfilter != YFilter.not_set or
                                    self.output_lsa_updates_lsa.yfilter != YFilter.not_set or
                                    self.output_packets.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.input_db_ds.is_set or self.input_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds.get_name_leafdata())
                                if (self.input_db_ds_lsa.is_set or self.input_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_db_ds_lsa.get_name_leafdata())
                                if (self.input_hello_packets.is_set or self.input_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_hello_packets.get_name_leafdata())
                                if (self.input_ls_requests.is_set or self.input_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests.get_name_leafdata())
                                if (self.input_ls_requests_lsa.is_set or self.input_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_ls_requests_lsa.get_name_leafdata())
                                if (self.input_lsa_acks.is_set or self.input_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks.get_name_leafdata())
                                if (self.input_lsa_acks_lsa.is_set or self.input_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_acks_lsa.get_name_leafdata())
                                if (self.input_lsa_updates.is_set or self.input_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates.get_name_leafdata())
                                if (self.input_lsa_updates_lsa.is_set or self.input_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_lsa_updates_lsa.get_name_leafdata())
                                if (self.input_packets.is_set or self.input_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_packets.get_name_leafdata())
                                if (self.output_db_ds.is_set or self.output_db_ds.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds.get_name_leafdata())
                                if (self.output_db_ds_lsa.is_set or self.output_db_ds_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_db_ds_lsa.get_name_leafdata())
                                if (self.output_hello_packets.is_set or self.output_hello_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_hello_packets.get_name_leafdata())
                                if (self.output_ls_requests.is_set or self.output_ls_requests.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests.get_name_leafdata())
                                if (self.output_ls_requests_lsa.is_set or self.output_ls_requests_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_ls_requests_lsa.get_name_leafdata())
                                if (self.output_lsa_acks.is_set or self.output_lsa_acks.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks.get_name_leafdata())
                                if (self.output_lsa_acks_lsa.is_set or self.output_lsa_acks_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_acks_lsa.get_name_leafdata())
                                if (self.output_lsa_updates.is_set or self.output_lsa_updates.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates.get_name_leafdata())
                                if (self.output_lsa_updates_lsa.is_set or self.output_lsa_updates_lsa.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_lsa_updates_lsa.get_name_leafdata())
                                if (self.output_packets.is_set or self.output_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_packets.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "input-db-ds" or name == "input-db-ds-lsa" or name == "input-hello-packets" or name == "input-ls-requests" or name == "input-ls-requests-lsa" or name == "input-lsa-acks" or name == "input-lsa-acks-lsa" or name == "input-lsa-updates" or name == "input-lsa-updates-lsa" or name == "input-packets" or name == "output-db-ds" or name == "output-db-ds-lsa" or name == "output-hello-packets" or name == "output-ls-requests" or name == "output-ls-requests-lsa" or name == "output-lsa-acks" or name == "output-lsa-acks-lsa" or name == "output-lsa-updates" or name == "output-lsa-updates-lsa" or name == "output-packets" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds"):
                                    self.input_db_ds = value
                                    self.input_db_ds.value_namespace = name_space
                                    self.input_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-db-ds-lsa"):
                                    self.input_db_ds_lsa = value
                                    self.input_db_ds_lsa.value_namespace = name_space
                                    self.input_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-hello-packets"):
                                    self.input_hello_packets = value
                                    self.input_hello_packets.value_namespace = name_space
                                    self.input_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests"):
                                    self.input_ls_requests = value
                                    self.input_ls_requests.value_namespace = name_space
                                    self.input_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-ls-requests-lsa"):
                                    self.input_ls_requests_lsa = value
                                    self.input_ls_requests_lsa.value_namespace = name_space
                                    self.input_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks"):
                                    self.input_lsa_acks = value
                                    self.input_lsa_acks.value_namespace = name_space
                                    self.input_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-acks-lsa"):
                                    self.input_lsa_acks_lsa = value
                                    self.input_lsa_acks_lsa.value_namespace = name_space
                                    self.input_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates"):
                                    self.input_lsa_updates = value
                                    self.input_lsa_updates.value_namespace = name_space
                                    self.input_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-lsa-updates-lsa"):
                                    self.input_lsa_updates_lsa = value
                                    self.input_lsa_updates_lsa.value_namespace = name_space
                                    self.input_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-packets"):
                                    self.input_packets = value
                                    self.input_packets.value_namespace = name_space
                                    self.input_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds"):
                                    self.output_db_ds = value
                                    self.output_db_ds.value_namespace = name_space
                                    self.output_db_ds.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-db-ds-lsa"):
                                    self.output_db_ds_lsa = value
                                    self.output_db_ds_lsa.value_namespace = name_space
                                    self.output_db_ds_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-hello-packets"):
                                    self.output_hello_packets = value
                                    self.output_hello_packets.value_namespace = name_space
                                    self.output_hello_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests"):
                                    self.output_ls_requests = value
                                    self.output_ls_requests.value_namespace = name_space
                                    self.output_ls_requests.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-ls-requests-lsa"):
                                    self.output_ls_requests_lsa = value
                                    self.output_ls_requests_lsa.value_namespace = name_space
                                    self.output_ls_requests_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks"):
                                    self.output_lsa_acks = value
                                    self.output_lsa_acks.value_namespace = name_space
                                    self.output_lsa_acks.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-acks-lsa"):
                                    self.output_lsa_acks_lsa = value
                                    self.output_lsa_acks_lsa.value_namespace = name_space
                                    self.output_lsa_acks_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates"):
                                    self.output_lsa_updates = value
                                    self.output_lsa_updates.value_namespace = name_space
                                    self.output_lsa_updates.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-lsa-updates-lsa"):
                                    self.output_lsa_updates_lsa = value
                                    self.output_lsa_updates_lsa.value_namespace = name_space
                                    self.output_lsa_updates_lsa.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-packets"):
                                    self.output_packets = value
                                    self.output_packets.value_namespace = name_space
                                    self.output_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.instance_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.instance_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ospfv3-protocol-instance" + "[instance-name='" + self.instance_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/ospfv3-protocol-instances/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.instance_name.is_set or self.instance_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.instance_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "instance-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "instance-name"):
                            self.instance_name = value
                            self.instance_name.value_namespace = name_space
                            self.instance_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ospfv3_protocol_instance:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ospfv3_protocol_instance:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ospfv3-protocol-instances" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/ospf/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ospfv3-protocol-instance"):
                        for c in self.ospfv3_protocol_instance:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ospfv3_protocol_instance.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ospfv3-protocol-instance"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.ospfv2_protocol_instances is not None and self.ospfv2_protocol_instances.has_data()) or
                    (self.ospfv3_protocol_instances is not None and self.ospfv3_protocol_instances.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ospfv2_protocol_instances is not None and self.ospfv2_protocol_instances.has_operation()) or
                    (self.ospfv3_protocol_instances is not None and self.ospfv3_protocol_instances.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ospf" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ospfv2-protocol-instances"):
                    if (self.ospfv2_protocol_instances is None):
                        self.ospfv2_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances()
                        self.ospfv2_protocol_instances.parent = self
                        self._children_name_map["ospfv2_protocol_instances"] = "ospfv2-protocol-instances"
                    return self.ospfv2_protocol_instances

                if (child_yang_name == "ospfv3-protocol-instances"):
                    if (self.ospfv3_protocol_instances is None):
                        self.ospfv3_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances()
                        self.ospfv3_protocol_instances.parent = self
                        self._children_name_map["ospfv3_protocol_instances"] = "ospfv3-protocol-instances"
                    return self.ospfv3_protocol_instances

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ospfv2-protocol-instances" or name == "ospfv3-protocol-instances"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.ldp_neighbors = PerfMgmt.Monitor.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self
                self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                self._children_yang_names.add("ldp-neighbors")


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

                    self.ldp_neighbor = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Mpls.LdpNeighbors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Mpls.LdpNeighbors, self).__setattr__(name, value)


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

                        self.nbr = YLeaf(YType.str, "nbr")

                        self.samples = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("nbr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "address_msgs_rcvd",
                                                "address_msgs_sent",
                                                "address_withdraw_msgs_rcvd",
                                                "address_withdraw_msgs_sent",
                                                "init_msgs_rcvd",
                                                "init_msgs_sent",
                                                "keepalive_msgs_rcvd",
                                                "keepalive_msgs_sent",
                                                "label_mapping_msgs_rcvd",
                                                "label_mapping_msgs_sent",
                                                "label_release_msgs_rcvd",
                                                "label_release_msgs_sent",
                                                "label_withdraw_msgs_rcvd",
                                                "label_withdraw_msgs_sent",
                                                "notification_msgs_rcvd",
                                                "notification_msgs_sent",
                                                "time_stamp",
                                                "total_msgs_rcvd",
                                                "total_msgs_sent") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.address_msgs_rcvd.is_set or
                                    self.address_msgs_sent.is_set or
                                    self.address_withdraw_msgs_rcvd.is_set or
                                    self.address_withdraw_msgs_sent.is_set or
                                    self.init_msgs_rcvd.is_set or
                                    self.init_msgs_sent.is_set or
                                    self.keepalive_msgs_rcvd.is_set or
                                    self.keepalive_msgs_sent.is_set or
                                    self.label_mapping_msgs_rcvd.is_set or
                                    self.label_mapping_msgs_sent.is_set or
                                    self.label_release_msgs_rcvd.is_set or
                                    self.label_release_msgs_sent.is_set or
                                    self.label_withdraw_msgs_rcvd.is_set or
                                    self.label_withdraw_msgs_sent.is_set or
                                    self.notification_msgs_rcvd.is_set or
                                    self.notification_msgs_sent.is_set or
                                    self.time_stamp.is_set or
                                    self.total_msgs_rcvd.is_set or
                                    self.total_msgs_sent.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.address_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.address_msgs_sent.yfilter != YFilter.not_set or
                                    self.address_withdraw_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.address_withdraw_msgs_sent.yfilter != YFilter.not_set or
                                    self.init_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.init_msgs_sent.yfilter != YFilter.not_set or
                                    self.keepalive_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.keepalive_msgs_sent.yfilter != YFilter.not_set or
                                    self.label_mapping_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.label_mapping_msgs_sent.yfilter != YFilter.not_set or
                                    self.label_release_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.label_release_msgs_sent.yfilter != YFilter.not_set or
                                    self.label_withdraw_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.label_withdraw_msgs_sent.yfilter != YFilter.not_set or
                                    self.notification_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.notification_msgs_sent.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set or
                                    self.total_msgs_rcvd.yfilter != YFilter.not_set or
                                    self.total_msgs_sent.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.address_msgs_rcvd.is_set or self.address_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_msgs_rcvd.get_name_leafdata())
                                if (self.address_msgs_sent.is_set or self.address_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_msgs_sent.get_name_leafdata())
                                if (self.address_withdraw_msgs_rcvd.is_set or self.address_withdraw_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_withdraw_msgs_rcvd.get_name_leafdata())
                                if (self.address_withdraw_msgs_sent.is_set or self.address_withdraw_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.address_withdraw_msgs_sent.get_name_leafdata())
                                if (self.init_msgs_rcvd.is_set or self.init_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.init_msgs_rcvd.get_name_leafdata())
                                if (self.init_msgs_sent.is_set or self.init_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.init_msgs_sent.get_name_leafdata())
                                if (self.keepalive_msgs_rcvd.is_set or self.keepalive_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.keepalive_msgs_rcvd.get_name_leafdata())
                                if (self.keepalive_msgs_sent.is_set or self.keepalive_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.keepalive_msgs_sent.get_name_leafdata())
                                if (self.label_mapping_msgs_rcvd.is_set or self.label_mapping_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_mapping_msgs_rcvd.get_name_leafdata())
                                if (self.label_mapping_msgs_sent.is_set or self.label_mapping_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_mapping_msgs_sent.get_name_leafdata())
                                if (self.label_release_msgs_rcvd.is_set or self.label_release_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_release_msgs_rcvd.get_name_leafdata())
                                if (self.label_release_msgs_sent.is_set or self.label_release_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_release_msgs_sent.get_name_leafdata())
                                if (self.label_withdraw_msgs_rcvd.is_set or self.label_withdraw_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_withdraw_msgs_rcvd.get_name_leafdata())
                                if (self.label_withdraw_msgs_sent.is_set or self.label_withdraw_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_withdraw_msgs_sent.get_name_leafdata())
                                if (self.notification_msgs_rcvd.is_set or self.notification_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.notification_msgs_rcvd.get_name_leafdata())
                                if (self.notification_msgs_sent.is_set or self.notification_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.notification_msgs_sent.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())
                                if (self.total_msgs_rcvd.is_set or self.total_msgs_rcvd.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_msgs_rcvd.get_name_leafdata())
                                if (self.total_msgs_sent.is_set or self.total_msgs_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.total_msgs_sent.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "address-msgs-rcvd" or name == "address-msgs-sent" or name == "address-withdraw-msgs-rcvd" or name == "address-withdraw-msgs-sent" or name == "init-msgs-rcvd" or name == "init-msgs-sent" or name == "keepalive-msgs-rcvd" or name == "keepalive-msgs-sent" or name == "label-mapping-msgs-rcvd" or name == "label-mapping-msgs-sent" or name == "label-release-msgs-rcvd" or name == "label-release-msgs-sent" or name == "label-withdraw-msgs-rcvd" or name == "label-withdraw-msgs-sent" or name == "notification-msgs-rcvd" or name == "notification-msgs-sent" or name == "time-stamp" or name == "total-msgs-rcvd" or name == "total-msgs-sent"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-msgs-rcvd"):
                                    self.address_msgs_rcvd = value
                                    self.address_msgs_rcvd.value_namespace = name_space
                                    self.address_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-msgs-sent"):
                                    self.address_msgs_sent = value
                                    self.address_msgs_sent.value_namespace = name_space
                                    self.address_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-withdraw-msgs-rcvd"):
                                    self.address_withdraw_msgs_rcvd = value
                                    self.address_withdraw_msgs_rcvd.value_namespace = name_space
                                    self.address_withdraw_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "address-withdraw-msgs-sent"):
                                    self.address_withdraw_msgs_sent = value
                                    self.address_withdraw_msgs_sent.value_namespace = name_space
                                    self.address_withdraw_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "init-msgs-rcvd"):
                                    self.init_msgs_rcvd = value
                                    self.init_msgs_rcvd.value_namespace = name_space
                                    self.init_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "init-msgs-sent"):
                                    self.init_msgs_sent = value
                                    self.init_msgs_sent.value_namespace = name_space
                                    self.init_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "keepalive-msgs-rcvd"):
                                    self.keepalive_msgs_rcvd = value
                                    self.keepalive_msgs_rcvd.value_namespace = name_space
                                    self.keepalive_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "keepalive-msgs-sent"):
                                    self.keepalive_msgs_sent = value
                                    self.keepalive_msgs_sent.value_namespace = name_space
                                    self.keepalive_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-mapping-msgs-rcvd"):
                                    self.label_mapping_msgs_rcvd = value
                                    self.label_mapping_msgs_rcvd.value_namespace = name_space
                                    self.label_mapping_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-mapping-msgs-sent"):
                                    self.label_mapping_msgs_sent = value
                                    self.label_mapping_msgs_sent.value_namespace = name_space
                                    self.label_mapping_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-release-msgs-rcvd"):
                                    self.label_release_msgs_rcvd = value
                                    self.label_release_msgs_rcvd.value_namespace = name_space
                                    self.label_release_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-release-msgs-sent"):
                                    self.label_release_msgs_sent = value
                                    self.label_release_msgs_sent.value_namespace = name_space
                                    self.label_release_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-withdraw-msgs-rcvd"):
                                    self.label_withdraw_msgs_rcvd = value
                                    self.label_withdraw_msgs_rcvd.value_namespace = name_space
                                    self.label_withdraw_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-withdraw-msgs-sent"):
                                    self.label_withdraw_msgs_sent = value
                                    self.label_withdraw_msgs_sent.value_namespace = name_space
                                    self.label_withdraw_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "notification-msgs-rcvd"):
                                    self.notification_msgs_rcvd = value
                                    self.notification_msgs_rcvd.value_namespace = name_space
                                    self.notification_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "notification-msgs-sent"):
                                    self.notification_msgs_sent = value
                                    self.notification_msgs_sent.value_namespace = name_space
                                    self.notification_msgs_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-msgs-rcvd"):
                                    self.total_msgs_rcvd = value
                                    self.total_msgs_rcvd.value_namespace = name_space
                                    self.total_msgs_rcvd.value_namespace_prefix = name_space_prefix
                                if(value_path == "total-msgs-sent"):
                                    self.total_msgs_sent = value
                                    self.total_msgs_sent.value_namespace = name_space
                                    self.total_msgs_sent.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.nbr.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.nbr.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ldp-neighbor" + "[nbr='" + self.nbr.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/mpls/ldp-neighbors/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.nbr.is_set or self.nbr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.nbr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "nbr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "nbr"):
                            self.nbr = value
                            self.nbr.value_namespace = name_space
                            self.nbr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ldp_neighbor:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ldp_neighbor:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ldp-neighbors" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/mpls/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ldp-neighbor"):
                        for c in self.ldp_neighbor:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ldp_neighbor.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ldp-neighbor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.ldp_neighbors is not None and self.ldp_neighbors.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.ldp_neighbors is not None and self.ldp_neighbors.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mpls" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "ldp-neighbors"):
                    if (self.ldp_neighbors is None):
                        self.ldp_neighbors = PerfMgmt.Monitor.Mpls.LdpNeighbors()
                        self.ldp_neighbors.parent = self
                        self._children_name_map["ldp_neighbors"] = "ldp-neighbors"
                    return self.ldp_neighbors

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ldp-neighbors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.node = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PerfMgmt.Monitor.Nodes, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PerfMgmt.Monitor.Nodes, self).__setattr__(name, value)


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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("node_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Nodes.Node, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Nodes.Node, self).__setattr__(name, value)


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

                        self.sample = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Nodes.Node.SampleXr, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Nodes.Node.SampleXr, self).__setattr__(name, value)


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

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                            self.no_processes = YLeaf(YType.uint32, "no-processes")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("sample_id",
                                            "average_cpu_used",
                                            "no_processes",
                                            "time_stamp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sample_id.is_set or
                                self.average_cpu_used.is_set or
                                self.no_processes.is_set or
                                self.time_stamp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sample_id.yfilter != YFilter.not_set or
                                self.average_cpu_used.yfilter != YFilter.not_set or
                                self.no_processes.yfilter != YFilter.not_set or
                                self.time_stamp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sample_id.get_name_leafdata())
                            if (self.average_cpu_used.is_set or self.average_cpu_used.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.average_cpu_used.get_name_leafdata())
                            if (self.no_processes.is_set or self.no_processes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.no_processes.get_name_leafdata())
                            if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample-id" or name == "average-cpu-used" or name == "no-processes" or name == "time-stamp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sample-id"):
                                self.sample_id = value
                                self.sample_id.value_namespace = name_space
                                self.sample_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "average-cpu-used"):
                                self.average_cpu_used = value
                                self.average_cpu_used.value_namespace = name_space
                                self.average_cpu_used.value_namespace_prefix = name_space_prefix
                            if(value_path == "no-processes"):
                                self.no_processes = value
                                self.no_processes.value_namespace = name_space
                                self.no_processes.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-stamp"):
                                self.time_stamp = value
                                self.time_stamp.value_namespace = name_space
                                self.time_stamp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sample:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sample:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sample-xr" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sample"):
                            for c in self.sample:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sample.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sample"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.process = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Nodes.Node.Processes, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Nodes.Node.Processes, self).__setattr__(name, value)


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

                            self.process_id = YLeaf(YType.int32, "process-id")

                            self.samples = PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                            self._children_yang_names.add("samples")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("process_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Nodes.Node.Processes.Process, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Nodes.Node.Processes.Process, self).__setattr__(name, value)


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

                                self.sample = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples, self).__setattr__(name, value)


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

                                    self.sample_id = YLeaf(YType.int32, "sample-id")

                                    self.average_cpu_used = YLeaf(YType.uint32, "average-cpu-used")

                                    self.no_threads = YLeaf(YType.uint32, "no-threads")

                                    self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                                    self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("sample_id",
                                                    "average_cpu_used",
                                                    "no_threads",
                                                    "peak_memory",
                                                    "time_stamp") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.sample_id.is_set or
                                        self.average_cpu_used.is_set or
                                        self.no_threads.is_set or
                                        self.peak_memory.is_set or
                                        self.time_stamp.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.sample_id.yfilter != YFilter.not_set or
                                        self.average_cpu_used.yfilter != YFilter.not_set or
                                        self.no_threads.yfilter != YFilter.not_set or
                                        self.peak_memory.yfilter != YFilter.not_set or
                                        self.time_stamp.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.sample_id.get_name_leafdata())
                                    if (self.average_cpu_used.is_set or self.average_cpu_used.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.average_cpu_used.get_name_leafdata())
                                    if (self.no_threads.is_set or self.no_threads.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.no_threads.get_name_leafdata())
                                    if (self.peak_memory.is_set or self.peak_memory.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peak_memory.get_name_leafdata())
                                    if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "sample-id" or name == "average-cpu-used" or name == "no-threads" or name == "peak-memory" or name == "time-stamp"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "sample-id"):
                                        self.sample_id = value
                                        self.sample_id.value_namespace = name_space
                                        self.sample_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "average-cpu-used"):
                                        self.average_cpu_used = value
                                        self.average_cpu_used.value_namespace = name_space
                                        self.average_cpu_used.value_namespace_prefix = name_space_prefix
                                    if(value_path == "no-threads"):
                                        self.no_threads = value
                                        self.no_threads.value_namespace = name_space
                                        self.no_threads.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peak-memory"):
                                        self.peak_memory = value
                                        self.peak_memory.value_namespace = name_space
                                        self.peak_memory.value_namespace_prefix = name_space_prefix
                                    if(value_path == "time-stamp"):
                                        self.time_stamp = value
                                        self.time_stamp.value_namespace = name_space
                                        self.time_stamp.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.sample:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.sample:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "samples" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "sample"):
                                    for c in self.sample:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.sample.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.process_id.is_set or
                                (self.samples is not None and self.samples.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.process_id.yfilter != YFilter.not_set or
                                (self.samples is not None and self.samples.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "process" + "[process-id='" + self.process_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.process_id.is_set or self.process_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.process_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "samples"):
                                if (self.samples is None):
                                    self.samples = PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples()
                                    self.samples.parent = self
                                    self._children_name_map["samples"] = "samples"
                                return self.samples

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "samples" or name == "process-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "process-id"):
                                self.process_id = value
                                self.process_id.value_namespace = name_space
                                self.process_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.process:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.process:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "processes" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "process"):
                            for c in self.process:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PerfMgmt.Monitor.Nodes.Node.Processes.Process()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.process.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "process"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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

                        self.sample = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Nodes.Node.Samples, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Nodes.Node.Samples, self).__setattr__(name, value)


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

                            self.sample_id = YLeaf(YType.int32, "sample-id")

                            self.curr_memory = YLeaf(YType.uint32, "curr-memory")

                            self.peak_memory = YLeaf(YType.uint32, "peak-memory")

                            self.time_stamp = YLeaf(YType.uint64, "time-stamp")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("sample_id",
                                            "curr_memory",
                                            "peak_memory",
                                            "time_stamp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Nodes.Node.Samples.Sample, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Nodes.Node.Samples.Sample, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.sample_id.is_set or
                                self.curr_memory.is_set or
                                self.peak_memory.is_set or
                                self.time_stamp.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.sample_id.yfilter != YFilter.not_set or
                                self.curr_memory.yfilter != YFilter.not_set or
                                self.peak_memory.yfilter != YFilter.not_set or
                                self.time_stamp.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.sample_id.get_name_leafdata())
                            if (self.curr_memory.is_set or self.curr_memory.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.curr_memory.get_name_leafdata())
                            if (self.peak_memory.is_set or self.peak_memory.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peak_memory.get_name_leafdata())
                            if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.time_stamp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample-id" or name == "curr-memory" or name == "peak-memory" or name == "time-stamp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "sample-id"):
                                self.sample_id = value
                                self.sample_id.value_namespace = name_space
                                self.sample_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "curr-memory"):
                                self.curr_memory = value
                                self.curr_memory.value_namespace = name_space
                                self.curr_memory.value_namespace_prefix = name_space_prefix
                            if(value_path == "peak-memory"):
                                self.peak_memory = value
                                self.peak_memory.value_namespace = name_space
                                self.peak_memory.value_namespace_prefix = name_space_prefix
                            if(value_path == "time-stamp"):
                                self.time_stamp = value
                                self.time_stamp.value_namespace = name_space
                                self.time_stamp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.sample:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.sample:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "samples" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "sample"):
                            for c in self.sample:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PerfMgmt.Monitor.Nodes.Node.Samples.Sample()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.sample.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "sample"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.node_id.is_set or
                        (self.processes is not None and self.processes.has_data()) or
                        (self.sample_xr is not None and self.sample_xr.has_data()) or
                        (self.samples is not None and self.samples.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.node_id.yfilter != YFilter.not_set or
                        (self.processes is not None and self.processes.has_operation()) or
                        (self.sample_xr is not None and self.sample_xr.has_operation()) or
                        (self.samples is not None and self.samples.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "node" + "[node-id='" + self.node_id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/nodes/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.node_id.is_set or self.node_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.node_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "processes"):
                        if (self.processes is None):
                            self.processes = PerfMgmt.Monitor.Nodes.Node.Processes()
                            self.processes.parent = self
                            self._children_name_map["processes"] = "processes"
                        return self.processes

                    if (child_yang_name == "sample-xr"):
                        if (self.sample_xr is None):
                            self.sample_xr = PerfMgmt.Monitor.Nodes.Node.SampleXr()
                            self.sample_xr.parent = self
                            self._children_name_map["sample_xr"] = "sample-xr"
                        return self.sample_xr

                    if (child_yang_name == "samples"):
                        if (self.samples is None):
                            self.samples = PerfMgmt.Monitor.Nodes.Node.Samples()
                            self.samples.parent = self
                            self._children_name_map["samples"] = "samples"
                        return self.samples

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "processes" or name == "sample-xr" or name == "samples" or name == "node-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "node-id"):
                        self.node_id = value
                        self.node_id.value_namespace = name_space
                        self.node_id.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.node:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.node:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nodes" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "node"):
                    for c in self.node:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = PerfMgmt.Monitor.Nodes.Node()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.node.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                self.bgp_neighbors = PerfMgmt.Monitor.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self
                self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                self._children_yang_names.add("bgp-neighbors")


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

                    self.bgp_neighbor = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Bgp.BgpNeighbors, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Bgp.BgpNeighbors, self).__setattr__(name, value)


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

                        self.ip_address = YLeaf(YType.str, "ip-address")

                        self.samples = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("ip_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "conn_dropped",
                                                "conn_established",
                                                "errors_received",
                                                "errors_sent",
                                                "input_messages",
                                                "input_update_messages",
                                                "output_messages",
                                                "output_update_messages",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.conn_dropped.is_set or
                                    self.conn_established.is_set or
                                    self.errors_received.is_set or
                                    self.errors_sent.is_set or
                                    self.input_messages.is_set or
                                    self.input_update_messages.is_set or
                                    self.output_messages.is_set or
                                    self.output_update_messages.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.conn_dropped.yfilter != YFilter.not_set or
                                    self.conn_established.yfilter != YFilter.not_set or
                                    self.errors_received.yfilter != YFilter.not_set or
                                    self.errors_sent.yfilter != YFilter.not_set or
                                    self.input_messages.yfilter != YFilter.not_set or
                                    self.input_update_messages.yfilter != YFilter.not_set or
                                    self.output_messages.yfilter != YFilter.not_set or
                                    self.output_update_messages.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.conn_dropped.is_set or self.conn_dropped.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.conn_dropped.get_name_leafdata())
                                if (self.conn_established.is_set or self.conn_established.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.conn_established.get_name_leafdata())
                                if (self.errors_received.is_set or self.errors_received.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.errors_received.get_name_leafdata())
                                if (self.errors_sent.is_set or self.errors_sent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.errors_sent.get_name_leafdata())
                                if (self.input_messages.is_set or self.input_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_messages.get_name_leafdata())
                                if (self.input_update_messages.is_set or self.input_update_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_update_messages.get_name_leafdata())
                                if (self.output_messages.is_set or self.output_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_messages.get_name_leafdata())
                                if (self.output_update_messages.is_set or self.output_update_messages.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_update_messages.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "conn-dropped" or name == "conn-established" or name == "errors-received" or name == "errors-sent" or name == "input-messages" or name == "input-update-messages" or name == "output-messages" or name == "output-update-messages" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "conn-dropped"):
                                    self.conn_dropped = value
                                    self.conn_dropped.value_namespace = name_space
                                    self.conn_dropped.value_namespace_prefix = name_space_prefix
                                if(value_path == "conn-established"):
                                    self.conn_established = value
                                    self.conn_established.value_namespace = name_space
                                    self.conn_established.value_namespace_prefix = name_space_prefix
                                if(value_path == "errors-received"):
                                    self.errors_received = value
                                    self.errors_received.value_namespace = name_space
                                    self.errors_received.value_namespace_prefix = name_space_prefix
                                if(value_path == "errors-sent"):
                                    self.errors_sent = value
                                    self.errors_sent.value_namespace = name_space
                                    self.errors_sent.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-messages"):
                                    self.input_messages = value
                                    self.input_messages.value_namespace = name_space
                                    self.input_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-update-messages"):
                                    self.input_update_messages = value
                                    self.input_update_messages.value_namespace = name_space
                                    self.input_update_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-messages"):
                                    self.output_messages = value
                                    self.output_messages.value_namespace = name_space
                                    self.output_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-update-messages"):
                                    self.output_update_messages = value
                                    self.output_update_messages.value_namespace = name_space
                                    self.output_update_messages.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.ip_address.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.ip_address.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bgp-neighbor" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/bgp/bgp-neighbors/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ip_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "ip-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "ip-address"):
                            self.ip_address = value
                            self.ip_address.value_namespace = name_space
                            self.ip_address.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bgp_neighbor:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bgp_neighbor:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bgp-neighbors" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/bgp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bgp-neighbor"):
                        for c in self.bgp_neighbor:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bgp_neighbor.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp-neighbor"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.bgp_neighbors is not None and self.bgp_neighbors.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.bgp_neighbors is not None and self.bgp_neighbors.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bgp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bgp-neighbors"):
                    if (self.bgp_neighbors is None):
                        self.bgp_neighbors = PerfMgmt.Monitor.Bgp.BgpNeighbors()
                        self.bgp_neighbors.parent = self
                        self._children_name_map["bgp_neighbors"] = "bgp-neighbors"
                    return self.bgp_neighbors

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgp-neighbors"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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

                    self.generic_counter_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces, self).__setattr__(name, value)


                class GenericCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "in_broadcast_pkts",
                                                "in_multicast_pkts",
                                                "in_octets",
                                                "in_packets",
                                                "in_ucast_pkts",
                                                "input_crc",
                                                "input_frame",
                                                "input_overrun",
                                                "input_queue_drops",
                                                "input_total_drops",
                                                "input_total_errors",
                                                "input_unknown_proto",
                                                "out_broadcast_pkts",
                                                "out_multicast_pkts",
                                                "out_octets",
                                                "out_packets",
                                                "out_ucast_pkts",
                                                "output_total_drops",
                                                "output_total_errors",
                                                "output_underrun",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.in_broadcast_pkts.is_set or
                                    self.in_multicast_pkts.is_set or
                                    self.in_octets.is_set or
                                    self.in_packets.is_set or
                                    self.in_ucast_pkts.is_set or
                                    self.input_crc.is_set or
                                    self.input_frame.is_set or
                                    self.input_overrun.is_set or
                                    self.input_queue_drops.is_set or
                                    self.input_total_drops.is_set or
                                    self.input_total_errors.is_set or
                                    self.input_unknown_proto.is_set or
                                    self.out_broadcast_pkts.is_set or
                                    self.out_multicast_pkts.is_set or
                                    self.out_octets.is_set or
                                    self.out_packets.is_set or
                                    self.out_ucast_pkts.is_set or
                                    self.output_total_drops.is_set or
                                    self.output_total_errors.is_set or
                                    self.output_underrun.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.in_broadcast_pkts.yfilter != YFilter.not_set or
                                    self.in_multicast_pkts.yfilter != YFilter.not_set or
                                    self.in_octets.yfilter != YFilter.not_set or
                                    self.in_packets.yfilter != YFilter.not_set or
                                    self.in_ucast_pkts.yfilter != YFilter.not_set or
                                    self.input_crc.yfilter != YFilter.not_set or
                                    self.input_frame.yfilter != YFilter.not_set or
                                    self.input_overrun.yfilter != YFilter.not_set or
                                    self.input_queue_drops.yfilter != YFilter.not_set or
                                    self.input_total_drops.yfilter != YFilter.not_set or
                                    self.input_total_errors.yfilter != YFilter.not_set or
                                    self.input_unknown_proto.yfilter != YFilter.not_set or
                                    self.out_broadcast_pkts.yfilter != YFilter.not_set or
                                    self.out_multicast_pkts.yfilter != YFilter.not_set or
                                    self.out_octets.yfilter != YFilter.not_set or
                                    self.out_packets.yfilter != YFilter.not_set or
                                    self.out_ucast_pkts.yfilter != YFilter.not_set or
                                    self.output_total_drops.yfilter != YFilter.not_set or
                                    self.output_total_errors.yfilter != YFilter.not_set or
                                    self.output_underrun.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.in_broadcast_pkts.is_set or self.in_broadcast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_broadcast_pkts.get_name_leafdata())
                                if (self.in_multicast_pkts.is_set or self.in_multicast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_multicast_pkts.get_name_leafdata())
                                if (self.in_octets.is_set or self.in_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_octets.get_name_leafdata())
                                if (self.in_packets.is_set or self.in_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_packets.get_name_leafdata())
                                if (self.in_ucast_pkts.is_set or self.in_ucast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_ucast_pkts.get_name_leafdata())
                                if (self.input_crc.is_set or self.input_crc.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_crc.get_name_leafdata())
                                if (self.input_frame.is_set or self.input_frame.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_frame.get_name_leafdata())
                                if (self.input_overrun.is_set or self.input_overrun.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_overrun.get_name_leafdata())
                                if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                                if (self.input_total_drops.is_set or self.input_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_drops.get_name_leafdata())
                                if (self.input_total_errors.is_set or self.input_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_errors.get_name_leafdata())
                                if (self.input_unknown_proto.is_set or self.input_unknown_proto.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_unknown_proto.get_name_leafdata())
                                if (self.out_broadcast_pkts.is_set or self.out_broadcast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_broadcast_pkts.get_name_leafdata())
                                if (self.out_multicast_pkts.is_set or self.out_multicast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_multicast_pkts.get_name_leafdata())
                                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                                if (self.out_packets.is_set or self.out_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_packets.get_name_leafdata())
                                if (self.out_ucast_pkts.is_set or self.out_ucast_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_ucast_pkts.get_name_leafdata())
                                if (self.output_total_drops.is_set or self.output_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_drops.get_name_leafdata())
                                if (self.output_total_errors.is_set or self.output_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_errors.get_name_leafdata())
                                if (self.output_underrun.is_set or self.output_underrun.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_underrun.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "in-broadcast-pkts" or name == "in-multicast-pkts" or name == "in-octets" or name == "in-packets" or name == "in-ucast-pkts" or name == "input-crc" or name == "input-frame" or name == "input-overrun" or name == "input-queue-drops" or name == "input-total-drops" or name == "input-total-errors" or name == "input-unknown-proto" or name == "out-broadcast-pkts" or name == "out-multicast-pkts" or name == "out-octets" or name == "out-packets" or name == "out-ucast-pkts" or name == "output-total-drops" or name == "output-total-errors" or name == "output-underrun" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-broadcast-pkts"):
                                    self.in_broadcast_pkts = value
                                    self.in_broadcast_pkts.value_namespace = name_space
                                    self.in_broadcast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-multicast-pkts"):
                                    self.in_multicast_pkts = value
                                    self.in_multicast_pkts.value_namespace = name_space
                                    self.in_multicast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-octets"):
                                    self.in_octets = value
                                    self.in_octets.value_namespace = name_space
                                    self.in_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-packets"):
                                    self.in_packets = value
                                    self.in_packets.value_namespace = name_space
                                    self.in_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-ucast-pkts"):
                                    self.in_ucast_pkts = value
                                    self.in_ucast_pkts.value_namespace = name_space
                                    self.in_ucast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-crc"):
                                    self.input_crc = value
                                    self.input_crc.value_namespace = name_space
                                    self.input_crc.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-frame"):
                                    self.input_frame = value
                                    self.input_frame.value_namespace = name_space
                                    self.input_frame.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-overrun"):
                                    self.input_overrun = value
                                    self.input_overrun.value_namespace = name_space
                                    self.input_overrun.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-queue-drops"):
                                    self.input_queue_drops = value
                                    self.input_queue_drops.value_namespace = name_space
                                    self.input_queue_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-drops"):
                                    self.input_total_drops = value
                                    self.input_total_drops.value_namespace = name_space
                                    self.input_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-errors"):
                                    self.input_total_errors = value
                                    self.input_total_errors.value_namespace = name_space
                                    self.input_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-unknown-proto"):
                                    self.input_unknown_proto = value
                                    self.input_unknown_proto.value_namespace = name_space
                                    self.input_unknown_proto.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-broadcast-pkts"):
                                    self.out_broadcast_pkts = value
                                    self.out_broadcast_pkts.value_namespace = name_space
                                    self.out_broadcast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-multicast-pkts"):
                                    self.out_multicast_pkts = value
                                    self.out_multicast_pkts.value_namespace = name_space
                                    self.out_multicast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-octets"):
                                    self.out_octets = value
                                    self.out_octets.value_namespace = name_space
                                    self.out_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-packets"):
                                    self.out_packets = value
                                    self.out_packets.value_namespace = name_space
                                    self.out_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-ucast-pkts"):
                                    self.out_ucast_pkts = value
                                    self.out_ucast_pkts.value_namespace = name_space
                                    self.out_ucast_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-drops"):
                                    self.output_total_drops = value
                                    self.output_total_drops.value_namespace = name_space
                                    self.output_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-errors"):
                                    self.output_total_errors = value
                                    self.output_total_errors.value_namespace = name_space
                                    self.output_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-underrun"):
                                    self.output_underrun = value
                                    self.output_underrun.value_namespace = name_space
                                    self.output_underrun.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "generic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/generic-counter-interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.generic_counter_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.generic_counter_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "generic-counter-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "generic-counter-interface"):
                        for c in self.generic_counter_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.generic_counter_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "generic-counter-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.basic_counter_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces, self).__setattr__(name, value)


                class BasicCounterInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "in_octets",
                                                "in_packets",
                                                "input_queue_drops",
                                                "input_total_drops",
                                                "input_total_errors",
                                                "out_octets",
                                                "out_packets",
                                                "output_queue_drops",
                                                "output_total_drops",
                                                "output_total_errors",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.in_octets.is_set or
                                    self.in_packets.is_set or
                                    self.input_queue_drops.is_set or
                                    self.input_total_drops.is_set or
                                    self.input_total_errors.is_set or
                                    self.out_octets.is_set or
                                    self.out_packets.is_set or
                                    self.output_queue_drops.is_set or
                                    self.output_total_drops.is_set or
                                    self.output_total_errors.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.in_octets.yfilter != YFilter.not_set or
                                    self.in_packets.yfilter != YFilter.not_set or
                                    self.input_queue_drops.yfilter != YFilter.not_set or
                                    self.input_total_drops.yfilter != YFilter.not_set or
                                    self.input_total_errors.yfilter != YFilter.not_set or
                                    self.out_octets.yfilter != YFilter.not_set or
                                    self.out_packets.yfilter != YFilter.not_set or
                                    self.output_queue_drops.yfilter != YFilter.not_set or
                                    self.output_total_drops.yfilter != YFilter.not_set or
                                    self.output_total_errors.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.in_octets.is_set or self.in_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_octets.get_name_leafdata())
                                if (self.in_packets.is_set or self.in_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.in_packets.get_name_leafdata())
                                if (self.input_queue_drops.is_set or self.input_queue_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_queue_drops.get_name_leafdata())
                                if (self.input_total_drops.is_set or self.input_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_drops.get_name_leafdata())
                                if (self.input_total_errors.is_set or self.input_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_total_errors.get_name_leafdata())
                                if (self.out_octets.is_set or self.out_octets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_octets.get_name_leafdata())
                                if (self.out_packets.is_set or self.out_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.out_packets.get_name_leafdata())
                                if (self.output_queue_drops.is_set or self.output_queue_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_queue_drops.get_name_leafdata())
                                if (self.output_total_drops.is_set or self.output_total_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_drops.get_name_leafdata())
                                if (self.output_total_errors.is_set or self.output_total_errors.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_total_errors.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "in-octets" or name == "in-packets" or name == "input-queue-drops" or name == "input-total-drops" or name == "input-total-errors" or name == "out-octets" or name == "out-packets" or name == "output-queue-drops" or name == "output-total-drops" or name == "output-total-errors" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-octets"):
                                    self.in_octets = value
                                    self.in_octets.value_namespace = name_space
                                    self.in_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "in-packets"):
                                    self.in_packets = value
                                    self.in_packets.value_namespace = name_space
                                    self.in_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-queue-drops"):
                                    self.input_queue_drops = value
                                    self.input_queue_drops.value_namespace = name_space
                                    self.input_queue_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-drops"):
                                    self.input_total_drops = value
                                    self.input_total_drops.value_namespace = name_space
                                    self.input_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-total-errors"):
                                    self.input_total_errors = value
                                    self.input_total_errors.value_namespace = name_space
                                    self.input_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-octets"):
                                    self.out_octets = value
                                    self.out_octets.value_namespace = name_space
                                    self.out_octets.value_namespace_prefix = name_space_prefix
                                if(value_path == "out-packets"):
                                    self.out_packets = value
                                    self.out_packets.value_namespace = name_space
                                    self.out_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-queue-drops"):
                                    self.output_queue_drops = value
                                    self.output_queue_drops.value_namespace = name_space
                                    self.output_queue_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-drops"):
                                    self.output_total_drops = value
                                    self.output_total_drops.value_namespace = name_space
                                    self.output_total_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-total-errors"):
                                    self.output_total_errors = value
                                    self.output_total_errors.value_namespace = name_space
                                    self.output_total_errors.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "basic-counter-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/basic-counter-interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.basic_counter_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.basic_counter_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "basic-counter-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "basic-counter-interface"):
                        for c in self.basic_counter_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.basic_counter_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "basic-counter-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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

                    self.data_rate_interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PerfMgmt.Monitor.Interface.DataRateInterfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PerfMgmt.Monitor.Interface.DataRateInterfaces, self).__setattr__(name, value)


                class DataRateInterface(Entity):
                    """
                    Samples for a particular interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface Name
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
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

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.samples = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self
                        self._children_name_map["samples"] = "samples"
                        self._children_yang_names.add("samples")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface, self).__setattr__(name, value)


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

                            self.sample = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples, self).__setattr__(name, value)


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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("sample_id",
                                                "bandwidth",
                                                "input_data_rate",
                                                "input_packet_rate",
                                                "input_peak_pkts",
                                                "input_peak_rate",
                                                "output_data_rate",
                                                "output_packet_rate",
                                                "output_peak_pkts",
                                                "output_peak_rate",
                                                "time_stamp") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.sample_id.is_set or
                                    self.bandwidth.is_set or
                                    self.input_data_rate.is_set or
                                    self.input_packet_rate.is_set or
                                    self.input_peak_pkts.is_set or
                                    self.input_peak_rate.is_set or
                                    self.output_data_rate.is_set or
                                    self.output_packet_rate.is_set or
                                    self.output_peak_pkts.is_set or
                                    self.output_peak_rate.is_set or
                                    self.time_stamp.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.sample_id.yfilter != YFilter.not_set or
                                    self.bandwidth.yfilter != YFilter.not_set or
                                    self.input_data_rate.yfilter != YFilter.not_set or
                                    self.input_packet_rate.yfilter != YFilter.not_set or
                                    self.input_peak_pkts.yfilter != YFilter.not_set or
                                    self.input_peak_rate.yfilter != YFilter.not_set or
                                    self.output_data_rate.yfilter != YFilter.not_set or
                                    self.output_packet_rate.yfilter != YFilter.not_set or
                                    self.output_peak_pkts.yfilter != YFilter.not_set or
                                    self.output_peak_rate.yfilter != YFilter.not_set or
                                    self.time_stamp.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sample" + "[sample-id='" + self.sample_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.sample_id.is_set or self.sample_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sample_id.get_name_leafdata())
                                if (self.bandwidth.is_set or self.bandwidth.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.bandwidth.get_name_leafdata())
                                if (self.input_data_rate.is_set or self.input_data_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_data_rate.get_name_leafdata())
                                if (self.input_packet_rate.is_set or self.input_packet_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_packet_rate.get_name_leafdata())
                                if (self.input_peak_pkts.is_set or self.input_peak_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_peak_pkts.get_name_leafdata())
                                if (self.input_peak_rate.is_set or self.input_peak_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.input_peak_rate.get_name_leafdata())
                                if (self.output_data_rate.is_set or self.output_data_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_data_rate.get_name_leafdata())
                                if (self.output_packet_rate.is_set or self.output_packet_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_packet_rate.get_name_leafdata())
                                if (self.output_peak_pkts.is_set or self.output_peak_pkts.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_peak_pkts.get_name_leafdata())
                                if (self.output_peak_rate.is_set or self.output_peak_rate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.output_peak_rate.get_name_leafdata())
                                if (self.time_stamp.is_set or self.time_stamp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time_stamp.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "sample-id" or name == "bandwidth" or name == "input-data-rate" or name == "input-packet-rate" or name == "input-peak-pkts" or name == "input-peak-rate" or name == "output-data-rate" or name == "output-packet-rate" or name == "output-peak-pkts" or name == "output-peak-rate" or name == "time-stamp"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "sample-id"):
                                    self.sample_id = value
                                    self.sample_id.value_namespace = name_space
                                    self.sample_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "bandwidth"):
                                    self.bandwidth = value
                                    self.bandwidth.value_namespace = name_space
                                    self.bandwidth.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-data-rate"):
                                    self.input_data_rate = value
                                    self.input_data_rate.value_namespace = name_space
                                    self.input_data_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-packet-rate"):
                                    self.input_packet_rate = value
                                    self.input_packet_rate.value_namespace = name_space
                                    self.input_packet_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-peak-pkts"):
                                    self.input_peak_pkts = value
                                    self.input_peak_pkts.value_namespace = name_space
                                    self.input_peak_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "input-peak-rate"):
                                    self.input_peak_rate = value
                                    self.input_peak_rate.value_namespace = name_space
                                    self.input_peak_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-data-rate"):
                                    self.output_data_rate = value
                                    self.output_data_rate.value_namespace = name_space
                                    self.output_data_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-packet-rate"):
                                    self.output_packet_rate = value
                                    self.output_packet_rate.value_namespace = name_space
                                    self.output_packet_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-peak-pkts"):
                                    self.output_peak_pkts = value
                                    self.output_peak_pkts.value_namespace = name_space
                                    self.output_peak_pkts.value_namespace_prefix = name_space_prefix
                                if(value_path == "output-peak-rate"):
                                    self.output_peak_rate = value
                                    self.output_peak_rate.value_namespace = name_space
                                    self.output_peak_rate.value_namespace_prefix = name_space_prefix
                                if(value_path == "time-stamp"):
                                    self.time_stamp = value
                                    self.time_stamp.value_namespace = name_space
                                    self.time_stamp.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.sample:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.sample:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "samples" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sample"):
                                for c in self.sample:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.sample.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sample"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            (self.samples is not None and self.samples.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            (self.samples is not None and self.samples.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "data-rate-interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/data-rate-interfaces/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "samples"):
                            if (self.samples is None):
                                self.samples = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples()
                                self.samples.parent = self
                                self._children_name_map["samples"] = "samples"
                            return self.samples

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "samples" or name == "interface-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.data_rate_interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.data_rate_interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "data-rate-interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/interface/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "data-rate-interface"):
                        for c in self.data_rate_interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.data_rate_interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "data-rate-interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    (self.basic_counter_interfaces is not None and self.basic_counter_interfaces.has_data()) or
                    (self.data_rate_interfaces is not None and self.data_rate_interfaces.has_data()) or
                    (self.generic_counter_interfaces is not None and self.generic_counter_interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.basic_counter_interfaces is not None and self.basic_counter_interfaces.has_operation()) or
                    (self.data_rate_interfaces is not None and self.data_rate_interfaces.has_operation()) or
                    (self.generic_counter_interfaces is not None and self.generic_counter_interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/monitor/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "basic-counter-interfaces"):
                    if (self.basic_counter_interfaces is None):
                        self.basic_counter_interfaces = PerfMgmt.Monitor.Interface.BasicCounterInterfaces()
                        self.basic_counter_interfaces.parent = self
                        self._children_name_map["basic_counter_interfaces"] = "basic-counter-interfaces"
                    return self.basic_counter_interfaces

                if (child_yang_name == "data-rate-interfaces"):
                    if (self.data_rate_interfaces is None):
                        self.data_rate_interfaces = PerfMgmt.Monitor.Interface.DataRateInterfaces()
                        self.data_rate_interfaces.parent = self
                        self._children_name_map["data_rate_interfaces"] = "data-rate-interfaces"
                    return self.data_rate_interfaces

                if (child_yang_name == "generic-counter-interfaces"):
                    if (self.generic_counter_interfaces is None):
                        self.generic_counter_interfaces = PerfMgmt.Monitor.Interface.GenericCounterInterfaces()
                        self.generic_counter_interfaces.parent = self
                        self._children_name_map["generic_counter_interfaces"] = "generic-counter-interfaces"
                    return self.generic_counter_interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "basic-counter-interfaces" or name == "data-rate-interfaces" or name == "generic-counter-interfaces"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.bgp is not None and self.bgp.has_data()) or
                (self.interface is not None and self.interface.has_data()) or
                (self.mpls is not None and self.mpls.has_data()) or
                (self.nodes is not None and self.nodes.has_data()) or
                (self.ospf is not None and self.ospf.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.bgp is not None and self.bgp.has_operation()) or
                (self.interface is not None and self.interface.has_operation()) or
                (self.mpls is not None and self.mpls.has_operation()) or
                (self.nodes is not None and self.nodes.has_operation()) or
                (self.ospf is not None and self.ospf.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "monitor" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgp"):
                if (self.bgp is None):
                    self.bgp = PerfMgmt.Monitor.Bgp()
                    self.bgp.parent = self
                    self._children_name_map["bgp"] = "bgp"
                return self.bgp

            if (child_yang_name == "interface"):
                if (self.interface is None):
                    self.interface = PerfMgmt.Monitor.Interface()
                    self.interface.parent = self
                    self._children_name_map["interface"] = "interface"
                return self.interface

            if (child_yang_name == "mpls"):
                if (self.mpls is None):
                    self.mpls = PerfMgmt.Monitor.Mpls()
                    self.mpls.parent = self
                    self._children_name_map["mpls"] = "mpls"
                return self.mpls

            if (child_yang_name == "nodes"):
                if (self.nodes is None):
                    self.nodes = PerfMgmt.Monitor.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                return self.nodes

            if (child_yang_name == "ospf"):
                if (self.ospf is None):
                    self.ospf = PerfMgmt.Monitor.Ospf()
                    self.ospf.parent = self
                    self._children_name_map["ospf"] = "ospf"
                return self.ospf

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgp" or name == "interface" or name == "mpls" or name == "nodes" or name == "ospf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.monitor is not None and self.monitor.has_data()) or
            (self.periodic is not None and self.periodic.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.monitor is not None and self.monitor.has_operation()) or
            (self.periodic is not None and self.periodic.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "monitor"):
            if (self.monitor is None):
                self.monitor = PerfMgmt.Monitor()
                self.monitor.parent = self
                self._children_name_map["monitor"] = "monitor"
            return self.monitor

        if (child_yang_name == "periodic"):
            if (self.periodic is None):
                self.periodic = PerfMgmt.Periodic()
                self.periodic.parent = self
                self._children_name_map["periodic"] = "periodic"
            return self.periodic

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "monitor" or name == "periodic"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PerfMgmt()
        return self._top_entity

