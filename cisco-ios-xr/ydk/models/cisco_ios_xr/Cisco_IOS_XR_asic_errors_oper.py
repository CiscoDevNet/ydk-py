""" Cisco_IOS_XR_asic_errors_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asic\-errors package operational data.

This module contains definitions
for the following management objects\:
  asic\-errors\: Error summary of all asics

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class AsicErrors(Entity):
    """
    Error summary of all asics
    
    .. attribute:: nodes
    
    	Asic errors for each available nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes>`
    
    

    """

    _prefix = 'asic-errors-oper'
    _revision = '2017-09-07'

    def __init__(self):
        super(AsicErrors, self).__init__()
        self._top_entity = None

        self.yang_name = "asic-errors"
        self.yang_parent_name = "Cisco-IOS-XR-asic-errors-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", AsicErrors.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = AsicErrors.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-asic-errors-oper:asic-errors"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(AsicErrors, [], name, value)


    class Nodes(Entity):
        """
        Asic errors for each available nodes
        
        .. attribute:: node
        
        	Asic error for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node>`
        
        

        """

        _prefix = 'asic-errors-oper'
        _revision = '2017-09-07'

        def __init__(self):
            super(AsicErrors.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "asic-errors"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", AsicErrors.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-asic-errors-oper:asic-errors/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(AsicErrors.Nodes, [], name, value)


        class Node(Entity):
            """
            Asic error for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node ID
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: asic_information
            
            	Asic on the node
            	**type**\: list of  		 :py:class:`AsicInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation>`
            
            

            """

            _prefix = 'asic-errors-oper'
            _revision = '2017-09-07'

            def __init__(self):
                super(AsicErrors.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("asic-information", ("asic_information", AsicErrors.Nodes.Node.AsicInformation))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.asic_information = YList(self)
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-asic-errors-oper:asic-errors/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(AsicErrors.Nodes.Node, ['node_name'], name, value)


            class AsicInformation(Entity):
                """
                Asic on the node
                
                .. attribute:: asic  (key)
                
                	Asic string
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: all_instances
                
                	All asic instance on the node
                	**type**\:  :py:class:`AllInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.AllInstances>`
                
                .. attribute:: instances
                
                	All asic errors  on the node
                	**type**\:  :py:class:`Instances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances>`
                
                

                """

                _prefix = 'asic-errors-oper'
                _revision = '2017-09-07'

                def __init__(self):
                    super(AsicErrors.Nodes.Node.AsicInformation, self).__init__()

                    self.yang_name = "asic-information"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['asic']
                    self._child_classes = OrderedDict([("all-instances", ("all_instances", AsicErrors.Nodes.Node.AsicInformation.AllInstances)), ("instances", ("instances", AsicErrors.Nodes.Node.AsicInformation.Instances))])
                    self._leafs = OrderedDict([
                        ('asic', (YLeaf(YType.str, 'asic'), ['str'])),
                    ])
                    self.asic = None

                    self.all_instances = AsicErrors.Nodes.Node.AsicInformation.AllInstances()
                    self.all_instances.parent = self
                    self._children_name_map["all_instances"] = "all-instances"

                    self.instances = AsicErrors.Nodes.Node.AsicInformation.Instances()
                    self.instances.parent = self
                    self._children_name_map["instances"] = "instances"
                    self._segment_path = lambda: "asic-information" + "[asic='" + str(self.asic) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation, ['asic'], name, value)


                class AllInstances(Entity):
                    """
                    All asic instance on the node
                    
                    .. attribute:: all_error_path
                    
                    	Error path of all instances
                    	**type**\:  :py:class:`AllErrorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath>`
                    
                    

                    """

                    _prefix = 'asic-errors-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AsicErrors.Nodes.Node.AsicInformation.AllInstances, self).__init__()

                        self.yang_name = "all-instances"
                        self.yang_parent_name = "asic-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("all-error-path", ("all_error_path", AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath))])
                        self._leafs = OrderedDict()

                        self.all_error_path = AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath()
                        self.all_error_path.parent = self
                        self._children_name_map["all_error_path"] = "all-error-path"
                        self._segment_path = lambda: "all-instances"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.AllInstances, [], name, value)


                    class AllErrorPath(Entity):
                        """
                        Error path of all instances
                        
                        .. attribute:: summary
                        
                        	Summary of all instances errors
                        	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary>`
                        
                        

                        """

                        _prefix = 'asic-errors-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath, self).__init__()

                            self.yang_name = "all-error-path"
                            self.yang_parent_name = "all-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("summary", ("summary", AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary))])
                            self._leafs = OrderedDict()

                            self.summary = AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary()
                            self.summary.parent = self
                            self._children_name_map["summary"] = "summary"
                            self._segment_path = lambda: "all-error-path"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath, [], name, value)


                        class Summary(Entity):
                            """
                            Summary of all instances errors
                            
                            .. attribute:: legacy_client
                            
                            	legacy client
                            	**type**\: bool
                            
                            .. attribute:: cih_client
                            
                            	cih client
                            	**type**\: bool
                            
                            .. attribute:: sum_data
                            
                            	sum data
                            	**type**\: list of  		 :py:class:`SumData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData>`
                            
                            

                            """

                            _prefix = 'asic-errors-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary, self).__init__()

                                self.yang_name = "summary"
                                self.yang_parent_name = "all-error-path"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("sum-data", ("sum_data", AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData))])
                                self._leafs = OrderedDict([
                                    ('legacy_client', (YLeaf(YType.boolean, 'legacy-client'), ['bool'])),
                                    ('cih_client', (YLeaf(YType.boolean, 'cih-client'), ['bool'])),
                                ])
                                self.legacy_client = None
                                self.cih_client = None

                                self.sum_data = YList(self)
                                self._segment_path = lambda: "summary"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary, [u'legacy_client', u'cih_client'], name, value)


                            class SumData(Entity):
                                """
                                sum data
                                
                                .. attribute:: num_nodes
                                
                                	num nodes
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: crc_err_count
                                
                                	crc err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: sbe_err_count
                                
                                	sbe err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: mbe_err_count
                                
                                	mbe err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: par_err_count
                                
                                	par err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: gen_err_count
                                
                                	gen err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reset_err_count
                                
                                	reset err count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: node_key
                                
                                	node key
                                	**type**\: list of int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: err_count
                                
                                	err count
                                	**type**\: list of  		 :py:class:`ErrCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.ErrCount>`
                                
                                .. attribute:: pcie_err_count
                                
                                	pcie err count
                                	**type**\: list of  		 :py:class:`PcieErrCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.PcieErrCount>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData, self).__init__()

                                    self.yang_name = "sum-data"
                                    self.yang_parent_name = "summary"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("err-count", ("err_count", AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.ErrCount)), ("pcie-err-count", ("pcie_err_count", AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.PcieErrCount))])
                                    self._leafs = OrderedDict([
                                        ('num_nodes', (YLeaf(YType.uint32, 'num-nodes'), ['int'])),
                                        ('crc_err_count', (YLeaf(YType.uint32, 'crc-err-count'), ['int'])),
                                        ('sbe_err_count', (YLeaf(YType.uint32, 'sbe-err-count'), ['int'])),
                                        ('mbe_err_count', (YLeaf(YType.uint32, 'mbe-err-count'), ['int'])),
                                        ('par_err_count', (YLeaf(YType.uint32, 'par-err-count'), ['int'])),
                                        ('gen_err_count', (YLeaf(YType.uint32, 'gen-err-count'), ['int'])),
                                        ('reset_err_count', (YLeaf(YType.uint32, 'reset-err-count'), ['int'])),
                                        ('node_key', (YLeafList(YType.uint32, 'node-key'), ['int'])),
                                    ])
                                    self.num_nodes = None
                                    self.crc_err_count = None
                                    self.sbe_err_count = None
                                    self.mbe_err_count = None
                                    self.par_err_count = None
                                    self.gen_err_count = None
                                    self.reset_err_count = None
                                    self.node_key = []

                                    self.err_count = YList(self)
                                    self.pcie_err_count = YList(self)
                                    self._segment_path = lambda: "sum-data"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData, [u'num_nodes', u'crc_err_count', u'sbe_err_count', u'mbe_err_count', u'par_err_count', u'gen_err_count', u'reset_err_count', u'node_key'], name, value)


                                class ErrCount(Entity):
                                    """
                                    err count
                                    
                                    .. attribute:: name
                                    
                                    	name
                                    	**type**\: str
                                    
                                    .. attribute:: count
                                    
                                    	count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.ErrCount, self).__init__()

                                        self.yang_name = "err-count"
                                        self.yang_parent_name = "sum-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                        ])
                                        self.name = None
                                        self.count = None
                                        self._segment_path = lambda: "err-count"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.ErrCount, [u'name', u'count'], name, value)


                                class PcieErrCount(Entity):
                                    """
                                    pcie err count
                                    
                                    .. attribute:: name
                                    
                                    	name
                                    	**type**\: str
                                    
                                    .. attribute:: count
                                    
                                    	count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.PcieErrCount, self).__init__()

                                        self.yang_name = "pcie-err-count"
                                        self.yang_parent_name = "sum-data"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                        ])
                                        self.name = None
                                        self.count = None
                                        self._segment_path = lambda: "pcie-err-count"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.AllInstances.AllErrorPath.Summary.SumData.PcieErrCount, [u'name', u'count'], name, value)


                class Instances(Entity):
                    """
                    All asic errors  on the node
                    
                    .. attribute:: instance
                    
                    	Particular asic instance on the node
                    	**type**\: list of  		 :py:class:`Instance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance>`
                    
                    

                    """

                    _prefix = 'asic-errors-oper'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(AsicErrors.Nodes.Node.AsicInformation.Instances, self).__init__()

                        self.yang_name = "instances"
                        self.yang_parent_name = "asic-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("instance", ("instance", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance))])
                        self._leafs = OrderedDict()

                        self.instance = YList(self)
                        self._segment_path = lambda: "instances"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances, [], name, value)


                    class Instance(Entity):
                        """
                        Particular asic instance on the node
                        
                        .. attribute:: asic_instance  (key)
                        
                        	asic instance
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: error_path
                        
                        	Error path of the instances
                        	**type**\:  :py:class:`ErrorPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath>`
                        
                        

                        """

                        _prefix = 'asic-errors-oper'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance, self).__init__()

                            self.yang_name = "instance"
                            self.yang_parent_name = "instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['asic_instance']
                            self._child_classes = OrderedDict([("error-path", ("error_path", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath))])
                            self._leafs = OrderedDict([
                                ('asic_instance', (YLeaf(YType.uint32, 'asic-instance'), ['int'])),
                            ])
                            self.asic_instance = None

                            self.error_path = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath()
                            self.error_path.parent = self
                            self._children_name_map["error_path"] = "error-path"
                            self._segment_path = lambda: "instance" + "[asic-instance='" + str(self.asic_instance) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance, ['asic_instance'], name, value)


                        class ErrorPath(Entity):
                            """
                            Error path of the instances
                            
                            .. attribute:: multiple_bit_soft_errors
                            
                            	Multiple bit soft error information
                            	**type**\:  :py:class:`MultipleBitSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors>`
                            
                            .. attribute:: asic_error_generic_soft
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorGenericSoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft>`
                            
                            .. attribute:: crc_hard_errors
                            
                            	CRC hard error information
                            	**type**\:  :py:class:`CrcHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors>`
                            
                            .. attribute:: asic_error_sbe_soft
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorSbeSoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft>`
                            
                            .. attribute:: hardware_soft_errors
                            
                            	Hardware soft error information
                            	**type**\:  :py:class:`HardwareSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors>`
                            
                            .. attribute:: asic_error_crc_soft
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorCrcSoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft>`
                            
                            .. attribute:: asic_error_parity_soft
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorParitySoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft>`
                            
                            .. attribute:: io_soft_errors
                            
                            	IO soft error information
                            	**type**\:  :py:class:`IoSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors>`
                            
                            .. attribute:: reset_soft_errors
                            
                            	Reset soft error information
                            	**type**\:  :py:class:`ResetSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors>`
                            
                            .. attribute:: barrier_hard_errors
                            
                            	Barrier hard error information
                            	**type**\:  :py:class:`BarrierHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors>`
                            
                            .. attribute:: ucode_soft_errors
                            
                            	Ucode soft error information
                            	**type**\:  :py:class:`UcodeSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors>`
                            
                            .. attribute:: asic_error_reset_hard
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorResetHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard>`
                            
                            .. attribute:: single_bit_hard_errors
                            
                            	Single bit hard error information
                            	**type**\:  :py:class:`SingleBitHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors>`
                            
                            .. attribute:: indirect_hard_errors
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`IndirectHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors>`
                            
                            .. attribute:: outof_resource_soft
                            
                            	OOR thresh information
                            	**type**\:  :py:class:`OutofResourceSoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft>`
                            
                            .. attribute:: crc_soft_errors
                            
                            	CRC soft error information
                            	**type**\:  :py:class:`CrcSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors>`
                            
                            .. attribute:: time_out_hard_errors
                            
                            	Time out hard error information
                            	**type**\:  :py:class:`TimeOutHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors>`
                            
                            .. attribute:: barrier_soft_errors
                            
                            	Barrier soft error information
                            	**type**\:  :py:class:`BarrierSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors>`
                            
                            .. attribute:: asic_error_mbe_soft
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorMbeSoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft>`
                            
                            .. attribute:: back_pressure_hard_errors
                            
                            	BP hard error information
                            	**type**\:  :py:class:`BackPressureHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors>`
                            
                            .. attribute:: single_bit_soft_errors
                            
                            	Single bit soft error information
                            	**type**\:  :py:class:`SingleBitSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors>`
                            
                            .. attribute:: indirect_soft_errors
                            
                            	Indirect soft error information
                            	**type**\:  :py:class:`IndirectSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors>`
                            
                            .. attribute:: generic_hard_errors
                            
                            	Generic hard error information
                            	**type**\:  :py:class:`GenericHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors>`
                            
                            .. attribute:: link_hard_errors
                            
                            	Link hard error information
                            	**type**\:  :py:class:`LinkHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors>`
                            
                            .. attribute:: configuration_hard_errors
                            
                            	Configuration hard error information
                            	**type**\:  :py:class:`ConfigurationHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors>`
                            
                            .. attribute:: instance_summary
                            
                            	Summary for a specific instance
                            	**type**\:  :py:class:`InstanceSummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary>`
                            
                            .. attribute:: unexpected_hard_errors
                            
                            	Unexpected hard error information
                            	**type**\:  :py:class:`UnexpectedHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors>`
                            
                            .. attribute:: time_out_soft_errors
                            
                            	Time out soft error information
                            	**type**\:  :py:class:`TimeOutSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors>`
                            
                            .. attribute:: asic_error_generic_hard
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorGenericHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard>`
                            
                            .. attribute:: parity_hard_errors
                            
                            	Parity hard error information
                            	**type**\:  :py:class:`ParityHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors>`
                            
                            .. attribute:: descriptor_hard_errors
                            
                            	Descriptor hard error information
                            	**type**\:  :py:class:`DescriptorHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors>`
                            
                            .. attribute:: interface_hard_errors
                            
                            	Interface hard error information
                            	**type**\:  :py:class:`InterfaceHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors>`
                            
                            .. attribute:: asic_error_sbe_hard
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorSbeHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard>`
                            
                            .. attribute:: asic_error_crc_hard
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorCrcHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard>`
                            
                            .. attribute:: asic_error_parity_hard
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorParityHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard>`
                            
                            .. attribute:: asic_error_reset_soft
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorResetSoft <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft>`
                            
                            .. attribute:: back_pressure_soft_errors
                            
                            	BP soft error information
                            	**type**\:  :py:class:`BackPressureSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors>`
                            
                            .. attribute:: generic_soft_errors
                            
                            	Generic soft error information
                            	**type**\:  :py:class:`GenericSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors>`
                            
                            .. attribute:: link_soft_errors
                            
                            	Link soft error information
                            	**type**\:  :py:class:`LinkSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors>`
                            
                            .. attribute:: configuration_soft_errors
                            
                            	Configuration soft error information
                            	**type**\:  :py:class:`ConfigurationSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors>`
                            
                            .. attribute:: multiple_bit_hard_errors
                            
                            	Multiple bit hard error information
                            	**type**\:  :py:class:`MultipleBitHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors>`
                            
                            .. attribute:: unexpected_soft_errors
                            
                            	Unexpected soft error information
                            	**type**\:  :py:class:`UnexpectedSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors>`
                            
                            .. attribute:: outof_resource_hard
                            
                            	OOR thresh information
                            	**type**\:  :py:class:`OutofResourceHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard>`
                            
                            .. attribute:: hardware_hard_errors
                            
                            	Hardware hard error information
                            	**type**\:  :py:class:`HardwareHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors>`
                            
                            .. attribute:: parity_soft_errors
                            
                            	Parity soft error information
                            	**type**\:  :py:class:`ParitySoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors>`
                            
                            .. attribute:: descriptor_soft_errors
                            
                            	Descriptor soft error information
                            	**type**\:  :py:class:`DescriptorSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors>`
                            
                            .. attribute:: interface_soft_errors
                            
                            	Interface soft error information
                            	**type**\:  :py:class:`InterfaceSoftErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors>`
                            
                            .. attribute:: io_hard_errors
                            
                            	IO hard error information
                            	**type**\:  :py:class:`IoHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors>`
                            
                            .. attribute:: reset_hard_errors
                            
                            	Reset hard error information
                            	**type**\:  :py:class:`ResetHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors>`
                            
                            .. attribute:: ucode_hard_errors
                            
                            	UCode hard error information
                            	**type**\:  :py:class:`UcodeHardErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors>`
                            
                            .. attribute:: asic_error_mbe_hard
                            
                            	Indirect hard error information
                            	**type**\:  :py:class:`AsicErrorMbeHard <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard>`
                            
                            

                            """

                            _prefix = 'asic-errors-oper'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath, self).__init__()

                                self.yang_name = "error-path"
                                self.yang_parent_name = "instance"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("multiple-bit-soft-errors", ("multiple_bit_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors)), ("asic-error-generic-soft", ("asic_error_generic_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft)), ("crc-hard-errors", ("crc_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors)), ("asic-error-sbe-soft", ("asic_error_sbe_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft)), ("hardware-soft-errors", ("hardware_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors)), ("asic-error-crc-soft", ("asic_error_crc_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft)), ("asic-error-parity-soft", ("asic_error_parity_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft)), ("io-soft-errors", ("io_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors)), ("reset-soft-errors", ("reset_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors)), ("barrier-hard-errors", ("barrier_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors)), ("ucode-soft-errors", ("ucode_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors)), ("asic-error-reset-hard", ("asic_error_reset_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard)), ("single-bit-hard-errors", ("single_bit_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors)), ("indirect-hard-errors", ("indirect_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors)), ("outof-resource-soft", ("outof_resource_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft)), ("crc-soft-errors", ("crc_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors)), ("time-out-hard-errors", ("time_out_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors)), ("barrier-soft-errors", ("barrier_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors)), ("asic-error-mbe-soft", ("asic_error_mbe_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft)), ("back-pressure-hard-errors", ("back_pressure_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors)), ("single-bit-soft-errors", ("single_bit_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors)), ("indirect-soft-errors", ("indirect_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors)), ("generic-hard-errors", ("generic_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors)), ("link-hard-errors", ("link_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors)), ("configuration-hard-errors", ("configuration_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors)), ("instance-summary", ("instance_summary", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary)), ("unexpected-hard-errors", ("unexpected_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors)), ("time-out-soft-errors", ("time_out_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors)), ("asic-error-generic-hard", ("asic_error_generic_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard)), ("parity-hard-errors", ("parity_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors)), ("descriptor-hard-errors", ("descriptor_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors)), ("interface-hard-errors", ("interface_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors)), ("asic-error-sbe-hard", ("asic_error_sbe_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard)), ("asic-error-crc-hard", ("asic_error_crc_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard)), ("asic-error-parity-hard", ("asic_error_parity_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard)), ("asic-error-reset-soft", ("asic_error_reset_soft", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft)), ("back-pressure-soft-errors", ("back_pressure_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors)), ("generic-soft-errors", ("generic_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors)), ("link-soft-errors", ("link_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors)), ("configuration-soft-errors", ("configuration_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors)), ("multiple-bit-hard-errors", ("multiple_bit_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors)), ("unexpected-soft-errors", ("unexpected_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors)), ("outof-resource-hard", ("outof_resource_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard)), ("hardware-hard-errors", ("hardware_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors)), ("parity-soft-errors", ("parity_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors)), ("descriptor-soft-errors", ("descriptor_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors)), ("interface-soft-errors", ("interface_soft_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors)), ("io-hard-errors", ("io_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors)), ("reset-hard-errors", ("reset_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors)), ("ucode-hard-errors", ("ucode_hard_errors", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors)), ("asic-error-mbe-hard", ("asic_error_mbe_hard", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard))])
                                self._leafs = OrderedDict()

                                self.multiple_bit_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors()
                                self.multiple_bit_soft_errors.parent = self
                                self._children_name_map["multiple_bit_soft_errors"] = "multiple-bit-soft-errors"

                                self.asic_error_generic_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft()
                                self.asic_error_generic_soft.parent = self
                                self._children_name_map["asic_error_generic_soft"] = "asic-error-generic-soft"

                                self.crc_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors()
                                self.crc_hard_errors.parent = self
                                self._children_name_map["crc_hard_errors"] = "crc-hard-errors"

                                self.asic_error_sbe_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft()
                                self.asic_error_sbe_soft.parent = self
                                self._children_name_map["asic_error_sbe_soft"] = "asic-error-sbe-soft"

                                self.hardware_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors()
                                self.hardware_soft_errors.parent = self
                                self._children_name_map["hardware_soft_errors"] = "hardware-soft-errors"

                                self.asic_error_crc_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft()
                                self.asic_error_crc_soft.parent = self
                                self._children_name_map["asic_error_crc_soft"] = "asic-error-crc-soft"

                                self.asic_error_parity_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft()
                                self.asic_error_parity_soft.parent = self
                                self._children_name_map["asic_error_parity_soft"] = "asic-error-parity-soft"

                                self.io_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors()
                                self.io_soft_errors.parent = self
                                self._children_name_map["io_soft_errors"] = "io-soft-errors"

                                self.reset_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors()
                                self.reset_soft_errors.parent = self
                                self._children_name_map["reset_soft_errors"] = "reset-soft-errors"

                                self.barrier_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors()
                                self.barrier_hard_errors.parent = self
                                self._children_name_map["barrier_hard_errors"] = "barrier-hard-errors"

                                self.ucode_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors()
                                self.ucode_soft_errors.parent = self
                                self._children_name_map["ucode_soft_errors"] = "ucode-soft-errors"

                                self.asic_error_reset_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard()
                                self.asic_error_reset_hard.parent = self
                                self._children_name_map["asic_error_reset_hard"] = "asic-error-reset-hard"

                                self.single_bit_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors()
                                self.single_bit_hard_errors.parent = self
                                self._children_name_map["single_bit_hard_errors"] = "single-bit-hard-errors"

                                self.indirect_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors()
                                self.indirect_hard_errors.parent = self
                                self._children_name_map["indirect_hard_errors"] = "indirect-hard-errors"

                                self.outof_resource_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft()
                                self.outof_resource_soft.parent = self
                                self._children_name_map["outof_resource_soft"] = "outof-resource-soft"

                                self.crc_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors()
                                self.crc_soft_errors.parent = self
                                self._children_name_map["crc_soft_errors"] = "crc-soft-errors"

                                self.time_out_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors()
                                self.time_out_hard_errors.parent = self
                                self._children_name_map["time_out_hard_errors"] = "time-out-hard-errors"

                                self.barrier_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors()
                                self.barrier_soft_errors.parent = self
                                self._children_name_map["barrier_soft_errors"] = "barrier-soft-errors"

                                self.asic_error_mbe_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft()
                                self.asic_error_mbe_soft.parent = self
                                self._children_name_map["asic_error_mbe_soft"] = "asic-error-mbe-soft"

                                self.back_pressure_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors()
                                self.back_pressure_hard_errors.parent = self
                                self._children_name_map["back_pressure_hard_errors"] = "back-pressure-hard-errors"

                                self.single_bit_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors()
                                self.single_bit_soft_errors.parent = self
                                self._children_name_map["single_bit_soft_errors"] = "single-bit-soft-errors"

                                self.indirect_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors()
                                self.indirect_soft_errors.parent = self
                                self._children_name_map["indirect_soft_errors"] = "indirect-soft-errors"

                                self.generic_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors()
                                self.generic_hard_errors.parent = self
                                self._children_name_map["generic_hard_errors"] = "generic-hard-errors"

                                self.link_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors()
                                self.link_hard_errors.parent = self
                                self._children_name_map["link_hard_errors"] = "link-hard-errors"

                                self.configuration_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors()
                                self.configuration_hard_errors.parent = self
                                self._children_name_map["configuration_hard_errors"] = "configuration-hard-errors"

                                self.instance_summary = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary()
                                self.instance_summary.parent = self
                                self._children_name_map["instance_summary"] = "instance-summary"

                                self.unexpected_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors()
                                self.unexpected_hard_errors.parent = self
                                self._children_name_map["unexpected_hard_errors"] = "unexpected-hard-errors"

                                self.time_out_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors()
                                self.time_out_soft_errors.parent = self
                                self._children_name_map["time_out_soft_errors"] = "time-out-soft-errors"

                                self.asic_error_generic_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard()
                                self.asic_error_generic_hard.parent = self
                                self._children_name_map["asic_error_generic_hard"] = "asic-error-generic-hard"

                                self.parity_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors()
                                self.parity_hard_errors.parent = self
                                self._children_name_map["parity_hard_errors"] = "parity-hard-errors"

                                self.descriptor_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors()
                                self.descriptor_hard_errors.parent = self
                                self._children_name_map["descriptor_hard_errors"] = "descriptor-hard-errors"

                                self.interface_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors()
                                self.interface_hard_errors.parent = self
                                self._children_name_map["interface_hard_errors"] = "interface-hard-errors"

                                self.asic_error_sbe_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard()
                                self.asic_error_sbe_hard.parent = self
                                self._children_name_map["asic_error_sbe_hard"] = "asic-error-sbe-hard"

                                self.asic_error_crc_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard()
                                self.asic_error_crc_hard.parent = self
                                self._children_name_map["asic_error_crc_hard"] = "asic-error-crc-hard"

                                self.asic_error_parity_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard()
                                self.asic_error_parity_hard.parent = self
                                self._children_name_map["asic_error_parity_hard"] = "asic-error-parity-hard"

                                self.asic_error_reset_soft = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft()
                                self.asic_error_reset_soft.parent = self
                                self._children_name_map["asic_error_reset_soft"] = "asic-error-reset-soft"

                                self.back_pressure_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors()
                                self.back_pressure_soft_errors.parent = self
                                self._children_name_map["back_pressure_soft_errors"] = "back-pressure-soft-errors"

                                self.generic_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors()
                                self.generic_soft_errors.parent = self
                                self._children_name_map["generic_soft_errors"] = "generic-soft-errors"

                                self.link_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors()
                                self.link_soft_errors.parent = self
                                self._children_name_map["link_soft_errors"] = "link-soft-errors"

                                self.configuration_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors()
                                self.configuration_soft_errors.parent = self
                                self._children_name_map["configuration_soft_errors"] = "configuration-soft-errors"

                                self.multiple_bit_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors()
                                self.multiple_bit_hard_errors.parent = self
                                self._children_name_map["multiple_bit_hard_errors"] = "multiple-bit-hard-errors"

                                self.unexpected_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors()
                                self.unexpected_soft_errors.parent = self
                                self._children_name_map["unexpected_soft_errors"] = "unexpected-soft-errors"

                                self.outof_resource_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard()
                                self.outof_resource_hard.parent = self
                                self._children_name_map["outof_resource_hard"] = "outof-resource-hard"

                                self.hardware_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors()
                                self.hardware_hard_errors.parent = self
                                self._children_name_map["hardware_hard_errors"] = "hardware-hard-errors"

                                self.parity_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors()
                                self.parity_soft_errors.parent = self
                                self._children_name_map["parity_soft_errors"] = "parity-soft-errors"

                                self.descriptor_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors()
                                self.descriptor_soft_errors.parent = self
                                self._children_name_map["descriptor_soft_errors"] = "descriptor-soft-errors"

                                self.interface_soft_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors()
                                self.interface_soft_errors.parent = self
                                self._children_name_map["interface_soft_errors"] = "interface-soft-errors"

                                self.io_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors()
                                self.io_hard_errors.parent = self
                                self._children_name_map["io_hard_errors"] = "io-hard-errors"

                                self.reset_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors()
                                self.reset_hard_errors.parent = self
                                self._children_name_map["reset_hard_errors"] = "reset-hard-errors"

                                self.ucode_hard_errors = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors()
                                self.ucode_hard_errors.parent = self
                                self._children_name_map["ucode_hard_errors"] = "ucode-hard-errors"

                                self.asic_error_mbe_hard = AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard()
                                self.asic_error_mbe_hard.parent = self
                                self._children_name_map["asic_error_mbe_hard"] = "asic-error-mbe-hard"
                                self._segment_path = lambda: "error-path"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath, [], name, value)


                            class MultipleBitSoftErrors(Entity):
                                """
                                Multiple bit soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors, self).__init__()

                                    self.yang_name = "multiple-bit-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "multiple-bit-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "multiple-bit-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorGenericSoft(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft, self).__init__()

                                    self.yang_name = "asic-error-generic-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-generic-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-generic-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericSoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class CrcHardErrors(Entity):
                                """
                                CRC hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors, self).__init__()

                                    self.yang_name = "crc-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "crc-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "crc-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorSbeSoft(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft, self).__init__()

                                    self.yang_name = "asic-error-sbe-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-sbe-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-sbe-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeSoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class HardwareSoftErrors(Entity):
                                """
                                Hardware soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors, self).__init__()

                                    self.yang_name = "hardware-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "hardware-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "hardware-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorCrcSoft(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft, self).__init__()

                                    self.yang_name = "asic-error-crc-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-crc-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-crc-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcSoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorParitySoft(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft, self).__init__()

                                    self.yang_name = "asic-error-parity-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-parity-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-parity-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParitySoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class IoSoftErrors(Entity):
                                """
                                IO soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors, self).__init__()

                                    self.yang_name = "io-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "io-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "io-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class ResetSoftErrors(Entity):
                                """
                                Reset soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors, self).__init__()

                                    self.yang_name = "reset-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "reset-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "reset-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class BarrierHardErrors(Entity):
                                """
                                Barrier hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors, self).__init__()

                                    self.yang_name = "barrier-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "barrier-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "barrier-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class UcodeSoftErrors(Entity):
                                """
                                Ucode soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors, self).__init__()

                                    self.yang_name = "ucode-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "ucode-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "ucode-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorResetHard(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard, self).__init__()

                                    self.yang_name = "asic-error-reset-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-reset-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-reset-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class SingleBitHardErrors(Entity):
                                """
                                Single bit hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors, self).__init__()

                                    self.yang_name = "single-bit-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "single-bit-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "single-bit-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class IndirectHardErrors(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors, self).__init__()

                                    self.yang_name = "indirect-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "indirect-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "indirect-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class OutofResourceSoft(Entity):
                                """
                                OOR thresh information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft, self).__init__()

                                    self.yang_name = "outof-resource-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "outof-resource-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "outof-resource-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceSoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class CrcSoftErrors(Entity):
                                """
                                CRC soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors, self).__init__()

                                    self.yang_name = "crc-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "crc-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "crc-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.CrcSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class TimeOutHardErrors(Entity):
                                """
                                Time out hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors, self).__init__()

                                    self.yang_name = "time-out-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "time-out-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "time-out-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class BarrierSoftErrors(Entity):
                                """
                                Barrier soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors, self).__init__()

                                    self.yang_name = "barrier-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "barrier-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "barrier-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BarrierSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorMbeSoft(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft, self).__init__()

                                    self.yang_name = "asic-error-mbe-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-mbe-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-mbe-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeSoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class BackPressureHardErrors(Entity):
                                """
                                BP hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors, self).__init__()

                                    self.yang_name = "back-pressure-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "back-pressure-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "back-pressure-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class SingleBitSoftErrors(Entity):
                                """
                                Single bit soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors, self).__init__()

                                    self.yang_name = "single-bit-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "single-bit-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "single-bit-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.SingleBitSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class IndirectSoftErrors(Entity):
                                """
                                Indirect soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors, self).__init__()

                                    self.yang_name = "indirect-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "indirect-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "indirect-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IndirectSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class GenericHardErrors(Entity):
                                """
                                Generic hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors, self).__init__()

                                    self.yang_name = "generic-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "generic-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "generic-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class LinkHardErrors(Entity):
                                """
                                Link hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors, self).__init__()

                                    self.yang_name = "link-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "link-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "link-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class ConfigurationHardErrors(Entity):
                                """
                                Configuration hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors, self).__init__()

                                    self.yang_name = "configuration-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "configuration-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "configuration-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class InstanceSummary(Entity):
                                """
                                Summary for a specific instance
                                
                                .. attribute:: legacy_client
                                
                                	legacy client
                                	**type**\: bool
                                
                                .. attribute:: cih_client
                                
                                	cih client
                                	**type**\: bool
                                
                                .. attribute:: sum_data
                                
                                	sum data
                                	**type**\: list of  		 :py:class:`SumData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary, self).__init__()

                                    self.yang_name = "instance-summary"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("sum-data", ("sum_data", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData))])
                                    self._leafs = OrderedDict([
                                        ('legacy_client', (YLeaf(YType.boolean, 'legacy-client'), ['bool'])),
                                        ('cih_client', (YLeaf(YType.boolean, 'cih-client'), ['bool'])),
                                    ])
                                    self.legacy_client = None
                                    self.cih_client = None

                                    self.sum_data = YList(self)
                                    self._segment_path = lambda: "instance-summary"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary, [u'legacy_client', u'cih_client'], name, value)


                                class SumData(Entity):
                                    """
                                    sum data
                                    
                                    .. attribute:: num_nodes
                                    
                                    	num nodes
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: crc_err_count
                                    
                                    	crc err count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: sbe_err_count
                                    
                                    	sbe err count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: mbe_err_count
                                    
                                    	mbe err count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: par_err_count
                                    
                                    	par err count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: gen_err_count
                                    
                                    	gen err count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: reset_err_count
                                    
                                    	reset err count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: node_key
                                    
                                    	node key
                                    	**type**\: list of int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: err_count
                                    
                                    	err count
                                    	**type**\: list of  		 :py:class:`ErrCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.ErrCount>`
                                    
                                    .. attribute:: pcie_err_count
                                    
                                    	pcie err count
                                    	**type**\: list of  		 :py:class:`PcieErrCount <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.PcieErrCount>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData, self).__init__()

                                        self.yang_name = "sum-data"
                                        self.yang_parent_name = "instance-summary"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("err-count", ("err_count", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.ErrCount)), ("pcie-err-count", ("pcie_err_count", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.PcieErrCount))])
                                        self._leafs = OrderedDict([
                                            ('num_nodes', (YLeaf(YType.uint32, 'num-nodes'), ['int'])),
                                            ('crc_err_count', (YLeaf(YType.uint32, 'crc-err-count'), ['int'])),
                                            ('sbe_err_count', (YLeaf(YType.uint32, 'sbe-err-count'), ['int'])),
                                            ('mbe_err_count', (YLeaf(YType.uint32, 'mbe-err-count'), ['int'])),
                                            ('par_err_count', (YLeaf(YType.uint32, 'par-err-count'), ['int'])),
                                            ('gen_err_count', (YLeaf(YType.uint32, 'gen-err-count'), ['int'])),
                                            ('reset_err_count', (YLeaf(YType.uint32, 'reset-err-count'), ['int'])),
                                            ('node_key', (YLeafList(YType.uint32, 'node-key'), ['int'])),
                                        ])
                                        self.num_nodes = None
                                        self.crc_err_count = None
                                        self.sbe_err_count = None
                                        self.mbe_err_count = None
                                        self.par_err_count = None
                                        self.gen_err_count = None
                                        self.reset_err_count = None
                                        self.node_key = []

                                        self.err_count = YList(self)
                                        self.pcie_err_count = YList(self)
                                        self._segment_path = lambda: "sum-data"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData, [u'num_nodes', u'crc_err_count', u'sbe_err_count', u'mbe_err_count', u'par_err_count', u'gen_err_count', u'reset_err_count', u'node_key'], name, value)


                                    class ErrCount(Entity):
                                        """
                                        err count
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: count
                                        
                                        	count
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.ErrCount, self).__init__()

                                            self.yang_name = "err-count"
                                            self.yang_parent_name = "sum-data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ])
                                            self.name = None
                                            self.count = None
                                            self._segment_path = lambda: "err-count"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.ErrCount, [u'name', u'count'], name, value)


                                    class PcieErrCount(Entity):
                                        """
                                        pcie err count
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: count
                                        
                                        	count
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.PcieErrCount, self).__init__()

                                            self.yang_name = "pcie-err-count"
                                            self.yang_parent_name = "sum-data"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ])
                                            self.name = None
                                            self.count = None
                                            self._segment_path = lambda: "pcie-err-count"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InstanceSummary.SumData.PcieErrCount, [u'name', u'count'], name, value)


                            class UnexpectedHardErrors(Entity):
                                """
                                Unexpected hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors, self).__init__()

                                    self.yang_name = "unexpected-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "unexpected-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "unexpected-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class TimeOutSoftErrors(Entity):
                                """
                                Time out soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors, self).__init__()

                                    self.yang_name = "time-out-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "time-out-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "time-out-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.TimeOutSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorGenericHard(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard, self).__init__()

                                    self.yang_name = "asic-error-generic-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-generic-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-generic-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorGenericHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class ParityHardErrors(Entity):
                                """
                                Parity hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors, self).__init__()

                                    self.yang_name = "parity-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "parity-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "parity-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParityHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class DescriptorHardErrors(Entity):
                                """
                                Descriptor hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors, self).__init__()

                                    self.yang_name = "descriptor-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "descriptor-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "descriptor-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class InterfaceHardErrors(Entity):
                                """
                                Interface hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors, self).__init__()

                                    self.yang_name = "interface-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "interface-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "interface-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorSbeHard(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard, self).__init__()

                                    self.yang_name = "asic-error-sbe-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-sbe-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-sbe-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorSbeHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorCrcHard(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard, self).__init__()

                                    self.yang_name = "asic-error-crc-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-crc-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-crc-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorCrcHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorParityHard(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard, self).__init__()

                                    self.yang_name = "asic-error-parity-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-parity-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-parity-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorParityHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorResetSoft(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft, self).__init__()

                                    self.yang_name = "asic-error-reset-soft"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-reset-soft"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-reset-soft"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorResetSoft.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class BackPressureSoftErrors(Entity):
                                """
                                BP soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors, self).__init__()

                                    self.yang_name = "back-pressure-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "back-pressure-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "back-pressure-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.BackPressureSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class GenericSoftErrors(Entity):
                                """
                                Generic soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors, self).__init__()

                                    self.yang_name = "generic-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "generic-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "generic-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.GenericSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class LinkSoftErrors(Entity):
                                """
                                Link soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors, self).__init__()

                                    self.yang_name = "link-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "link-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "link-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.LinkSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class ConfigurationSoftErrors(Entity):
                                """
                                Configuration soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors, self).__init__()

                                    self.yang_name = "configuration-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "configuration-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "configuration-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ConfigurationSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class MultipleBitHardErrors(Entity):
                                """
                                Multiple bit hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors, self).__init__()

                                    self.yang_name = "multiple-bit-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "multiple-bit-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "multiple-bit-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.MultipleBitHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class UnexpectedSoftErrors(Entity):
                                """
                                Unexpected soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors, self).__init__()

                                    self.yang_name = "unexpected-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "unexpected-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "unexpected-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UnexpectedSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class OutofResourceHard(Entity):
                                """
                                OOR thresh information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard, self).__init__()

                                    self.yang_name = "outof-resource-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "outof-resource-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "outof-resource-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.OutofResourceHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class HardwareHardErrors(Entity):
                                """
                                Hardware hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors, self).__init__()

                                    self.yang_name = "hardware-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "hardware-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "hardware-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.HardwareHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class ParitySoftErrors(Entity):
                                """
                                Parity soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors, self).__init__()

                                    self.yang_name = "parity-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "parity-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "parity-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ParitySoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class DescriptorSoftErrors(Entity):
                                """
                                Descriptor soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors, self).__init__()

                                    self.yang_name = "descriptor-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "descriptor-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "descriptor-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.DescriptorSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class InterfaceSoftErrors(Entity):
                                """
                                Interface soft error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors, self).__init__()

                                    self.yang_name = "interface-soft-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "interface-soft-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "interface-soft-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.InterfaceSoftErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class IoHardErrors(Entity):
                                """
                                IO hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors, self).__init__()

                                    self.yang_name = "io-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "io-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "io-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.IoHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class ResetHardErrors(Entity):
                                """
                                Reset hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors, self).__init__()

                                    self.yang_name = "reset-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "reset-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "reset-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.ResetHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class UcodeHardErrors(Entity):
                                """
                                UCode hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors, self).__init__()

                                    self.yang_name = "ucode-hard-errors"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "ucode-hard-errors"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "ucode-hard-errors"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.UcodeHardErrors.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)


                            class AsicErrorMbeHard(Entity):
                                """
                                Indirect hard error information
                                
                                .. attribute:: error
                                
                                	Collection of errors
                                	**type**\: list of  		 :py:class:`Error <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error>`
                                
                                

                                """

                                _prefix = 'asic-errors-oper'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard, self).__init__()

                                    self.yang_name = "asic-error-mbe-hard"
                                    self.yang_parent_name = "error-path"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("error", ("error", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error))])
                                    self._leafs = OrderedDict()

                                    self.error = YList(self)
                                    self._segment_path = lambda: "asic-error-mbe-hard"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard, [], name, value)


                                class Error(Entity):
                                    """
                                    Collection of errors
                                    
                                    .. attribute:: name
                                    
                                    	Name assigned to mem
                                    	**type**\: str
                                    
                                    .. attribute:: asic_info
                                    
                                    	Name of rack/board/asic
                                    	**type**\: str
                                    
                                    .. attribute:: node_key
                                    
                                    	32 bit key
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: alarm_on
                                    
                                    	High threshold crossed
                                    	**type**\: bool
                                    
                                    .. attribute:: thresh_hi
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_hi
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: thresh_lo
                                    
                                    	High threshold value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: period_lo
                                    
                                    	High period value
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: count
                                    
                                    	Accumulated count
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: intr_type
                                    
                                    	Type of error
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: leaf_id
                                    
                                    	Leaf ID defined in user data
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: last_cleared
                                    
                                    	Time  cleared
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: csrs_info
                                    
                                    	List of csrs\_info
                                    	**type**\: list of  		 :py:class:`CsrsInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo>`
                                    
                                    .. attribute:: last_err
                                    
                                    	Last Printable error information
                                    	**type**\: list of  		 :py:class:`LastErr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asic_errors_oper.AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr>`
                                    
                                    

                                    """

                                    _prefix = 'asic-errors-oper'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error, self).__init__()

                                        self.yang_name = "error"
                                        self.yang_parent_name = "asic-error-mbe-hard"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("csrs-info", ("csrs_info", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo)), ("last-err", ("last_err", AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr))])
                                        self._leafs = OrderedDict([
                                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                            ('asic_info', (YLeaf(YType.str, 'asic-info'), ['str'])),
                                            ('node_key', (YLeaf(YType.uint32, 'node-key'), ['int'])),
                                            ('alarm_on', (YLeaf(YType.boolean, 'alarm-on'), ['bool'])),
                                            ('thresh_hi', (YLeaf(YType.uint32, 'thresh-hi'), ['int'])),
                                            ('period_hi', (YLeaf(YType.uint32, 'period-hi'), ['int'])),
                                            ('thresh_lo', (YLeaf(YType.uint32, 'thresh-lo'), ['int'])),
                                            ('period_lo', (YLeaf(YType.uint32, 'period-lo'), ['int'])),
                                            ('count', (YLeaf(YType.uint32, 'count'), ['int'])),
                                            ('intr_type', (YLeaf(YType.uint32, 'intr-type'), ['int'])),
                                            ('leaf_id', (YLeaf(YType.uint32, 'leaf-id'), ['int'])),
                                            ('last_cleared', (YLeaf(YType.uint64, 'last-cleared'), ['int'])),
                                        ])
                                        self.name = None
                                        self.asic_info = None
                                        self.node_key = None
                                        self.alarm_on = None
                                        self.thresh_hi = None
                                        self.period_hi = None
                                        self.thresh_lo = None
                                        self.period_lo = None
                                        self.count = None
                                        self.intr_type = None
                                        self.leaf_id = None
                                        self.last_cleared = None

                                        self.csrs_info = YList(self)
                                        self.last_err = YList(self)
                                        self._segment_path = lambda: "error"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error, [u'name', u'asic_info', u'node_key', u'alarm_on', u'thresh_hi', u'period_hi', u'thresh_lo', u'period_lo', u'count', u'intr_type', u'leaf_id', u'last_cleared'], name, value)


                                    class CsrsInfo(Entity):
                                        """
                                        List of csrs\_info
                                        
                                        .. attribute:: name
                                        
                                        	name
                                        	**type**\: str
                                        
                                        .. attribute:: address
                                        
                                        	address
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: width
                                        
                                        	width
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo, self).__init__()

                                            self.yang_name = "csrs-info"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                                ('address', (YLeaf(YType.uint64, 'address'), ['int'])),
                                                ('width', (YLeaf(YType.uint32, 'width'), ['int'])),
                                            ])
                                            self.name = None
                                            self.address = None
                                            self.width = None
                                            self._segment_path = lambda: "csrs-info"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.CsrsInfo, [u'name', u'address', u'width'], name, value)


                                    class LastErr(Entity):
                                        """
                                        Last Printable error information
                                        
                                        .. attribute:: at_time
                                        
                                        	at time
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: at_time_nsec
                                        
                                        	at time nsec
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: counter_val
                                        
                                        	counter val
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: error_desc
                                        
                                        	error desc
                                        	**type**\: str
                                        
                                        .. attribute:: error_regval
                                        
                                        	error regval
                                        	**type**\: list of int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'asic-errors-oper'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr, self).__init__()

                                            self.yang_name = "last-err"
                                            self.yang_parent_name = "error"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('at_time', (YLeaf(YType.uint64, 'at-time'), ['int'])),
                                                ('at_time_nsec', (YLeaf(YType.uint64, 'at-time-nsec'), ['int'])),
                                                ('counter_val', (YLeaf(YType.uint32, 'counter-val'), ['int'])),
                                                ('error_desc', (YLeaf(YType.str, 'error-desc'), ['str'])),
                                                ('error_regval', (YLeafList(YType.uint8, 'error-regval'), ['int'])),
                                            ])
                                            self.at_time = None
                                            self.at_time_nsec = None
                                            self.counter_val = None
                                            self.error_desc = None
                                            self.error_regval = []
                                            self._segment_path = lambda: "last-err"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(AsicErrors.Nodes.Node.AsicInformation.Instances.Instance.ErrorPath.AsicErrorMbeHard.Error.LastErr, [u'at_time', u'at_time_nsec', u'counter_val', u'error_desc', u'error_regval'], name, value)

    def clone_ptr(self):
        self._top_entity = AsicErrors()
        return self._top_entity

