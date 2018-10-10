""" Cisco_IOS_XR_manageability_perfmgmt_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-perfmgmt package configuration.

This module contains definitions
for the following management objects\:
  perf\-mgmt\: Performance Management configuration & operations

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PmThresholdOp(Enum):
    """
    PmThresholdOp (Enum Class)

    Pm threshold op

    .. data:: eq = 1

    	Equal to

    .. data:: ne = 2

    	Not equal to

    .. data:: lt = 3

    	Less than

    .. data:: le = 4

    	Less than or equal to

    .. data:: gt = 5

    	Greater than

    .. data:: ge = 6

    	Greater than or equal to

    .. data:: rg = 7

    	Not in Range

    """

    eq = Enum.YLeaf(1, "eq")

    ne = Enum.YLeaf(2, "ne")

    lt = Enum.YLeaf(3, "lt")

    le = Enum.YLeaf(4, "le")

    gt = Enum.YLeaf(5, "gt")

    ge = Enum.YLeaf(6, "ge")

    rg = Enum.YLeaf(7, "rg")


class PmThresholdRearm(Enum):
    """
    PmThresholdRearm (Enum Class)

    Pm threshold rearm

    .. data:: always = 0

    	Rearm Always

    .. data:: window = 1

    	Rearm after window of sampling periods

    .. data:: toggle = 2

    	Rearm after the first period when condition is

    	not met

    """

    always = Enum.YLeaf(0, "always")

    window = Enum.YLeaf(1, "window")

    toggle = Enum.YLeaf(2, "toggle")



class PerfMgmt(Entity):
    """
    Performance Management configuration & operations
    
    .. attribute:: resources
    
    	Resources configuration
    	**type**\:  :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources>`
    
    .. attribute:: statistics
    
    	Templates for collection of statistics
    	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics>`
    
    .. attribute:: enable
    
    	Start data collection and/or threshold monitoring
    	**type**\:  :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable>`
    
    .. attribute:: reg_exp_groups
    
    	Configure regular expression group
    	**type**\:  :py:class:`RegExpGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups>`
    
    .. attribute:: threshold
    
    	Container for threshold templates
    	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold>`
    
    

    """

    _prefix = 'manageability-perfmgmt-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(PerfMgmt, self).__init__()
        self._top_entity = None

        self.yang_name = "perf-mgmt"
        self.yang_parent_name = "Cisco-IOS-XR-manageability-perfmgmt-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("resources", ("resources", PerfMgmt.Resources)), ("statistics", ("statistics", PerfMgmt.Statistics)), ("enable", ("enable", PerfMgmt.Enable)), ("reg-exp-groups", ("reg_exp_groups", PerfMgmt.RegExpGroups)), ("threshold", ("threshold", PerfMgmt.Threshold))])
        self._leafs = OrderedDict()

        self.resources = PerfMgmt.Resources()
        self.resources.parent = self
        self._children_name_map["resources"] = "resources"

        self.statistics = PerfMgmt.Statistics()
        self.statistics.parent = self
        self._children_name_map["statistics"] = "statistics"

        self.enable = PerfMgmt.Enable()
        self.enable.parent = self
        self._children_name_map["enable"] = "enable"

        self.reg_exp_groups = PerfMgmt.RegExpGroups()
        self.reg_exp_groups.parent = self
        self._children_name_map["reg_exp_groups"] = "reg-exp-groups"

        self.threshold = PerfMgmt.Threshold()
        self.threshold.parent = self
        self._children_name_map["threshold"] = "threshold"
        self._segment_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PerfMgmt, [], name, value)


    class Resources(Entity):
        """
        Resources configuration
        
        .. attribute:: tftp_resources
        
        	Configure the TFTP server IP address and directory name
        	**type**\:  :py:class:`TftpResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources.TftpResources>`
        
        	**presence node**\: True
        
        .. attribute:: dump_local
        
        	Configure local dump parameters
        	**type**\:  :py:class:`DumpLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources.DumpLocal>`
        
        .. attribute:: memory_resources
        
        	Configure the memory usage limits of performance management
        	**type**\:  :py:class:`MemoryResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources.MemoryResources>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.Resources, self).__init__()

            self.yang_name = "resources"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("tftp-resources", ("tftp_resources", PerfMgmt.Resources.TftpResources)), ("dump-local", ("dump_local", PerfMgmt.Resources.DumpLocal)), ("memory-resources", ("memory_resources", PerfMgmt.Resources.MemoryResources))])
            self._leafs = OrderedDict()

            self.tftp_resources = None
            self._children_name_map["tftp_resources"] = "tftp-resources"

            self.dump_local = PerfMgmt.Resources.DumpLocal()
            self.dump_local.parent = self
            self._children_name_map["dump_local"] = "dump-local"

            self.memory_resources = PerfMgmt.Resources.MemoryResources()
            self.memory_resources.parent = self
            self._children_name_map["memory_resources"] = "memory-resources"
            self._segment_path = lambda: "resources"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.Resources, [], name, value)


        class TftpResources(Entity):
            """
            Configure the TFTP server IP address and
            directory name
            
            .. attribute:: server_address
            
            	IP address of the TFTP server
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            .. attribute:: directory
            
            	Directory name on TFTP server
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            	**length:** 1..32
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Resources.TftpResources, self).__init__()

                self.yang_name = "tftp-resources"
                self.yang_parent_name = "resources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                    ('directory', (YLeaf(YType.str, 'directory'), ['str'])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.server_address = None
                self.directory = None
                self.vrf_name = None
                self._segment_path = lambda: "tftp-resources"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/resources/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Resources.TftpResources, ['server_address', 'directory', 'vrf_name'], name, value)


        class DumpLocal(Entity):
            """
            Configure local dump parameters
            
            .. attribute:: enable
            
            	Enable data dump onto local filesystem
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Resources.DumpLocal, self).__init__()

                self.yang_name = "dump-local"
                self.yang_parent_name = "resources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.enable = None
                self._segment_path = lambda: "dump-local"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/resources/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Resources.DumpLocal, ['enable'], name, value)


        class MemoryResources(Entity):
            """
            Configure the memory usage limits of
            performance management
            
            .. attribute:: max_limit
            
            	Maximum limit for memory usage (Kbytes) for data buffers
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobyte
            
            .. attribute:: min_reserved
            
            	Specify a minimum free memory (Kbytes) to be ensured before allowing a collection request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobyte
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Resources.MemoryResources, self).__init__()

                self.yang_name = "memory-resources"
                self.yang_parent_name = "resources"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('max_limit', (YLeaf(YType.uint32, 'max-limit'), ['int'])),
                    ('min_reserved', (YLeaf(YType.uint32, 'min-reserved'), ['int'])),
                ])
                self.max_limit = None
                self.min_reserved = None
                self._segment_path = lambda: "memory-resources"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/resources/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Resources.MemoryResources, ['max_limit', 'min_reserved'], name, value)


    class Statistics(Entity):
        """
        Templates for collection of statistics
        
        .. attribute:: generic_counter_interface
        
        	Interface Generic GenericCounter collection templates
        	**type**\:  :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.GenericCounterInterface>`
        
        .. attribute:: process_node
        
        	Node Process collection templates
        	**type**\:  :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.ProcessNode>`
        
        .. attribute:: basic_counter_interface
        
        	Interface BasicCounter collection templates
        	**type**\:  :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.BasicCounterInterface>`
        
        .. attribute:: ospfv3_protocol
        
        	OSPF v3 Protocol collection templates
        	**type**\:  :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv3Protocol>`
        
        .. attribute:: cpu_node
        
        	Node CPU collection templates
        	**type**\:  :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.CpuNode>`
        
        .. attribute:: data_rate_interface
        
        	Interface DataRate collection templates
        	**type**\:  :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.DataRateInterface>`
        
        .. attribute:: memory_node
        
        	Node Memory collection templates
        	**type**\:  :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.MemoryNode>`
        
        .. attribute:: ldp_mpls
        
        	MPLS LDP collection templates
        	**type**\:  :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.LdpMpls>`
        
        .. attribute:: bgp
        
        	BGP collection templates
        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Bgp>`
        
        .. attribute:: ospfv2_protocol
        
        	OSPF v2 Protocol collection templates
        	**type**\:  :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv2Protocol>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.Statistics, self).__init__()

            self.yang_name = "statistics"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("generic-counter-interface", ("generic_counter_interface", PerfMgmt.Statistics.GenericCounterInterface)), ("process-node", ("process_node", PerfMgmt.Statistics.ProcessNode)), ("basic-counter-interface", ("basic_counter_interface", PerfMgmt.Statistics.BasicCounterInterface)), ("ospfv3-protocol", ("ospfv3_protocol", PerfMgmt.Statistics.Ospfv3Protocol)), ("cpu-node", ("cpu_node", PerfMgmt.Statistics.CpuNode)), ("data-rate-interface", ("data_rate_interface", PerfMgmt.Statistics.DataRateInterface)), ("memory-node", ("memory_node", PerfMgmt.Statistics.MemoryNode)), ("ldp-mpls", ("ldp_mpls", PerfMgmt.Statistics.LdpMpls)), ("bgp", ("bgp", PerfMgmt.Statistics.Bgp)), ("ospfv2-protocol", ("ospfv2_protocol", PerfMgmt.Statistics.Ospfv2Protocol))])
            self._leafs = OrderedDict()

            self.generic_counter_interface = PerfMgmt.Statistics.GenericCounterInterface()
            self.generic_counter_interface.parent = self
            self._children_name_map["generic_counter_interface"] = "generic-counter-interface"

            self.process_node = PerfMgmt.Statistics.ProcessNode()
            self.process_node.parent = self
            self._children_name_map["process_node"] = "process-node"

            self.basic_counter_interface = PerfMgmt.Statistics.BasicCounterInterface()
            self.basic_counter_interface.parent = self
            self._children_name_map["basic_counter_interface"] = "basic-counter-interface"

            self.ospfv3_protocol = PerfMgmt.Statistics.Ospfv3Protocol()
            self.ospfv3_protocol.parent = self
            self._children_name_map["ospfv3_protocol"] = "ospfv3-protocol"

            self.cpu_node = PerfMgmt.Statistics.CpuNode()
            self.cpu_node.parent = self
            self._children_name_map["cpu_node"] = "cpu-node"

            self.data_rate_interface = PerfMgmt.Statistics.DataRateInterface()
            self.data_rate_interface.parent = self
            self._children_name_map["data_rate_interface"] = "data-rate-interface"

            self.memory_node = PerfMgmt.Statistics.MemoryNode()
            self.memory_node.parent = self
            self._children_name_map["memory_node"] = "memory-node"

            self.ldp_mpls = PerfMgmt.Statistics.LdpMpls()
            self.ldp_mpls.parent = self
            self._children_name_map["ldp_mpls"] = "ldp-mpls"

            self.bgp = PerfMgmt.Statistics.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"

            self.ospfv2_protocol = PerfMgmt.Statistics.Ospfv2Protocol()
            self.ospfv2_protocol.parent = self
            self._children_name_map["ospfv2_protocol"] = "ospfv2-protocol"
            self._segment_path = lambda: "statistics"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.Statistics, [], name, value)


        class GenericCounterInterface(Entity):
            """
            Interface Generic GenericCounter collection
            templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.GenericCounterInterface.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.GenericCounterInterface, self).__init__()

                self.yang_name = "generic-counter-interface"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.GenericCounterInterface.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.GenericCounterInterface.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "generic-counter-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.GenericCounterInterface, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.GenericCounterInterface.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.GenericCounterInterface.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "generic-counter-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.GenericCounterInterface.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/generic-counter-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.GenericCounterInterface.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.GenericCounterInterface.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/generic-counter-interface/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.GenericCounterInterface.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class ProcessNode(Entity):
            """
            Node Process collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.ProcessNode.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.ProcessNode, self).__init__()

                self.yang_name = "process-node"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.ProcessNode.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.ProcessNode.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "process-node"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.ProcessNode, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.ProcessNode.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.ProcessNode.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "process-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.ProcessNode.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/process-node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.ProcessNode.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.ProcessNode.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/process-node/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.ProcessNode.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class BasicCounterInterface(Entity):
            """
            Interface BasicCounter collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.BasicCounterInterface.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.BasicCounterInterface, self).__init__()

                self.yang_name = "basic-counter-interface"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.BasicCounterInterface.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.BasicCounterInterface.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "basic-counter-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.BasicCounterInterface, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.BasicCounterInterface.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.BasicCounterInterface.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "basic-counter-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.BasicCounterInterface.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/basic-counter-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.BasicCounterInterface.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.BasicCounterInterface.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/basic-counter-interface/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.BasicCounterInterface.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class Ospfv3Protocol(Entity):
            """
            OSPF v3 Protocol collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv3Protocol.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.Ospfv3Protocol, self).__init__()

                self.yang_name = "ospfv3-protocol"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.Ospfv3Protocol.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.Ospfv3Protocol.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "ospfv3-protocol"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.Ospfv3Protocol, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.Ospfv3Protocol.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "ospfv3-protocol"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/ospfv3-protocol/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.Ospfv3Protocol.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/ospfv3-protocol/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class CpuNode(Entity):
            """
            Node CPU collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.CpuNode.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.CpuNode, self).__init__()

                self.yang_name = "cpu-node"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.CpuNode.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.CpuNode.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "cpu-node"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.CpuNode, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.CpuNode.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.CpuNode.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "cpu-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.CpuNode.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/cpu-node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.CpuNode.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.CpuNode.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/cpu-node/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.CpuNode.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class DataRateInterface(Entity):
            """
            Interface DataRate collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.DataRateInterface.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.DataRateInterface, self).__init__()

                self.yang_name = "data-rate-interface"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.DataRateInterface.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.DataRateInterface.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "data-rate-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.DataRateInterface, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.DataRateInterface.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.DataRateInterface.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "data-rate-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.DataRateInterface.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/data-rate-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.DataRateInterface.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.DataRateInterface.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/data-rate-interface/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.DataRateInterface.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class MemoryNode(Entity):
            """
            Node Memory collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.MemoryNode.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.MemoryNode, self).__init__()

                self.yang_name = "memory-node"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.MemoryNode.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.MemoryNode.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "memory-node"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.MemoryNode, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.MemoryNode.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.MemoryNode.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "memory-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.MemoryNode.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/memory-node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.MemoryNode.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.MemoryNode.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/memory-node/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.MemoryNode.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class LdpMpls(Entity):
            """
            MPLS LDP collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.LdpMpls.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.LdpMpls, self).__init__()

                self.yang_name = "ldp-mpls"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.LdpMpls.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.LdpMpls.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "ldp-mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.LdpMpls, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.LdpMpls.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.LdpMpls.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "ldp-mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.LdpMpls.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/ldp-mpls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.LdpMpls.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.LdpMpls.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/ldp-mpls/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.LdpMpls.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class Bgp(Entity):
            """
            BGP collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Bgp.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.Bgp.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.Bgp.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.Bgp, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Bgp.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.Bgp.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.Bgp.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/bgp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.Bgp.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.Bgp.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/bgp/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.Bgp.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


        class Ospfv2Protocol(Entity):
            """
            OSPF v2 Protocol collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:  :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv2Protocol.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Statistics.Ospfv2Protocol, self).__init__()

                self.yang_name = "ospfv2-protocol"
                self.yang_parent_name = "statistics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("templates", ("templates", PerfMgmt.Statistics.Ospfv2Protocol.Templates))])
                self._leafs = OrderedDict()

                self.templates = PerfMgmt.Statistics.Ospfv2Protocol.Templates()
                self.templates.parent = self
                self._children_name_map["templates"] = "templates"
                self._segment_path = lambda: "ospfv2-protocol"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Statistics.Ospfv2Protocol, [], name, value)


            class Templates(Entity):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of  		 :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Statistics.Ospfv2Protocol.Templates, self).__init__()

                    self.yang_name = "templates"
                    self.yang_parent_name = "ospfv2-protocol"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("template", ("template", PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template))])
                    self._leafs = OrderedDict()

                    self.template = YList(self)
                    self._segment_path = lambda: "templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/ospfv2-protocol/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Statistics.Ospfv2Protocol.Templates, [], name, value)


                class Template(Entity):
                    """
                    A template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template, self).__init__()

                        self.yang_name = "template"
                        self.yang_parent_name = "templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('history_persistent', (YLeaf(YType.empty, 'history-persistent'), ['Empty'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('sample_size', (YLeaf(YType.uint32, 'sample-size'), ['int'])),
                        ])
                        self.template_name = None
                        self.reg_exp_group = None
                        self.history_persistent = None
                        self.vrf_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self._segment_path = lambda: "template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/statistics/ospfv2-protocol/templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template, ['template_name', 'reg_exp_group', 'history_persistent', 'vrf_group', 'sample_interval', 'sample_size'], name, value)


    class Enable(Entity):
        """
        Start data collection and/or threshold
        monitoring
        
        .. attribute:: threshold
        
        	Start threshold monitoring using a defined template
        	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold>`
        
        .. attribute:: statistics
        
        	Start periodic collection using a defined a template
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics>`
        
        .. attribute:: monitor_enable
        
        	Start data collection for a monitored instance
        	**type**\:  :py:class:`MonitorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.Enable, self).__init__()

            self.yang_name = "enable"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("threshold", ("threshold", PerfMgmt.Enable.Threshold)), ("statistics", ("statistics", PerfMgmt.Enable.Statistics)), ("monitor-enable", ("monitor_enable", PerfMgmt.Enable.MonitorEnable))])
            self._leafs = OrderedDict()

            self.threshold = PerfMgmt.Enable.Threshold()
            self.threshold.parent = self
            self._children_name_map["threshold"] = "threshold"

            self.statistics = PerfMgmt.Enable.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"

            self.monitor_enable = PerfMgmt.Enable.MonitorEnable()
            self.monitor_enable.parent = self
            self._children_name_map["monitor_enable"] = "monitor-enable"
            self._segment_path = lambda: "enable"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.Enable, [], name, value)


        class Threshold(Entity):
            """
            Start threshold monitoring using a defined
            template
            
            .. attribute:: ospfv3_protocol
            
            	Threshold monitoring for OSPF v3 Protocol
            	**type**\:  :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.Ospfv3Protocol>`
            
            .. attribute:: bgp
            
            	Threshold monitoring for BGP
            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.Bgp>`
            
            .. attribute:: data_rate_interface
            
            	Threshold monitoring for Interface  data\-rates
            	**type**\:  :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.DataRateInterface>`
            
            .. attribute:: ospfv2_protocol
            
            	Threshold monitoring for OSPF v2 Protocol
            	**type**\:  :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.Ospfv2Protocol>`
            
            .. attribute:: memory_node
            
            	Threshold monitoring for memory
            	**type**\:  :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode>`
            
            .. attribute:: generic_counter_interface
            
            	Threshold monitoring for Interface generic\-counters
            	**type**\:  :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.GenericCounterInterface>`
            
            .. attribute:: cpu_node
            
            	Threshold monitoring for CPU
            	**type**\:  :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode>`
            
            .. attribute:: ldp_mpls
            
            	Threshold monitoring for LDP
            	**type**\:  :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.LdpMpls>`
            
            .. attribute:: process_node
            
            	Threshold monitoring for process
            	**type**\:  :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode>`
            
            .. attribute:: basic_counter_interface
            
            	Threshold monitoring for Interface basic\-counters
            	**type**\:  :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.BasicCounterInterface>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Enable.Threshold, self).__init__()

                self.yang_name = "threshold"
                self.yang_parent_name = "enable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ospfv3-protocol", ("ospfv3_protocol", PerfMgmt.Enable.Threshold.Ospfv3Protocol)), ("bgp", ("bgp", PerfMgmt.Enable.Threshold.Bgp)), ("data-rate-interface", ("data_rate_interface", PerfMgmt.Enable.Threshold.DataRateInterface)), ("ospfv2-protocol", ("ospfv2_protocol", PerfMgmt.Enable.Threshold.Ospfv2Protocol)), ("memory-node", ("memory_node", PerfMgmt.Enable.Threshold.MemoryNode)), ("generic-counter-interface", ("generic_counter_interface", PerfMgmt.Enable.Threshold.GenericCounterInterface)), ("cpu-node", ("cpu_node", PerfMgmt.Enable.Threshold.CpuNode)), ("ldp-mpls", ("ldp_mpls", PerfMgmt.Enable.Threshold.LdpMpls)), ("process-node", ("process_node", PerfMgmt.Enable.Threshold.ProcessNode)), ("basic-counter-interface", ("basic_counter_interface", PerfMgmt.Enable.Threshold.BasicCounterInterface))])
                self._leafs = OrderedDict()

                self.ospfv3_protocol = PerfMgmt.Enable.Threshold.Ospfv3Protocol()
                self.ospfv3_protocol.parent = self
                self._children_name_map["ospfv3_protocol"] = "ospfv3-protocol"

                self.bgp = PerfMgmt.Enable.Threshold.Bgp()
                self.bgp.parent = self
                self._children_name_map["bgp"] = "bgp"

                self.data_rate_interface = PerfMgmt.Enable.Threshold.DataRateInterface()
                self.data_rate_interface.parent = self
                self._children_name_map["data_rate_interface"] = "data-rate-interface"

                self.ospfv2_protocol = PerfMgmt.Enable.Threshold.Ospfv2Protocol()
                self.ospfv2_protocol.parent = self
                self._children_name_map["ospfv2_protocol"] = "ospfv2-protocol"

                self.memory_node = PerfMgmt.Enable.Threshold.MemoryNode()
                self.memory_node.parent = self
                self._children_name_map["memory_node"] = "memory-node"

                self.generic_counter_interface = PerfMgmt.Enable.Threshold.GenericCounterInterface()
                self.generic_counter_interface.parent = self
                self._children_name_map["generic_counter_interface"] = "generic-counter-interface"

                self.cpu_node = PerfMgmt.Enable.Threshold.CpuNode()
                self.cpu_node.parent = self
                self._children_name_map["cpu_node"] = "cpu-node"

                self.ldp_mpls = PerfMgmt.Enable.Threshold.LdpMpls()
                self.ldp_mpls.parent = self
                self._children_name_map["ldp_mpls"] = "ldp-mpls"

                self.process_node = PerfMgmt.Enable.Threshold.ProcessNode()
                self.process_node.parent = self
                self._children_name_map["process_node"] = "process-node"

                self.basic_counter_interface = PerfMgmt.Enable.Threshold.BasicCounterInterface()
                self.basic_counter_interface.parent = self
                self._children_name_map["basic_counter_interface"] = "basic-counter-interface"
                self._segment_path = lambda: "threshold"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Enable.Threshold, [], name, value)


            class Ospfv3Protocol(Entity):
                """
                Threshold monitoring for OSPF v3 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.Ospfv3Protocol, self).__init__()

                    self.yang_name = "ospfv3-protocol"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "ospfv3-protocol"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.Ospfv3Protocol, ['template_name'], name, value)


            class Bgp(Entity):
                """
                Threshold monitoring for BGP
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.Bgp, self).__init__()

                    self.yang_name = "bgp"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "bgp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.Bgp, ['template_name'], name, value)


            class DataRateInterface(Entity):
                """
                Threshold monitoring for Interface  data\-rates
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.DataRateInterface, self).__init__()

                    self.yang_name = "data-rate-interface"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "data-rate-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.DataRateInterface, ['template_name'], name, value)


            class Ospfv2Protocol(Entity):
                """
                Threshold monitoring for OSPF v2 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.Ospfv2Protocol, self).__init__()

                    self.yang_name = "ospfv2-protocol"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "ospfv2-protocol"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.Ospfv2Protocol, ['template_name'], name, value)


            class MemoryNode(Entity):
                """
                Threshold monitoring for memory
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode.Nodes>`
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode.NodeAll>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.MemoryNode, self).__init__()

                    self.yang_name = "memory-node"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nodes", ("nodes", PerfMgmt.Enable.Threshold.MemoryNode.Nodes)), ("node-all", ("node_all", PerfMgmt.Enable.Threshold.MemoryNode.NodeAll))])
                    self._leafs = OrderedDict()

                    self.nodes = PerfMgmt.Enable.Threshold.MemoryNode.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"

                    self.node_all = PerfMgmt.Enable.Threshold.MemoryNode.NodeAll()
                    self.node_all.parent = self
                    self._children_name_map["node_all"] = "node-all"
                    self._segment_path = lambda: "memory-node"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.MemoryNode, [], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Threshold.MemoryNode.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "memory-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/memory-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Threshold.MemoryNode.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/memory-node/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node, ['node_id', 'template_name'], name, value)


                class NodeAll(Entity):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Threshold.MemoryNode.NodeAll, self).__init__()

                        self.yang_name = "node-all"
                        self.yang_parent_name = "memory-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ])
                        self.template_name = None
                        self._segment_path = lambda: "node-all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/memory-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Threshold.MemoryNode.NodeAll, ['template_name'], name, value)


            class GenericCounterInterface(Entity):
                """
                Threshold monitoring for Interface
                generic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.GenericCounterInterface, self).__init__()

                    self.yang_name = "generic-counter-interface"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "generic-counter-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.GenericCounterInterface, ['template_name'], name, value)


            class CpuNode(Entity):
                """
                Threshold monitoring for CPU
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode.Nodes>`
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode.NodeAll>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.CpuNode, self).__init__()

                    self.yang_name = "cpu-node"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nodes", ("nodes", PerfMgmt.Enable.Threshold.CpuNode.Nodes)), ("node-all", ("node_all", PerfMgmt.Enable.Threshold.CpuNode.NodeAll))])
                    self._leafs = OrderedDict()

                    self.nodes = PerfMgmt.Enable.Threshold.CpuNode.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"

                    self.node_all = PerfMgmt.Enable.Threshold.CpuNode.NodeAll()
                    self.node_all.parent = self
                    self._children_name_map["node_all"] = "node-all"
                    self._segment_path = lambda: "cpu-node"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.CpuNode, [], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Threshold.CpuNode.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "cpu-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/cpu-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Threshold.CpuNode.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/cpu-node/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node, ['node_id', 'template_name'], name, value)


                class NodeAll(Entity):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Threshold.CpuNode.NodeAll, self).__init__()

                        self.yang_name = "node-all"
                        self.yang_parent_name = "cpu-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ])
                        self.template_name = None
                        self._segment_path = lambda: "node-all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/cpu-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Threshold.CpuNode.NodeAll, ['template_name'], name, value)


            class LdpMpls(Entity):
                """
                Threshold monitoring for LDP
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.LdpMpls, self).__init__()

                    self.yang_name = "ldp-mpls"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "ldp-mpls"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.LdpMpls, ['template_name'], name, value)


            class ProcessNode(Entity):
                """
                Threshold monitoring for process
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode.Nodes>`
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode.NodeAll>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.ProcessNode, self).__init__()

                    self.yang_name = "process-node"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nodes", ("nodes", PerfMgmt.Enable.Threshold.ProcessNode.Nodes)), ("node-all", ("node_all", PerfMgmt.Enable.Threshold.ProcessNode.NodeAll))])
                    self._leafs = OrderedDict()

                    self.nodes = PerfMgmt.Enable.Threshold.ProcessNode.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"

                    self.node_all = PerfMgmt.Enable.Threshold.ProcessNode.NodeAll()
                    self.node_all.parent = self
                    self._children_name_map["node_all"] = "node-all"
                    self._segment_path = lambda: "process-node"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.ProcessNode, [], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Threshold.ProcessNode.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "process-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/process-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Threshold.ProcessNode.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/process-node/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node, ['node_id', 'template_name'], name, value)


                class NodeAll(Entity):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Threshold.ProcessNode.NodeAll, self).__init__()

                        self.yang_name = "node-all"
                        self.yang_parent_name = "process-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ])
                        self.template_name = None
                        self._segment_path = lambda: "node-all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/process-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Threshold.ProcessNode.NodeAll, ['template_name'], name, value)


            class BasicCounterInterface(Entity):
                """
                Threshold monitoring for Interface
                basic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Threshold.BasicCounterInterface, self).__init__()

                    self.yang_name = "basic-counter-interface"
                    self.yang_parent_name = "threshold"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "basic-counter-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/threshold/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Threshold.BasicCounterInterface, ['template_name'], name, value)


        class Statistics(Entity):
            """
            Start periodic collection using a defined a
            template
            
            .. attribute:: generic_counter_interface
            
            	Statistics collection for generic\-counters
            	**type**\:  :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.GenericCounterInterface>`
            
            .. attribute:: bgp
            
            	Data collection for BGP
            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.Bgp>`
            
            .. attribute:: ospfv2_protocol
            
            	Data collection for OSPF v2 Protocol
            	**type**\:  :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.Ospfv2Protocol>`
            
            .. attribute:: ospfv3_protocol
            
            	Data collection for OSPF v3 Protocol
            	**type**\:  :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.Ospfv3Protocol>`
            
            .. attribute:: cpu_node
            
            	Collection for CPU
            	**type**\:  :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode>`
            
            .. attribute:: basic_counter_interface
            
            	Statistics collection for basic\-counters
            	**type**\:  :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.BasicCounterInterface>`
            
            .. attribute:: process_node
            
            	Collection for process
            	**type**\:  :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode>`
            
            .. attribute:: data_rate_interface
            
            	Statistics collection for generic\-counters
            	**type**\:  :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.DataRateInterface>`
            
            .. attribute:: memory_node
            
            	Collection for memory
            	**type**\:  :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode>`
            
            .. attribute:: ldp_mpls
            
            	Collection for labels distribution protocol
            	**type**\:  :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.LdpMpls>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Enable.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "enable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("generic-counter-interface", ("generic_counter_interface", PerfMgmt.Enable.Statistics.GenericCounterInterface)), ("bgp", ("bgp", PerfMgmt.Enable.Statistics.Bgp)), ("ospfv2-protocol", ("ospfv2_protocol", PerfMgmt.Enable.Statistics.Ospfv2Protocol)), ("ospfv3-protocol", ("ospfv3_protocol", PerfMgmt.Enable.Statistics.Ospfv3Protocol)), ("cpu-node", ("cpu_node", PerfMgmt.Enable.Statistics.CpuNode)), ("basic-counter-interface", ("basic_counter_interface", PerfMgmt.Enable.Statistics.BasicCounterInterface)), ("process-node", ("process_node", PerfMgmt.Enable.Statistics.ProcessNode)), ("data-rate-interface", ("data_rate_interface", PerfMgmt.Enable.Statistics.DataRateInterface)), ("memory-node", ("memory_node", PerfMgmt.Enable.Statistics.MemoryNode)), ("ldp-mpls", ("ldp_mpls", PerfMgmt.Enable.Statistics.LdpMpls))])
                self._leafs = OrderedDict()

                self.generic_counter_interface = PerfMgmt.Enable.Statistics.GenericCounterInterface()
                self.generic_counter_interface.parent = self
                self._children_name_map["generic_counter_interface"] = "generic-counter-interface"

                self.bgp = PerfMgmt.Enable.Statistics.Bgp()
                self.bgp.parent = self
                self._children_name_map["bgp"] = "bgp"

                self.ospfv2_protocol = PerfMgmt.Enable.Statistics.Ospfv2Protocol()
                self.ospfv2_protocol.parent = self
                self._children_name_map["ospfv2_protocol"] = "ospfv2-protocol"

                self.ospfv3_protocol = PerfMgmt.Enable.Statistics.Ospfv3Protocol()
                self.ospfv3_protocol.parent = self
                self._children_name_map["ospfv3_protocol"] = "ospfv3-protocol"

                self.cpu_node = PerfMgmt.Enable.Statistics.CpuNode()
                self.cpu_node.parent = self
                self._children_name_map["cpu_node"] = "cpu-node"

                self.basic_counter_interface = PerfMgmt.Enable.Statistics.BasicCounterInterface()
                self.basic_counter_interface.parent = self
                self._children_name_map["basic_counter_interface"] = "basic-counter-interface"

                self.process_node = PerfMgmt.Enable.Statistics.ProcessNode()
                self.process_node.parent = self
                self._children_name_map["process_node"] = "process-node"

                self.data_rate_interface = PerfMgmt.Enable.Statistics.DataRateInterface()
                self.data_rate_interface.parent = self
                self._children_name_map["data_rate_interface"] = "data-rate-interface"

                self.memory_node = PerfMgmt.Enable.Statistics.MemoryNode()
                self.memory_node.parent = self
                self._children_name_map["memory_node"] = "memory-node"

                self.ldp_mpls = PerfMgmt.Enable.Statistics.LdpMpls()
                self.ldp_mpls.parent = self
                self._children_name_map["ldp_mpls"] = "ldp-mpls"
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Enable.Statistics, [], name, value)


            class GenericCounterInterface(Entity):
                """
                Statistics collection for generic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.GenericCounterInterface, self).__init__()

                    self.yang_name = "generic-counter-interface"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "generic-counter-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.GenericCounterInterface, ['template_name'], name, value)


            class Bgp(Entity):
                """
                Data collection for BGP
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.Bgp, self).__init__()

                    self.yang_name = "bgp"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "bgp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.Bgp, ['template_name'], name, value)


            class Ospfv2Protocol(Entity):
                """
                Data collection for OSPF v2 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.Ospfv2Protocol, self).__init__()

                    self.yang_name = "ospfv2-protocol"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "ospfv2-protocol"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.Ospfv2Protocol, ['template_name'], name, value)


            class Ospfv3Protocol(Entity):
                """
                Data collection for OSPF v3 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.Ospfv3Protocol, self).__init__()

                    self.yang_name = "ospfv3-protocol"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "ospfv3-protocol"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.Ospfv3Protocol, ['template_name'], name, value)


            class CpuNode(Entity):
                """
                Collection for CPU
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.CpuNode, self).__init__()

                    self.yang_name = "cpu-node"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-all", ("node_all", PerfMgmt.Enable.Statistics.CpuNode.NodeAll)), ("nodes", ("nodes", PerfMgmt.Enable.Statistics.CpuNode.Nodes))])
                    self._leafs = OrderedDict()

                    self.node_all = PerfMgmt.Enable.Statistics.CpuNode.NodeAll()
                    self.node_all.parent = self
                    self._children_name_map["node_all"] = "node-all"

                    self.nodes = PerfMgmt.Enable.Statistics.CpuNode.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "cpu-node"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.CpuNode, [], name, value)


                class NodeAll(Entity):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Statistics.CpuNode.NodeAll, self).__init__()

                        self.yang_name = "node-all"
                        self.yang_parent_name = "cpu-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ])
                        self.template_name = None
                        self._segment_path = lambda: "node-all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/cpu-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Statistics.CpuNode.NodeAll, ['template_name'], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Statistics.CpuNode.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "cpu-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/cpu-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Statistics.CpuNode.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/cpu-node/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node, ['node_id', 'template_name'], name, value)


            class BasicCounterInterface(Entity):
                """
                Statistics collection for basic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.BasicCounterInterface, self).__init__()

                    self.yang_name = "basic-counter-interface"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "basic-counter-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.BasicCounterInterface, ['template_name'], name, value)


            class ProcessNode(Entity):
                """
                Collection for process
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.ProcessNode, self).__init__()

                    self.yang_name = "process-node"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-all", ("node_all", PerfMgmt.Enable.Statistics.ProcessNode.NodeAll)), ("nodes", ("nodes", PerfMgmt.Enable.Statistics.ProcessNode.Nodes))])
                    self._leafs = OrderedDict()

                    self.node_all = PerfMgmt.Enable.Statistics.ProcessNode.NodeAll()
                    self.node_all.parent = self
                    self._children_name_map["node_all"] = "node-all"

                    self.nodes = PerfMgmt.Enable.Statistics.ProcessNode.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "process-node"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.ProcessNode, [], name, value)


                class NodeAll(Entity):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Statistics.ProcessNode.NodeAll, self).__init__()

                        self.yang_name = "node-all"
                        self.yang_parent_name = "process-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ])
                        self.template_name = None
                        self._segment_path = lambda: "node-all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/process-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Statistics.ProcessNode.NodeAll, ['template_name'], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Statistics.ProcessNode.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "process-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/process-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Statistics.ProcessNode.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/process-node/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node, ['node_id', 'template_name'], name, value)


            class DataRateInterface(Entity):
                """
                Statistics collection for generic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.DataRateInterface, self).__init__()

                    self.yang_name = "data-rate-interface"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "data-rate-interface"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.DataRateInterface, ['template_name'], name, value)


            class MemoryNode(Entity):
                """
                Collection for memory
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:  :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.MemoryNode, self).__init__()

                    self.yang_name = "memory-node"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("node-all", ("node_all", PerfMgmt.Enable.Statistics.MemoryNode.NodeAll)), ("nodes", ("nodes", PerfMgmt.Enable.Statistics.MemoryNode.Nodes))])
                    self._leafs = OrderedDict()

                    self.node_all = PerfMgmt.Enable.Statistics.MemoryNode.NodeAll()
                    self.node_all.parent = self
                    self._children_name_map["node_all"] = "node-all"

                    self.nodes = PerfMgmt.Enable.Statistics.MemoryNode.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "memory-node"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.MemoryNode, [], name, value)


                class NodeAll(Entity):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Statistics.MemoryNode.NodeAll, self).__init__()

                        self.yang_name = "node-all"
                        self.yang_parent_name = "memory-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                        ])
                        self.template_name = None
                        self._segment_path = lambda: "node-all"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/memory-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Statistics.MemoryNode.NodeAll, ['template_name'], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.Statistics.MemoryNode.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "memory-node"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/memory-node/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.Statistics.MemoryNode.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/memory-node/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node, ['node_id', 'template_name'], name, value)


            class LdpMpls(Entity):
                """
                Collection for labels distribution protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\: str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.Statistics.LdpMpls, self).__init__()

                    self.yang_name = "ldp-mpls"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                    ])
                    self.template_name = None
                    self._segment_path = lambda: "ldp-mpls"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.Statistics.LdpMpls, ['template_name'], name, value)


        class MonitorEnable(Entity):
            """
            Start data collection for a monitored instance
            
            .. attribute:: ldp_mpls
            
            	Monitoring for LDP
            	**type**\:  :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.LdpMpls>`
            
            .. attribute:: ospfv3_protocol
            
            	Monitor OSPF v3 Protocol
            	**type**\:  :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol>`
            
            .. attribute:: generic_counters
            
            	Monitoring for generic\-counters
            	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.GenericCounters>`
            
            .. attribute:: process
            
            	Collection for a single process
            	**type**\:  :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process>`
            
            .. attribute:: basic_counters
            
            	Monitoring for basic\-counters
            	**type**\:  :py:class:`BasicCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.BasicCounters>`
            
            .. attribute:: memory
            
            	Collection for memory
            	**type**\:  :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Memory>`
            
            .. attribute:: ospfv2_protocol
            
            	Monitor OSPF v2 Protocol
            	**type**\:  :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol>`
            
            .. attribute:: cpu
            
            	Collection for CPU
            	**type**\:  :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Cpu>`
            
            .. attribute:: bgp
            
            	Monitor BGP protocol
            	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Bgp>`
            
            .. attribute:: data_rates
            
            	Monitoring for data\-rates
            	**type**\:  :py:class:`DataRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.DataRates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Enable.MonitorEnable, self).__init__()

                self.yang_name = "monitor-enable"
                self.yang_parent_name = "enable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ldp-mpls", ("ldp_mpls", PerfMgmt.Enable.MonitorEnable.LdpMpls)), ("ospfv3-protocol", ("ospfv3_protocol", PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol)), ("generic-counters", ("generic_counters", PerfMgmt.Enable.MonitorEnable.GenericCounters)), ("process", ("process", PerfMgmt.Enable.MonitorEnable.Process)), ("basic-counters", ("basic_counters", PerfMgmt.Enable.MonitorEnable.BasicCounters)), ("memory", ("memory", PerfMgmt.Enable.MonitorEnable.Memory)), ("ospfv2-protocol", ("ospfv2_protocol", PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol)), ("cpu", ("cpu", PerfMgmt.Enable.MonitorEnable.Cpu)), ("bgp", ("bgp", PerfMgmt.Enable.MonitorEnable.Bgp)), ("data-rates", ("data_rates", PerfMgmt.Enable.MonitorEnable.DataRates))])
                self._leafs = OrderedDict()

                self.ldp_mpls = PerfMgmt.Enable.MonitorEnable.LdpMpls()
                self.ldp_mpls.parent = self
                self._children_name_map["ldp_mpls"] = "ldp-mpls"

                self.ospfv3_protocol = PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol()
                self.ospfv3_protocol.parent = self
                self._children_name_map["ospfv3_protocol"] = "ospfv3-protocol"

                self.generic_counters = PerfMgmt.Enable.MonitorEnable.GenericCounters()
                self.generic_counters.parent = self
                self._children_name_map["generic_counters"] = "generic-counters"

                self.process = PerfMgmt.Enable.MonitorEnable.Process()
                self.process.parent = self
                self._children_name_map["process"] = "process"

                self.basic_counters = PerfMgmt.Enable.MonitorEnable.BasicCounters()
                self.basic_counters.parent = self
                self._children_name_map["basic_counters"] = "basic-counters"

                self.memory = PerfMgmt.Enable.MonitorEnable.Memory()
                self.memory.parent = self
                self._children_name_map["memory"] = "memory"

                self.ospfv2_protocol = PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol()
                self.ospfv2_protocol.parent = self
                self._children_name_map["ospfv2_protocol"] = "ospfv2-protocol"

                self.cpu = PerfMgmt.Enable.MonitorEnable.Cpu()
                self.cpu.parent = self
                self._children_name_map["cpu"] = "cpu"

                self.bgp = PerfMgmt.Enable.MonitorEnable.Bgp()
                self.bgp.parent = self
                self._children_name_map["bgp"] = "bgp"

                self.data_rates = PerfMgmt.Enable.MonitorEnable.DataRates()
                self.data_rates.parent = self
                self._children_name_map["data_rates"] = "data-rates"
                self._segment_path = lambda: "monitor-enable"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Enable.MonitorEnable, [], name, value)


            class LdpMpls(Entity):
                """
                Monitoring for LDP
                
                .. attribute:: sessions
                
                	LDP session specification
                	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.LdpMpls, self).__init__()

                    self.yang_name = "ldp-mpls"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sessions", ("sessions", PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions))])
                    self._leafs = OrderedDict()

                    self.sessions = PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions()
                    self.sessions.parent = self
                    self._children_name_map["sessions"] = "sessions"
                    self._segment_path = lambda: "ldp-mpls"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.LdpMpls, [], name, value)


                class Sessions(Entity):
                    """
                    LDP session specification
                    
                    .. attribute:: session
                    
                    	IP address of the LDP Session
                    	**type**\: list of  		 :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions, self).__init__()

                        self.yang_name = "sessions"
                        self.yang_parent_name = "ldp-mpls"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("session", ("session", PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session))])
                        self._leafs = OrderedDict()

                        self.session = YList(self)
                        self._segment_path = lambda: "sessions"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/ldp-mpls/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions, [], name, value)


                    class Session(Entity):
                        """
                        IP address of the LDP Session
                        
                        .. attribute:: session  (key)
                        
                        	IP address of the LDP Session
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session, self).__init__()

                            self.yang_name = "session"
                            self.yang_parent_name = "sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['session']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('session', (YLeaf(YType.str, 'session'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.session = None
                            self.template_name = None
                            self._segment_path = lambda: "session" + "[session='" + str(self.session) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/ldp-mpls/sessions/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session, ['session', 'template_name'], name, value)


            class Ospfv3Protocol(Entity):
                """
                Monitor OSPF v3 Protocol
                
                .. attribute:: ospf_instances
                
                	Monitor an instance
                	**type**\:  :py:class:`OspfInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol, self).__init__()

                    self.yang_name = "ospfv3-protocol"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospf-instances", ("ospf_instances", PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances))])
                    self._leafs = OrderedDict()

                    self.ospf_instances = PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances()
                    self.ospf_instances.parent = self
                    self._children_name_map["ospf_instances"] = "ospf-instances"
                    self._segment_path = lambda: "ospfv3-protocol"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol, [], name, value)


                class OspfInstances(Entity):
                    """
                    Monitor an instance
                    
                    .. attribute:: ospf_instance
                    
                    	Instance being monitored
                    	**type**\: list of  		 :py:class:`OspfInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances, self).__init__()

                        self.yang_name = "ospf-instances"
                        self.yang_parent_name = "ospfv3-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ospf-instance", ("ospf_instance", PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance))])
                        self._leafs = OrderedDict()

                        self.ospf_instance = YList(self)
                        self._segment_path = lambda: "ospf-instances"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/ospfv3-protocol/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances, [], name, value)


                    class OspfInstance(Entity):
                        """
                        Instance being monitored
                        
                        .. attribute:: instance_name  (key)
                        
                        	OSPF Instance Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance, self).__init__()

                            self.yang_name = "ospf-instance"
                            self.yang_parent_name = "ospf-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['instance_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.instance_name = None
                            self.template_name = None
                            self._segment_path = lambda: "ospf-instance" + "[instance-name='" + str(self.instance_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/ospfv3-protocol/ospf-instances/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance, ['instance_name', 'template_name'], name, value)


            class GenericCounters(Entity):
                """
                Monitoring for generic\-counters
                
                .. attribute:: interfaces
                
                	Monitor an Interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.GenericCounters, self).__init__()

                    self.yang_name = "generic-counters"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces))])
                    self._leafs = OrderedDict()

                    self.interfaces = PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "generic-counters"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.GenericCounters, [], name, value)


                class Interfaces(Entity):
                    """
                    Monitor an Interface
                    
                    .. attribute:: interface
                    
                    	Interface being Monitored
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "generic-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/generic-counters/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        Interface being Monitored
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self.template_name = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/generic-counters/interfaces/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface, ['interface_name', 'template_name'], name, value)


            class Process(Entity):
                """
                Collection for a single process
                
                .. attribute:: process_nodes
                
                	Node specification
                	**type**\:  :py:class:`ProcessNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.Process, self).__init__()

                    self.yang_name = "process"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process-nodes", ("process_nodes", PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes))])
                    self._leafs = OrderedDict()

                    self.process_nodes = PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes()
                    self.process_nodes.parent = self
                    self._children_name_map["process_nodes"] = "process-nodes"
                    self._segment_path = lambda: "process"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Process, [], name, value)


                class ProcessNodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: process_node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes, self).__init__()

                        self.yang_name = "process-nodes"
                        self.yang_parent_name = "process"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("process-node", ("process_node", PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode))])
                        self._leafs = OrderedDict()

                        self.process_node = YList(self)
                        self._segment_path = lambda: "process-nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/process/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes, [], name, value)


                    class ProcessNode(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: pids
                        
                        	Process ID specification
                        	**type**\:  :py:class:`Pids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode, self).__init__()

                            self.yang_name = "process-node"
                            self.yang_parent_name = "process-nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([("pids", ("pids", PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids))])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                            ])
                            self.node_id = None

                            self.pids = PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids()
                            self.pids.parent = self
                            self._children_name_map["pids"] = "pids"
                            self._segment_path = lambda: "process-node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/process/process-nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode, ['node_id'], name, value)


                        class Pids(Entity):
                            """
                            Process ID specification
                            
                            .. attribute:: pid
                            
                            	Specify an existing template for data collection
                            	**type**\: list of  		 :py:class:`Pid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids, self).__init__()

                                self.yang_name = "pids"
                                self.yang_parent_name = "process-node"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("pid", ("pid", PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid))])
                                self._leafs = OrderedDict()

                                self.pid = YList(self)
                                self._segment_path = lambda: "pids"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids, [], name, value)


                            class Pid(Entity):
                                """
                                Specify an existing template for data
                                collection
                                
                                .. attribute:: pid  (key)
                                
                                	Specify Process ID
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: template_name
                                
                                	Template name
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'manageability-perfmgmt-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid, self).__init__()

                                    self.yang_name = "pid"
                                    self.yang_parent_name = "pids"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['pid']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('pid', (YLeaf(YType.uint32, 'pid'), ['int'])),
                                        ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                                    ])
                                    self.pid = None
                                    self.template_name = None
                                    self._segment_path = lambda: "pid" + "[pid='" + str(self.pid) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid, ['pid', 'template_name'], name, value)


            class BasicCounters(Entity):
                """
                Monitoring for basic\-counters
                
                .. attribute:: interfaces
                
                	Monitor an Interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.BasicCounters, self).__init__()

                    self.yang_name = "basic-counters"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces))])
                    self._leafs = OrderedDict()

                    self.interfaces = PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "basic-counters"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.BasicCounters, [], name, value)


                class Interfaces(Entity):
                    """
                    Monitor an Interface
                    
                    .. attribute:: interface
                    
                    	Interface being Monitored
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "basic-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/basic-counters/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        Interface being Monitored
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self.template_name = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/basic-counters/interfaces/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface, ['interface_name', 'template_name'], name, value)


            class Memory(Entity):
                """
                Collection for memory
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Memory.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.Memory, self).__init__()

                    self.yang_name = "memory"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nodes", ("nodes", PerfMgmt.Enable.MonitorEnable.Memory.Nodes))])
                    self._leafs = OrderedDict()

                    self.nodes = PerfMgmt.Enable.MonitorEnable.Memory.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "memory"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Memory, [], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.Memory.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "memory"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/memory/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Memory.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/memory/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node, ['node_id', 'template_name'], name, value)


            class Ospfv2Protocol(Entity):
                """
                Monitor OSPF v2 Protocol
                
                .. attribute:: ospf_instances
                
                	Monitor an instance
                	**type**\:  :py:class:`OspfInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol, self).__init__()

                    self.yang_name = "ospfv2-protocol"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospf-instances", ("ospf_instances", PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances))])
                    self._leafs = OrderedDict()

                    self.ospf_instances = PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances()
                    self.ospf_instances.parent = self
                    self._children_name_map["ospf_instances"] = "ospf-instances"
                    self._segment_path = lambda: "ospfv2-protocol"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol, [], name, value)


                class OspfInstances(Entity):
                    """
                    Monitor an instance
                    
                    .. attribute:: ospf_instance
                    
                    	Instance being monitored
                    	**type**\: list of  		 :py:class:`OspfInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances, self).__init__()

                        self.yang_name = "ospf-instances"
                        self.yang_parent_name = "ospfv2-protocol"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ospf-instance", ("ospf_instance", PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance))])
                        self._leafs = OrderedDict()

                        self.ospf_instance = YList(self)
                        self._segment_path = lambda: "ospf-instances"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/ospfv2-protocol/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances, [], name, value)


                    class OspfInstance(Entity):
                        """
                        Instance being monitored
                        
                        .. attribute:: instance_name  (key)
                        
                        	OSPF Instance Name
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance, self).__init__()

                            self.yang_name = "ospf-instance"
                            self.yang_parent_name = "ospf-instances"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['instance_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('instance_name', (YLeaf(YType.str, 'instance-name'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.instance_name = None
                            self.template_name = None
                            self._segment_path = lambda: "ospf-instance" + "[instance-name='" + str(self.instance_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/ospfv2-protocol/ospf-instances/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance, ['instance_name', 'template_name'], name, value)


            class Cpu(Entity):
                """
                Collection for CPU
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Cpu.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.Cpu, self).__init__()

                    self.yang_name = "cpu"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nodes", ("nodes", PerfMgmt.Enable.MonitorEnable.Cpu.Nodes))])
                    self._leafs = OrderedDict()

                    self.nodes = PerfMgmt.Enable.MonitorEnable.Cpu.Nodes()
                    self.nodes.parent = self
                    self._children_name_map["nodes"] = "nodes"
                    self._segment_path = lambda: "cpu"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Cpu, [], name, value)


                class Nodes(Entity):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.Cpu.Nodes, self).__init__()

                        self.yang_name = "nodes"
                        self.yang_parent_name = "cpu"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("node", ("node", PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node))])
                        self._leafs = OrderedDict()

                        self.node = YList(self)
                        self._segment_path = lambda: "nodes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/cpu/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Cpu.Nodes, [], name, value)


                    class Node(Entity):
                        """
                        Node instance
                        
                        .. attribute:: node_id  (key)
                        
                        	Node ID
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node, self).__init__()

                            self.yang_name = "node"
                            self.yang_parent_name = "nodes"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['node_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('node_id', (YLeaf(YType.str, 'node-id'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.node_id = None
                            self.template_name = None
                            self._segment_path = lambda: "node" + "[node-id='" + str(self.node_id) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/cpu/nodes/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node, ['node_id', 'template_name'], name, value)


            class Bgp(Entity):
                """
                Monitor BGP protocol
                
                .. attribute:: neighbors
                
                	Monitor BGP protocol for a BGP peer
                	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.Bgp, self).__init__()

                    self.yang_name = "bgp"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("neighbors", ("neighbors", PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors))])
                    self._leafs = OrderedDict()

                    self.neighbors = PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors()
                    self.neighbors.parent = self
                    self._children_name_map["neighbors"] = "neighbors"
                    self._segment_path = lambda: "bgp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Bgp, [], name, value)


                class Neighbors(Entity):
                    """
                    Monitor BGP protocol for a BGP peer
                    
                    .. attribute:: neighbor
                    
                    	Neighbor being monitored
                    	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors, self).__init__()

                        self.yang_name = "neighbors"
                        self.yang_parent_name = "bgp"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("neighbor", ("neighbor", PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor))])
                        self._leafs = OrderedDict()

                        self.neighbor = YList(self)
                        self._segment_path = lambda: "neighbors"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/bgp/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors, [], name, value)


                    class Neighbor(Entity):
                        """
                        Neighbor being monitored
                        
                        .. attribute:: peer_address  (key)
                        
                        	IP address of the Neighbor
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor, self).__init__()

                            self.yang_name = "neighbor"
                            self.yang_parent_name = "neighbors"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['peer_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('peer_address', (YLeaf(YType.str, 'peer-address'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.peer_address = None
                            self.template_name = None
                            self._segment_path = lambda: "neighbor" + "[peer-address='" + str(self.peer_address) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/bgp/neighbors/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor, ['peer_address', 'template_name'], name, value)


            class DataRates(Entity):
                """
                Monitoring for data\-rates
                
                .. attribute:: interfaces
                
                	Monitor an Interface
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Enable.MonitorEnable.DataRates, self).__init__()

                    self.yang_name = "data-rates"
                    self.yang_parent_name = "monitor-enable"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interfaces", ("interfaces", PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces))])
                    self._leafs = OrderedDict()

                    self.interfaces = PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "data-rates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Enable.MonitorEnable.DataRates, [], name, value)


                class Interfaces(Entity):
                    """
                    Monitor an Interface
                    
                    .. attribute:: interface
                    
                    	Interface being Monitored
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "data-rates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/data-rates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        Interface being Monitored
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface Name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ])
                            self.interface_name = None
                            self.template_name = None
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/enable/monitor-enable/data-rates/interfaces/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface, ['interface_name', 'template_name'], name, value)


    class RegExpGroups(Entity):
        """
        Configure regular expression group
        
        .. attribute:: reg_exp_group
        
        	Specify regular expression group name
        	**type**\: list of  		 :py:class:`RegExpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups.RegExpGroup>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.RegExpGroups, self).__init__()

            self.yang_name = "reg-exp-groups"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("reg-exp-group", ("reg_exp_group", PerfMgmt.RegExpGroups.RegExpGroup))])
            self._leafs = OrderedDict()

            self.reg_exp_group = YList(self)
            self._segment_path = lambda: "reg-exp-groups"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.RegExpGroups, [], name, value)


        class RegExpGroup(Entity):
            """
            Specify regular expression group name
            
            .. attribute:: reg_exp_group_name  (key)
            
            	Regular expression group name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: reg_exps
            
            	Configure regular expression
            	**type**\:  :py:class:`RegExps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups.RegExpGroup.RegExps>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.RegExpGroups.RegExpGroup, self).__init__()

                self.yang_name = "reg-exp-group"
                self.yang_parent_name = "reg-exp-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['reg_exp_group_name']
                self._child_classes = OrderedDict([("reg-exps", ("reg_exps", PerfMgmt.RegExpGroups.RegExpGroup.RegExps))])
                self._leafs = OrderedDict([
                    ('reg_exp_group_name', (YLeaf(YType.str, 'reg-exp-group-name'), ['str'])),
                ])
                self.reg_exp_group_name = None

                self.reg_exps = PerfMgmt.RegExpGroups.RegExpGroup.RegExps()
                self.reg_exps.parent = self
                self._children_name_map["reg_exps"] = "reg-exps"
                self._segment_path = lambda: "reg-exp-group" + "[reg-exp-group-name='" + str(self.reg_exp_group_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/reg-exp-groups/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.RegExpGroups.RegExpGroup, ['reg_exp_group_name'], name, value)


            class RegExps(Entity):
                """
                Configure regular expression
                
                .. attribute:: reg_exp
                
                	Specify regular expression index number
                	**type**\: list of  		 :py:class:`RegExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.RegExpGroups.RegExpGroup.RegExps, self).__init__()

                    self.yang_name = "reg-exps"
                    self.yang_parent_name = "reg-exp-group"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("reg-exp", ("reg_exp", PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp))])
                    self._leafs = OrderedDict()

                    self.reg_exp = YList(self)
                    self._segment_path = lambda: "reg-exps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.RegExpGroups.RegExpGroup.RegExps, [], name, value)


                class RegExp(Entity):
                    """
                    Specify regular expression index number
                    
                    .. attribute:: reg_exp_index  (key)
                    
                    	Regular expression index number
                    	**type**\: int
                    
                    	**range:** 1..100
                    
                    .. attribute:: reg_exp_string
                    
                    	Regular expression string to match
                    	**type**\: str
                    
                    	**length:** 1..128
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp, self).__init__()

                        self.yang_name = "reg-exp"
                        self.yang_parent_name = "reg-exps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['reg_exp_index']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('reg_exp_index', (YLeaf(YType.uint32, 'reg-exp-index'), ['int'])),
                            ('reg_exp_string', (YLeaf(YType.str, 'reg-exp-string'), ['str'])),
                        ])
                        self.reg_exp_index = None
                        self.reg_exp_string = None
                        self._segment_path = lambda: "reg-exp" + "[reg-exp-index='" + str(self.reg_exp_index) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp, ['reg_exp_index', 'reg_exp_string'], name, value)


    class Threshold(Entity):
        """
        Container for threshold templates
        
        .. attribute:: generic_counter_interface
        
        	Interface Generic Counter threshold configuration
        	**type**\:  :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface>`
        
        .. attribute:: ldp_mpls
        
        	MPLS LDP threshold configuration
        	**type**\:  :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls>`
        
        .. attribute:: basic_counter_interface
        
        	Interface Basic Counter threshold configuration
        	**type**\:  :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface>`
        
        .. attribute:: bgp
        
        	BGP threshold configuration
        	**type**\:  :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp>`
        
        .. attribute:: ospfv2_protocol
        
        	OSPF v2 Protocol threshold configuration
        	**type**\:  :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol>`
        
        .. attribute:: cpu_node
        
        	Node CPU threshold configuration
        	**type**\:  :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode>`
        
        .. attribute:: data_rate_interface
        
        	Interface Data Rates threshold configuration
        	**type**\:  :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface>`
        
        .. attribute:: process_node
        
        	Node Process threshold configuration
        	**type**\:  :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode>`
        
        .. attribute:: memory_node
        
        	Node Memory threshold configuration
        	**type**\:  :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode>`
        
        .. attribute:: ospfv3_protocol
        
        	OSPF v2 Protocol threshold configuration
        	**type**\:  :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(PerfMgmt.Threshold, self).__init__()

            self.yang_name = "threshold"
            self.yang_parent_name = "perf-mgmt"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("generic-counter-interface", ("generic_counter_interface", PerfMgmt.Threshold.GenericCounterInterface)), ("ldp-mpls", ("ldp_mpls", PerfMgmt.Threshold.LdpMpls)), ("basic-counter-interface", ("basic_counter_interface", PerfMgmt.Threshold.BasicCounterInterface)), ("bgp", ("bgp", PerfMgmt.Threshold.Bgp)), ("ospfv2-protocol", ("ospfv2_protocol", PerfMgmt.Threshold.Ospfv2Protocol)), ("cpu-node", ("cpu_node", PerfMgmt.Threshold.CpuNode)), ("data-rate-interface", ("data_rate_interface", PerfMgmt.Threshold.DataRateInterface)), ("process-node", ("process_node", PerfMgmt.Threshold.ProcessNode)), ("memory-node", ("memory_node", PerfMgmt.Threshold.MemoryNode)), ("ospfv3-protocol", ("ospfv3_protocol", PerfMgmt.Threshold.Ospfv3Protocol))])
            self._leafs = OrderedDict()

            self.generic_counter_interface = PerfMgmt.Threshold.GenericCounterInterface()
            self.generic_counter_interface.parent = self
            self._children_name_map["generic_counter_interface"] = "generic-counter-interface"

            self.ldp_mpls = PerfMgmt.Threshold.LdpMpls()
            self.ldp_mpls.parent = self
            self._children_name_map["ldp_mpls"] = "ldp-mpls"

            self.basic_counter_interface = PerfMgmt.Threshold.BasicCounterInterface()
            self.basic_counter_interface.parent = self
            self._children_name_map["basic_counter_interface"] = "basic-counter-interface"

            self.bgp = PerfMgmt.Threshold.Bgp()
            self.bgp.parent = self
            self._children_name_map["bgp"] = "bgp"

            self.ospfv2_protocol = PerfMgmt.Threshold.Ospfv2Protocol()
            self.ospfv2_protocol.parent = self
            self._children_name_map["ospfv2_protocol"] = "ospfv2-protocol"

            self.cpu_node = PerfMgmt.Threshold.CpuNode()
            self.cpu_node.parent = self
            self._children_name_map["cpu_node"] = "cpu-node"

            self.data_rate_interface = PerfMgmt.Threshold.DataRateInterface()
            self.data_rate_interface.parent = self
            self._children_name_map["data_rate_interface"] = "data-rate-interface"

            self.process_node = PerfMgmt.Threshold.ProcessNode()
            self.process_node.parent = self
            self._children_name_map["process_node"] = "process-node"

            self.memory_node = PerfMgmt.Threshold.MemoryNode()
            self.memory_node.parent = self
            self._children_name_map["memory_node"] = "memory-node"

            self.ospfv3_protocol = PerfMgmt.Threshold.Ospfv3Protocol()
            self.ospfv3_protocol.parent = self
            self._children_name_map["ospfv3_protocol"] = "ospfv3-protocol"
            self._segment_path = lambda: "threshold"
            self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerfMgmt.Threshold, [], name, value)


        class GenericCounterInterface(Entity):
            """
            Interface Generic Counter threshold
            configuration
            
            .. attribute:: generic_counter_interface_templates
            
            	Interface Generic Counter threshold templates
            	**type**\:  :py:class:`GenericCounterInterfaceTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.GenericCounterInterface, self).__init__()

                self.yang_name = "generic-counter-interface"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("generic-counter-interface-templates", ("generic_counter_interface_templates", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates))])
                self._leafs = OrderedDict()

                self.generic_counter_interface_templates = PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates()
                self.generic_counter_interface_templates.parent = self
                self._children_name_map["generic_counter_interface_templates"] = "generic-counter-interface-templates"
                self._segment_path = lambda: "generic-counter-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface, [], name, value)


            class GenericCounterInterfaceTemplates(Entity):
                """
                Interface Generic Counter threshold templates
                
                .. attribute:: generic_counter_interface_template
                
                	Interface Generic Counter threshold template instance
                	**type**\: list of  		 :py:class:`GenericCounterInterfaceTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates, self).__init__()

                    self.yang_name = "generic-counter-interface-templates"
                    self.yang_parent_name = "generic-counter-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("generic-counter-interface-template", ("generic_counter_interface_template", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate))])
                    self._leafs = OrderedDict()

                    self.generic_counter_interface_template = YList(self)
                    self._segment_path = lambda: "generic-counter-interface-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/generic-counter-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates, [], name, value)


                class GenericCounterInterfaceTemplate(Entity):
                    """
                    Interface Generic Counter threshold template
                    instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: in_octets
                    
                    	Number of inbound octets/bytes
                    	**type**\:  :py:class:`InOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_ucast_pkts
                    
                    	Number of inbound unicast packets
                    	**type**\:  :py:class:`InUcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_ucast_pkts
                    
                    	Number of outbound unicast packets
                    	**type**\:  :py:class:`OutUcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_broadcast_pkts
                    
                    	Number of outbound broadcast packets
                    	**type**\:  :py:class:`OutBroadcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_multicast_pkts
                    
                    	Number of outbound multicast packets
                    	**type**\:  :py:class:`OutMulticastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_overrun
                    
                    	Number of inbound packets with overrun errors
                    	**type**\:  :py:class:`InputOverrun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_octets
                    
                    	Number of outbound octets/bytes
                    	**type**\:  :py:class:`OutOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_underrun
                    
                    	Number of outbound packets with underrun errors
                    	**type**\:  :py:class:`OutputUnderrun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_errors
                    
                    	Number of inbound incorrect packets discarded
                    	**type**\:  :py:class:`InputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_drops
                    
                    	Number of outbound correct packets discarded
                    	**type**\:  :py:class:`OutputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_crc
                    
                    	Number of inbound packets discarded with incorrect CRC
                    	**type**\:  :py:class:`InputCrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_broadcast_pkts
                    
                    	Number of inbound broadcast packets
                    	**type**\:  :py:class:`InBroadcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_multicast_pkts
                    
                    	Number of inbound multicast packets
                    	**type**\:  :py:class:`InMulticastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_packets
                    
                    	Number of outbound packets
                    	**type**\:  :py:class:`OutPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_errors
                    
                    	Number of outbound incorrect packets discarded
                    	**type**\:  :py:class:`OutputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_packets
                    
                    	Number of inbound packets
                    	**type**\:  :py:class:`InPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_unknown_proto
                    
                    	Number of inbound packets discarded with unknown protocol
                    	**type**\:  :py:class:`InputUnknownProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_queue_drops
                    
                    	Number of input queue drops
                    	**type**\:  :py:class:`InputQueueDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_drops
                    
                    	Number of inbound correct packets discarded
                    	**type**\:  :py:class:`InputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_frame
                    
                    	Number of inbound packets with framing errors
                    	**type**\:  :py:class:`InputFrame <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: vrf_group
                    
                    	Enable instance filtering by VRF name regular expression 
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate, self).__init__()

                        self.yang_name = "generic-counter-interface-template"
                        self.yang_parent_name = "generic-counter-interface-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("in-octets", ("in_octets", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets)), ("in-ucast-pkts", ("in_ucast_pkts", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts)), ("out-ucast-pkts", ("out_ucast_pkts", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts)), ("out-broadcast-pkts", ("out_broadcast_pkts", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts)), ("out-multicast-pkts", ("out_multicast_pkts", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts)), ("input-overrun", ("input_overrun", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun)), ("out-octets", ("out_octets", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets)), ("output-underrun", ("output_underrun", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun)), ("input-total-errors", ("input_total_errors", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors)), ("output-total-drops", ("output_total_drops", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops)), ("input-crc", ("input_crc", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc)), ("in-broadcast-pkts", ("in_broadcast_pkts", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts)), ("in-multicast-pkts", ("in_multicast_pkts", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts)), ("out-packets", ("out_packets", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets)), ("output-total-errors", ("output_total_errors", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors)), ("in-packets", ("in_packets", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets)), ("input-unknown-proto", ("input_unknown_proto", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto)), ("input-queue-drops", ("input_queue_drops", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops)), ("input-total-drops", ("input_total_drops", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops)), ("input-frame", ("input_frame", PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None
                        self.reg_exp_group = None
                        self.vrf_group = None

                        self.in_octets = None
                        self._children_name_map["in_octets"] = "in-octets"

                        self.in_ucast_pkts = None
                        self._children_name_map["in_ucast_pkts"] = "in-ucast-pkts"

                        self.out_ucast_pkts = None
                        self._children_name_map["out_ucast_pkts"] = "out-ucast-pkts"

                        self.out_broadcast_pkts = None
                        self._children_name_map["out_broadcast_pkts"] = "out-broadcast-pkts"

                        self.out_multicast_pkts = None
                        self._children_name_map["out_multicast_pkts"] = "out-multicast-pkts"

                        self.input_overrun = None
                        self._children_name_map["input_overrun"] = "input-overrun"

                        self.out_octets = None
                        self._children_name_map["out_octets"] = "out-octets"

                        self.output_underrun = None
                        self._children_name_map["output_underrun"] = "output-underrun"

                        self.input_total_errors = None
                        self._children_name_map["input_total_errors"] = "input-total-errors"

                        self.output_total_drops = None
                        self._children_name_map["output_total_drops"] = "output-total-drops"

                        self.input_crc = None
                        self._children_name_map["input_crc"] = "input-crc"

                        self.in_broadcast_pkts = None
                        self._children_name_map["in_broadcast_pkts"] = "in-broadcast-pkts"

                        self.in_multicast_pkts = None
                        self._children_name_map["in_multicast_pkts"] = "in-multicast-pkts"

                        self.out_packets = None
                        self._children_name_map["out_packets"] = "out-packets"

                        self.output_total_errors = None
                        self._children_name_map["output_total_errors"] = "output-total-errors"

                        self.in_packets = None
                        self._children_name_map["in_packets"] = "in-packets"

                        self.input_unknown_proto = None
                        self._children_name_map["input_unknown_proto"] = "input-unknown-proto"

                        self.input_queue_drops = None
                        self._children_name_map["input_queue_drops"] = "input-queue-drops"

                        self.input_total_drops = None
                        self._children_name_map["input_total_drops"] = "input-total-drops"

                        self.input_frame = None
                        self._children_name_map["input_frame"] = "input-frame"
                        self._segment_path = lambda: "generic-counter-interface-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/generic-counter-interface/generic-counter-interface-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate, ['template_name', 'sample_interval', 'reg_exp_group', 'vrf_group'], name, value)


                    class InOctets(Entity):
                        """
                        Number of inbound octets/bytes
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets, self).__init__()

                            self.yang_name = "in-octets"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-octets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InUcastPkts(Entity):
                        """
                        Number of inbound unicast packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts, self).__init__()

                            self.yang_name = "in-ucast-pkts"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-ucast-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutUcastPkts(Entity):
                        """
                        Number of outbound unicast packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts, self).__init__()

                            self.yang_name = "out-ucast-pkts"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-ucast-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutBroadcastPkts(Entity):
                        """
                        Number of outbound broadcast packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts, self).__init__()

                            self.yang_name = "out-broadcast-pkts"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-broadcast-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutMulticastPkts(Entity):
                        """
                        Number of outbound multicast packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts, self).__init__()

                            self.yang_name = "out-multicast-pkts"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-multicast-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputOverrun(Entity):
                        """
                        Number of inbound packets with overrun
                        errors
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun, self).__init__()

                            self.yang_name = "input-overrun"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-overrun"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutOctets(Entity):
                        """
                        Number of outbound octets/bytes
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets, self).__init__()

                            self.yang_name = "out-octets"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-octets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputUnderrun(Entity):
                        """
                        Number of outbound packets with underrun
                        errors
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun, self).__init__()

                            self.yang_name = "output-underrun"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-underrun"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputTotalErrors(Entity):
                        """
                        Number of inbound incorrect packets
                        discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors, self).__init__()

                            self.yang_name = "input-total-errors"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-total-errors"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputTotalDrops(Entity):
                        """
                        Number of outbound correct packets discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops, self).__init__()

                            self.yang_name = "output-total-drops"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-total-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputCrc(Entity):
                        """
                        Number of inbound packets discarded with
                        incorrect CRC
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc, self).__init__()

                            self.yang_name = "input-crc"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-crc"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InBroadcastPkts(Entity):
                        """
                        Number of inbound broadcast packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts, self).__init__()

                            self.yang_name = "in-broadcast-pkts"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-broadcast-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InMulticastPkts(Entity):
                        """
                        Number of inbound multicast packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts, self).__init__()

                            self.yang_name = "in-multicast-pkts"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-multicast-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutPackets(Entity):
                        """
                        Number of outbound packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets, self).__init__()

                            self.yang_name = "out-packets"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputTotalErrors(Entity):
                        """
                        Number of outbound incorrect packets
                        discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors, self).__init__()

                            self.yang_name = "output-total-errors"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-total-errors"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InPackets(Entity):
                        """
                        Number of inbound packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets, self).__init__()

                            self.yang_name = "in-packets"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputUnknownProto(Entity):
                        """
                        Number of inbound packets discarded with
                        unknown protocol
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto, self).__init__()

                            self.yang_name = "input-unknown-proto"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-unknown-proto"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputQueueDrops(Entity):
                        """
                        Number of input queue drops
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops, self).__init__()

                            self.yang_name = "input-queue-drops"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-queue-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputTotalDrops(Entity):
                        """
                        Number of inbound correct packets discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops, self).__init__()

                            self.yang_name = "input-total-drops"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-total-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputFrame(Entity):
                        """
                        Number of inbound packets with framing
                        errors
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame, self).__init__()

                            self.yang_name = "input-frame"
                            self.yang_parent_name = "generic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-frame"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class LdpMpls(Entity):
            """
            MPLS LDP threshold configuration
            
            .. attribute:: ldp_mpls_templates
            
            	MPLS LDP threshold templates
            	**type**\:  :py:class:`LdpMplsTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.LdpMpls, self).__init__()

                self.yang_name = "ldp-mpls"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ldp-mpls-templates", ("ldp_mpls_templates", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates))])
                self._leafs = OrderedDict()

                self.ldp_mpls_templates = PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates()
                self.ldp_mpls_templates.parent = self
                self._children_name_map["ldp_mpls_templates"] = "ldp-mpls-templates"
                self._segment_path = lambda: "ldp-mpls"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.LdpMpls, [], name, value)


            class LdpMplsTemplates(Entity):
                """
                MPLS LDP threshold templates
                
                .. attribute:: ldp_mpls_template
                
                	MPLS LDP threshold template instance
                	**type**\: list of  		 :py:class:`LdpMplsTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates, self).__init__()

                    self.yang_name = "ldp-mpls-templates"
                    self.yang_parent_name = "ldp-mpls"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ldp-mpls-template", ("ldp_mpls_template", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate))])
                    self._leafs = OrderedDict()

                    self.ldp_mpls_template = YList(self)
                    self._segment_path = lambda: "ldp-mpls-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/ldp-mpls/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates, [], name, value)


                class LdpMplsTemplate(Entity):
                    """
                    MPLS LDP threshold template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: address_withdraw_msgs_rcvd
                    
                    	Number of Address Withdraw messages received
                    	**type**\:  :py:class:`AddressWithdrawMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_withdraw_msgs_rcvd
                    
                    	Number of Label Withdraw messages received
                    	**type**\:  :py:class:`LabelWithdrawMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: address_withdraw_msgs_sent
                    
                    	Number of Address Withdraw messages sent
                    	**type**\:  :py:class:`AddressWithdrawMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_withdraw_msgs_sent
                    
                    	Number of Label Withdraw messages sent
                    	**type**\:  :py:class:`LabelWithdrawMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: notification_msgs_rcvd
                    
                    	Number of Notification messages received
                    	**type**\:  :py:class:`NotificationMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: total_msgs_rcvd
                    
                    	Total number of messages received
                    	**type**\:  :py:class:`TotalMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: notification_msgs_sent
                    
                    	Number of Notification messages sent
                    	**type**\:  :py:class:`NotificationMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: total_msgs_sent
                    
                    	Total number of messages sent
                    	**type**\:  :py:class:`TotalMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_release_msgs_rcvd
                    
                    	Number of LAbel Release messages received
                    	**type**\:  :py:class:`LabelReleaseMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: init_msgs_rcvd
                    
                    	Number of Init messages received
                    	**type**\:  :py:class:`InitMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_release_msgs_sent
                    
                    	Number of Label Release messages sent
                    	**type**\:  :py:class:`LabelReleaseMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: init_msgs_sent
                    
                    	Number of Init messages sent
                    	**type**\:  :py:class:`InitMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_mapping_msgs_rcvd
                    
                    	Number of Label Mapping messages received
                    	**type**\:  :py:class:`LabelMappingMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: keepalive_msgs_rcvd
                    
                    	Number of Keepalive messages received
                    	**type**\:  :py:class:`KeepaliveMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_mapping_msgs_sent
                    
                    	Number of Label Mapping messages sent
                    	**type**\:  :py:class:`LabelMappingMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: keepalive_msgs_sent
                    
                    	Number of Keepalive messages sent
                    	**type**\:  :py:class:`KeepaliveMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: address_msgs_rcvd
                    
                    	Number of Address messages received
                    	**type**\:  :py:class:`AddressMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: address_msgs_sent
                    
                    	Number of Address messages sent
                    	**type**\:  :py:class:`AddressMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate, self).__init__()

                        self.yang_name = "ldp-mpls-template"
                        self.yang_parent_name = "ldp-mpls-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("address-withdraw-msgs-rcvd", ("address_withdraw_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd)), ("label-withdraw-msgs-rcvd", ("label_withdraw_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd)), ("address-withdraw-msgs-sent", ("address_withdraw_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent)), ("label-withdraw-msgs-sent", ("label_withdraw_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent)), ("notification-msgs-rcvd", ("notification_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd)), ("total-msgs-rcvd", ("total_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd)), ("notification-msgs-sent", ("notification_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent)), ("total-msgs-sent", ("total_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent)), ("label-release-msgs-rcvd", ("label_release_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd)), ("init-msgs-rcvd", ("init_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd)), ("label-release-msgs-sent", ("label_release_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent)), ("init-msgs-sent", ("init_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent)), ("label-mapping-msgs-rcvd", ("label_mapping_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd)), ("keepalive-msgs-rcvd", ("keepalive_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd)), ("label-mapping-msgs-sent", ("label_mapping_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent)), ("keepalive-msgs-sent", ("keepalive_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent)), ("address-msgs-rcvd", ("address_msgs_rcvd", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd)), ("address-msgs-sent", ("address_msgs_sent", PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.address_withdraw_msgs_rcvd = None
                        self._children_name_map["address_withdraw_msgs_rcvd"] = "address-withdraw-msgs-rcvd"

                        self.label_withdraw_msgs_rcvd = None
                        self._children_name_map["label_withdraw_msgs_rcvd"] = "label-withdraw-msgs-rcvd"

                        self.address_withdraw_msgs_sent = None
                        self._children_name_map["address_withdraw_msgs_sent"] = "address-withdraw-msgs-sent"

                        self.label_withdraw_msgs_sent = None
                        self._children_name_map["label_withdraw_msgs_sent"] = "label-withdraw-msgs-sent"

                        self.notification_msgs_rcvd = None
                        self._children_name_map["notification_msgs_rcvd"] = "notification-msgs-rcvd"

                        self.total_msgs_rcvd = None
                        self._children_name_map["total_msgs_rcvd"] = "total-msgs-rcvd"

                        self.notification_msgs_sent = None
                        self._children_name_map["notification_msgs_sent"] = "notification-msgs-sent"

                        self.total_msgs_sent = None
                        self._children_name_map["total_msgs_sent"] = "total-msgs-sent"

                        self.label_release_msgs_rcvd = None
                        self._children_name_map["label_release_msgs_rcvd"] = "label-release-msgs-rcvd"

                        self.init_msgs_rcvd = None
                        self._children_name_map["init_msgs_rcvd"] = "init-msgs-rcvd"

                        self.label_release_msgs_sent = None
                        self._children_name_map["label_release_msgs_sent"] = "label-release-msgs-sent"

                        self.init_msgs_sent = None
                        self._children_name_map["init_msgs_sent"] = "init-msgs-sent"

                        self.label_mapping_msgs_rcvd = None
                        self._children_name_map["label_mapping_msgs_rcvd"] = "label-mapping-msgs-rcvd"

                        self.keepalive_msgs_rcvd = None
                        self._children_name_map["keepalive_msgs_rcvd"] = "keepalive-msgs-rcvd"

                        self.label_mapping_msgs_sent = None
                        self._children_name_map["label_mapping_msgs_sent"] = "label-mapping-msgs-sent"

                        self.keepalive_msgs_sent = None
                        self._children_name_map["keepalive_msgs_sent"] = "keepalive-msgs-sent"

                        self.address_msgs_rcvd = None
                        self._children_name_map["address_msgs_rcvd"] = "address-msgs-rcvd"

                        self.address_msgs_sent = None
                        self._children_name_map["address_msgs_sent"] = "address-msgs-sent"
                        self._segment_path = lambda: "ldp-mpls-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/ldp-mpls/ldp-mpls-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate, ['template_name', 'sample_interval'], name, value)


                    class AddressWithdrawMsgsRcvd(Entity):
                        """
                        Number of Address Withdraw messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd, self).__init__()

                            self.yang_name = "address-withdraw-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "address-withdraw-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class LabelWithdrawMsgsRcvd(Entity):
                        """
                        Number of Label Withdraw messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd, self).__init__()

                            self.yang_name = "label-withdraw-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "label-withdraw-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class AddressWithdrawMsgsSent(Entity):
                        """
                        Number of Address Withdraw messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent, self).__init__()

                            self.yang_name = "address-withdraw-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "address-withdraw-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class LabelWithdrawMsgsSent(Entity):
                        """
                        Number of Label Withdraw messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent, self).__init__()

                            self.yang_name = "label-withdraw-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "label-withdraw-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class NotificationMsgsRcvd(Entity):
                        """
                        Number of Notification messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd, self).__init__()

                            self.yang_name = "notification-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "notification-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class TotalMsgsRcvd(Entity):
                        """
                        Total number of messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..65536
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..65536
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd, self).__init__()

                            self.yang_name = "total-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "total-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class NotificationMsgsSent(Entity):
                        """
                        Number of Notification messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent, self).__init__()

                            self.yang_name = "notification-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "notification-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class TotalMsgsSent(Entity):
                        """
                        Total number of messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent, self).__init__()

                            self.yang_name = "total-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "total-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class LabelReleaseMsgsRcvd(Entity):
                        """
                        Number of LAbel Release messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd, self).__init__()

                            self.yang_name = "label-release-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "label-release-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InitMsgsRcvd(Entity):
                        """
                        Number of Init messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd, self).__init__()

                            self.yang_name = "init-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "init-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class LabelReleaseMsgsSent(Entity):
                        """
                        Number of Label Release messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent, self).__init__()

                            self.yang_name = "label-release-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "label-release-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InitMsgsSent(Entity):
                        """
                        Number of Init messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent, self).__init__()

                            self.yang_name = "init-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "init-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class LabelMappingMsgsRcvd(Entity):
                        """
                        Number of Label Mapping messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd, self).__init__()

                            self.yang_name = "label-mapping-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "label-mapping-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class KeepaliveMsgsRcvd(Entity):
                        """
                        Number of Keepalive messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd, self).__init__()

                            self.yang_name = "keepalive-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "keepalive-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class LabelMappingMsgsSent(Entity):
                        """
                        Number of Label Mapping messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent, self).__init__()

                            self.yang_name = "label-mapping-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "label-mapping-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class KeepaliveMsgsSent(Entity):
                        """
                        Number of Keepalive messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent, self).__init__()

                            self.yang_name = "keepalive-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "keepalive-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class AddressMsgsRcvd(Entity):
                        """
                        Number of Address messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd, self).__init__()

                            self.yang_name = "address-msgs-rcvd"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "address-msgs-rcvd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class AddressMsgsSent(Entity):
                        """
                        Number of Address messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent, self).__init__()

                            self.yang_name = "address-msgs-sent"
                            self.yang_parent_name = "ldp-mpls-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "address-msgs-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class BasicCounterInterface(Entity):
            """
            Interface Basic Counter threshold configuration
            
            .. attribute:: basic_counter_interface_templates
            
            	Interface Basic Counter threshold templates
            	**type**\:  :py:class:`BasicCounterInterfaceTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.BasicCounterInterface, self).__init__()

                self.yang_name = "basic-counter-interface"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("basic-counter-interface-templates", ("basic_counter_interface_templates", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates))])
                self._leafs = OrderedDict()

                self.basic_counter_interface_templates = PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates()
                self.basic_counter_interface_templates.parent = self
                self._children_name_map["basic_counter_interface_templates"] = "basic-counter-interface-templates"
                self._segment_path = lambda: "basic-counter-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface, [], name, value)


            class BasicCounterInterfaceTemplates(Entity):
                """
                Interface Basic Counter threshold templates
                
                .. attribute:: basic_counter_interface_template
                
                	Interface Basic Counter threshold template instance
                	**type**\: list of  		 :py:class:`BasicCounterInterfaceTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates, self).__init__()

                    self.yang_name = "basic-counter-interface-templates"
                    self.yang_parent_name = "basic-counter-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("basic-counter-interface-template", ("basic_counter_interface_template", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate))])
                    self._leafs = OrderedDict()

                    self.basic_counter_interface_template = YList(self)
                    self._segment_path = lambda: "basic-counter-interface-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/basic-counter-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates, [], name, value)


                class BasicCounterInterfaceTemplate(Entity):
                    """
                    Interface Basic Counter threshold template
                    instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: in_octets
                    
                    	Number of inbound octets/bytes
                    	**type**\:  :py:class:`InOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_octets
                    
                    	Number of outbound octets/bytes
                    	**type**\:  :py:class:`OutOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_queue_drops
                    
                    	Number of outbound queue drops
                    	**type**\:  :py:class:`OutputQueueDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_errors
                    
                    	Number of inbound incorrect packets discarded
                    	**type**\:  :py:class:`InputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_drops
                    
                    	Number of outbound correct packets discarded
                    	**type**\:  :py:class:`OutputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_packets
                    
                    	Number of outbound packets
                    	**type**\:  :py:class:`OutPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_errors
                    
                    	Number of outbound incorrect packets discarded
                    	**type**\:  :py:class:`OutputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_packets
                    
                    	Number of inbound packets
                    	**type**\:  :py:class:`InPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_queue_drops
                    
                    	Number of input queue drops
                    	**type**\:  :py:class:`InputQueueDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_drops
                    
                    	Number of inbound correct packets discarded
                    	**type**\:  :py:class:`InputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: vrf_group
                    
                    	Enable instance filtering by VRF name regular expression 
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate, self).__init__()

                        self.yang_name = "basic-counter-interface-template"
                        self.yang_parent_name = "basic-counter-interface-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("in-octets", ("in_octets", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets)), ("out-octets", ("out_octets", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets)), ("output-queue-drops", ("output_queue_drops", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops)), ("input-total-errors", ("input_total_errors", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors)), ("output-total-drops", ("output_total_drops", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops)), ("out-packets", ("out_packets", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets)), ("output-total-errors", ("output_total_errors", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors)), ("in-packets", ("in_packets", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets)), ("input-queue-drops", ("input_queue_drops", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops)), ("input-total-drops", ("input_total_drops", PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None
                        self.reg_exp_group = None
                        self.vrf_group = None

                        self.in_octets = None
                        self._children_name_map["in_octets"] = "in-octets"

                        self.out_octets = None
                        self._children_name_map["out_octets"] = "out-octets"

                        self.output_queue_drops = None
                        self._children_name_map["output_queue_drops"] = "output-queue-drops"

                        self.input_total_errors = None
                        self._children_name_map["input_total_errors"] = "input-total-errors"

                        self.output_total_drops = None
                        self._children_name_map["output_total_drops"] = "output-total-drops"

                        self.out_packets = None
                        self._children_name_map["out_packets"] = "out-packets"

                        self.output_total_errors = None
                        self._children_name_map["output_total_errors"] = "output-total-errors"

                        self.in_packets = None
                        self._children_name_map["in_packets"] = "in-packets"

                        self.input_queue_drops = None
                        self._children_name_map["input_queue_drops"] = "input-queue-drops"

                        self.input_total_drops = None
                        self._children_name_map["input_total_drops"] = "input-total-drops"
                        self._segment_path = lambda: "basic-counter-interface-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/basic-counter-interface/basic-counter-interface-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate, ['template_name', 'sample_interval', 'reg_exp_group', 'vrf_group'], name, value)


                    class InOctets(Entity):
                        """
                        Number of inbound octets/bytes
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets, self).__init__()

                            self.yang_name = "in-octets"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-octets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutOctets(Entity):
                        """
                        Number of outbound octets/bytes
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets, self).__init__()

                            self.yang_name = "out-octets"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-octets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputQueueDrops(Entity):
                        """
                        Number of outbound queue drops
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops, self).__init__()

                            self.yang_name = "output-queue-drops"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-queue-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputTotalErrors(Entity):
                        """
                        Number of inbound incorrect packets
                        discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors, self).__init__()

                            self.yang_name = "input-total-errors"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-total-errors"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputTotalDrops(Entity):
                        """
                        Number of outbound correct packets discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops, self).__init__()

                            self.yang_name = "output-total-drops"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-total-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutPackets(Entity):
                        """
                        Number of outbound packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets, self).__init__()

                            self.yang_name = "out-packets"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "out-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputTotalErrors(Entity):
                        """
                        Number of outbound incorrect packets
                        discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors, self).__init__()

                            self.yang_name = "output-total-errors"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-total-errors"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InPackets(Entity):
                        """
                        Number of inbound packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets, self).__init__()

                            self.yang_name = "in-packets"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "in-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputQueueDrops(Entity):
                        """
                        Number of input queue drops
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops, self).__init__()

                            self.yang_name = "input-queue-drops"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-queue-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputTotalDrops(Entity):
                        """
                        Number of inbound correct packets discarded
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops, self).__init__()

                            self.yang_name = "input-total-drops"
                            self.yang_parent_name = "basic-counter-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-total-drops"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class Bgp(Entity):
            """
            BGP threshold configuration
            
            .. attribute:: bgp_templates
            
            	BGP threshold templates
            	**type**\:  :py:class:`BgpTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.Bgp, self).__init__()

                self.yang_name = "bgp"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("bgp-templates", ("bgp_templates", PerfMgmt.Threshold.Bgp.BgpTemplates))])
                self._leafs = OrderedDict()

                self.bgp_templates = PerfMgmt.Threshold.Bgp.BgpTemplates()
                self.bgp_templates.parent = self
                self._children_name_map["bgp_templates"] = "bgp-templates"
                self._segment_path = lambda: "bgp"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.Bgp, [], name, value)


            class BgpTemplates(Entity):
                """
                BGP threshold templates
                
                .. attribute:: bgp_template
                
                	BGP threshold template instance
                	**type**\: list of  		 :py:class:`BgpTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.Bgp.BgpTemplates, self).__init__()

                    self.yang_name = "bgp-templates"
                    self.yang_parent_name = "bgp"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bgp-template", ("bgp_template", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate))])
                    self._leafs = OrderedDict()

                    self.bgp_template = YList(self)
                    self._segment_path = lambda: "bgp-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/bgp/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates, [], name, value)


                class BgpTemplate(Entity):
                    """
                    BGP threshold template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: output_update_messages
                    
                    	Number of update messages sent
                    	**type**\:  :py:class:`OutputUpdateMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: errors_received
                    
                    	Number of error notifications received
                    	**type**\:  :py:class:`ErrorsReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: conn_established
                    
                    	Number of times the connection was established
                    	**type**\:  :py:class:`ConnEstablished <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_messages
                    
                    	Number of messages sent
                    	**type**\:  :py:class:`OutputMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: conn_dropped
                    
                    	Number of times the connection was dropped
                    	**type**\:  :py:class:`ConnDropped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_update_messages
                    
                    	Number of update messages received
                    	**type**\:  :py:class:`InputUpdateMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: errors_sent
                    
                    	Number of error notifications sent
                    	**type**\:  :py:class:`ErrorsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_messages
                    
                    	Number of messages received
                    	**type**\:  :py:class:`InputMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate, self).__init__()

                        self.yang_name = "bgp-template"
                        self.yang_parent_name = "bgp-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("output-update-messages", ("output_update_messages", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages)), ("errors-received", ("errors_received", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived)), ("conn-established", ("conn_established", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished)), ("output-messages", ("output_messages", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages)), ("conn-dropped", ("conn_dropped", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped)), ("input-update-messages", ("input_update_messages", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages)), ("errors-sent", ("errors_sent", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent)), ("input-messages", ("input_messages", PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.output_update_messages = None
                        self._children_name_map["output_update_messages"] = "output-update-messages"

                        self.errors_received = None
                        self._children_name_map["errors_received"] = "errors-received"

                        self.conn_established = None
                        self._children_name_map["conn_established"] = "conn-established"

                        self.output_messages = None
                        self._children_name_map["output_messages"] = "output-messages"

                        self.conn_dropped = None
                        self._children_name_map["conn_dropped"] = "conn-dropped"

                        self.input_update_messages = None
                        self._children_name_map["input_update_messages"] = "input-update-messages"

                        self.errors_sent = None
                        self._children_name_map["errors_sent"] = "errors-sent"

                        self.input_messages = None
                        self._children_name_map["input_messages"] = "input-messages"
                        self._segment_path = lambda: "bgp-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/bgp/bgp-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate, ['template_name', 'sample_interval'], name, value)


                    class OutputUpdateMessages(Entity):
                        """
                        Number of update messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages, self).__init__()

                            self.yang_name = "output-update-messages"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-update-messages"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class ErrorsReceived(Entity):
                        """
                        Number of error notifications received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived, self).__init__()

                            self.yang_name = "errors-received"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "errors-received"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class ConnEstablished(Entity):
                        """
                        Number of times the connection was
                        established
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished, self).__init__()

                            self.yang_name = "conn-established"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "conn-established"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputMessages(Entity):
                        """
                        Number of messages sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages, self).__init__()

                            self.yang_name = "output-messages"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-messages"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class ConnDropped(Entity):
                        """
                        Number of times the connection was dropped
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped, self).__init__()

                            self.yang_name = "conn-dropped"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "conn-dropped"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputUpdateMessages(Entity):
                        """
                        Number of update messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages, self).__init__()

                            self.yang_name = "input-update-messages"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-update-messages"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class ErrorsSent(Entity):
                        """
                        Number of error notifications sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent, self).__init__()

                            self.yang_name = "errors-sent"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "errors-sent"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputMessages(Entity):
                        """
                        Number of messages received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages, self).__init__()

                            self.yang_name = "input-messages"
                            self.yang_parent_name = "bgp-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-messages"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class Ospfv2Protocol(Entity):
            """
            OSPF v2 Protocol threshold configuration
            
            .. attribute:: ospfv2_protocol_templates
            
            	OSPF v2 Protocol threshold templates
            	**type**\:  :py:class:`Ospfv2ProtocolTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.Ospfv2Protocol, self).__init__()

                self.yang_name = "ospfv2-protocol"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ospfv2-protocol-templates", ("ospfv2_protocol_templates", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates))])
                self._leafs = OrderedDict()

                self.ospfv2_protocol_templates = PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates()
                self.ospfv2_protocol_templates.parent = self
                self._children_name_map["ospfv2_protocol_templates"] = "ospfv2-protocol-templates"
                self._segment_path = lambda: "ospfv2-protocol"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol, [], name, value)


            class Ospfv2ProtocolTemplates(Entity):
                """
                OSPF v2 Protocol threshold templates
                
                .. attribute:: ospfv2_protocol_template
                
                	OSPF v2 Protocol threshold template instance
                	**type**\: list of  		 :py:class:`Ospfv2ProtocolTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates, self).__init__()

                    self.yang_name = "ospfv2-protocol-templates"
                    self.yang_parent_name = "ospfv2-protocol"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospfv2-protocol-template", ("ospfv2_protocol_template", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate))])
                    self._leafs = OrderedDict()

                    self.ospfv2_protocol_template = YList(self)
                    self._segment_path = lambda: "ospfv2-protocol-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/ospfv2-protocol/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates, [], name, value)


                class Ospfv2ProtocolTemplate(Entity):
                    """
                    OSPF v2 Protocol threshold template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: checksum_errors
                    
                    	Number of packets received with checksum errors
                    	**type**\:  :py:class:`ChecksumErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks_lsa
                    
                    	Number of LSA received in LSA Acknowledgements
                    	**type**\:  :py:class:`InputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds_lsa
                    
                    	Number of LSA sent in DBD packets
                    	**type**\:  :py:class:`OutputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds_lsa
                    
                    	Number of LSA received in DBD packets
                    	**type**\:  :py:class:`InputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates
                    
                    	Number of LSA Updates received
                    	**type**\:  :py:class:`InputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds
                    
                    	Number of DBD packets sent
                    	**type**\:  :py:class:`OutputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates_lsa
                    
                    	Number of LSA sent in LSA Updates
                    	**type**\:  :py:class:`OutputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds
                    
                    	Number of DBD packets received
                    	**type**\:  :py:class:`InputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates_lsa
                    
                    	Number of LSA received in LSA Updates
                    	**type**\:  :py:class:`InputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: output_packets
                    
                    	Total number of packets sent
                    	**type**\:  :py:class:`OutputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_packets
                    
                    	Total number of packets received
                    	**type**\:  :py:class:`InputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_hello_packets
                    
                    	Total number of packets sent
                    	**type**\:  :py:class:`OutputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_hello_packets
                    
                    	Number of Hello packets received
                    	**type**\:  :py:class:`InputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests
                    
                    	Number of LS Requests sent
                    	**type**\:  :py:class:`OutputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks_lsa
                    
                    	Number of LSA sent in LSA Acknowledgements
                    	**type**\:  :py:class:`OutputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks
                    
                    	Number of LSA Acknowledgements sent
                    	**type**\:  :py:class:`OutputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks
                    
                    	Number of LSA Acknowledgements received
                    	**type**\:  :py:class:`InputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates
                    
                    	Number of LSA Updates sent
                    	**type**\:  :py:class:`OutputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests_lsa
                    
                    	Number of LSA sent in LS Requests
                    	**type**\:  :py:class:`OutputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests_lsa
                    
                    	Number of LSA received in LS Requests
                    	**type**\:  :py:class:`InputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests
                    
                    	Number of LS Requests received
                    	**type**\:  :py:class:`InputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate, self).__init__()

                        self.yang_name = "ospfv2-protocol-template"
                        self.yang_parent_name = "ospfv2-protocol-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("checksum-errors", ("checksum_errors", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors)), ("input-lsa-acks-lsa", ("input_lsa_acks_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa)), ("output-db-ds-lsa", ("output_db_ds_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa)), ("input-db-ds-lsa", ("input_db_ds_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa)), ("input-lsa-updates", ("input_lsa_updates", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates)), ("output-db-ds", ("output_db_ds", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs)), ("output-lsa-updates-lsa", ("output_lsa_updates_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa)), ("input-db-ds", ("input_db_ds", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs)), ("input-lsa-updates-lsa", ("input_lsa_updates_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa)), ("output-packets", ("output_packets", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets)), ("input-packets", ("input_packets", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets)), ("output-hello-packets", ("output_hello_packets", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets)), ("input-hello-packets", ("input_hello_packets", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets)), ("output-ls-requests", ("output_ls_requests", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests)), ("output-lsa-acks-lsa", ("output_lsa_acks_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa)), ("output-lsa-acks", ("output_lsa_acks", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks)), ("input-lsa-acks", ("input_lsa_acks", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks)), ("output-lsa-updates", ("output_lsa_updates", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates)), ("output-ls-requests-lsa", ("output_ls_requests_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa)), ("input-ls-requests-lsa", ("input_ls_requests_lsa", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa)), ("input-ls-requests", ("input_ls_requests", PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.checksum_errors = None
                        self._children_name_map["checksum_errors"] = "checksum-errors"

                        self.input_lsa_acks_lsa = None
                        self._children_name_map["input_lsa_acks_lsa"] = "input-lsa-acks-lsa"

                        self.output_db_ds_lsa = None
                        self._children_name_map["output_db_ds_lsa"] = "output-db-ds-lsa"

                        self.input_db_ds_lsa = None
                        self._children_name_map["input_db_ds_lsa"] = "input-db-ds-lsa"

                        self.input_lsa_updates = None
                        self._children_name_map["input_lsa_updates"] = "input-lsa-updates"

                        self.output_db_ds = None
                        self._children_name_map["output_db_ds"] = "output-db-ds"

                        self.output_lsa_updates_lsa = None
                        self._children_name_map["output_lsa_updates_lsa"] = "output-lsa-updates-lsa"

                        self.input_db_ds = None
                        self._children_name_map["input_db_ds"] = "input-db-ds"

                        self.input_lsa_updates_lsa = None
                        self._children_name_map["input_lsa_updates_lsa"] = "input-lsa-updates-lsa"

                        self.output_packets = None
                        self._children_name_map["output_packets"] = "output-packets"

                        self.input_packets = None
                        self._children_name_map["input_packets"] = "input-packets"

                        self.output_hello_packets = None
                        self._children_name_map["output_hello_packets"] = "output-hello-packets"

                        self.input_hello_packets = None
                        self._children_name_map["input_hello_packets"] = "input-hello-packets"

                        self.output_ls_requests = None
                        self._children_name_map["output_ls_requests"] = "output-ls-requests"

                        self.output_lsa_acks_lsa = None
                        self._children_name_map["output_lsa_acks_lsa"] = "output-lsa-acks-lsa"

                        self.output_lsa_acks = None
                        self._children_name_map["output_lsa_acks"] = "output-lsa-acks"

                        self.input_lsa_acks = None
                        self._children_name_map["input_lsa_acks"] = "input-lsa-acks"

                        self.output_lsa_updates = None
                        self._children_name_map["output_lsa_updates"] = "output-lsa-updates"

                        self.output_ls_requests_lsa = None
                        self._children_name_map["output_ls_requests_lsa"] = "output-ls-requests-lsa"

                        self.input_ls_requests_lsa = None
                        self._children_name_map["input_ls_requests_lsa"] = "input-ls-requests-lsa"

                        self.input_ls_requests = None
                        self._children_name_map["input_ls_requests"] = "input-ls-requests"
                        self._segment_path = lambda: "ospfv2-protocol-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/ospfv2-protocol/ospfv2-protocol-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate, ['template_name', 'sample_interval'], name, value)


                    class ChecksumErrors(Entity):
                        """
                        Number of packets received with checksum
                        errors
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors, self).__init__()

                            self.yang_name = "checksum-errors"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "checksum-errors"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaAcksLsa(Entity):
                        """
                        Number of LSA received in LSA Acknowledgements
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa, self).__init__()

                            self.yang_name = "input-lsa-acks-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-acks-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputDbDsLsa(Entity):
                        """
                        Number of LSA sent in DBD packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa, self).__init__()

                            self.yang_name = "output-db-ds-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-db-ds-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputDbDsLsa(Entity):
                        """
                        Number of LSA received in DBD packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa, self).__init__()

                            self.yang_name = "input-db-ds-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-db-ds-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaUpdates(Entity):
                        """
                        Number of LSA Updates received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates, self).__init__()

                            self.yang_name = "input-lsa-updates"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-updates"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputDbDs(Entity):
                        """
                        Number of DBD packets sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs, self).__init__()

                            self.yang_name = "output-db-ds"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-db-ds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaUpdatesLsa(Entity):
                        """
                        Number of LSA sent in LSA Updates
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa, self).__init__()

                            self.yang_name = "output-lsa-updates-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-updates-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputDbDs(Entity):
                        """
                        Number of DBD packets received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs, self).__init__()

                            self.yang_name = "input-db-ds"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-db-ds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaUpdatesLsa(Entity):
                        """
                        Number of LSA received in LSA Updates
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa, self).__init__()

                            self.yang_name = "input-lsa-updates-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-updates-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputPackets(Entity):
                        """
                        Total number of packets sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets, self).__init__()

                            self.yang_name = "output-packets"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputPackets(Entity):
                        """
                        Total number of packets received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets, self).__init__()

                            self.yang_name = "input-packets"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputHelloPackets(Entity):
                        """
                        Total number of packets sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets, self).__init__()

                            self.yang_name = "output-hello-packets"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-hello-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputHelloPackets(Entity):
                        """
                        Number of Hello packets received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets, self).__init__()

                            self.yang_name = "input-hello-packets"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-hello-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsRequests(Entity):
                        """
                        Number of LS Requests sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests, self).__init__()

                            self.yang_name = "output-ls-requests"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-ls-requests"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaAcksLsa(Entity):
                        """
                        Number of LSA sent in LSA Acknowledgements
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa, self).__init__()

                            self.yang_name = "output-lsa-acks-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-acks-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaAcks(Entity):
                        """
                        Number of LSA Acknowledgements sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks, self).__init__()

                            self.yang_name = "output-lsa-acks"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-acks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaAcks(Entity):
                        """
                        Number of LSA Acknowledgements received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks, self).__init__()

                            self.yang_name = "input-lsa-acks"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-acks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaUpdates(Entity):
                        """
                        Number of LSA Updates sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates, self).__init__()

                            self.yang_name = "output-lsa-updates"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-updates"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsRequestsLsa(Entity):
                        """
                        Number of LSA sent in LS Requests
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa, self).__init__()

                            self.yang_name = "output-ls-requests-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-ls-requests-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsRequestsLsa(Entity):
                        """
                        Number of LSA received in LS Requests
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa, self).__init__()

                            self.yang_name = "input-ls-requests-lsa"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-ls-requests-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsRequests(Entity):
                        """
                        Number of LS Requests received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests, self).__init__()

                            self.yang_name = "input-ls-requests"
                            self.yang_parent_name = "ospfv2-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-ls-requests"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class CpuNode(Entity):
            """
            Node CPU threshold configuration
            
            .. attribute:: cpu_node_templates
            
            	Node CPU threshold configuration templates
            	**type**\:  :py:class:`CpuNodeTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.CpuNode, self).__init__()

                self.yang_name = "cpu-node"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("cpu-node-templates", ("cpu_node_templates", PerfMgmt.Threshold.CpuNode.CpuNodeTemplates))])
                self._leafs = OrderedDict()

                self.cpu_node_templates = PerfMgmt.Threshold.CpuNode.CpuNodeTemplates()
                self.cpu_node_templates.parent = self
                self._children_name_map["cpu_node_templates"] = "cpu-node-templates"
                self._segment_path = lambda: "cpu-node"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.CpuNode, [], name, value)


            class CpuNodeTemplates(Entity):
                """
                Node CPU threshold configuration templates
                
                .. attribute:: cpu_node_template
                
                	Node CPU threshold configuration template instances
                	**type**\: list of  		 :py:class:`CpuNodeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates, self).__init__()

                    self.yang_name = "cpu-node-templates"
                    self.yang_parent_name = "cpu-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("cpu-node-template", ("cpu_node_template", PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate))])
                    self._leafs = OrderedDict()

                    self.cpu_node_template = YList(self)
                    self._segment_path = lambda: "cpu-node-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/cpu-node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates, [], name, value)


                class CpuNodeTemplate(Entity):
                    """
                    Node CPU threshold configuration template
                    instances
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: average_cpu_used
                    
                    	Average %CPU utilization
                    	**type**\:  :py:class:`AverageCpuUsed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: no_processes
                    
                    	Number of processes
                    	**type**\:  :py:class:`NoProcesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate, self).__init__()

                        self.yang_name = "cpu-node-template"
                        self.yang_parent_name = "cpu-node-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("average-cpu-used", ("average_cpu_used", PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed)), ("no-processes", ("no_processes", PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.average_cpu_used = None
                        self._children_name_map["average_cpu_used"] = "average-cpu-used"

                        self.no_processes = None
                        self._children_name_map["no_processes"] = "no-processes"
                        self._segment_path = lambda: "cpu-node-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/cpu-node/cpu-node-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate, ['template_name', 'sample_interval'], name, value)


                    class AverageCpuUsed(Entity):
                        """
                        Average %CPU utilization
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed, self).__init__()

                            self.yang_name = "average-cpu-used"
                            self.yang_parent_name = "cpu-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "average-cpu-used"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class NoProcesses(Entity):
                        """
                        Number of processes
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses, self).__init__()

                            self.yang_name = "no-processes"
                            self.yang_parent_name = "cpu-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "no-processes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class DataRateInterface(Entity):
            """
            Interface Data Rates threshold configuration
            
            .. attribute:: data_rate_interface_templates
            
            	Interface Data Rates threshold templates
            	**type**\:  :py:class:`DataRateInterfaceTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.DataRateInterface, self).__init__()

                self.yang_name = "data-rate-interface"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("data-rate-interface-templates", ("data_rate_interface_templates", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates))])
                self._leafs = OrderedDict()

                self.data_rate_interface_templates = PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates()
                self.data_rate_interface_templates.parent = self
                self._children_name_map["data_rate_interface_templates"] = "data-rate-interface-templates"
                self._segment_path = lambda: "data-rate-interface"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.DataRateInterface, [], name, value)


            class DataRateInterfaceTemplates(Entity):
                """
                Interface Data Rates threshold templates
                
                .. attribute:: data_rate_interface_template
                
                	Interface Data Rates threshold template instance
                	**type**\: list of  		 :py:class:`DataRateInterfaceTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates, self).__init__()

                    self.yang_name = "data-rate-interface-templates"
                    self.yang_parent_name = "data-rate-interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("data-rate-interface-template", ("data_rate_interface_template", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate))])
                    self._leafs = OrderedDict()

                    self.data_rate_interface_template = YList(self)
                    self._segment_path = lambda: "data-rate-interface-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/data-rate-interface/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates, [], name, value)


                class DataRateInterfaceTemplate(Entity):
                    """
                    Interface Data Rates threshold template
                    instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in kbps
                    	**type**\:  :py:class:`InputDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth in kbps
                    	**type**\:  :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_packet_rate
                    
                    	Number of Output packets per second
                    	**type**\:  :py:class:`OutputPacketRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_peak_pkts
                    
                    	Maximum number of input packets per second
                    	**type**\:  :py:class:`InputPeakPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_peak_rate
                    
                    	Peak output data rate in kbps
                    	**type**\:  :py:class:`OutputPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in kbps
                    	**type**\:  :py:class:`OutputDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_packet_rate
                    
                    	Number of input packets per second
                    	**type**\:  :py:class:`InputPacketRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_peak_pkts
                    
                    	Maximum number of output packets per second
                    	**type**\:  :py:class:`OutputPeakPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_peak_rate
                    
                    	Peak input data rate in kbps
                    	**type**\:  :py:class:`InputPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: vrf_group
                    
                    	Enable instance filtering by VRF name regular expression 
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate, self).__init__()

                        self.yang_name = "data-rate-interface-template"
                        self.yang_parent_name = "data-rate-interface-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("input-data-rate", ("input_data_rate", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate)), ("bandwidth", ("bandwidth", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth)), ("output-packet-rate", ("output_packet_rate", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate)), ("input-peak-pkts", ("input_peak_pkts", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts)), ("output-peak-rate", ("output_peak_rate", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate)), ("output-data-rate", ("output_data_rate", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate)), ("input-packet-rate", ("input_packet_rate", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate)), ("output-peak-pkts", ("output_peak_pkts", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts)), ("input-peak-rate", ("input_peak_rate", PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                            ('reg_exp_group', (YLeaf(YType.str, 'reg-exp-group'), ['str'])),
                            ('vrf_group', (YLeaf(YType.str, 'vrf-group'), ['str'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None
                        self.reg_exp_group = None
                        self.vrf_group = None

                        self.input_data_rate = None
                        self._children_name_map["input_data_rate"] = "input-data-rate"

                        self.bandwidth = None
                        self._children_name_map["bandwidth"] = "bandwidth"

                        self.output_packet_rate = None
                        self._children_name_map["output_packet_rate"] = "output-packet-rate"

                        self.input_peak_pkts = None
                        self._children_name_map["input_peak_pkts"] = "input-peak-pkts"

                        self.output_peak_rate = None
                        self._children_name_map["output_peak_rate"] = "output-peak-rate"

                        self.output_data_rate = None
                        self._children_name_map["output_data_rate"] = "output-data-rate"

                        self.input_packet_rate = None
                        self._children_name_map["input_packet_rate"] = "input-packet-rate"

                        self.output_peak_pkts = None
                        self._children_name_map["output_peak_pkts"] = "output-peak-pkts"

                        self.input_peak_rate = None
                        self._children_name_map["input_peak_rate"] = "input-peak-rate"
                        self._segment_path = lambda: "data-rate-interface-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/data-rate-interface/data-rate-interface-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate, ['template_name', 'sample_interval', 'reg_exp_group', 'vrf_group'], name, value)


                    class InputDataRate(Entity):
                        """
                        Input data rate in kbps
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate, self).__init__()

                            self.yang_name = "input-data-rate"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-data-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class Bandwidth(Entity):
                        """
                        Bandwidth in kbps
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth, self).__init__()

                            self.yang_name = "bandwidth"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "bandwidth"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputPacketRate(Entity):
                        """
                        Number of Output packets per second
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate, self).__init__()

                            self.yang_name = "output-packet-rate"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-packet-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputPeakPkts(Entity):
                        """
                        Maximum number of input packets per second
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts, self).__init__()

                            self.yang_name = "input-peak-pkts"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-peak-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputPeakRate(Entity):
                        """
                        Peak output data rate in kbps
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate, self).__init__()

                            self.yang_name = "output-peak-rate"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-peak-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputDataRate(Entity):
                        """
                        Output data rate in kbps
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate, self).__init__()

                            self.yang_name = "output-data-rate"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-data-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputPacketRate(Entity):
                        """
                        Number of input packets per second
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate, self).__init__()

                            self.yang_name = "input-packet-rate"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-packet-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputPeakPkts(Entity):
                        """
                        Maximum number of output packets per second
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts, self).__init__()

                            self.yang_name = "output-peak-pkts"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-peak-pkts"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputPeakRate(Entity):
                        """
                        Peak input data rate in kbps
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate, self).__init__()

                            self.yang_name = "input-peak-rate"
                            self.yang_parent_name = "data-rate-interface-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-peak-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class ProcessNode(Entity):
            """
            Node Process threshold configuration
            
            .. attribute:: process_node_templates
            
            	Node Memory threshold templates
            	**type**\:  :py:class:`ProcessNodeTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.ProcessNode, self).__init__()

                self.yang_name = "process-node"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("process-node-templates", ("process_node_templates", PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates))])
                self._leafs = OrderedDict()

                self.process_node_templates = PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates()
                self.process_node_templates.parent = self
                self._children_name_map["process_node_templates"] = "process-node-templates"
                self._segment_path = lambda: "process-node"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.ProcessNode, [], name, value)


            class ProcessNodeTemplates(Entity):
                """
                Node Memory threshold templates
                
                .. attribute:: process_node_template
                
                	Node Memory threshold template instance
                	**type**\: list of  		 :py:class:`ProcessNodeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates, self).__init__()

                    self.yang_name = "process-node-templates"
                    self.yang_parent_name = "process-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("process-node-template", ("process_node_template", PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate))])
                    self._leafs = OrderedDict()

                    self.process_node_template = YList(self)
                    self._segment_path = lambda: "process-node-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/process-node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates, [], name, value)


                class ProcessNodeTemplate(Entity):
                    """
                    Node Memory threshold template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: average_cpu_used
                    
                    	Average %CPU utilization
                    	**type**\:  :py:class:`AverageCpuUsed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: peak_memory
                    
                    	Max memory (KBytes) used since startup time
                    	**type**\:  :py:class:`PeakMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: no_threads
                    
                    	Number of threads
                    	**type**\:  :py:class:`NoThreads <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate, self).__init__()

                        self.yang_name = "process-node-template"
                        self.yang_parent_name = "process-node-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("average-cpu-used", ("average_cpu_used", PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed)), ("peak-memory", ("peak_memory", PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory)), ("no-threads", ("no_threads", PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.average_cpu_used = None
                        self._children_name_map["average_cpu_used"] = "average-cpu-used"

                        self.peak_memory = None
                        self._children_name_map["peak_memory"] = "peak-memory"

                        self.no_threads = None
                        self._children_name_map["no_threads"] = "no-threads"
                        self._segment_path = lambda: "process-node-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/process-node/process-node-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate, ['template_name', 'sample_interval'], name, value)


                    class AverageCpuUsed(Entity):
                        """
                        Average %CPU utilization
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..100
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed, self).__init__()

                            self.yang_name = "average-cpu-used"
                            self.yang_parent_name = "process-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "average-cpu-used"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class PeakMemory(Entity):
                        """
                        Max memory (KBytes) used since startup time
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory, self).__init__()

                            self.yang_name = "peak-memory"
                            self.yang_parent_name = "process-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "peak-memory"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class NoThreads(Entity):
                        """
                        Number of threads
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..32767
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..32767
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads, self).__init__()

                            self.yang_name = "no-threads"
                            self.yang_parent_name = "process-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "no-threads"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class MemoryNode(Entity):
            """
            Node Memory threshold configuration
            
            .. attribute:: memory_node_templates
            
            	Node Memory threshold configuration templates
            	**type**\:  :py:class:`MemoryNodeTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.MemoryNode, self).__init__()

                self.yang_name = "memory-node"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("memory-node-templates", ("memory_node_templates", PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates))])
                self._leafs = OrderedDict()

                self.memory_node_templates = PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates()
                self.memory_node_templates.parent = self
                self._children_name_map["memory_node_templates"] = "memory-node-templates"
                self._segment_path = lambda: "memory-node"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.MemoryNode, [], name, value)


            class MemoryNodeTemplates(Entity):
                """
                Node Memory threshold configuration templates
                
                .. attribute:: memory_node_template
                
                	Node Memory threshold configuration template instance
                	**type**\: list of  		 :py:class:`MemoryNodeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates, self).__init__()

                    self.yang_name = "memory-node-templates"
                    self.yang_parent_name = "memory-node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("memory-node-template", ("memory_node_template", PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate))])
                    self._leafs = OrderedDict()

                    self.memory_node_template = YList(self)
                    self._segment_path = lambda: "memory-node-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/memory-node/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates, [], name, value)


                class MemoryNodeTemplate(Entity):
                    """
                    Node Memory threshold configuration template
                    instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: peak_memory
                    
                    	Maximum memory (KBytes) used
                    	**type**\:  :py:class:`PeakMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: curr_memory
                    
                    	Current memory (Bytes) in use
                    	**type**\:  :py:class:`CurrMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate, self).__init__()

                        self.yang_name = "memory-node-template"
                        self.yang_parent_name = "memory-node-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("peak-memory", ("peak_memory", PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory)), ("curr-memory", ("curr_memory", PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.peak_memory = None
                        self._children_name_map["peak_memory"] = "peak-memory"

                        self.curr_memory = None
                        self._children_name_map["curr_memory"] = "curr-memory"
                        self._segment_path = lambda: "memory-node-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/memory-node/memory-node-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate, ['template_name', 'sample_interval'], name, value)


                    class PeakMemory(Entity):
                        """
                        Maximum memory (KBytes) used
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4194304
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4194304
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory, self).__init__()

                            self.yang_name = "peak-memory"
                            self.yang_parent_name = "memory-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "peak-memory"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class CurrMemory(Entity):
                        """
                        Current memory (Bytes) in use
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory, self).__init__()

                            self.yang_name = "curr-memory"
                            self.yang_parent_name = "memory-node-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "curr-memory"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


        class Ospfv3Protocol(Entity):
            """
            OSPF v2 Protocol threshold configuration
            
            .. attribute:: ospfv3_protocol_templates
            
            	OSPF v2 Protocol threshold templates
            	**type**\:  :py:class:`Ospfv3ProtocolTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(PerfMgmt.Threshold.Ospfv3Protocol, self).__init__()

                self.yang_name = "ospfv3-protocol"
                self.yang_parent_name = "threshold"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("ospfv3-protocol-templates", ("ospfv3_protocol_templates", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates))])
                self._leafs = OrderedDict()

                self.ospfv3_protocol_templates = PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates()
                self.ospfv3_protocol_templates.parent = self
                self._children_name_map["ospfv3_protocol_templates"] = "ospfv3-protocol-templates"
                self._segment_path = lambda: "ospfv3-protocol"
                self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol, [], name, value)


            class Ospfv3ProtocolTemplates(Entity):
                """
                OSPF v2 Protocol threshold templates
                
                .. attribute:: ospfv3_protocol_template
                
                	OSPF v2 Protocol threshold template instance
                	**type**\: list of  		 :py:class:`Ospfv3ProtocolTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates, self).__init__()

                    self.yang_name = "ospfv3-protocol-templates"
                    self.yang_parent_name = "ospfv3-protocol"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ospfv3-protocol-template", ("ospfv3_protocol_template", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate))])
                    self._leafs = OrderedDict()

                    self.ospfv3_protocol_template = YList(self)
                    self._segment_path = lambda: "ospfv3-protocol-templates"
                    self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/ospfv3-protocol/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates, [], name, value)


                class Ospfv3ProtocolTemplate(Entity):
                    """
                    OSPF v2 Protocol threshold template instance
                    
                    .. attribute:: template_name  (key)
                    
                    	Template Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: input_lsa_acks_lsa
                    
                    	Number of LSA received in LSA Acknowledgements
                    	**type**\:  :py:class:`InputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds_lsa
                    
                    	Number of LSA sent in DBD packets
                    	**type**\:  :py:class:`OutputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds_lsa
                    
                    	Number of LSA received in DBD packets
                    	**type**\:  :py:class:`InputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates
                    
                    	Number of LSA Updates received
                    	**type**\:  :py:class:`InputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds
                    
                    	Number of DBD packets sent
                    	**type**\:  :py:class:`OutputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates_lsa
                    
                    	Number of LSA sent in LSA Updates
                    	**type**\:  :py:class:`OutputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds
                    
                    	Number of DBD packets received
                    	**type**\:  :py:class:`InputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates_lsa
                    
                    	Number of LSA received in LSA Updates
                    	**type**\:  :py:class:`InputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\: int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: output_packets
                    
                    	Total number of packets sent
                    	**type**\:  :py:class:`OutputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_packets
                    
                    	Total number of packets received
                    	**type**\:  :py:class:`InputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_hello_packets
                    
                    	Total number of packets sent
                    	**type**\:  :py:class:`OutputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_hello_packets
                    
                    	Number of Hello packets received
                    	**type**\:  :py:class:`InputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests
                    
                    	Number of LS Requests sent
                    	**type**\:  :py:class:`OutputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks_lsa
                    
                    	Number of LSA sent in LSA Acknowledgements
                    	**type**\:  :py:class:`OutputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks
                    
                    	Number of LSA Acknowledgements sent
                    	**type**\:  :py:class:`OutputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks
                    
                    	Number of LSA Acknowledgements received
                    	**type**\:  :py:class:`InputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates
                    
                    	Number of LSA Updates sent
                    	**type**\:  :py:class:`OutputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests_lsa
                    
                    	Number of LSA sent in LS Requests
                    	**type**\:  :py:class:`OutputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests_lsa
                    
                    	Number of LSA received in LS Requests
                    	**type**\:  :py:class:`InputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests
                    
                    	Number of LS Requests received
                    	**type**\:  :py:class:`InputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate, self).__init__()

                        self.yang_name = "ospfv3-protocol-template"
                        self.yang_parent_name = "ospfv3-protocol-templates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['template_name']
                        self._child_classes = OrderedDict([("input-lsa-acks-lsa", ("input_lsa_acks_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa)), ("output-db-ds-lsa", ("output_db_ds_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa)), ("input-db-ds-lsa", ("input_db_ds_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa)), ("input-lsa-updates", ("input_lsa_updates", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates)), ("output-db-ds", ("output_db_ds", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs)), ("output-lsa-updates-lsa", ("output_lsa_updates_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa)), ("input-db-ds", ("input_db_ds", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs)), ("input-lsa-updates-lsa", ("input_lsa_updates_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa)), ("output-packets", ("output_packets", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets)), ("input-packets", ("input_packets", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets)), ("output-hello-packets", ("output_hello_packets", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets)), ("input-hello-packets", ("input_hello_packets", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets)), ("output-ls-requests", ("output_ls_requests", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests)), ("output-lsa-acks-lsa", ("output_lsa_acks_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa)), ("output-lsa-acks", ("output_lsa_acks", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks)), ("input-lsa-acks", ("input_lsa_acks", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks)), ("output-lsa-updates", ("output_lsa_updates", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates)), ("output-ls-requests-lsa", ("output_ls_requests_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa)), ("input-ls-requests-lsa", ("input_ls_requests_lsa", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa)), ("input-ls-requests", ("input_ls_requests", PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests))])
                        self._leafs = OrderedDict([
                            ('template_name', (YLeaf(YType.str, 'template-name'), ['str'])),
                            ('sample_interval', (YLeaf(YType.uint32, 'sample-interval'), ['int'])),
                        ])
                        self.template_name = None
                        self.sample_interval = None

                        self.input_lsa_acks_lsa = None
                        self._children_name_map["input_lsa_acks_lsa"] = "input-lsa-acks-lsa"

                        self.output_db_ds_lsa = None
                        self._children_name_map["output_db_ds_lsa"] = "output-db-ds-lsa"

                        self.input_db_ds_lsa = None
                        self._children_name_map["input_db_ds_lsa"] = "input-db-ds-lsa"

                        self.input_lsa_updates = None
                        self._children_name_map["input_lsa_updates"] = "input-lsa-updates"

                        self.output_db_ds = None
                        self._children_name_map["output_db_ds"] = "output-db-ds"

                        self.output_lsa_updates_lsa = None
                        self._children_name_map["output_lsa_updates_lsa"] = "output-lsa-updates-lsa"

                        self.input_db_ds = None
                        self._children_name_map["input_db_ds"] = "input-db-ds"

                        self.input_lsa_updates_lsa = None
                        self._children_name_map["input_lsa_updates_lsa"] = "input-lsa-updates-lsa"

                        self.output_packets = None
                        self._children_name_map["output_packets"] = "output-packets"

                        self.input_packets = None
                        self._children_name_map["input_packets"] = "input-packets"

                        self.output_hello_packets = None
                        self._children_name_map["output_hello_packets"] = "output-hello-packets"

                        self.input_hello_packets = None
                        self._children_name_map["input_hello_packets"] = "input-hello-packets"

                        self.output_ls_requests = None
                        self._children_name_map["output_ls_requests"] = "output-ls-requests"

                        self.output_lsa_acks_lsa = None
                        self._children_name_map["output_lsa_acks_lsa"] = "output-lsa-acks-lsa"

                        self.output_lsa_acks = None
                        self._children_name_map["output_lsa_acks"] = "output-lsa-acks"

                        self.input_lsa_acks = None
                        self._children_name_map["input_lsa_acks"] = "input-lsa-acks"

                        self.output_lsa_updates = None
                        self._children_name_map["output_lsa_updates"] = "output-lsa-updates"

                        self.output_ls_requests_lsa = None
                        self._children_name_map["output_ls_requests_lsa"] = "output-ls-requests-lsa"

                        self.input_ls_requests_lsa = None
                        self._children_name_map["input_ls_requests_lsa"] = "input-ls-requests-lsa"

                        self.input_ls_requests = None
                        self._children_name_map["input_ls_requests"] = "input-ls-requests"
                        self._segment_path = lambda: "ospfv3-protocol-template" + "[template-name='" + str(self.template_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/threshold/ospfv3-protocol/ospfv3-protocol-templates/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate, ['template_name', 'sample_interval'], name, value)


                    class InputLsaAcksLsa(Entity):
                        """
                        Number of LSA received in LSA Acknowledgements
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa, self).__init__()

                            self.yang_name = "input-lsa-acks-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-acks-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputDbDsLsa(Entity):
                        """
                        Number of LSA sent in DBD packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa, self).__init__()

                            self.yang_name = "output-db-ds-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-db-ds-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputDbDsLsa(Entity):
                        """
                        Number of LSA received in DBD packets
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa, self).__init__()

                            self.yang_name = "input-db-ds-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-db-ds-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaUpdates(Entity):
                        """
                        Number of LSA Updates received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates, self).__init__()

                            self.yang_name = "input-lsa-updates"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-updates"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputDbDs(Entity):
                        """
                        Number of DBD packets sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs, self).__init__()

                            self.yang_name = "output-db-ds"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-db-ds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaUpdatesLsa(Entity):
                        """
                        Number of LSA sent in LSA Updates
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa, self).__init__()

                            self.yang_name = "output-lsa-updates-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-updates-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputDbDs(Entity):
                        """
                        Number of DBD packets received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs, self).__init__()

                            self.yang_name = "input-db-ds"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-db-ds"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaUpdatesLsa(Entity):
                        """
                        Number of LSA received in LSA Updates
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa, self).__init__()

                            self.yang_name = "input-lsa-updates-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-updates-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputPackets(Entity):
                        """
                        Total number of packets sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets, self).__init__()

                            self.yang_name = "output-packets"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputPackets(Entity):
                        """
                        Total number of packets received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets, self).__init__()

                            self.yang_name = "input-packets"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputHelloPackets(Entity):
                        """
                        Total number of packets sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets, self).__init__()

                            self.yang_name = "output-hello-packets"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-hello-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputHelloPackets(Entity):
                        """
                        Number of Hello packets received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets, self).__init__()

                            self.yang_name = "input-hello-packets"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-hello-packets"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsRequests(Entity):
                        """
                        Number of LS Requests sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests, self).__init__()

                            self.yang_name = "output-ls-requests"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-ls-requests"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaAcksLsa(Entity):
                        """
                        Number of LSA sent in LSA Acknowledgements
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa, self).__init__()

                            self.yang_name = "output-lsa-acks-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-acks-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaAcks(Entity):
                        """
                        Number of LSA Acknowledgements sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks, self).__init__()

                            self.yang_name = "output-lsa-acks"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-acks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsaAcks(Entity):
                        """
                        Number of LSA Acknowledgements received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks, self).__init__()

                            self.yang_name = "input-lsa-acks"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-lsa-acks"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsaUpdates(Entity):
                        """
                        Number of LSA Updates sent
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates, self).__init__()

                            self.yang_name = "output-lsa-updates"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-lsa-updates"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class OutputLsRequestsLsa(Entity):
                        """
                        Number of LSA sent in LS Requests
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa, self).__init__()

                            self.yang_name = "output-ls-requests-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "output-ls-requests-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsRequestsLsa(Entity):
                        """
                        Number of LSA received in LS Requests
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa, self).__init__()

                            self.yang_name = "input-ls-requests-lsa"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-ls-requests-lsa"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)


                    class InputLsRequests(Entity):
                        """
                        Number of LS Requests received
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:  :py:class:`PmThresholdOp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOp>`
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\: bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:  :py:class:`PmThresholdRearm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearm>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\: int
                        
                        	**range:** 1..100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests, self).__init__()

                            self.yang_name = "input-ls-requests"
                            self.yang_parent_name = "ospfv3-protocol-template"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('operator', (YLeaf(YType.enumeration, 'operator'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdOp', '')])),
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('end_range_value', (YLeaf(YType.uint32, 'end-range-value'), ['int'])),
                                ('percent', (YLeaf(YType.boolean, 'percent'), ['bool'])),
                                ('rearm_type', (YLeaf(YType.enumeration, 'rearm-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg', 'PmThresholdRearm', '')])),
                                ('rearm_window', (YLeaf(YType.uint32, 'rearm-window'), ['int'])),
                            ])
                            self.operator = None
                            self.value = None
                            self.end_range_value = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self._segment_path = lambda: "input-ls-requests"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests, ['operator', 'value', 'end_range_value', 'percent', 'rearm_type', 'rearm_window'], name, value)

    def clone_ptr(self):
        self._top_entity = PerfMgmt()
        return self._top_entity

