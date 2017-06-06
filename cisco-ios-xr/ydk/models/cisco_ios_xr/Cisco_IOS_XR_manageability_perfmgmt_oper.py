""" Cisco_IOS_XR_manageability_perfmgmt_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-perfmgmt package operational data.

This module contains definitions
for the following management objects\:
  perf\-mgmt\: Performance Management agent operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PerfMgmt(object):
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
        self.monitor = PerfMgmt.Monitor()
        self.monitor.parent = self
        self.periodic = PerfMgmt.Periodic()
        self.periodic.parent = self


    class Periodic(object):
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
            self.parent = None
            self.bgp = PerfMgmt.Periodic.Bgp()
            self.bgp.parent = self
            self.interface = PerfMgmt.Periodic.Interface()
            self.interface.parent = self
            self.mpls = PerfMgmt.Periodic.Mpls()
            self.mpls.parent = self
            self.nodes = PerfMgmt.Periodic.Nodes()
            self.nodes.parent = self
            self.ospf = PerfMgmt.Periodic.Ospf()
            self.ospf.parent = self


        class Ospf(object):
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
                self.parent = None
                self.ospfv2_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self.ospfv3_protocol_instances = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self


            class Ospfv2ProtocolInstances(object):
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
                    self.parent = None
                    self.ospfv2_protocol_instance = YList()
                    self.ospfv2_protocol_instance.parent = self
                    self.ospfv2_protocol_instance.name = 'ospfv2_protocol_instance'


                class Ospfv2ProtocolInstance(object):
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
                        self.parent = None
                        self.instance_name = None
                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Sample Table for an OSPV v2 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.checksum_errors = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.input_hello_packets = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.input_packets = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.output_hello_packets = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.output_packets = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.checksum_errors is not None:
                                    return True

                                if self.input_db_ds is not None:
                                    return True

                                if self.input_db_ds_lsa is not None:
                                    return True

                                if self.input_hello_packets is not None:
                                    return True

                                if self.input_ls_requests is not None:
                                    return True

                                if self.input_ls_requests_lsa is not None:
                                    return True

                                if self.input_lsa_acks is not None:
                                    return True

                                if self.input_lsa_acks_lsa is not None:
                                    return True

                                if self.input_lsa_updates is not None:
                                    return True

                                if self.input_lsa_updates_lsa is not None:
                                    return True

                                if self.input_packets is not None:
                                    return True

                                if self.output_db_ds is not None:
                                    return True

                                if self.output_db_ds_lsa is not None:
                                    return True

                                if self.output_hello_packets is not None:
                                    return True

                                if self.output_ls_requests is not None:
                                    return True

                                if self.output_ls_requests_lsa is not None:
                                    return True

                                if self.output_lsa_acks is not None:
                                    return True

                                if self.output_lsa_acks_lsa is not None:
                                    return True

                                if self.output_lsa_updates is not None:
                                    return True

                                if self.output_lsa_updates_lsa is not None:
                                    return True

                                if self.output_packets is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.instance_name is None:
                            raise YPYModelError('Key property instance_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv2-protocol-instances/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv2-protocol-instance[Cisco-IOS-XR-manageability-perfmgmt-oper:instance-name = ' + str(self.instance_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.instance_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv2-protocol-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ospfv2_protocol_instance is not None:
                        for child_ref in self.ospfv2_protocol_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv2ProtocolInstances']['meta_info']


            class Ospfv3ProtocolInstances(object):
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
                    self.parent = None
                    self.ospfv3_protocol_instance = YList()
                    self.ospfv3_protocol_instance.parent = self
                    self.ospfv3_protocol_instance.name = 'ospfv3_protocol_instance'


                class Ospfv3ProtocolInstance(object):
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
                        self.parent = None
                        self.instance_name = None
                        self.samples = PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Sample Table for an OSPV v3 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.input_hello_packets = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.input_packets = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.output_hello_packets = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.output_packets = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.input_db_ds is not None:
                                    return True

                                if self.input_db_ds_lsa is not None:
                                    return True

                                if self.input_hello_packets is not None:
                                    return True

                                if self.input_ls_requests is not None:
                                    return True

                                if self.input_ls_requests_lsa is not None:
                                    return True

                                if self.input_lsa_acks is not None:
                                    return True

                                if self.input_lsa_acks_lsa is not None:
                                    return True

                                if self.input_lsa_updates is not None:
                                    return True

                                if self.input_lsa_updates_lsa is not None:
                                    return True

                                if self.input_packets is not None:
                                    return True

                                if self.output_db_ds is not None:
                                    return True

                                if self.output_db_ds_lsa is not None:
                                    return True

                                if self.output_hello_packets is not None:
                                    return True

                                if self.output_ls_requests is not None:
                                    return True

                                if self.output_ls_requests_lsa is not None:
                                    return True

                                if self.output_lsa_acks is not None:
                                    return True

                                if self.output_lsa_acks_lsa is not None:
                                    return True

                                if self.output_lsa_updates is not None:
                                    return True

                                if self.output_lsa_updates_lsa is not None:
                                    return True

                                if self.output_packets is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.instance_name is None:
                            raise YPYModelError('Key property instance_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv3-protocol-instances/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv3-protocol-instance[Cisco-IOS-XR-manageability-perfmgmt-oper:instance-name = ' + str(self.instance_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.instance_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv3-protocol-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ospfv3_protocol_instance is not None:
                        for child_ref in self.ospfv3_protocol_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Ospf.Ospfv3ProtocolInstances']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfv2_protocol_instances is not None and self.ospfv2_protocol_instances._has_data():
                    return True

                if self.ospfv3_protocol_instances is not None and self.ospfv3_protocol_instances._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Periodic.Ospf']['meta_info']


        class Mpls(object):
            """
            Collected MPLS data
            
            .. attribute:: ldp_neighbors
            
            	LDP neighbors for which statistics are collected
            	**type**\:   :py:class:`LdpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ldp_neighbors = PerfMgmt.Periodic.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self


            class LdpNeighbors(object):
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
                    self.parent = None
                    self.ldp_neighbor = YList()
                    self.ldp_neighbor.parent = self
                    self.ldp_neighbor.name = 'ldp_neighbor'


                class LdpNeighbor(object):
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
                        self.parent = None
                        self.nbr = None
                        self.samples = PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Samples for a particular LDP neighbor
                        
                        .. attribute:: sample
                        
                        	LDP neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.address_msgs_rcvd = None
                                self.address_msgs_sent = None
                                self.address_withdraw_msgs_rcvd = None
                                self.address_withdraw_msgs_sent = None
                                self.init_msgs_rcvd = None
                                self.init_msgs_sent = None
                                self.keepalive_msgs_rcvd = None
                                self.keepalive_msgs_sent = None
                                self.label_mapping_msgs_rcvd = None
                                self.label_mapping_msgs_sent = None
                                self.label_release_msgs_rcvd = None
                                self.label_release_msgs_sent = None
                                self.label_withdraw_msgs_rcvd = None
                                self.label_withdraw_msgs_sent = None
                                self.notification_msgs_rcvd = None
                                self.notification_msgs_sent = None
                                self.time_stamp = None
                                self.total_msgs_rcvd = None
                                self.total_msgs_sent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.address_msgs_rcvd is not None:
                                    return True

                                if self.address_msgs_sent is not None:
                                    return True

                                if self.address_withdraw_msgs_rcvd is not None:
                                    return True

                                if self.address_withdraw_msgs_sent is not None:
                                    return True

                                if self.init_msgs_rcvd is not None:
                                    return True

                                if self.init_msgs_sent is not None:
                                    return True

                                if self.keepalive_msgs_rcvd is not None:
                                    return True

                                if self.keepalive_msgs_sent is not None:
                                    return True

                                if self.label_mapping_msgs_rcvd is not None:
                                    return True

                                if self.label_mapping_msgs_sent is not None:
                                    return True

                                if self.label_release_msgs_rcvd is not None:
                                    return True

                                if self.label_release_msgs_sent is not None:
                                    return True

                                if self.label_withdraw_msgs_rcvd is not None:
                                    return True

                                if self.label_withdraw_msgs_sent is not None:
                                    return True

                                if self.notification_msgs_rcvd is not None:
                                    return True

                                if self.notification_msgs_sent is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                if self.total_msgs_rcvd is not None:
                                    return True

                                if self.total_msgs_sent is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.nbr is None:
                            raise YPYModelError('Key property nbr is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:mpls/Cisco-IOS-XR-manageability-perfmgmt-oper:ldp-neighbors/Cisco-IOS-XR-manageability-perfmgmt-oper:ldp-neighbor[Cisco-IOS-XR-manageability-perfmgmt-oper:nbr = ' + str(self.nbr) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nbr is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors.LdpNeighbor']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:mpls/Cisco-IOS-XR-manageability-perfmgmt-oper:ldp-neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ldp_neighbor is not None:
                        for child_ref in self.ldp_neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Mpls.LdpNeighbors']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:mpls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ldp_neighbors is not None and self.ldp_neighbors._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Periodic.Mpls']['meta_info']


        class Nodes(object):
            """
            Nodes for which data is collected
            
            .. attribute:: node
            
            	Node Instance
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
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
                    self.parent = None
                    self.node_id = None
                    self.processes = PerfMgmt.Periodic.Nodes.Node.Processes()
                    self.processes.parent = self
                    self.sample_xr = PerfMgmt.Periodic.Nodes.Node.SampleXr()
                    self.sample_xr.parent = self
                    self.samples = PerfMgmt.Periodic.Nodes.Node.Samples()
                    self.samples.parent = self


                class SampleXr(object):
                    """
                    Node CPU data
                    
                    .. attribute:: sample
                    
                    	Node CPU data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sample = YList()
                        self.sample.parent = self
                        self.sample.name = 'sample'


                    class Sample(object):
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
                            self.parent = None
                            self.sample_id = None
                            self.average_cpu_used = None
                            self.no_processes = None
                            self.time_stamp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sample_id is None:
                                raise YPYModelError('Key property sample_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample_id is not None:
                                return True

                            if self.average_cpu_used is not None:
                                return True

                            if self.no_processes is not None:
                                return True

                            if self.time_stamp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.SampleXr.Sample']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample-xr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sample is not None:
                            for child_ref in self.sample:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.SampleXr']['meta_info']


                class Processes(object):
                    """
                    Processes data
                    
                    .. attribute:: process
                    
                    	Process data
                    	**type**\: list of    :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.process = YList()
                        self.process.parent = self
                        self.process.name = 'process'


                    class Process(object):
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
                            self.parent = None
                            self.process_id = None
                            self.samples = PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self


                        class Samples(object):
                            """
                            Process data
                            
                            .. attribute:: sample
                            
                            	Process data sample
                            	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sample = YList()
                                self.sample.parent = self
                                self.sample.name = 'sample'


                            class Sample(object):
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
                                    self.parent = None
                                    self.sample_id = None
                                    self.average_cpu_used = None
                                    self.no_threads = None
                                    self.peak_memory = None
                                    self.time_stamp = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.sample_id is None:
                                        raise YPYModelError('Key property sample_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sample_id is not None:
                                        return True

                                    if self.average_cpu_used is not None:
                                        return True

                                    if self.no_threads is not None:
                                        return True

                                    if self.peak_memory is not None:
                                        return True

                                    if self.time_stamp is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                    return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples.Sample']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample is not None:
                                    for child_ref in self.sample:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process.Samples']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.process_id is None:
                                raise YPYModelError('Key property process_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:process[Cisco-IOS-XR-manageability-perfmgmt-oper:process-id = ' + str(self.process_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.process_id is not None:
                                return True

                            if self.samples is not None and self.samples._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.Processes.Process']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:processes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.process is not None:
                            for child_ref in self.process:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.Processes']['meta_info']


                class Samples(object):
                    """
                    Node Memory data
                    
                    .. attribute:: sample
                    
                    	Node Memory data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Nodes.Node.Samples.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sample = YList()
                        self.sample.parent = self
                        self.sample.name = 'sample'


                    class Sample(object):
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
                            self.parent = None
                            self.sample_id = None
                            self.curr_memory = None
                            self.peak_memory = None
                            self.time_stamp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sample_id is None:
                                raise YPYModelError('Key property sample_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample_id is not None:
                                return True

                            if self.curr_memory is not None:
                                return True

                            if self.peak_memory is not None:
                                return True

                            if self.time_stamp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.Samples.Sample']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sample is not None:
                            for child_ref in self.sample:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Nodes.Node.Samples']['meta_info']

                @property
                def _common_path(self):
                    if self.node_id is None:
                        raise YPYModelError('Key property node_id is None')

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:nodes/Cisco-IOS-XR-manageability-perfmgmt-oper:node[Cisco-IOS-XR-manageability-perfmgmt-oper:node-id = ' + str(self.node_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_id is not None:
                        return True

                    if self.processes is not None and self.processes._has_data():
                        return True

                    if self.sample_xr is not None and self.sample_xr._has_data():
                        return True

                    if self.samples is not None and self.samples._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:nodes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    for child_ref in self.node:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Periodic.Nodes']['meta_info']


        class Bgp(object):
            """
            Collected BGP data
            
            .. attribute:: bgp_neighbors
            
            	Neighbors for which statistics are collected
            	**type**\:   :py:class:`BgpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bgp_neighbors = PerfMgmt.Periodic.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self


            class BgpNeighbors(object):
                """
                Neighbors for which statistics are collected
                
                .. attribute:: bgp_neighbor
                
                	Samples for particular neighbor
                	**type**\: list of    :py:class:`BgpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bgp_neighbor = YList()
                    self.bgp_neighbor.parent = self
                    self.bgp_neighbor.name = 'bgp_neighbor'


                class BgpNeighbor(object):
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
                        self.parent = None
                        self.ip_address = None
                        self.samples = PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Sample Table for a BGP neighbor
                        
                        .. attribute:: sample
                        
                        	Neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.conn_dropped = None
                                self.conn_established = None
                                self.errors_received = None
                                self.errors_sent = None
                                self.input_messages = None
                                self.input_update_messages = None
                                self.output_messages = None
                                self.output_update_messages = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.conn_dropped is not None:
                                    return True

                                if self.conn_established is not None:
                                    return True

                                if self.errors_received is not None:
                                    return True

                                if self.errors_sent is not None:
                                    return True

                                if self.input_messages is not None:
                                    return True

                                if self.input_update_messages is not None:
                                    return True

                                if self.output_messages is not None:
                                    return True

                                if self.output_update_messages is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.ip_address is None:
                            raise YPYModelError('Key property ip_address is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp-neighbors/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp-neighbor[Cisco-IOS-XR-manageability-perfmgmt-oper:ip-address = ' + str(self.ip_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ip_address is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors.BgpNeighbor']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp-neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bgp_neighbor is not None:
                        for child_ref in self.bgp_neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Bgp.BgpNeighbors']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgp_neighbors is not None and self.bgp_neighbors._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Periodic.Bgp']['meta_info']


        class Interface(object):
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
                self.parent = None
                self.basic_counter_interfaces = PerfMgmt.Periodic.Interface.BasicCounterInterfaces()
                self.basic_counter_interfaces.parent = self
                self.data_rate_interfaces = PerfMgmt.Periodic.Interface.DataRateInterfaces()
                self.data_rate_interfaces.parent = self
                self.generic_counter_interfaces = PerfMgmt.Periodic.Interface.GenericCounterInterfaces()
                self.generic_counter_interfaces.parent = self


            class GenericCounterInterfaces(object):
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
                    self.parent = None
                    self.generic_counter_interface = YList()
                    self.generic_counter_interface.parent = self
                    self.generic_counter_interface.name = 'generic_counter_interface'


                class GenericCounterInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.samples = PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Generic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.in_broadcast_pkts = None
                                self.in_multicast_pkts = None
                                self.in_octets = None
                                self.in_packets = None
                                self.in_ucast_pkts = None
                                self.input_crc = None
                                self.input_frame = None
                                self.input_overrun = None
                                self.input_queue_drops = None
                                self.input_total_drops = None
                                self.input_total_errors = None
                                self.input_unknown_proto = None
                                self.out_broadcast_pkts = None
                                self.out_multicast_pkts = None
                                self.out_octets = None
                                self.out_packets = None
                                self.out_ucast_pkts = None
                                self.output_total_drops = None
                                self.output_total_errors = None
                                self.output_underrun = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.in_broadcast_pkts is not None:
                                    return True

                                if self.in_multicast_pkts is not None:
                                    return True

                                if self.in_octets is not None:
                                    return True

                                if self.in_packets is not None:
                                    return True

                                if self.in_ucast_pkts is not None:
                                    return True

                                if self.input_crc is not None:
                                    return True

                                if self.input_frame is not None:
                                    return True

                                if self.input_overrun is not None:
                                    return True

                                if self.input_queue_drops is not None:
                                    return True

                                if self.input_total_drops is not None:
                                    return True

                                if self.input_total_errors is not None:
                                    return True

                                if self.input_unknown_proto is not None:
                                    return True

                                if self.out_broadcast_pkts is not None:
                                    return True

                                if self.out_multicast_pkts is not None:
                                    return True

                                if self.out_octets is not None:
                                    return True

                                if self.out_packets is not None:
                                    return True

                                if self.out_ucast_pkts is not None:
                                    return True

                                if self.output_total_drops is not None:
                                    return True

                                if self.output_total_errors is not None:
                                    return True

                                if self.output_underrun is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:generic-counter-interfaces/Cisco-IOS-XR-manageability-perfmgmt-oper:generic-counter-interface[Cisco-IOS-XR-manageability-perfmgmt-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces.GenericCounterInterface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:generic-counter-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.generic_counter_interface is not None:
                        for child_ref in self.generic_counter_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Interface.GenericCounterInterfaces']['meta_info']


            class BasicCounterInterfaces(object):
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
                    self.parent = None
                    self.basic_counter_interface = YList()
                    self.basic_counter_interface.parent = self
                    self.basic_counter_interface.name = 'basic_counter_interface'


                class BasicCounterInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.samples = PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Basic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Basic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.in_octets = None
                                self.in_packets = None
                                self.input_queue_drops = None
                                self.input_total_drops = None
                                self.input_total_errors = None
                                self.out_octets = None
                                self.out_packets = None
                                self.output_queue_drops = None
                                self.output_total_drops = None
                                self.output_total_errors = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.in_octets is not None:
                                    return True

                                if self.in_packets is not None:
                                    return True

                                if self.input_queue_drops is not None:
                                    return True

                                if self.input_total_drops is not None:
                                    return True

                                if self.input_total_errors is not None:
                                    return True

                                if self.out_octets is not None:
                                    return True

                                if self.out_packets is not None:
                                    return True

                                if self.output_queue_drops is not None:
                                    return True

                                if self.output_total_drops is not None:
                                    return True

                                if self.output_total_errors is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:basic-counter-interfaces/Cisco-IOS-XR-manageability-perfmgmt-oper:basic-counter-interface[Cisco-IOS-XR-manageability-perfmgmt-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces.BasicCounterInterface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:basic-counter-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.basic_counter_interface is not None:
                        for child_ref in self.basic_counter_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Interface.BasicCounterInterfaces']['meta_info']


            class DataRateInterfaces(object):
                """
                Interfaces for which Data Rates are collected
                
                .. attribute:: data_rate_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.data_rate_interface = YList()
                    self.data_rate_interface.parent = self
                    self.data_rate_interface.name = 'data_rate_interface'


                class DataRateInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.samples = PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Data Rate samples for an interface
                        
                        .. attribute:: sample
                        
                        	Data Rates sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.bandwidth = None
                                self.input_data_rate = None
                                self.input_packet_rate = None
                                self.input_peak_pkts = None
                                self.input_peak_rate = None
                                self.output_data_rate = None
                                self.output_packet_rate = None
                                self.output_peak_pkts = None
                                self.output_peak_rate = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.bandwidth is not None:
                                    return True

                                if self.input_data_rate is not None:
                                    return True

                                if self.input_packet_rate is not None:
                                    return True

                                if self.input_peak_pkts is not None:
                                    return True

                                if self.input_peak_rate is not None:
                                    return True

                                if self.output_data_rate is not None:
                                    return True

                                if self.output_packet_rate is not None:
                                    return True

                                if self.output_peak_pkts is not None:
                                    return True

                                if self.output_peak_rate is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:data-rate-interfaces/Cisco-IOS-XR-manageability-perfmgmt-oper:data-rate-interface[Cisco-IOS-XR-manageability-perfmgmt-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces.DataRateInterface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:data-rate-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.data_rate_interface is not None:
                        for child_ref in self.data_rate_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Periodic.Interface.DataRateInterfaces']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic/Cisco-IOS-XR-manageability-perfmgmt-oper:interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.basic_counter_interfaces is not None and self.basic_counter_interfaces._has_data():
                    return True

                if self.data_rate_interfaces is not None and self.data_rate_interfaces._has_data():
                    return True

                if self.generic_counter_interfaces is not None and self.generic_counter_interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Periodic.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:periodic'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bgp is not None and self.bgp._has_data():
                return True

            if self.interface is not None and self.interface._has_data():
                return True

            if self.mpls is not None and self.mpls._has_data():
                return True

            if self.nodes is not None and self.nodes._has_data():
                return True

            if self.ospf is not None and self.ospf._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
            return meta._meta_table['PerfMgmt.Periodic']['meta_info']


    class Monitor(object):
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
            self.parent = None
            self.bgp = PerfMgmt.Monitor.Bgp()
            self.bgp.parent = self
            self.interface = PerfMgmt.Monitor.Interface()
            self.interface.parent = self
            self.mpls = PerfMgmt.Monitor.Mpls()
            self.mpls.parent = self
            self.nodes = PerfMgmt.Monitor.Nodes()
            self.nodes.parent = self
            self.ospf = PerfMgmt.Monitor.Ospf()
            self.ospf.parent = self


        class Ospf(object):
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
                self.parent = None
                self.ospfv2_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances()
                self.ospfv2_protocol_instances.parent = self
                self.ospfv3_protocol_instances = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances()
                self.ospfv3_protocol_instances.parent = self


            class Ospfv2ProtocolInstances(object):
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
                    self.parent = None
                    self.ospfv2_protocol_instance = YList()
                    self.ospfv2_protocol_instance.parent = self
                    self.ospfv2_protocol_instance.name = 'ospfv2_protocol_instance'


                class Ospfv2ProtocolInstance(object):
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
                        self.parent = None
                        self.instance_name = None
                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Sample Table for an OSPV v2 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.checksum_errors = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.input_hello_packets = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.input_packets = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.output_hello_packets = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.output_packets = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.checksum_errors is not None:
                                    return True

                                if self.input_db_ds is not None:
                                    return True

                                if self.input_db_ds_lsa is not None:
                                    return True

                                if self.input_hello_packets is not None:
                                    return True

                                if self.input_ls_requests is not None:
                                    return True

                                if self.input_ls_requests_lsa is not None:
                                    return True

                                if self.input_lsa_acks is not None:
                                    return True

                                if self.input_lsa_acks_lsa is not None:
                                    return True

                                if self.input_lsa_updates is not None:
                                    return True

                                if self.input_lsa_updates_lsa is not None:
                                    return True

                                if self.input_packets is not None:
                                    return True

                                if self.output_db_ds is not None:
                                    return True

                                if self.output_db_ds_lsa is not None:
                                    return True

                                if self.output_hello_packets is not None:
                                    return True

                                if self.output_ls_requests is not None:
                                    return True

                                if self.output_ls_requests_lsa is not None:
                                    return True

                                if self.output_lsa_acks is not None:
                                    return True

                                if self.output_lsa_acks_lsa is not None:
                                    return True

                                if self.output_lsa_updates is not None:
                                    return True

                                if self.output_lsa_updates_lsa is not None:
                                    return True

                                if self.output_packets is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.instance_name is None:
                            raise YPYModelError('Key property instance_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv2-protocol-instances/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv2-protocol-instance[Cisco-IOS-XR-manageability-perfmgmt-oper:instance-name = ' + str(self.instance_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.instance_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances.Ospfv2ProtocolInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv2-protocol-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ospfv2_protocol_instance is not None:
                        for child_ref in self.ospfv2_protocol_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv2ProtocolInstances']['meta_info']


            class Ospfv3ProtocolInstances(object):
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
                    self.parent = None
                    self.ospfv3_protocol_instance = YList()
                    self.ospfv3_protocol_instance.parent = self
                    self.ospfv3_protocol_instance.name = 'ospfv3_protocol_instance'


                class Ospfv3ProtocolInstance(object):
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
                        self.parent = None
                        self.instance_name = None
                        self.samples = PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Sample Table for an OSPV v3 instance
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.input_db_ds = None
                                self.input_db_ds_lsa = None
                                self.input_hello_packets = None
                                self.input_ls_requests = None
                                self.input_ls_requests_lsa = None
                                self.input_lsa_acks = None
                                self.input_lsa_acks_lsa = None
                                self.input_lsa_updates = None
                                self.input_lsa_updates_lsa = None
                                self.input_packets = None
                                self.output_db_ds = None
                                self.output_db_ds_lsa = None
                                self.output_hello_packets = None
                                self.output_ls_requests = None
                                self.output_ls_requests_lsa = None
                                self.output_lsa_acks = None
                                self.output_lsa_acks_lsa = None
                                self.output_lsa_updates = None
                                self.output_lsa_updates_lsa = None
                                self.output_packets = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.input_db_ds is not None:
                                    return True

                                if self.input_db_ds_lsa is not None:
                                    return True

                                if self.input_hello_packets is not None:
                                    return True

                                if self.input_ls_requests is not None:
                                    return True

                                if self.input_ls_requests_lsa is not None:
                                    return True

                                if self.input_lsa_acks is not None:
                                    return True

                                if self.input_lsa_acks_lsa is not None:
                                    return True

                                if self.input_lsa_updates is not None:
                                    return True

                                if self.input_lsa_updates_lsa is not None:
                                    return True

                                if self.input_packets is not None:
                                    return True

                                if self.output_db_ds is not None:
                                    return True

                                if self.output_db_ds_lsa is not None:
                                    return True

                                if self.output_hello_packets is not None:
                                    return True

                                if self.output_ls_requests is not None:
                                    return True

                                if self.output_ls_requests_lsa is not None:
                                    return True

                                if self.output_lsa_acks is not None:
                                    return True

                                if self.output_lsa_acks_lsa is not None:
                                    return True

                                if self.output_lsa_updates is not None:
                                    return True

                                if self.output_lsa_updates_lsa is not None:
                                    return True

                                if self.output_packets is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.instance_name is None:
                            raise YPYModelError('Key property instance_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv3-protocol-instances/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv3-protocol-instance[Cisco-IOS-XR-manageability-perfmgmt-oper:instance-name = ' + str(self.instance_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.instance_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances.Ospfv3ProtocolInstance']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf/Cisco-IOS-XR-manageability-perfmgmt-oper:ospfv3-protocol-instances'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ospfv3_protocol_instance is not None:
                        for child_ref in self.ospfv3_protocol_instance:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Ospf.Ospfv3ProtocolInstances']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:ospf'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ospfv2_protocol_instances is not None and self.ospfv2_protocol_instances._has_data():
                    return True

                if self.ospfv3_protocol_instances is not None and self.ospfv3_protocol_instances._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Monitor.Ospf']['meta_info']


        class Mpls(object):
            """
            Collected MPLS data
            
            .. attribute:: ldp_neighbors
            
            	LDP neighbors for which statistics are collected
            	**type**\:   :py:class:`LdpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ldp_neighbors = PerfMgmt.Monitor.Mpls.LdpNeighbors()
                self.ldp_neighbors.parent = self


            class LdpNeighbors(object):
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
                    self.parent = None
                    self.ldp_neighbor = YList()
                    self.ldp_neighbor.parent = self
                    self.ldp_neighbor.name = 'ldp_neighbor'


                class LdpNeighbor(object):
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
                        self.parent = None
                        self.nbr = None
                        self.samples = PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Samples for a particular LDP neighbor
                        
                        .. attribute:: sample
                        
                        	LDP neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.address_msgs_rcvd = None
                                self.address_msgs_sent = None
                                self.address_withdraw_msgs_rcvd = None
                                self.address_withdraw_msgs_sent = None
                                self.init_msgs_rcvd = None
                                self.init_msgs_sent = None
                                self.keepalive_msgs_rcvd = None
                                self.keepalive_msgs_sent = None
                                self.label_mapping_msgs_rcvd = None
                                self.label_mapping_msgs_sent = None
                                self.label_release_msgs_rcvd = None
                                self.label_release_msgs_sent = None
                                self.label_withdraw_msgs_rcvd = None
                                self.label_withdraw_msgs_sent = None
                                self.notification_msgs_rcvd = None
                                self.notification_msgs_sent = None
                                self.time_stamp = None
                                self.total_msgs_rcvd = None
                                self.total_msgs_sent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.address_msgs_rcvd is not None:
                                    return True

                                if self.address_msgs_sent is not None:
                                    return True

                                if self.address_withdraw_msgs_rcvd is not None:
                                    return True

                                if self.address_withdraw_msgs_sent is not None:
                                    return True

                                if self.init_msgs_rcvd is not None:
                                    return True

                                if self.init_msgs_sent is not None:
                                    return True

                                if self.keepalive_msgs_rcvd is not None:
                                    return True

                                if self.keepalive_msgs_sent is not None:
                                    return True

                                if self.label_mapping_msgs_rcvd is not None:
                                    return True

                                if self.label_mapping_msgs_sent is not None:
                                    return True

                                if self.label_release_msgs_rcvd is not None:
                                    return True

                                if self.label_release_msgs_sent is not None:
                                    return True

                                if self.label_withdraw_msgs_rcvd is not None:
                                    return True

                                if self.label_withdraw_msgs_sent is not None:
                                    return True

                                if self.notification_msgs_rcvd is not None:
                                    return True

                                if self.notification_msgs_sent is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                if self.total_msgs_rcvd is not None:
                                    return True

                                if self.total_msgs_sent is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.nbr is None:
                            raise YPYModelError('Key property nbr is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:mpls/Cisco-IOS-XR-manageability-perfmgmt-oper:ldp-neighbors/Cisco-IOS-XR-manageability-perfmgmt-oper:ldp-neighbor[Cisco-IOS-XR-manageability-perfmgmt-oper:nbr = ' + str(self.nbr) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.nbr is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors.LdpNeighbor']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:mpls/Cisco-IOS-XR-manageability-perfmgmt-oper:ldp-neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ldp_neighbor is not None:
                        for child_ref in self.ldp_neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Mpls.LdpNeighbors']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:mpls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ldp_neighbors is not None and self.ldp_neighbors._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Monitor.Mpls']['meta_info']


        class Nodes(object):
            """
            Nodes for which data is collected
            
            .. attribute:: node
            
            	Node Instance
            	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node = YList()
                self.node.parent = self
                self.node.name = 'node'


            class Node(object):
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
                    self.parent = None
                    self.node_id = None
                    self.processes = PerfMgmt.Monitor.Nodes.Node.Processes()
                    self.processes.parent = self
                    self.sample_xr = PerfMgmt.Monitor.Nodes.Node.SampleXr()
                    self.sample_xr.parent = self
                    self.samples = PerfMgmt.Monitor.Nodes.Node.Samples()
                    self.samples.parent = self


                class SampleXr(object):
                    """
                    Node CPU data
                    
                    .. attribute:: sample
                    
                    	Node CPU data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sample = YList()
                        self.sample.parent = self
                        self.sample.name = 'sample'


                    class Sample(object):
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
                            self.parent = None
                            self.sample_id = None
                            self.average_cpu_used = None
                            self.no_processes = None
                            self.time_stamp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sample_id is None:
                                raise YPYModelError('Key property sample_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample_id is not None:
                                return True

                            if self.average_cpu_used is not None:
                                return True

                            if self.no_processes is not None:
                                return True

                            if self.time_stamp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.SampleXr.Sample']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample-xr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sample is not None:
                            for child_ref in self.sample:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.SampleXr']['meta_info']


                class Processes(object):
                    """
                    Processes data
                    
                    .. attribute:: process
                    
                    	Process data
                    	**type**\: list of    :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.process = YList()
                        self.process.parent = self
                        self.process.name = 'process'


                    class Process(object):
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
                            self.parent = None
                            self.process_id = None
                            self.samples = PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples()
                            self.samples.parent = self


                        class Samples(object):
                            """
                            Process data
                            
                            .. attribute:: sample
                            
                            	Process data sample
                            	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sample = YList()
                                self.sample.parent = self
                                self.sample.name = 'sample'


                            class Sample(object):
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
                                    self.parent = None
                                    self.sample_id = None
                                    self.average_cpu_used = None
                                    self.no_threads = None
                                    self.peak_memory = None
                                    self.time_stamp = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.sample_id is None:
                                        raise YPYModelError('Key property sample_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.sample_id is not None:
                                        return True

                                    if self.average_cpu_used is not None:
                                        return True

                                    if self.no_threads is not None:
                                        return True

                                    if self.peak_memory is not None:
                                        return True

                                    if self.time_stamp is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                    return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples.Sample']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample is not None:
                                    for child_ref in self.sample:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process.Samples']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.process_id is None:
                                raise YPYModelError('Key property process_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:process[Cisco-IOS-XR-manageability-perfmgmt-oper:process-id = ' + str(self.process_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.process_id is not None:
                                return True

                            if self.samples is not None and self.samples._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.Processes.Process']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:processes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.process is not None:
                            for child_ref in self.process:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.Processes']['meta_info']


                class Samples(object):
                    """
                    Node Memory data
                    
                    .. attribute:: sample
                    
                    	Node Memory data sample
                    	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Nodes.Node.Samples.Sample>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.sample = YList()
                        self.sample.parent = self
                        self.sample.name = 'sample'


                    class Sample(object):
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
                            self.parent = None
                            self.sample_id = None
                            self.curr_memory = None
                            self.peak_memory = None
                            self.time_stamp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.sample_id is None:
                                raise YPYModelError('Key property sample_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample_id is not None:
                                return True

                            if self.curr_memory is not None:
                                return True

                            if self.peak_memory is not None:
                                return True

                            if self.time_stamp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.Samples.Sample']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.sample is not None:
                            for child_ref in self.sample:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Nodes.Node.Samples']['meta_info']

                @property
                def _common_path(self):
                    if self.node_id is None:
                        raise YPYModelError('Key property node_id is None')

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:nodes/Cisco-IOS-XR-manageability-perfmgmt-oper:node[Cisco-IOS-XR-manageability-perfmgmt-oper:node-id = ' + str(self.node_id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.node_id is not None:
                        return True

                    if self.processes is not None and self.processes._has_data():
                        return True

                    if self.sample_xr is not None and self.sample_xr._has_data():
                        return True

                    if self.samples is not None and self.samples._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Nodes.Node']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:nodes'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node is not None:
                    for child_ref in self.node:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Monitor.Nodes']['meta_info']


        class Bgp(object):
            """
            Collected BGP data
            
            .. attribute:: bgp_neighbors
            
            	Neighbors for which statistics are collected
            	**type**\:   :py:class:`BgpNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors>`
            
            

            """

            _prefix = 'manageability-perfmgmt-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bgp_neighbors = PerfMgmt.Monitor.Bgp.BgpNeighbors()
                self.bgp_neighbors.parent = self


            class BgpNeighbors(object):
                """
                Neighbors for which statistics are collected
                
                .. attribute:: bgp_neighbor
                
                	Samples for particular neighbor
                	**type**\: list of    :py:class:`BgpNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bgp_neighbor = YList()
                    self.bgp_neighbor.parent = self
                    self.bgp_neighbor.name = 'bgp_neighbor'


                class BgpNeighbor(object):
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
                        self.parent = None
                        self.ip_address = None
                        self.samples = PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Sample Table for a BGP neighbor
                        
                        .. attribute:: sample
                        
                        	Neighbor statistics sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.conn_dropped = None
                                self.conn_established = None
                                self.errors_received = None
                                self.errors_sent = None
                                self.input_messages = None
                                self.input_update_messages = None
                                self.output_messages = None
                                self.output_update_messages = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.conn_dropped is not None:
                                    return True

                                if self.conn_established is not None:
                                    return True

                                if self.errors_received is not None:
                                    return True

                                if self.errors_sent is not None:
                                    return True

                                if self.input_messages is not None:
                                    return True

                                if self.input_update_messages is not None:
                                    return True

                                if self.output_messages is not None:
                                    return True

                                if self.output_update_messages is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.ip_address is None:
                            raise YPYModelError('Key property ip_address is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp-neighbors/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp-neighbor[Cisco-IOS-XR-manageability-perfmgmt-oper:ip-address = ' + str(self.ip_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.ip_address is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors.BgpNeighbor']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp-neighbors'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bgp_neighbor is not None:
                        for child_ref in self.bgp_neighbor:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Bgp.BgpNeighbors']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.bgp_neighbors is not None and self.bgp_neighbors._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Monitor.Bgp']['meta_info']


        class Interface(object):
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
                self.parent = None
                self.basic_counter_interfaces = PerfMgmt.Monitor.Interface.BasicCounterInterfaces()
                self.basic_counter_interfaces.parent = self
                self.data_rate_interfaces = PerfMgmt.Monitor.Interface.DataRateInterfaces()
                self.data_rate_interfaces.parent = self
                self.generic_counter_interfaces = PerfMgmt.Monitor.Interface.GenericCounterInterfaces()
                self.generic_counter_interfaces.parent = self


            class GenericCounterInterfaces(object):
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
                    self.parent = None
                    self.generic_counter_interface = YList()
                    self.generic_counter_interface.parent = self
                    self.generic_counter_interface.name = 'generic_counter_interface'


                class GenericCounterInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.samples = PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Generic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Generic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.in_broadcast_pkts = None
                                self.in_multicast_pkts = None
                                self.in_octets = None
                                self.in_packets = None
                                self.in_ucast_pkts = None
                                self.input_crc = None
                                self.input_frame = None
                                self.input_overrun = None
                                self.input_queue_drops = None
                                self.input_total_drops = None
                                self.input_total_errors = None
                                self.input_unknown_proto = None
                                self.out_broadcast_pkts = None
                                self.out_multicast_pkts = None
                                self.out_octets = None
                                self.out_packets = None
                                self.out_ucast_pkts = None
                                self.output_total_drops = None
                                self.output_total_errors = None
                                self.output_underrun = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.in_broadcast_pkts is not None:
                                    return True

                                if self.in_multicast_pkts is not None:
                                    return True

                                if self.in_octets is not None:
                                    return True

                                if self.in_packets is not None:
                                    return True

                                if self.in_ucast_pkts is not None:
                                    return True

                                if self.input_crc is not None:
                                    return True

                                if self.input_frame is not None:
                                    return True

                                if self.input_overrun is not None:
                                    return True

                                if self.input_queue_drops is not None:
                                    return True

                                if self.input_total_drops is not None:
                                    return True

                                if self.input_total_errors is not None:
                                    return True

                                if self.input_unknown_proto is not None:
                                    return True

                                if self.out_broadcast_pkts is not None:
                                    return True

                                if self.out_multicast_pkts is not None:
                                    return True

                                if self.out_octets is not None:
                                    return True

                                if self.out_packets is not None:
                                    return True

                                if self.out_ucast_pkts is not None:
                                    return True

                                if self.output_total_drops is not None:
                                    return True

                                if self.output_total_errors is not None:
                                    return True

                                if self.output_underrun is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:generic-counter-interfaces/Cisco-IOS-XR-manageability-perfmgmt-oper:generic-counter-interface[Cisco-IOS-XR-manageability-perfmgmt-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces.GenericCounterInterface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:generic-counter-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.generic_counter_interface is not None:
                        for child_ref in self.generic_counter_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Interface.GenericCounterInterfaces']['meta_info']


            class BasicCounterInterfaces(object):
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
                    self.parent = None
                    self.basic_counter_interface = YList()
                    self.basic_counter_interface.parent = self
                    self.basic_counter_interface.name = 'basic_counter_interface'


                class BasicCounterInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.samples = PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Basic Counter samples for an interface
                        
                        .. attribute:: sample
                        
                        	Basic Counters sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.in_octets = None
                                self.in_packets = None
                                self.input_queue_drops = None
                                self.input_total_drops = None
                                self.input_total_errors = None
                                self.out_octets = None
                                self.out_packets = None
                                self.output_queue_drops = None
                                self.output_total_drops = None
                                self.output_total_errors = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.in_octets is not None:
                                    return True

                                if self.in_packets is not None:
                                    return True

                                if self.input_queue_drops is not None:
                                    return True

                                if self.input_total_drops is not None:
                                    return True

                                if self.input_total_errors is not None:
                                    return True

                                if self.out_octets is not None:
                                    return True

                                if self.out_packets is not None:
                                    return True

                                if self.output_queue_drops is not None:
                                    return True

                                if self.output_total_drops is not None:
                                    return True

                                if self.output_total_errors is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:basic-counter-interfaces/Cisco-IOS-XR-manageability-perfmgmt-oper:basic-counter-interface[Cisco-IOS-XR-manageability-perfmgmt-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces.BasicCounterInterface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:basic-counter-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.basic_counter_interface is not None:
                        for child_ref in self.basic_counter_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Interface.BasicCounterInterfaces']['meta_info']


            class DataRateInterfaces(object):
                """
                Interfaces for which Data Rates are collected
                
                .. attribute:: data_rate_interface
                
                	Samples for a particular interface
                	**type**\: list of    :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface>`
                
                

                """

                _prefix = 'manageability-perfmgmt-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.data_rate_interface = YList()
                    self.data_rate_interface.parent = self
                    self.data_rate_interface.name = 'data_rate_interface'


                class DataRateInterface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.samples = PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples()
                        self.samples.parent = self


                    class Samples(object):
                        """
                        Data Rate samples for an interface
                        
                        .. attribute:: sample
                        
                        	Data Rates sample
                        	**type**\: list of    :py:class:`Sample <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_oper.PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sample = YList()
                            self.sample.parent = self
                            self.sample.name = 'sample'


                        class Sample(object):
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
                                self.parent = None
                                self.sample_id = None
                                self.bandwidth = None
                                self.input_data_rate = None
                                self.input_packet_rate = None
                                self.input_peak_pkts = None
                                self.input_peak_rate = None
                                self.output_data_rate = None
                                self.output_packet_rate = None
                                self.output_peak_pkts = None
                                self.output_peak_rate = None
                                self.time_stamp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.sample_id is None:
                                    raise YPYModelError('Key property sample_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:sample[Cisco-IOS-XR-manageability-perfmgmt-oper:sample-id = ' + str(self.sample_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.sample_id is not None:
                                    return True

                                if self.bandwidth is not None:
                                    return True

                                if self.input_data_rate is not None:
                                    return True

                                if self.input_packet_rate is not None:
                                    return True

                                if self.input_peak_pkts is not None:
                                    return True

                                if self.input_peak_rate is not None:
                                    return True

                                if self.output_data_rate is not None:
                                    return True

                                if self.output_packet_rate is not None:
                                    return True

                                if self.output_peak_pkts is not None:
                                    return True

                                if self.output_peak_rate is not None:
                                    return True

                                if self.time_stamp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                                return meta._meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples.Sample']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-oper:samples'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.sample is not None:
                                for child_ref in self.sample:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                            return meta._meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface.Samples']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:data-rate-interfaces/Cisco-IOS-XR-manageability-perfmgmt-oper:data-rate-interface[Cisco-IOS-XR-manageability-perfmgmt-oper:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.samples is not None and self.samples._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                        return meta._meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces.DataRateInterface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface/Cisco-IOS-XR-manageability-perfmgmt-oper:data-rate-interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.data_rate_interface is not None:
                        for child_ref in self.data_rate_interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                    return meta._meta_table['PerfMgmt.Monitor.Interface.DataRateInterfaces']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor/Cisco-IOS-XR-manageability-perfmgmt-oper:interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.basic_counter_interfaces is not None and self.basic_counter_interfaces._has_data():
                    return True

                if self.data_rate_interfaces is not None and self.data_rate_interfaces._has_data():
                    return True

                if self.generic_counter_interfaces is not None and self.generic_counter_interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
                return meta._meta_table['PerfMgmt.Monitor.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-oper:monitor'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bgp is not None and self.bgp._has_data():
                return True

            if self.interface is not None and self.interface._has_data():
                return True

            if self.mpls is not None and self.mpls._has_data():
                return True

            if self.nodes is not None and self.nodes._has_data():
                return True

            if self.ospf is not None and self.ospf._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
            return meta._meta_table['PerfMgmt.Monitor']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-manageability-perfmgmt-oper:perf-mgmt'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.monitor is not None and self.monitor._has_data():
            return True

        if self.periodic is not None and self.periodic._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_oper as meta
        return meta._meta_table['PerfMgmt']['meta_info']


