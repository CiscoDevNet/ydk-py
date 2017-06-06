""" Cisco_IOS_XR_manageability_perfmgmt_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR manageability\-perfmgmt package configuration.

This module contains definitions
for the following management objects\:
  perf\-mgmt\: Performance Management configuration & operations

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PmThresholdOpEnum(Enum):
    """
    PmThresholdOpEnum

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

    eq = 1

    ne = 2

    lt = 3

    le = 4

    gt = 5

    ge = 6

    rg = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
        return meta._meta_table['PmThresholdOpEnum']


class PmThresholdRearmEnum(Enum):
    """
    PmThresholdRearmEnum

    Pm threshold rearm

    .. data:: always = 0

    	Rearm Always

    .. data:: window = 1

    	Rearm after window of sampling periods

    .. data:: toggle = 2

    	Rearm after the first period when condition is

    	not met

    """

    always = 0

    window = 1

    toggle = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
        return meta._meta_table['PmThresholdRearmEnum']



class PerfMgmt(object):
    """
    Performance Management configuration & operations
    
    .. attribute:: enable
    
    	Start data collection and/or threshold monitoring
    	**type**\:   :py:class:`Enable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable>`
    
    .. attribute:: reg_exp_groups
    
    	Configure regular expression group
    	**type**\:   :py:class:`RegExpGroups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups>`
    
    .. attribute:: resources
    
    	Resources configuration
    	**type**\:   :py:class:`Resources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources>`
    
    .. attribute:: statistics
    
    	Templates for collection of statistics
    	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics>`
    
    .. attribute:: threshold
    
    	Container for threshold templates
    	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold>`
    
    

    """

    _prefix = 'manageability-perfmgmt-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.enable = PerfMgmt.Enable()
        self.enable.parent = self
        self.reg_exp_groups = PerfMgmt.RegExpGroups()
        self.reg_exp_groups.parent = self
        self.resources = PerfMgmt.Resources()
        self.resources.parent = self
        self.statistics = PerfMgmt.Statistics()
        self.statistics.parent = self
        self.threshold = PerfMgmt.Threshold()
        self.threshold.parent = self


    class Resources(object):
        """
        Resources configuration
        
        .. attribute:: dump_local
        
        	Configure local dump parameters
        	**type**\:   :py:class:`DumpLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources.DumpLocal>`
        
        .. attribute:: memory_resources
        
        	Configure the memory usage limits of performance management
        	**type**\:   :py:class:`MemoryResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources.MemoryResources>`
        
        .. attribute:: tftp_resources
        
        	Configure the TFTP server IP address and directory name
        	**type**\:   :py:class:`TftpResources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Resources.TftpResources>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.dump_local = PerfMgmt.Resources.DumpLocal()
            self.dump_local.parent = self
            self.memory_resources = PerfMgmt.Resources.MemoryResources()
            self.memory_resources.parent = self
            self.tftp_resources = None


        class TftpResources(object):
            """
            Configure the TFTP server IP address and
            directory name
            
            .. attribute:: directory
            
            	Directory name on TFTP server
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: server_address
            
            	IP address of the TFTP server
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**mandatory**\: True
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.directory = None
                self.server_address = None
                self.vrf_name = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:resources/Cisco-IOS-XR-manageability-perfmgmt-cfg:tftp-resources'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.directory is not None:
                    return True

                if self.server_address is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Resources.TftpResources']['meta_info']


        class DumpLocal(object):
            """
            Configure local dump parameters
            
            .. attribute:: enable
            
            	Enable data dump onto local filesystem
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:resources/Cisco-IOS-XR-manageability-perfmgmt-cfg:dump-local'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Resources.DumpLocal']['meta_info']


        class MemoryResources(object):
            """
            Configure the memory usage limits of
            performance management
            
            .. attribute:: max_limit
            
            	Maximum limit for memory usage (Kbytes) for data buffers
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: kilobyte
            
            .. attribute:: min_reserved
            
            	Specify a minimum free memory (Kbytes) to be ensured before allowing a collection request
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: kilobyte
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.max_limit = None
                self.min_reserved = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:resources/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-resources'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.max_limit is not None:
                    return True

                if self.min_reserved is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Resources.MemoryResources']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:resources'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.dump_local is not None and self.dump_local._has_data():
                return True

            if self.memory_resources is not None and self.memory_resources._has_data():
                return True

            if self.tftp_resources is not None and self.tftp_resources._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
            return meta._meta_table['PerfMgmt.Resources']['meta_info']


    class Statistics(object):
        """
        Templates for collection of statistics
        
        .. attribute:: basic_counter_interface
        
        	Interface BasicCounter collection templates
        	**type**\:   :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.BasicCounterInterface>`
        
        .. attribute:: bgp
        
        	BGP collection templates
        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Bgp>`
        
        .. attribute:: cpu_node
        
        	Node CPU collection templates
        	**type**\:   :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.CpuNode>`
        
        .. attribute:: data_rate_interface
        
        	Interface DataRate collection templates
        	**type**\:   :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.DataRateInterface>`
        
        .. attribute:: generic_counter_interface
        
        	Interface Generic GenericCounter collection templates
        	**type**\:   :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.GenericCounterInterface>`
        
        .. attribute:: ldp_mpls
        
        	MPLS LDP collection templates
        	**type**\:   :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.LdpMpls>`
        
        .. attribute:: memory_node
        
        	Node Memory collection templates
        	**type**\:   :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.MemoryNode>`
        
        .. attribute:: ospfv2_protocol
        
        	OSPF v2 Protocol collection templates
        	**type**\:   :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv2Protocol>`
        
        .. attribute:: ospfv3_protocol
        
        	OSPF v3 Protocol collection templates
        	**type**\:   :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv3Protocol>`
        
        .. attribute:: process_node
        
        	Node Process collection templates
        	**type**\:   :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.ProcessNode>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.basic_counter_interface = PerfMgmt.Statistics.BasicCounterInterface()
            self.basic_counter_interface.parent = self
            self.bgp = PerfMgmt.Statistics.Bgp()
            self.bgp.parent = self
            self.cpu_node = PerfMgmt.Statistics.CpuNode()
            self.cpu_node.parent = self
            self.data_rate_interface = PerfMgmt.Statistics.DataRateInterface()
            self.data_rate_interface.parent = self
            self.generic_counter_interface = PerfMgmt.Statistics.GenericCounterInterface()
            self.generic_counter_interface.parent = self
            self.ldp_mpls = PerfMgmt.Statistics.LdpMpls()
            self.ldp_mpls.parent = self
            self.memory_node = PerfMgmt.Statistics.MemoryNode()
            self.memory_node.parent = self
            self.ospfv2_protocol = PerfMgmt.Statistics.Ospfv2Protocol()
            self.ospfv2_protocol.parent = self
            self.ospfv3_protocol = PerfMgmt.Statistics.Ospfv3Protocol()
            self.ospfv3_protocol.parent = self
            self.process_node = PerfMgmt.Statistics.ProcessNode()
            self.process_node.parent = self


        class GenericCounterInterface(object):
            """
            Interface Generic GenericCounter collection
            templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.GenericCounterInterface.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.GenericCounterInterface.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.GenericCounterInterface.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.GenericCounterInterface.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.GenericCounterInterface.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.GenericCounterInterface']['meta_info']


        class ProcessNode(object):
            """
            Node Process collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.ProcessNode.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.ProcessNode.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.ProcessNode.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.ProcessNode.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.ProcessNode.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.ProcessNode']['meta_info']


        class BasicCounterInterface(object):
            """
            Interface BasicCounter collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.BasicCounterInterface.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.BasicCounterInterface.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.BasicCounterInterface.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.BasicCounterInterface.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.BasicCounterInterface.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.BasicCounterInterface']['meta_info']


        class Ospfv3Protocol(object):
            """
            OSPF v3 Protocol collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv3Protocol.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.Ospfv3Protocol.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.Ospfv3Protocol.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.Ospfv3Protocol.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.Ospfv3Protocol']['meta_info']


        class CpuNode(object):
            """
            Node CPU collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.CpuNode.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.CpuNode.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.CpuNode.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.CpuNode.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.CpuNode.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.CpuNode']['meta_info']


        class DataRateInterface(object):
            """
            Interface DataRate collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.DataRateInterface.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.DataRateInterface.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.DataRateInterface.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.DataRateInterface.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.DataRateInterface.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.DataRateInterface']['meta_info']


        class MemoryNode(object):
            """
            Node Memory collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.MemoryNode.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.MemoryNode.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.MemoryNode.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.MemoryNode.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.MemoryNode.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.MemoryNode']['meta_info']


        class LdpMpls(object):
            """
            MPLS LDP collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.LdpMpls.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.LdpMpls.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.LdpMpls.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.LdpMpls.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.LdpMpls.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.LdpMpls']['meta_info']


        class Bgp(object):
            """
            BGP collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Bgp.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.Bgp.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Bgp.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.Bgp.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.Bgp.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.Bgp']['meta_info']


        class Ospfv2Protocol(object):
            """
            OSPF v2 Protocol collection templates
            
            .. attribute:: templates
            
            	Template name
            	**type**\:   :py:class:`Templates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv2Protocol.Templates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.templates = PerfMgmt.Statistics.Ospfv2Protocol.Templates()
                self.templates.parent = self


            class Templates(object):
                """
                Template name
                
                .. attribute:: template
                
                	A template instance
                	**type**\: list of    :py:class:`Template <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template = YList()
                    self.template.parent = self
                    self.template.name = 'template'


                class Template(object):
                    """
                    A template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: history_persistent
                    
                    	Enable persistent history statistics
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of each sample in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: sample_size
                    
                    	Number of samples to be taken
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    .. attribute:: vrf_group
                    
                    	VRF group configured in regular expression to be applied
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.history_persistent = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.sample_size = None
                        self.vrf_group = None

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.history_persistent is not None:
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.sample_size is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Statistics.Ospfv2Protocol.Templates.Template']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template is not None:
                        for child_ref in self.template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Statistics.Ospfv2Protocol.Templates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.templates is not None and self.templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Statistics.Ospfv2Protocol']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.basic_counter_interface is not None and self.basic_counter_interface._has_data():
                return True

            if self.bgp is not None and self.bgp._has_data():
                return True

            if self.cpu_node is not None and self.cpu_node._has_data():
                return True

            if self.data_rate_interface is not None and self.data_rate_interface._has_data():
                return True

            if self.generic_counter_interface is not None and self.generic_counter_interface._has_data():
                return True

            if self.ldp_mpls is not None and self.ldp_mpls._has_data():
                return True

            if self.memory_node is not None and self.memory_node._has_data():
                return True

            if self.ospfv2_protocol is not None and self.ospfv2_protocol._has_data():
                return True

            if self.ospfv3_protocol is not None and self.ospfv3_protocol._has_data():
                return True

            if self.process_node is not None and self.process_node._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
            return meta._meta_table['PerfMgmt.Statistics']['meta_info']


    class Enable(object):
        """
        Start data collection and/or threshold
        monitoring
        
        .. attribute:: monitor_enable
        
        	Start data collection for a monitored instance
        	**type**\:   :py:class:`MonitorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable>`
        
        .. attribute:: statistics
        
        	Start periodic collection using a defined a template
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics>`
        
        .. attribute:: threshold
        
        	Start threshold monitoring using a defined template
        	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.monitor_enable = PerfMgmt.Enable.MonitorEnable()
            self.monitor_enable.parent = self
            self.statistics = PerfMgmt.Enable.Statistics()
            self.statistics.parent = self
            self.threshold = PerfMgmt.Enable.Threshold()
            self.threshold.parent = self


        class Threshold(object):
            """
            Start threshold monitoring using a defined
            template
            
            .. attribute:: basic_counter_interface
            
            	Threshold monitoring for Interface basic\-counters
            	**type**\:   :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.BasicCounterInterface>`
            
            .. attribute:: bgp
            
            	Threshold monitoring for BGP
            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.Bgp>`
            
            .. attribute:: cpu_node
            
            	Threshold monitoring for CPU
            	**type**\:   :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode>`
            
            .. attribute:: data_rate_interface
            
            	Threshold monitoring for Interface  data\-rates
            	**type**\:   :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.DataRateInterface>`
            
            .. attribute:: generic_counter_interface
            
            	Threshold monitoring for Interface generic\-counters
            	**type**\:   :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.GenericCounterInterface>`
            
            .. attribute:: ldp_mpls
            
            	Threshold monitoring for LDP
            	**type**\:   :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.LdpMpls>`
            
            .. attribute:: memory_node
            
            	Threshold monitoring for memory
            	**type**\:   :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode>`
            
            .. attribute:: ospfv2_protocol
            
            	Threshold monitoring for OSPF v2 Protocol
            	**type**\:   :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.Ospfv2Protocol>`
            
            .. attribute:: ospfv3_protocol
            
            	Threshold monitoring for OSPF v3 Protocol
            	**type**\:   :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.Ospfv3Protocol>`
            
            .. attribute:: process_node
            
            	Threshold monitoring for process
            	**type**\:   :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.basic_counter_interface = PerfMgmt.Enable.Threshold.BasicCounterInterface()
                self.basic_counter_interface.parent = self
                self.bgp = PerfMgmt.Enable.Threshold.Bgp()
                self.bgp.parent = self
                self.cpu_node = PerfMgmt.Enable.Threshold.CpuNode()
                self.cpu_node.parent = self
                self.data_rate_interface = PerfMgmt.Enable.Threshold.DataRateInterface()
                self.data_rate_interface.parent = self
                self.generic_counter_interface = PerfMgmt.Enable.Threshold.GenericCounterInterface()
                self.generic_counter_interface.parent = self
                self.ldp_mpls = PerfMgmt.Enable.Threshold.LdpMpls()
                self.ldp_mpls.parent = self
                self.memory_node = PerfMgmt.Enable.Threshold.MemoryNode()
                self.memory_node.parent = self
                self.ospfv2_protocol = PerfMgmt.Enable.Threshold.Ospfv2Protocol()
                self.ospfv2_protocol.parent = self
                self.ospfv3_protocol = PerfMgmt.Enable.Threshold.Ospfv3Protocol()
                self.ospfv3_protocol.parent = self
                self.process_node = PerfMgmt.Enable.Threshold.ProcessNode()
                self.process_node.parent = self


            class Ospfv3Protocol(object):
                """
                Threshold monitoring for OSPF v3 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.Ospfv3Protocol']['meta_info']


            class Bgp(object):
                """
                Threshold monitoring for BGP
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.Bgp']['meta_info']


            class DataRateInterface(object):
                """
                Threshold monitoring for Interface  data\-rates
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.DataRateInterface']['meta_info']


            class Ospfv2Protocol(object):
                """
                Threshold monitoring for OSPF v2 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.Ospfv2Protocol']['meta_info']


            class MemoryNode(object):
                """
                Threshold monitoring for memory
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_all = PerfMgmt.Enable.Threshold.MemoryNode.NodeAll()
                    self.node_all.parent = self
                    self.nodes = PerfMgmt.Enable.Threshold.MemoryNode.Nodes()
                    self.nodes.parent = self


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.Threshold.MemoryNode.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Threshold.MemoryNode.Nodes']['meta_info']


                class NodeAll(object):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:node-all'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Threshold.MemoryNode.NodeAll']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.node_all is not None and self.node_all._has_data():
                        return True

                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.MemoryNode']['meta_info']


            class GenericCounterInterface(object):
                """
                Threshold monitoring for Interface
                generic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.GenericCounterInterface']['meta_info']


            class CpuNode(object):
                """
                Threshold monitoring for CPU
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_all = PerfMgmt.Enable.Threshold.CpuNode.NodeAll()
                    self.node_all.parent = self
                    self.nodes = PerfMgmt.Enable.Threshold.CpuNode.Nodes()
                    self.nodes.parent = self


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.Threshold.CpuNode.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Threshold.CpuNode.Nodes']['meta_info']


                class NodeAll(object):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:node-all'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Threshold.CpuNode.NodeAll']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.node_all is not None and self.node_all._has_data():
                        return True

                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.CpuNode']['meta_info']


            class LdpMpls(object):
                """
                Threshold monitoring for LDP
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.LdpMpls']['meta_info']


            class ProcessNode(object):
                """
                Threshold monitoring for process
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_all = PerfMgmt.Enable.Threshold.ProcessNode.NodeAll()
                    self.node_all.parent = self
                    self.nodes = PerfMgmt.Enable.Threshold.ProcessNode.Nodes()
                    self.nodes.parent = self


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.Threshold.ProcessNode.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Threshold.ProcessNode.Nodes']['meta_info']


                class NodeAll(object):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:node-all'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Threshold.ProcessNode.NodeAll']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.node_all is not None and self.node_all._has_data():
                        return True

                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.ProcessNode']['meta_info']


            class BasicCounterInterface(object):
                """
                Threshold monitoring for Interface
                basic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Threshold.BasicCounterInterface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.basic_counter_interface is not None and self.basic_counter_interface._has_data():
                    return True

                if self.bgp is not None and self.bgp._has_data():
                    return True

                if self.cpu_node is not None and self.cpu_node._has_data():
                    return True

                if self.data_rate_interface is not None and self.data_rate_interface._has_data():
                    return True

                if self.generic_counter_interface is not None and self.generic_counter_interface._has_data():
                    return True

                if self.ldp_mpls is not None and self.ldp_mpls._has_data():
                    return True

                if self.memory_node is not None and self.memory_node._has_data():
                    return True

                if self.ospfv2_protocol is not None and self.ospfv2_protocol._has_data():
                    return True

                if self.ospfv3_protocol is not None and self.ospfv3_protocol._has_data():
                    return True

                if self.process_node is not None and self.process_node._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Enable.Threshold']['meta_info']


        class Statistics(object):
            """
            Start periodic collection using a defined a
            template
            
            .. attribute:: basic_counter_interface
            
            	Statistics collection for basic\-counters
            	**type**\:   :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.BasicCounterInterface>`
            
            .. attribute:: bgp
            
            	Data collection for BGP
            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.Bgp>`
            
            .. attribute:: cpu_node
            
            	Collection for CPU
            	**type**\:   :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode>`
            
            .. attribute:: data_rate_interface
            
            	Statistics collection for generic\-counters
            	**type**\:   :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.DataRateInterface>`
            
            .. attribute:: generic_counter_interface
            
            	Statistics collection for generic\-counters
            	**type**\:   :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.GenericCounterInterface>`
            
            .. attribute:: ldp_mpls
            
            	Collection for labels distribution protocol
            	**type**\:   :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.LdpMpls>`
            
            .. attribute:: memory_node
            
            	Collection for memory
            	**type**\:   :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode>`
            
            .. attribute:: ospfv2_protocol
            
            	Data collection for OSPF v2 Protocol
            	**type**\:   :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.Ospfv2Protocol>`
            
            .. attribute:: ospfv3_protocol
            
            	Data collection for OSPF v3 Protocol
            	**type**\:   :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.Ospfv3Protocol>`
            
            .. attribute:: process_node
            
            	Collection for process
            	**type**\:   :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.basic_counter_interface = PerfMgmt.Enable.Statistics.BasicCounterInterface()
                self.basic_counter_interface.parent = self
                self.bgp = PerfMgmt.Enable.Statistics.Bgp()
                self.bgp.parent = self
                self.cpu_node = PerfMgmt.Enable.Statistics.CpuNode()
                self.cpu_node.parent = self
                self.data_rate_interface = PerfMgmt.Enable.Statistics.DataRateInterface()
                self.data_rate_interface.parent = self
                self.generic_counter_interface = PerfMgmt.Enable.Statistics.GenericCounterInterface()
                self.generic_counter_interface.parent = self
                self.ldp_mpls = PerfMgmt.Enable.Statistics.LdpMpls()
                self.ldp_mpls.parent = self
                self.memory_node = PerfMgmt.Enable.Statistics.MemoryNode()
                self.memory_node.parent = self
                self.ospfv2_protocol = PerfMgmt.Enable.Statistics.Ospfv2Protocol()
                self.ospfv2_protocol.parent = self
                self.ospfv3_protocol = PerfMgmt.Enable.Statistics.Ospfv3Protocol()
                self.ospfv3_protocol.parent = self
                self.process_node = PerfMgmt.Enable.Statistics.ProcessNode()
                self.process_node.parent = self


            class GenericCounterInterface(object):
                """
                Statistics collection for generic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.GenericCounterInterface']['meta_info']


            class Bgp(object):
                """
                Data collection for BGP
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.Bgp']['meta_info']


            class Ospfv2Protocol(object):
                """
                Data collection for OSPF v2 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.Ospfv2Protocol']['meta_info']


            class Ospfv3Protocol(object):
                """
                Data collection for OSPF v3 Protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.Ospfv3Protocol']['meta_info']


            class CpuNode(object):
                """
                Collection for CPU
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_all = PerfMgmt.Enable.Statistics.CpuNode.NodeAll()
                    self.node_all.parent = self
                    self.nodes = PerfMgmt.Enable.Statistics.CpuNode.Nodes()
                    self.nodes.parent = self


                class NodeAll(object):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:node-all'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Statistics.CpuNode.NodeAll']['meta_info']


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.Statistics.CpuNode.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Statistics.CpuNode.Nodes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.node_all is not None and self.node_all._has_data():
                        return True

                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.CpuNode']['meta_info']


            class BasicCounterInterface(object):
                """
                Statistics collection for basic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.BasicCounterInterface']['meta_info']


            class ProcessNode(object):
                """
                Collection for process
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_all = PerfMgmt.Enable.Statistics.ProcessNode.NodeAll()
                    self.node_all.parent = self
                    self.nodes = PerfMgmt.Enable.Statistics.ProcessNode.Nodes()
                    self.nodes.parent = self


                class NodeAll(object):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:node-all'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Statistics.ProcessNode.NodeAll']['meta_info']


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.Statistics.ProcessNode.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Statistics.ProcessNode.Nodes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.node_all is not None and self.node_all._has_data():
                        return True

                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.ProcessNode']['meta_info']


            class DataRateInterface(object):
                """
                Statistics collection for generic\-counters
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.DataRateInterface']['meta_info']


            class MemoryNode(object):
                """
                Collection for memory
                
                .. attribute:: node_all
                
                	All the the nodes
                	**type**\:   :py:class:`NodeAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode.NodeAll>`
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.node_all = PerfMgmt.Enable.Statistics.MemoryNode.NodeAll()
                    self.node_all.parent = self
                    self.nodes = PerfMgmt.Enable.Statistics.MemoryNode.Nodes()
                    self.nodes.parent = self


                class NodeAll(object):
                    """
                    All the the nodes
                    
                    .. attribute:: template_name
                    
                    	Template name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:node-all'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Statistics.MemoryNode.NodeAll']['meta_info']


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.Statistics.MemoryNode.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.Statistics.MemoryNode.Nodes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.node_all is not None and self.node_all._has_data():
                        return True

                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.MemoryNode']['meta_info']


            class LdpMpls(object):
                """
                Collection for labels distribution protocol
                
                .. attribute:: template_name
                
                	Template name
                	**type**\:  str
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.template_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.template_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.Statistics.LdpMpls']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:statistics'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.basic_counter_interface is not None and self.basic_counter_interface._has_data():
                    return True

                if self.bgp is not None and self.bgp._has_data():
                    return True

                if self.cpu_node is not None and self.cpu_node._has_data():
                    return True

                if self.data_rate_interface is not None and self.data_rate_interface._has_data():
                    return True

                if self.generic_counter_interface is not None and self.generic_counter_interface._has_data():
                    return True

                if self.ldp_mpls is not None and self.ldp_mpls._has_data():
                    return True

                if self.memory_node is not None and self.memory_node._has_data():
                    return True

                if self.ospfv2_protocol is not None and self.ospfv2_protocol._has_data():
                    return True

                if self.ospfv3_protocol is not None and self.ospfv3_protocol._has_data():
                    return True

                if self.process_node is not None and self.process_node._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Enable.Statistics']['meta_info']


        class MonitorEnable(object):
            """
            Start data collection for a monitored instance
            
            .. attribute:: basic_counters
            
            	Monitoring for basic\-counters
            	**type**\:   :py:class:`BasicCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.BasicCounters>`
            
            .. attribute:: bgp
            
            	Monitor BGP protocol
            	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Bgp>`
            
            .. attribute:: cpu
            
            	Collection for CPU
            	**type**\:   :py:class:`Cpu <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Cpu>`
            
            .. attribute:: data_rates
            
            	Monitoring for data\-rates
            	**type**\:   :py:class:`DataRates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.DataRates>`
            
            .. attribute:: generic_counters
            
            	Monitoring for generic\-counters
            	**type**\:   :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.GenericCounters>`
            
            .. attribute:: ldp_mpls
            
            	Monitoring for LDP
            	**type**\:   :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.LdpMpls>`
            
            .. attribute:: memory
            
            	Collection for memory
            	**type**\:   :py:class:`Memory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Memory>`
            
            .. attribute:: ospfv2_protocol
            
            	Monitor OSPF v2 Protocol
            	**type**\:   :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol>`
            
            .. attribute:: ospfv3_protocol
            
            	Monitor OSPF v3 Protocol
            	**type**\:   :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol>`
            
            .. attribute:: process
            
            	Collection for a single process
            	**type**\:   :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.basic_counters = PerfMgmt.Enable.MonitorEnable.BasicCounters()
                self.basic_counters.parent = self
                self.bgp = PerfMgmt.Enable.MonitorEnable.Bgp()
                self.bgp.parent = self
                self.cpu = PerfMgmt.Enable.MonitorEnable.Cpu()
                self.cpu.parent = self
                self.data_rates = PerfMgmt.Enable.MonitorEnable.DataRates()
                self.data_rates.parent = self
                self.generic_counters = PerfMgmt.Enable.MonitorEnable.GenericCounters()
                self.generic_counters.parent = self
                self.ldp_mpls = PerfMgmt.Enable.MonitorEnable.LdpMpls()
                self.ldp_mpls.parent = self
                self.memory = PerfMgmt.Enable.MonitorEnable.Memory()
                self.memory.parent = self
                self.ospfv2_protocol = PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol()
                self.ospfv2_protocol.parent = self
                self.ospfv3_protocol = PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol()
                self.ospfv3_protocol.parent = self
                self.process = PerfMgmt.Enable.MonitorEnable.Process()
                self.process.parent = self


            class LdpMpls(object):
                """
                Monitoring for LDP
                
                .. attribute:: sessions
                
                	LDP session specification
                	**type**\:   :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.sessions = PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions()
                    self.sessions.parent = self


                class Sessions(object):
                    """
                    LDP session specification
                    
                    .. attribute:: session
                    
                    	IP address of the LDP Session
                    	**type**\: list of    :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.session = YList()
                        self.session.parent = self
                        self.session.name = 'session'


                    class Session(object):
                        """
                        IP address of the LDP Session
                        
                        .. attribute:: session  <key>
                        
                        	IP address of the LDP Session
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.session = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.session is None:
                                raise YPYModelError('Key property session is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls/Cisco-IOS-XR-manageability-perfmgmt-cfg:sessions/Cisco-IOS-XR-manageability-perfmgmt-cfg:session[Cisco-IOS-XR-manageability-perfmgmt-cfg:session = ' + str(self.session) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.session is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions.Session']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls/Cisco-IOS-XR-manageability-perfmgmt-cfg:sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.session is not None:
                            for child_ref in self.session:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls.Sessions']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.sessions is not None and self.sessions._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.LdpMpls']['meta_info']


            class Ospfv3Protocol(object):
                """
                Monitor OSPF v3 Protocol
                
                .. attribute:: ospf_instances
                
                	Monitor an instance
                	**type**\:   :py:class:`OspfInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ospf_instances = PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances()
                    self.ospf_instances.parent = self


                class OspfInstances(object):
                    """
                    Monitor an instance
                    
                    .. attribute:: ospf_instance
                    
                    	Instance being monitored
                    	**type**\: list of    :py:class:`OspfInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ospf_instance = YList()
                        self.ospf_instance.parent = self
                        self.ospf_instance.name = 'ospf_instance'


                    class OspfInstance(object):
                        """
                        Instance being monitored
                        
                        .. attribute:: instance_name  <key>
                        
                        	OSPF Instance Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.instance_name = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.instance_name is None:
                                raise YPYModelError('Key property instance_name is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospf-instances/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospf-instance[Cisco-IOS-XR-manageability-perfmgmt-cfg:instance-name = ' + str(self.instance_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.instance_name is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances.OspfInstance']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospf-instances'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ospf_instance is not None:
                            for child_ref in self.ospf_instance:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol.OspfInstances']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ospf_instances is not None and self.ospf_instances._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv3Protocol']['meta_info']


            class GenericCounters(object):
                """
                Monitoring for generic\-counters
                
                .. attribute:: interfaces
                
                	Monitor an Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interfaces = PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces()
                    self.interfaces.parent = self


                class Interfaces(object):
                    """
                    Monitor an Interface
                    
                    .. attribute:: interface
                    
                    	Interface being Monitored
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        Interface being Monitored
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counters/Cisco-IOS-XR-manageability-perfmgmt-cfg:interfaces/Cisco-IOS-XR-manageability-perfmgmt-cfg:interface[Cisco-IOS-XR-manageability-perfmgmt-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counters/Cisco-IOS-XR-manageability-perfmgmt-cfg:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters.Interfaces']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.GenericCounters']['meta_info']


            class Process(object):
                """
                Collection for a single process
                
                .. attribute:: process_nodes
                
                	Node specification
                	**type**\:   :py:class:`ProcessNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.process_nodes = PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes()
                    self.process_nodes.parent = self


                class ProcessNodes(object):
                    """
                    Node specification
                    
                    .. attribute:: process_node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.process_node = YList()
                        self.process_node.parent = self
                        self.process_node.name = 'process_node'


                    class ProcessNode(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: pids
                        
                        	Process ID specification
                        	**type**\:   :py:class:`Pids <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids>`
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.pids = PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids()
                            self.pids.parent = self


                        class Pids(object):
                            """
                            Process ID specification
                            
                            .. attribute:: pid
                            
                            	Specify an existing template for data collection
                            	**type**\: list of    :py:class:`Pid <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid>`
                            
                            

                            """

                            _prefix = 'manageability-perfmgmt-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pid = YList()
                                self.pid.parent = self
                                self.pid.name = 'pid'


                            class Pid(object):
                                """
                                Specify an existing template for data
                                collection
                                
                                .. attribute:: pid  <key>
                                
                                	Specify Process ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: template_name
                                
                                	Template name
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'manageability-perfmgmt-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.pid = None
                                    self.template_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.pid is None:
                                        raise YPYModelError('Key property pid is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:pid[Cisco-IOS-XR-manageability-perfmgmt-cfg:pid = ' + str(self.pid) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.pid is not None:
                                        return True

                                    if self.template_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids.Pid']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:pids'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.pid is not None:
                                    for child_ref in self.pid:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                                return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode.Pids']['meta_info']

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:process/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.pids is not None and self.pids._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes.ProcessNode']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:process/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.process_node is not None:
                            for child_ref in self.process_node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Process.ProcessNodes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:process'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.process_nodes is not None and self.process_nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Process']['meta_info']


            class BasicCounters(object):
                """
                Monitoring for basic\-counters
                
                .. attribute:: interfaces
                
                	Monitor an Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interfaces = PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces()
                    self.interfaces.parent = self


                class Interfaces(object):
                    """
                    Monitor an Interface
                    
                    .. attribute:: interface
                    
                    	Interface being Monitored
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        Interface being Monitored
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counters/Cisco-IOS-XR-manageability-perfmgmt-cfg:interfaces/Cisco-IOS-XR-manageability-perfmgmt-cfg:interface[Cisco-IOS-XR-manageability-perfmgmt-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counters/Cisco-IOS-XR-manageability-perfmgmt-cfg:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters.Interfaces']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.BasicCounters']['meta_info']


            class Memory(object):
                """
                Collection for memory
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Memory.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nodes = PerfMgmt.Enable.MonitorEnable.Memory.Nodes()
                    self.nodes.parent = self


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Memory.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Memory.Nodes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Memory']['meta_info']


            class Ospfv2Protocol(object):
                """
                Monitor OSPF v2 Protocol
                
                .. attribute:: ospf_instances
                
                	Monitor an instance
                	**type**\:   :py:class:`OspfInstances <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ospf_instances = PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances()
                    self.ospf_instances.parent = self


                class OspfInstances(object):
                    """
                    Monitor an instance
                    
                    .. attribute:: ospf_instance
                    
                    	Instance being monitored
                    	**type**\: list of    :py:class:`OspfInstance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.ospf_instance = YList()
                        self.ospf_instance.parent = self
                        self.ospf_instance.name = 'ospf_instance'


                    class OspfInstance(object):
                        """
                        Instance being monitored
                        
                        .. attribute:: instance_name  <key>
                        
                        	OSPF Instance Name
                        	**type**\:  str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.instance_name = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.instance_name is None:
                                raise YPYModelError('Key property instance_name is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospf-instances/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospf-instance[Cisco-IOS-XR-manageability-perfmgmt-cfg:instance-name = ' + str(self.instance_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.instance_name is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances.OspfInstance']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospf-instances'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ospf_instance is not None:
                            for child_ref in self.ospf_instance:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol.OspfInstances']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ospf_instances is not None and self.ospf_instances._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Ospfv2Protocol']['meta_info']


            class Cpu(object):
                """
                Collection for CPU
                
                .. attribute:: nodes
                
                	Node specification
                	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Cpu.Nodes>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.nodes = PerfMgmt.Enable.MonitorEnable.Cpu.Nodes()
                    self.nodes.parent = self


                class Nodes(object):
                    """
                    Node specification
                    
                    .. attribute:: node
                    
                    	Node instance
                    	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.node = YList()
                        self.node.parent = self
                        self.node.name = 'node'


                    class Node(object):
                        """
                        Node instance
                        
                        .. attribute:: node_id  <key>
                        
                        	Node ID
                        	**type**\:  str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.node_id = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.node_id is None:
                                raise YPYModelError('Key property node_id is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes/Cisco-IOS-XR-manageability-perfmgmt-cfg:node[Cisco-IOS-XR-manageability-perfmgmt-cfg:node-id = ' + str(self.node_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.node_id is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Cpu.Nodes.Node']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu/Cisco-IOS-XR-manageability-perfmgmt-cfg:nodes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.node is not None:
                            for child_ref in self.node:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Cpu.Nodes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.nodes is not None and self.nodes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Cpu']['meta_info']


            class Bgp(object):
                """
                Monitor BGP protocol
                
                .. attribute:: neighbors
                
                	Monitor BGP protocol for a BGP peer
                	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.neighbors = PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors()
                    self.neighbors.parent = self


                class Neighbors(object):
                    """
                    Monitor BGP protocol for a BGP peer
                    
                    .. attribute:: neighbor
                    
                    	Neighbor being monitored
                    	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.neighbor = YList()
                        self.neighbor.parent = self
                        self.neighbor.name = 'neighbor'


                    class Neighbor(object):
                        """
                        Neighbor being monitored
                        
                        .. attribute:: peer_address  <key>
                        
                        	IP address of the Neighbor
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.peer_address = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.peer_address is None:
                                raise YPYModelError('Key property peer_address is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp/Cisco-IOS-XR-manageability-perfmgmt-cfg:neighbors/Cisco-IOS-XR-manageability-perfmgmt-cfg:neighbor[Cisco-IOS-XR-manageability-perfmgmt-cfg:peer-address = ' + str(self.peer_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.peer_address is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors.Neighbor']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp/Cisco-IOS-XR-manageability-perfmgmt-cfg:neighbors'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.neighbor is not None:
                            for child_ref in self.neighbor:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Bgp.Neighbors']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.neighbors is not None and self.neighbors._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.Bgp']['meta_info']


            class DataRates(object):
                """
                Monitoring for data\-rates
                
                .. attribute:: interfaces
                
                	Monitor an Interface
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interfaces = PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces()
                    self.interfaces.parent = self


                class Interfaces(object):
                    """
                    Monitor an Interface
                    
                    .. attribute:: interface
                    
                    	Interface being Monitored
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        Interface being Monitored
                        
                        .. attribute:: interface_name  <key>
                        
                        	Interface Name
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: template_name
                        
                        	Template name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.template_name = None

                        @property
                        def _common_path(self):
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rates/Cisco-IOS-XR-manageability-perfmgmt-cfg:interfaces/Cisco-IOS-XR-manageability-perfmgmt-cfg:interface[Cisco-IOS-XR-manageability-perfmgmt-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.template_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rates/Cisco-IOS-XR-manageability-perfmgmt-cfg:interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface is not None:
                            for child_ref in self.interface:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Enable.MonitorEnable.DataRates.Interfaces']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Enable.MonitorEnable.DataRates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable/Cisco-IOS-XR-manageability-perfmgmt-cfg:monitor-enable'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.basic_counters is not None and self.basic_counters._has_data():
                    return True

                if self.bgp is not None and self.bgp._has_data():
                    return True

                if self.cpu is not None and self.cpu._has_data():
                    return True

                if self.data_rates is not None and self.data_rates._has_data():
                    return True

                if self.generic_counters is not None and self.generic_counters._has_data():
                    return True

                if self.ldp_mpls is not None and self.ldp_mpls._has_data():
                    return True

                if self.memory is not None and self.memory._has_data():
                    return True

                if self.ospfv2_protocol is not None and self.ospfv2_protocol._has_data():
                    return True

                if self.ospfv3_protocol is not None and self.ospfv3_protocol._has_data():
                    return True

                if self.process is not None and self.process._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Enable.MonitorEnable']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:enable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.monitor_enable is not None and self.monitor_enable._has_data():
                return True

            if self.statistics is not None and self.statistics._has_data():
                return True

            if self.threshold is not None and self.threshold._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
            return meta._meta_table['PerfMgmt.Enable']['meta_info']


    class RegExpGroups(object):
        """
        Configure regular expression group
        
        .. attribute:: reg_exp_group
        
        	Specify regular expression group name
        	**type**\: list of    :py:class:`RegExpGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups.RegExpGroup>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.reg_exp_group = YList()
            self.reg_exp_group.parent = self
            self.reg_exp_group.name = 'reg_exp_group'


        class RegExpGroup(object):
            """
            Specify regular expression group name
            
            .. attribute:: reg_exp_group_name  <key>
            
            	Regular expression group name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: reg_exps
            
            	Configure regular expression
            	**type**\:   :py:class:`RegExps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups.RegExpGroup.RegExps>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.reg_exp_group_name = None
                self.reg_exps = PerfMgmt.RegExpGroups.RegExpGroup.RegExps()
                self.reg_exps.parent = self


            class RegExps(object):
                """
                Configure regular expression
                
                .. attribute:: reg_exp
                
                	Specify regular expression index number
                	**type**\: list of    :py:class:`RegExp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.reg_exp = YList()
                    self.reg_exp.parent = self
                    self.reg_exp.name = 'reg_exp'


                class RegExp(object):
                    """
                    Specify regular expression index number
                    
                    .. attribute:: reg_exp_index  <key>
                    
                    	Regular expression index number
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: reg_exp_string
                    
                    	Regular expression string to match
                    	**type**\:  str
                    
                    	**length:** 1..128
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.reg_exp_index = None
                        self.reg_exp_string = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.reg_exp_index is None:
                            raise YPYModelError('Key property reg_exp_index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exp[Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exp-index = ' + str(self.reg_exp_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.reg_exp_index is not None:
                            return True

                        if self.reg_exp_string is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.RegExpGroups.RegExpGroup.RegExps.RegExp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.reg_exp is not None:
                        for child_ref in self.reg_exp:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.RegExpGroups.RegExpGroup.RegExps']['meta_info']

            @property
            def _common_path(self):
                if self.reg_exp_group_name is None:
                    raise YPYModelError('Key property reg_exp_group_name is None')

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exp-groups/Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exp-group[Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exp-group-name = ' + str(self.reg_exp_group_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.reg_exp_group_name is not None:
                    return True

                if self.reg_exps is not None and self.reg_exps._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.RegExpGroups.RegExpGroup']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:reg-exp-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.reg_exp_group is not None:
                for child_ref in self.reg_exp_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
            return meta._meta_table['PerfMgmt.RegExpGroups']['meta_info']


    class Threshold(object):
        """
        Container for threshold templates
        
        .. attribute:: basic_counter_interface
        
        	Interface Basic Counter threshold configuration
        	**type**\:   :py:class:`BasicCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface>`
        
        .. attribute:: bgp
        
        	BGP threshold configuration
        	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp>`
        
        .. attribute:: cpu_node
        
        	Node CPU threshold configuration
        	**type**\:   :py:class:`CpuNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode>`
        
        .. attribute:: data_rate_interface
        
        	Interface Data Rates threshold configuration
        	**type**\:   :py:class:`DataRateInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface>`
        
        .. attribute:: generic_counter_interface
        
        	Interface Generic Counter threshold configuration
        	**type**\:   :py:class:`GenericCounterInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface>`
        
        .. attribute:: ldp_mpls
        
        	MPLS LDP threshold configuration
        	**type**\:   :py:class:`LdpMpls <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls>`
        
        .. attribute:: memory_node
        
        	Node Memory threshold configuration
        	**type**\:   :py:class:`MemoryNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode>`
        
        .. attribute:: ospfv2_protocol
        
        	OSPF v2 Protocol threshold configuration
        	**type**\:   :py:class:`Ospfv2Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol>`
        
        .. attribute:: ospfv3_protocol
        
        	OSPF v2 Protocol threshold configuration
        	**type**\:   :py:class:`Ospfv3Protocol <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol>`
        
        .. attribute:: process_node
        
        	Node Process threshold configuration
        	**type**\:   :py:class:`ProcessNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode>`
        
        

        """

        _prefix = 'manageability-perfmgmt-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.basic_counter_interface = PerfMgmt.Threshold.BasicCounterInterface()
            self.basic_counter_interface.parent = self
            self.bgp = PerfMgmt.Threshold.Bgp()
            self.bgp.parent = self
            self.cpu_node = PerfMgmt.Threshold.CpuNode()
            self.cpu_node.parent = self
            self.data_rate_interface = PerfMgmt.Threshold.DataRateInterface()
            self.data_rate_interface.parent = self
            self.generic_counter_interface = PerfMgmt.Threshold.GenericCounterInterface()
            self.generic_counter_interface.parent = self
            self.ldp_mpls = PerfMgmt.Threshold.LdpMpls()
            self.ldp_mpls.parent = self
            self.memory_node = PerfMgmt.Threshold.MemoryNode()
            self.memory_node.parent = self
            self.ospfv2_protocol = PerfMgmt.Threshold.Ospfv2Protocol()
            self.ospfv2_protocol.parent = self
            self.ospfv3_protocol = PerfMgmt.Threshold.Ospfv3Protocol()
            self.ospfv3_protocol.parent = self
            self.process_node = PerfMgmt.Threshold.ProcessNode()
            self.process_node.parent = self


        class GenericCounterInterface(object):
            """
            Interface Generic Counter threshold
            configuration
            
            .. attribute:: generic_counter_interface_templates
            
            	Interface Generic Counter threshold templates
            	**type**\:   :py:class:`GenericCounterInterfaceTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.generic_counter_interface_templates = PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates()
                self.generic_counter_interface_templates.parent = self


            class GenericCounterInterfaceTemplates(object):
                """
                Interface Generic Counter threshold templates
                
                .. attribute:: generic_counter_interface_template
                
                	Interface Generic Counter threshold template instance
                	**type**\: list of    :py:class:`GenericCounterInterfaceTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.generic_counter_interface_template = YList()
                    self.generic_counter_interface_template.parent = self
                    self.generic_counter_interface_template.name = 'generic_counter_interface_template'


                class GenericCounterInterfaceTemplate(object):
                    """
                    Interface Generic Counter threshold template
                    instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: in_broadcast_pkts
                    
                    	Number of inbound broadcast packets
                    	**type**\:   :py:class:`InBroadcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_multicast_pkts
                    
                    	Number of inbound multicast packets
                    	**type**\:   :py:class:`InMulticastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_octets
                    
                    	Number of inbound octets/bytes
                    	**type**\:   :py:class:`InOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_packets
                    
                    	Number of inbound packets
                    	**type**\:   :py:class:`InPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_ucast_pkts
                    
                    	Number of inbound unicast packets
                    	**type**\:   :py:class:`InUcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_crc
                    
                    	Number of inbound packets discarded with incorrect CRC
                    	**type**\:   :py:class:`InputCrc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_frame
                    
                    	Number of inbound packets with framing errors
                    	**type**\:   :py:class:`InputFrame <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_overrun
                    
                    	Number of inbound packets with overrun errors
                    	**type**\:   :py:class:`InputOverrun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_queue_drops
                    
                    	Number of input queue drops
                    	**type**\:   :py:class:`InputQueueDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_drops
                    
                    	Number of inbound correct packets discarded
                    	**type**\:   :py:class:`InputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_errors
                    
                    	Number of inbound incorrect packets discarded
                    	**type**\:   :py:class:`InputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_unknown_proto
                    
                    	Number of inbound packets discarded with unknown protocol
                    	**type**\:   :py:class:`InputUnknownProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_broadcast_pkts
                    
                    	Number of outbound broadcast packets
                    	**type**\:   :py:class:`OutBroadcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_multicast_pkts
                    
                    	Number of outbound multicast packets
                    	**type**\:   :py:class:`OutMulticastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_octets
                    
                    	Number of outbound octets/bytes
                    	**type**\:   :py:class:`OutOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_packets
                    
                    	Number of outbound packets
                    	**type**\:   :py:class:`OutPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_ucast_pkts
                    
                    	Number of outbound unicast packets
                    	**type**\:   :py:class:`OutUcastPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_drops
                    
                    	Number of outbound correct packets discarded
                    	**type**\:   :py:class:`OutputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_errors
                    
                    	Number of outbound incorrect packets discarded
                    	**type**\:   :py:class:`OutputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_underrun
                    
                    	Number of outbound packets with underrun errors
                    	**type**\:   :py:class:`OutputUnderrun <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: vrf_group
                    
                    	Enable instance filtering by VRF name regular expression 
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
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
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.vrf_group = None


                    class InOctets(object):
                        """
                        Number of inbound octets/bytes
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-octets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InOctets']['meta_info']


                    class InUcastPkts(object):
                        """
                        Number of inbound unicast packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-ucast-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InUcastPkts']['meta_info']


                    class OutUcastPkts(object):
                        """
                        Number of outbound unicast packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-ucast-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutUcastPkts']['meta_info']


                    class OutBroadcastPkts(object):
                        """
                        Number of outbound broadcast packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-broadcast-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutBroadcastPkts']['meta_info']


                    class OutMulticastPkts(object):
                        """
                        Number of outbound multicast packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-multicast-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutMulticastPkts']['meta_info']


                    class InputOverrun(object):
                        """
                        Number of inbound packets with overrun
                        errors
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-overrun'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputOverrun']['meta_info']


                    class OutOctets(object):
                        """
                        Number of outbound octets/bytes
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-octets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutOctets']['meta_info']


                    class OutputUnderrun(object):
                        """
                        Number of outbound packets with underrun
                        errors
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-underrun'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputUnderrun']['meta_info']


                    class InputTotalErrors(object):
                        """
                        Number of inbound incorrect packets
                        discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-total-errors'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalErrors']['meta_info']


                    class OutputTotalDrops(object):
                        """
                        Number of outbound correct packets discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-total-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalDrops']['meta_info']


                    class InputCrc(object):
                        """
                        Number of inbound packets discarded with
                        incorrect CRC
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-crc'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputCrc']['meta_info']


                    class InBroadcastPkts(object):
                        """
                        Number of inbound broadcast packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-broadcast-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InBroadcastPkts']['meta_info']


                    class InMulticastPkts(object):
                        """
                        Number of inbound multicast packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-multicast-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InMulticastPkts']['meta_info']


                    class OutPackets(object):
                        """
                        Number of outbound packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutPackets']['meta_info']


                    class OutputTotalErrors(object):
                        """
                        Number of outbound incorrect packets
                        discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-total-errors'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.OutputTotalErrors']['meta_info']


                    class InPackets(object):
                        """
                        Number of inbound packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InPackets']['meta_info']


                    class InputUnknownProto(object):
                        """
                        Number of inbound packets discarded with
                        unknown protocol
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-unknown-proto'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputUnknownProto']['meta_info']


                    class InputQueueDrops(object):
                        """
                        Number of input queue drops
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-queue-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputQueueDrops']['meta_info']


                    class InputTotalDrops(object):
                        """
                        Number of inbound correct packets discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-total-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputTotalDrops']['meta_info']


                    class InputFrame(object):
                        """
                        Number of inbound packets with framing
                        errors
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-frame'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate.InputFrame']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.in_broadcast_pkts is not None and self.in_broadcast_pkts._has_data():
                            return True

                        if self.in_multicast_pkts is not None and self.in_multicast_pkts._has_data():
                            return True

                        if self.in_octets is not None and self.in_octets._has_data():
                            return True

                        if self.in_packets is not None and self.in_packets._has_data():
                            return True

                        if self.in_ucast_pkts is not None and self.in_ucast_pkts._has_data():
                            return True

                        if self.input_crc is not None and self.input_crc._has_data():
                            return True

                        if self.input_frame is not None and self.input_frame._has_data():
                            return True

                        if self.input_overrun is not None and self.input_overrun._has_data():
                            return True

                        if self.input_queue_drops is not None and self.input_queue_drops._has_data():
                            return True

                        if self.input_total_drops is not None and self.input_total_drops._has_data():
                            return True

                        if self.input_total_errors is not None and self.input_total_errors._has_data():
                            return True

                        if self.input_unknown_proto is not None and self.input_unknown_proto._has_data():
                            return True

                        if self.out_broadcast_pkts is not None and self.out_broadcast_pkts._has_data():
                            return True

                        if self.out_multicast_pkts is not None and self.out_multicast_pkts._has_data():
                            return True

                        if self.out_octets is not None and self.out_octets._has_data():
                            return True

                        if self.out_packets is not None and self.out_packets._has_data():
                            return True

                        if self.out_ucast_pkts is not None and self.out_ucast_pkts._has_data():
                            return True

                        if self.output_total_drops is not None and self.output_total_drops._has_data():
                            return True

                        if self.output_total_errors is not None and self.output_total_errors._has_data():
                            return True

                        if self.output_underrun is not None and self.output_underrun._has_data():
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates.GenericCounterInterfaceTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.generic_counter_interface_template is not None:
                        for child_ref in self.generic_counter_interface_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface.GenericCounterInterfaceTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:generic-counter-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.generic_counter_interface_templates is not None and self.generic_counter_interface_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.GenericCounterInterface']['meta_info']


        class LdpMpls(object):
            """
            MPLS LDP threshold configuration
            
            .. attribute:: ldp_mpls_templates
            
            	MPLS LDP threshold templates
            	**type**\:   :py:class:`LdpMplsTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ldp_mpls_templates = PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates()
                self.ldp_mpls_templates.parent = self


            class LdpMplsTemplates(object):
                """
                MPLS LDP threshold templates
                
                .. attribute:: ldp_mpls_template
                
                	MPLS LDP threshold template instance
                	**type**\: list of    :py:class:`LdpMplsTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ldp_mpls_template = YList()
                    self.ldp_mpls_template.parent = self
                    self.ldp_mpls_template.name = 'ldp_mpls_template'


                class LdpMplsTemplate(object):
                    """
                    MPLS LDP threshold template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: address_msgs_rcvd
                    
                    	Number of Address messages received
                    	**type**\:   :py:class:`AddressMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: address_msgs_sent
                    
                    	Number of Address messages sent
                    	**type**\:   :py:class:`AddressMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: address_withdraw_msgs_rcvd
                    
                    	Number of Address Withdraw messages received
                    	**type**\:   :py:class:`AddressWithdrawMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: address_withdraw_msgs_sent
                    
                    	Number of Address Withdraw messages sent
                    	**type**\:   :py:class:`AddressWithdrawMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: init_msgs_rcvd
                    
                    	Number of Init messages received
                    	**type**\:   :py:class:`InitMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: init_msgs_sent
                    
                    	Number of Init messages sent
                    	**type**\:   :py:class:`InitMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: keepalive_msgs_rcvd
                    
                    	Number of Keepalive messages received
                    	**type**\:   :py:class:`KeepaliveMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: keepalive_msgs_sent
                    
                    	Number of Keepalive messages sent
                    	**type**\:   :py:class:`KeepaliveMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_mapping_msgs_rcvd
                    
                    	Number of Label Mapping messages received
                    	**type**\:   :py:class:`LabelMappingMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_mapping_msgs_sent
                    
                    	Number of Label Mapping messages sent
                    	**type**\:   :py:class:`LabelMappingMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_release_msgs_rcvd
                    
                    	Number of LAbel Release messages received
                    	**type**\:   :py:class:`LabelReleaseMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_release_msgs_sent
                    
                    	Number of Label Release messages sent
                    	**type**\:   :py:class:`LabelReleaseMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_withdraw_msgs_rcvd
                    
                    	Number of Label Withdraw messages received
                    	**type**\:   :py:class:`LabelWithdrawMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: label_withdraw_msgs_sent
                    
                    	Number of Label Withdraw messages sent
                    	**type**\:   :py:class:`LabelWithdrawMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: notification_msgs_rcvd
                    
                    	Number of Notification messages received
                    	**type**\:   :py:class:`NotificationMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: notification_msgs_sent
                    
                    	Number of Notification messages sent
                    	**type**\:   :py:class:`NotificationMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: total_msgs_rcvd
                    
                    	Total number of messages received
                    	**type**\:   :py:class:`TotalMsgsRcvd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: total_msgs_sent
                    
                    	Total number of messages sent
                    	**type**\:   :py:class:`TotalMsgsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
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
                        self.sample_interval = None
                        self.total_msgs_rcvd = None
                        self.total_msgs_sent = None


                    class AddressWithdrawMsgsRcvd(object):
                        """
                        Number of Address Withdraw messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:address-withdraw-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsRcvd']['meta_info']


                    class LabelWithdrawMsgsRcvd(object):
                        """
                        Number of Label Withdraw messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:label-withdraw-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsRcvd']['meta_info']


                    class AddressWithdrawMsgsSent(object):
                        """
                        Number of Address Withdraw messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:address-withdraw-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressWithdrawMsgsSent']['meta_info']


                    class LabelWithdrawMsgsSent(object):
                        """
                        Number of Label Withdraw messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:label-withdraw-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelWithdrawMsgsSent']['meta_info']


                    class NotificationMsgsRcvd(object):
                        """
                        Number of Notification messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:notification-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsRcvd']['meta_info']


                    class TotalMsgsRcvd(object):
                        """
                        Total number of messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..65536
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..65536
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:total-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsRcvd']['meta_info']


                    class NotificationMsgsSent(object):
                        """
                        Number of Notification messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:notification-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.NotificationMsgsSent']['meta_info']


                    class TotalMsgsSent(object):
                        """
                        Total number of messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:total-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.TotalMsgsSent']['meta_info']


                    class LabelReleaseMsgsRcvd(object):
                        """
                        Number of LAbel Release messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:label-release-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsRcvd']['meta_info']


                    class InitMsgsRcvd(object):
                        """
                        Number of Init messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:init-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsRcvd']['meta_info']


                    class LabelReleaseMsgsSent(object):
                        """
                        Number of Label Release messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:label-release-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelReleaseMsgsSent']['meta_info']


                    class InitMsgsSent(object):
                        """
                        Number of Init messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:init-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.InitMsgsSent']['meta_info']


                    class LabelMappingMsgsRcvd(object):
                        """
                        Number of Label Mapping messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:label-mapping-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsRcvd']['meta_info']


                    class KeepaliveMsgsRcvd(object):
                        """
                        Number of Keepalive messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:keepalive-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsRcvd']['meta_info']


                    class LabelMappingMsgsSent(object):
                        """
                        Number of Label Mapping messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:label-mapping-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.LabelMappingMsgsSent']['meta_info']


                    class KeepaliveMsgsSent(object):
                        """
                        Number of Keepalive messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:keepalive-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.KeepaliveMsgsSent']['meta_info']


                    class AddressMsgsRcvd(object):
                        """
                        Number of Address messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:address-msgs-rcvd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsRcvd']['meta_info']


                    class AddressMsgsSent(object):
                        """
                        Number of Address messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:address-msgs-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate.AddressMsgsSent']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.address_msgs_rcvd is not None and self.address_msgs_rcvd._has_data():
                            return True

                        if self.address_msgs_sent is not None and self.address_msgs_sent._has_data():
                            return True

                        if self.address_withdraw_msgs_rcvd is not None and self.address_withdraw_msgs_rcvd._has_data():
                            return True

                        if self.address_withdraw_msgs_sent is not None and self.address_withdraw_msgs_sent._has_data():
                            return True

                        if self.init_msgs_rcvd is not None and self.init_msgs_rcvd._has_data():
                            return True

                        if self.init_msgs_sent is not None and self.init_msgs_sent._has_data():
                            return True

                        if self.keepalive_msgs_rcvd is not None and self.keepalive_msgs_rcvd._has_data():
                            return True

                        if self.keepalive_msgs_sent is not None and self.keepalive_msgs_sent._has_data():
                            return True

                        if self.label_mapping_msgs_rcvd is not None and self.label_mapping_msgs_rcvd._has_data():
                            return True

                        if self.label_mapping_msgs_sent is not None and self.label_mapping_msgs_sent._has_data():
                            return True

                        if self.label_release_msgs_rcvd is not None and self.label_release_msgs_rcvd._has_data():
                            return True

                        if self.label_release_msgs_sent is not None and self.label_release_msgs_sent._has_data():
                            return True

                        if self.label_withdraw_msgs_rcvd is not None and self.label_withdraw_msgs_rcvd._has_data():
                            return True

                        if self.label_withdraw_msgs_sent is not None and self.label_withdraw_msgs_sent._has_data():
                            return True

                        if self.notification_msgs_rcvd is not None and self.notification_msgs_rcvd._has_data():
                            return True

                        if self.notification_msgs_sent is not None and self.notification_msgs_sent._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.total_msgs_rcvd is not None and self.total_msgs_rcvd._has_data():
                            return True

                        if self.total_msgs_sent is not None and self.total_msgs_sent._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates.LdpMplsTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ldp_mpls_template is not None:
                        for child_ref in self.ldp_mpls_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.LdpMpls.LdpMplsTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ldp-mpls'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ldp_mpls_templates is not None and self.ldp_mpls_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.LdpMpls']['meta_info']


        class BasicCounterInterface(object):
            """
            Interface Basic Counter threshold configuration
            
            .. attribute:: basic_counter_interface_templates
            
            	Interface Basic Counter threshold templates
            	**type**\:   :py:class:`BasicCounterInterfaceTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.basic_counter_interface_templates = PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates()
                self.basic_counter_interface_templates.parent = self


            class BasicCounterInterfaceTemplates(object):
                """
                Interface Basic Counter threshold templates
                
                .. attribute:: basic_counter_interface_template
                
                	Interface Basic Counter threshold template instance
                	**type**\: list of    :py:class:`BasicCounterInterfaceTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.basic_counter_interface_template = YList()
                    self.basic_counter_interface_template.parent = self
                    self.basic_counter_interface_template.name = 'basic_counter_interface_template'


                class BasicCounterInterfaceTemplate(object):
                    """
                    Interface Basic Counter threshold template
                    instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: in_octets
                    
                    	Number of inbound octets/bytes
                    	**type**\:   :py:class:`InOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: in_packets
                    
                    	Number of inbound packets
                    	**type**\:   :py:class:`InPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_queue_drops
                    
                    	Number of input queue drops
                    	**type**\:   :py:class:`InputQueueDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_drops
                    
                    	Number of inbound correct packets discarded
                    	**type**\:   :py:class:`InputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_total_errors
                    
                    	Number of inbound incorrect packets discarded
                    	**type**\:   :py:class:`InputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_octets
                    
                    	Number of outbound octets/bytes
                    	**type**\:   :py:class:`OutOctets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: out_packets
                    
                    	Number of outbound packets
                    	**type**\:   :py:class:`OutPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_queue_drops
                    
                    	Number of outbound queue drops
                    	**type**\:   :py:class:`OutputQueueDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_drops
                    
                    	Number of outbound correct packets discarded
                    	**type**\:   :py:class:`OutputTotalDrops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_total_errors
                    
                    	Number of outbound incorrect packets discarded
                    	**type**\:   :py:class:`OutputTotalErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: vrf_group
                    
                    	Enable instance filtering by VRF name regular expression 
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
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
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.vrf_group = None


                    class InOctets(object):
                        """
                        Number of inbound octets/bytes
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-octets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InOctets']['meta_info']


                    class OutOctets(object):
                        """
                        Number of outbound octets/bytes
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-octets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutOctets']['meta_info']


                    class OutputQueueDrops(object):
                        """
                        Number of outbound queue drops
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-queue-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputQueueDrops']['meta_info']


                    class InputTotalErrors(object):
                        """
                        Number of inbound incorrect packets
                        discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-total-errors'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalErrors']['meta_info']


                    class OutputTotalDrops(object):
                        """
                        Number of outbound correct packets discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-total-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalDrops']['meta_info']


                    class OutPackets(object):
                        """
                        Number of outbound packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:out-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutPackets']['meta_info']


                    class OutputTotalErrors(object):
                        """
                        Number of outbound incorrect packets
                        discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-total-errors'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.OutputTotalErrors']['meta_info']


                    class InPackets(object):
                        """
                        Number of inbound packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:in-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InPackets']['meta_info']


                    class InputQueueDrops(object):
                        """
                        Number of input queue drops
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-queue-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputQueueDrops']['meta_info']


                    class InputTotalDrops(object):
                        """
                        Number of inbound correct packets discarded
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-total-drops'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate.InputTotalDrops']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.in_octets is not None and self.in_octets._has_data():
                            return True

                        if self.in_packets is not None and self.in_packets._has_data():
                            return True

                        if self.input_queue_drops is not None and self.input_queue_drops._has_data():
                            return True

                        if self.input_total_drops is not None and self.input_total_drops._has_data():
                            return True

                        if self.input_total_errors is not None and self.input_total_errors._has_data():
                            return True

                        if self.out_octets is not None and self.out_octets._has_data():
                            return True

                        if self.out_packets is not None and self.out_packets._has_data():
                            return True

                        if self.output_queue_drops is not None and self.output_queue_drops._has_data():
                            return True

                        if self.output_total_drops is not None and self.output_total_drops._has_data():
                            return True

                        if self.output_total_errors is not None and self.output_total_errors._has_data():
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates.BasicCounterInterfaceTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.basic_counter_interface_template is not None:
                        for child_ref in self.basic_counter_interface_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface.BasicCounterInterfaceTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:basic-counter-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.basic_counter_interface_templates is not None and self.basic_counter_interface_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.BasicCounterInterface']['meta_info']


        class Bgp(object):
            """
            BGP threshold configuration
            
            .. attribute:: bgp_templates
            
            	BGP threshold templates
            	**type**\:   :py:class:`BgpTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.bgp_templates = PerfMgmt.Threshold.Bgp.BgpTemplates()
                self.bgp_templates.parent = self


            class BgpTemplates(object):
                """
                BGP threshold templates
                
                .. attribute:: bgp_template
                
                	BGP threshold template instance
                	**type**\: list of    :py:class:`BgpTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.bgp_template = YList()
                    self.bgp_template.parent = self
                    self.bgp_template.name = 'bgp_template'


                class BgpTemplate(object):
                    """
                    BGP threshold template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: conn_dropped
                    
                    	Number of times the connection was dropped
                    	**type**\:   :py:class:`ConnDropped <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: conn_established
                    
                    	Number of times the connection was established
                    	**type**\:   :py:class:`ConnEstablished <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: errors_received
                    
                    	Number of error notifications received
                    	**type**\:   :py:class:`ErrorsReceived <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: errors_sent
                    
                    	Number of error notifications sent
                    	**type**\:   :py:class:`ErrorsSent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_messages
                    
                    	Number of messages received
                    	**type**\:   :py:class:`InputMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_update_messages
                    
                    	Number of update messages received
                    	**type**\:   :py:class:`InputUpdateMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_messages
                    
                    	Number of messages sent
                    	**type**\:   :py:class:`OutputMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_update_messages
                    
                    	Number of update messages sent
                    	**type**\:   :py:class:`OutputUpdateMessages <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.conn_dropped = None
                        self.conn_established = None
                        self.errors_received = None
                        self.errors_sent = None
                        self.input_messages = None
                        self.input_update_messages = None
                        self.output_messages = None
                        self.output_update_messages = None
                        self.sample_interval = None


                    class OutputUpdateMessages(object):
                        """
                        Number of update messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-update-messages'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputUpdateMessages']['meta_info']


                    class ErrorsReceived(object):
                        """
                        Number of error notifications received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:errors-received'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsReceived']['meta_info']


                    class ConnEstablished(object):
                        """
                        Number of times the connection was
                        established
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:conn-established'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnEstablished']['meta_info']


                    class OutputMessages(object):
                        """
                        Number of messages sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-messages'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.OutputMessages']['meta_info']


                    class ConnDropped(object):
                        """
                        Number of times the connection was dropped
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:conn-dropped'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ConnDropped']['meta_info']


                    class InputUpdateMessages(object):
                        """
                        Number of update messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-update-messages'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputUpdateMessages']['meta_info']


                    class ErrorsSent(object):
                        """
                        Number of error notifications sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:errors-sent'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.ErrorsSent']['meta_info']


                    class InputMessages(object):
                        """
                        Number of messages received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-messages'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate.InputMessages']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.conn_dropped is not None and self.conn_dropped._has_data():
                            return True

                        if self.conn_established is not None and self.conn_established._has_data():
                            return True

                        if self.errors_received is not None and self.errors_received._has_data():
                            return True

                        if self.errors_sent is not None and self.errors_sent._has_data():
                            return True

                        if self.input_messages is not None and self.input_messages._has_data():
                            return True

                        if self.input_update_messages is not None and self.input_update_messages._has_data():
                            return True

                        if self.output_messages is not None and self.output_messages._has_data():
                            return True

                        if self.output_update_messages is not None and self.output_update_messages._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates.BgpTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bgp_template is not None:
                        for child_ref in self.bgp_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.Bgp.BgpTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:bgp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.bgp_templates is not None and self.bgp_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.Bgp']['meta_info']


        class Ospfv2Protocol(object):
            """
            OSPF v2 Protocol threshold configuration
            
            .. attribute:: ospfv2_protocol_templates
            
            	OSPF v2 Protocol threshold templates
            	**type**\:   :py:class:`Ospfv2ProtocolTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ospfv2_protocol_templates = PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates()
                self.ospfv2_protocol_templates.parent = self


            class Ospfv2ProtocolTemplates(object):
                """
                OSPF v2 Protocol threshold templates
                
                .. attribute:: ospfv2_protocol_template
                
                	OSPF v2 Protocol threshold template instance
                	**type**\: list of    :py:class:`Ospfv2ProtocolTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ospfv2_protocol_template = YList()
                    self.ospfv2_protocol_template.parent = self
                    self.ospfv2_protocol_template.name = 'ospfv2_protocol_template'


                class Ospfv2ProtocolTemplate(object):
                    """
                    OSPF v2 Protocol threshold template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: checksum_errors
                    
                    	Number of packets received with checksum errors
                    	**type**\:   :py:class:`ChecksumErrors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds
                    
                    	Number of DBD packets received
                    	**type**\:   :py:class:`InputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds_lsa
                    
                    	Number of LSA received in DBD packets
                    	**type**\:   :py:class:`InputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_hello_packets
                    
                    	Number of Hello packets received
                    	**type**\:   :py:class:`InputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests
                    
                    	Number of LS Requests received
                    	**type**\:   :py:class:`InputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests_lsa
                    
                    	Number of LSA received in LS Requests
                    	**type**\:   :py:class:`InputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks
                    
                    	Number of LSA Acknowledgements received
                    	**type**\:   :py:class:`InputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks_lsa
                    
                    	Number of LSA received in LSA Acknowledgements
                    	**type**\:   :py:class:`InputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates
                    
                    	Number of LSA Updates received
                    	**type**\:   :py:class:`InputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates_lsa
                    
                    	Number of LSA received in LSA Updates
                    	**type**\:   :py:class:`InputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_packets
                    
                    	Total number of packets received
                    	**type**\:   :py:class:`InputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds
                    
                    	Number of DBD packets sent
                    	**type**\:   :py:class:`OutputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds_lsa
                    
                    	Number of LSA sent in DBD packets
                    	**type**\:   :py:class:`OutputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_hello_packets
                    
                    	Total number of packets sent
                    	**type**\:   :py:class:`OutputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests
                    
                    	Number of LS Requests sent
                    	**type**\:   :py:class:`OutputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests_lsa
                    
                    	Number of LSA sent in LS Requests
                    	**type**\:   :py:class:`OutputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks
                    
                    	Number of LSA Acknowledgements sent
                    	**type**\:   :py:class:`OutputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks_lsa
                    
                    	Number of LSA sent in LSA Acknowledgements
                    	**type**\:   :py:class:`OutputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates
                    
                    	Number of LSA Updates sent
                    	**type**\:   :py:class:`OutputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates_lsa
                    
                    	Number of LSA sent in LSA Updates
                    	**type**\:   :py:class:`OutputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_packets
                    
                    	Total number of packets sent
                    	**type**\:   :py:class:`OutputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
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
                        self.sample_interval = None


                    class ChecksumErrors(object):
                        """
                        Number of packets received with checksum
                        errors
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:checksum-errors'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.ChecksumErrors']['meta_info']


                    class InputLsaAcksLsa(object):
                        """
                        Number of LSA received in LSA Acknowledgements
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-acks-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcksLsa']['meta_info']


                    class OutputDbDsLsa(object):
                        """
                        Number of LSA sent in DBD packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-db-ds-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDsLsa']['meta_info']


                    class InputDbDsLsa(object):
                        """
                        Number of LSA received in DBD packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-db-ds-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDsLsa']['meta_info']


                    class InputLsaUpdates(object):
                        """
                        Number of LSA Updates received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-updates'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdates']['meta_info']


                    class OutputDbDs(object):
                        """
                        Number of DBD packets sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-db-ds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputDbDs']['meta_info']


                    class OutputLsaUpdatesLsa(object):
                        """
                        Number of LSA sent in LSA Updates
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-updates-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdatesLsa']['meta_info']


                    class InputDbDs(object):
                        """
                        Number of DBD packets received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-db-ds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputDbDs']['meta_info']


                    class InputLsaUpdatesLsa(object):
                        """
                        Number of LSA received in LSA Updates
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-updates-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaUpdatesLsa']['meta_info']


                    class OutputPackets(object):
                        """
                        Total number of packets sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputPackets']['meta_info']


                    class InputPackets(object):
                        """
                        Total number of packets received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputPackets']['meta_info']


                    class OutputHelloPackets(object):
                        """
                        Total number of packets sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-hello-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputHelloPackets']['meta_info']


                    class InputHelloPackets(object):
                        """
                        Number of Hello packets received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-hello-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputHelloPackets']['meta_info']


                    class OutputLsRequests(object):
                        """
                        Number of LS Requests sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-ls-requests'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequests']['meta_info']


                    class OutputLsaAcksLsa(object):
                        """
                        Number of LSA sent in LSA Acknowledgements
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-acks-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcksLsa']['meta_info']


                    class OutputLsaAcks(object):
                        """
                        Number of LSA Acknowledgements sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-acks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaAcks']['meta_info']


                    class InputLsaAcks(object):
                        """
                        Number of LSA Acknowledgements received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-acks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsaAcks']['meta_info']


                    class OutputLsaUpdates(object):
                        """
                        Number of LSA Updates sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-updates'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsaUpdates']['meta_info']


                    class OutputLsRequestsLsa(object):
                        """
                        Number of LSA sent in LS Requests
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-ls-requests-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.OutputLsRequestsLsa']['meta_info']


                    class InputLsRequestsLsa(object):
                        """
                        Number of LSA received in LS Requests
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-ls-requests-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequestsLsa']['meta_info']


                    class InputLsRequests(object):
                        """
                        Number of LS Requests received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-ls-requests'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate.InputLsRequests']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.checksum_errors is not None and self.checksum_errors._has_data():
                            return True

                        if self.input_db_ds is not None and self.input_db_ds._has_data():
                            return True

                        if self.input_db_ds_lsa is not None and self.input_db_ds_lsa._has_data():
                            return True

                        if self.input_hello_packets is not None and self.input_hello_packets._has_data():
                            return True

                        if self.input_ls_requests is not None and self.input_ls_requests._has_data():
                            return True

                        if self.input_ls_requests_lsa is not None and self.input_ls_requests_lsa._has_data():
                            return True

                        if self.input_lsa_acks is not None and self.input_lsa_acks._has_data():
                            return True

                        if self.input_lsa_acks_lsa is not None and self.input_lsa_acks_lsa._has_data():
                            return True

                        if self.input_lsa_updates is not None and self.input_lsa_updates._has_data():
                            return True

                        if self.input_lsa_updates_lsa is not None and self.input_lsa_updates_lsa._has_data():
                            return True

                        if self.input_packets is not None and self.input_packets._has_data():
                            return True

                        if self.output_db_ds is not None and self.output_db_ds._has_data():
                            return True

                        if self.output_db_ds_lsa is not None and self.output_db_ds_lsa._has_data():
                            return True

                        if self.output_hello_packets is not None and self.output_hello_packets._has_data():
                            return True

                        if self.output_ls_requests is not None and self.output_ls_requests._has_data():
                            return True

                        if self.output_ls_requests_lsa is not None and self.output_ls_requests_lsa._has_data():
                            return True

                        if self.output_lsa_acks is not None and self.output_lsa_acks._has_data():
                            return True

                        if self.output_lsa_acks_lsa is not None and self.output_lsa_acks_lsa._has_data():
                            return True

                        if self.output_lsa_updates is not None and self.output_lsa_updates._has_data():
                            return True

                        if self.output_lsa_updates_lsa is not None and self.output_lsa_updates_lsa._has_data():
                            return True

                        if self.output_packets is not None and self.output_packets._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates.Ospfv2ProtocolTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ospfv2_protocol_template is not None:
                        for child_ref in self.ospfv2_protocol_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol.Ospfv2ProtocolTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv2-protocol'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ospfv2_protocol_templates is not None and self.ospfv2_protocol_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.Ospfv2Protocol']['meta_info']


        class CpuNode(object):
            """
            Node CPU threshold configuration
            
            .. attribute:: cpu_node_templates
            
            	Node CPU threshold configuration templates
            	**type**\:   :py:class:`CpuNodeTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.cpu_node_templates = PerfMgmt.Threshold.CpuNode.CpuNodeTemplates()
                self.cpu_node_templates.parent = self


            class CpuNodeTemplates(object):
                """
                Node CPU threshold configuration templates
                
                .. attribute:: cpu_node_template
                
                	Node CPU threshold configuration template instances
                	**type**\: list of    :py:class:`CpuNodeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.cpu_node_template = YList()
                    self.cpu_node_template.parent = self
                    self.cpu_node_template.name = 'cpu_node_template'


                class CpuNodeTemplate(object):
                    """
                    Node CPU threshold configuration template
                    instances
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: average_cpu_used
                    
                    	Average %CPU utilization
                    	**type**\:   :py:class:`AverageCpuUsed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: no_processes
                    
                    	Number of processes
                    	**type**\:   :py:class:`NoProcesses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.average_cpu_used = None
                        self.no_processes = None
                        self.sample_interval = None


                    class AverageCpuUsed(object):
                        """
                        Average %CPU utilization
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:average-cpu-used'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.AverageCpuUsed']['meta_info']


                    class NoProcesses(object):
                        """
                        Number of processes
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:no-processes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate.NoProcesses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.average_cpu_used is not None and self.average_cpu_used._has_data():
                            return True

                        if self.no_processes is not None and self.no_processes._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates.CpuNodeTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.cpu_node_template is not None:
                        for child_ref in self.cpu_node_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.CpuNode.CpuNodeTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:cpu-node'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.cpu_node_templates is not None and self.cpu_node_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.CpuNode']['meta_info']


        class DataRateInterface(object):
            """
            Interface Data Rates threshold configuration
            
            .. attribute:: data_rate_interface_templates
            
            	Interface Data Rates threshold templates
            	**type**\:   :py:class:`DataRateInterfaceTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.data_rate_interface_templates = PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates()
                self.data_rate_interface_templates.parent = self


            class DataRateInterfaceTemplates(object):
                """
                Interface Data Rates threshold templates
                
                .. attribute:: data_rate_interface_template
                
                	Interface Data Rates threshold template instance
                	**type**\: list of    :py:class:`DataRateInterfaceTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.data_rate_interface_template = YList()
                    self.data_rate_interface_template.parent = self
                    self.data_rate_interface_template.name = 'data_rate_interface_template'


                class DataRateInterfaceTemplate(object):
                    """
                    Interface Data Rates threshold template
                    instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: bandwidth
                    
                    	Bandwidth in kbps
                    	**type**\:   :py:class:`Bandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_data_rate
                    
                    	Input data rate in kbps
                    	**type**\:   :py:class:`InputDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_packet_rate
                    
                    	Number of input packets per second
                    	**type**\:   :py:class:`InputPacketRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_peak_pkts
                    
                    	Maximum number of input packets per second
                    	**type**\:   :py:class:`InputPeakPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_peak_rate
                    
                    	Peak input data rate in kbps
                    	**type**\:   :py:class:`InputPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_data_rate
                    
                    	Output data rate in kbps
                    	**type**\:   :py:class:`OutputDataRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_packet_rate
                    
                    	Number of Output packets per second
                    	**type**\:   :py:class:`OutputPacketRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_peak_pkts
                    
                    	Maximum number of output packets per second
                    	**type**\:   :py:class:`OutputPeakPkts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_peak_rate
                    
                    	Peak output data rate in kbps
                    	**type**\:   :py:class:`OutputPeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: reg_exp_group
                    
                    	Enable instance filtering by regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    .. attribute:: vrf_group
                    
                    	Enable instance filtering by VRF name regular expression 
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.bandwidth = None
                        self.input_data_rate = None
                        self.input_packet_rate = None
                        self.input_peak_pkts = None
                        self.input_peak_rate = None
                        self.output_data_rate = None
                        self.output_packet_rate = None
                        self.output_peak_pkts = None
                        self.output_peak_rate = None
                        self.reg_exp_group = None
                        self.sample_interval = None
                        self.vrf_group = None


                    class InputDataRate(object):
                        """
                        Input data rate in kbps
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-data-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputDataRate']['meta_info']


                    class Bandwidth(object):
                        """
                        Bandwidth in kbps
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:bandwidth'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.Bandwidth']['meta_info']


                    class OutputPacketRate(object):
                        """
                        Number of Output packets per second
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-packet-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPacketRate']['meta_info']


                    class InputPeakPkts(object):
                        """
                        Maximum number of input packets per second
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-peak-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakPkts']['meta_info']


                    class OutputPeakRate(object):
                        """
                        Peak output data rate in kbps
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-peak-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakRate']['meta_info']


                    class OutputDataRate(object):
                        """
                        Output data rate in kbps
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-data-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputDataRate']['meta_info']


                    class InputPacketRate(object):
                        """
                        Number of input packets per second
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-packet-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPacketRate']['meta_info']


                    class OutputPeakPkts(object):
                        """
                        Maximum number of output packets per second
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-peak-pkts'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.OutputPeakPkts']['meta_info']


                    class InputPeakRate(object):
                        """
                        Peak input data rate in kbps
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-peak-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate.InputPeakRate']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.bandwidth is not None and self.bandwidth._has_data():
                            return True

                        if self.input_data_rate is not None and self.input_data_rate._has_data():
                            return True

                        if self.input_packet_rate is not None and self.input_packet_rate._has_data():
                            return True

                        if self.input_peak_pkts is not None and self.input_peak_pkts._has_data():
                            return True

                        if self.input_peak_rate is not None and self.input_peak_rate._has_data():
                            return True

                        if self.output_data_rate is not None and self.output_data_rate._has_data():
                            return True

                        if self.output_packet_rate is not None and self.output_packet_rate._has_data():
                            return True

                        if self.output_peak_pkts is not None and self.output_peak_pkts._has_data():
                            return True

                        if self.output_peak_rate is not None and self.output_peak_rate._has_data():
                            return True

                        if self.reg_exp_group is not None:
                            return True

                        if self.sample_interval is not None:
                            return True

                        if self.vrf_group is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates.DataRateInterfaceTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.data_rate_interface_template is not None:
                        for child_ref in self.data_rate_interface_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.DataRateInterface.DataRateInterfaceTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:data-rate-interface'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.data_rate_interface_templates is not None and self.data_rate_interface_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.DataRateInterface']['meta_info']


        class ProcessNode(object):
            """
            Node Process threshold configuration
            
            .. attribute:: process_node_templates
            
            	Node Memory threshold templates
            	**type**\:   :py:class:`ProcessNodeTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.process_node_templates = PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates()
                self.process_node_templates.parent = self


            class ProcessNodeTemplates(object):
                """
                Node Memory threshold templates
                
                .. attribute:: process_node_template
                
                	Node Memory threshold template instance
                	**type**\: list of    :py:class:`ProcessNodeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.process_node_template = YList()
                    self.process_node_template.parent = self
                    self.process_node_template.name = 'process_node_template'


                class ProcessNodeTemplate(object):
                    """
                    Node Memory threshold template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: average_cpu_used
                    
                    	Average %CPU utilization
                    	**type**\:   :py:class:`AverageCpuUsed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: no_threads
                    
                    	Number of threads
                    	**type**\:   :py:class:`NoThreads <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: peak_memory
                    
                    	Max memory (KBytes) used since startup time
                    	**type**\:   :py:class:`PeakMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.average_cpu_used = None
                        self.no_threads = None
                        self.peak_memory = None
                        self.sample_interval = None


                    class AverageCpuUsed(object):
                        """
                        Average %CPU utilization
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:average-cpu-used'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.AverageCpuUsed']['meta_info']


                    class PeakMemory(object):
                        """
                        Max memory (KBytes) used since startup time
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:peak-memory'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.PeakMemory']['meta_info']


                    class NoThreads(object):
                        """
                        Number of threads
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..32767
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..32767
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:no-threads'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate.NoThreads']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.average_cpu_used is not None and self.average_cpu_used._has_data():
                            return True

                        if self.no_threads is not None and self.no_threads._has_data():
                            return True

                        if self.peak_memory is not None and self.peak_memory._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates.ProcessNodeTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.process_node_template is not None:
                        for child_ref in self.process_node_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.ProcessNode.ProcessNodeTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:process-node'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.process_node_templates is not None and self.process_node_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.ProcessNode']['meta_info']


        class MemoryNode(object):
            """
            Node Memory threshold configuration
            
            .. attribute:: memory_node_templates
            
            	Node Memory threshold configuration templates
            	**type**\:   :py:class:`MemoryNodeTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.memory_node_templates = PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates()
                self.memory_node_templates.parent = self


            class MemoryNodeTemplates(object):
                """
                Node Memory threshold configuration templates
                
                .. attribute:: memory_node_template
                
                	Node Memory threshold configuration template instance
                	**type**\: list of    :py:class:`MemoryNodeTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.memory_node_template = YList()
                    self.memory_node_template.parent = self
                    self.memory_node_template.name = 'memory_node_template'


                class MemoryNodeTemplate(object):
                    """
                    Node Memory threshold configuration template
                    instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: curr_memory
                    
                    	Current memory (Bytes) in use
                    	**type**\:   :py:class:`CurrMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: peak_memory
                    
                    	Maximum memory (KBytes) used
                    	**type**\:   :py:class:`PeakMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
                        self.curr_memory = None
                        self.peak_memory = None
                        self.sample_interval = None


                    class PeakMemory(object):
                        """
                        Maximum memory (KBytes) used
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4194304
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4194304
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:peak-memory'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.PeakMemory']['meta_info']


                    class CurrMemory(object):
                        """
                        Current memory (Bytes) in use
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:curr-memory'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate.CurrMemory']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.curr_memory is not None and self.curr_memory._has_data():
                            return True

                        if self.peak_memory is not None and self.peak_memory._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates.MemoryNodeTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.memory_node_template is not None:
                        for child_ref in self.memory_node_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.MemoryNode.MemoryNodeTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:memory-node'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.memory_node_templates is not None and self.memory_node_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.MemoryNode']['meta_info']


        class Ospfv3Protocol(object):
            """
            OSPF v2 Protocol threshold configuration
            
            .. attribute:: ospfv3_protocol_templates
            
            	OSPF v2 Protocol threshold templates
            	**type**\:   :py:class:`Ospfv3ProtocolTemplates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates>`
            
            

            """

            _prefix = 'manageability-perfmgmt-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ospfv3_protocol_templates = PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates()
                self.ospfv3_protocol_templates.parent = self


            class Ospfv3ProtocolTemplates(object):
                """
                OSPF v2 Protocol threshold templates
                
                .. attribute:: ospfv3_protocol_template
                
                	OSPF v2 Protocol threshold template instance
                	**type**\: list of    :py:class:`Ospfv3ProtocolTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate>`
                
                

                """

                _prefix = 'manageability-perfmgmt-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ospfv3_protocol_template = YList()
                    self.ospfv3_protocol_template.parent = self
                    self.ospfv3_protocol_template.name = 'ospfv3_protocol_template'


                class Ospfv3ProtocolTemplate(object):
                    """
                    OSPF v2 Protocol threshold template instance
                    
                    .. attribute:: template_name  <key>
                    
                    	Template Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: input_db_ds
                    
                    	Number of DBD packets received
                    	**type**\:   :py:class:`InputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_db_ds_lsa
                    
                    	Number of LSA received in DBD packets
                    	**type**\:   :py:class:`InputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_hello_packets
                    
                    	Number of Hello packets received
                    	**type**\:   :py:class:`InputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests
                    
                    	Number of LS Requests received
                    	**type**\:   :py:class:`InputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_ls_requests_lsa
                    
                    	Number of LSA received in LS Requests
                    	**type**\:   :py:class:`InputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks
                    
                    	Number of LSA Acknowledgements received
                    	**type**\:   :py:class:`InputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_acks_lsa
                    
                    	Number of LSA received in LSA Acknowledgements
                    	**type**\:   :py:class:`InputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates
                    
                    	Number of LSA Updates received
                    	**type**\:   :py:class:`InputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_lsa_updates_lsa
                    
                    	Number of LSA received in LSA Updates
                    	**type**\:   :py:class:`InputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: input_packets
                    
                    	Total number of packets received
                    	**type**\:   :py:class:`InputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds
                    
                    	Number of DBD packets sent
                    	**type**\:   :py:class:`OutputDbDs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_db_ds_lsa
                    
                    	Number of LSA sent in DBD packets
                    	**type**\:   :py:class:`OutputDbDsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_hello_packets
                    
                    	Total number of packets sent
                    	**type**\:   :py:class:`OutputHelloPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests
                    
                    	Number of LS Requests sent
                    	**type**\:   :py:class:`OutputLsRequests <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_ls_requests_lsa
                    
                    	Number of LSA sent in LS Requests
                    	**type**\:   :py:class:`OutputLsRequestsLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks
                    
                    	Number of LSA Acknowledgements sent
                    	**type**\:   :py:class:`OutputLsaAcks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_acks_lsa
                    
                    	Number of LSA sent in LSA Acknowledgements
                    	**type**\:   :py:class:`OutputLsaAcksLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates
                    
                    	Number of LSA Updates sent
                    	**type**\:   :py:class:`OutputLsaUpdates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_lsa_updates_lsa
                    
                    	Number of LSA sent in LSA Updates
                    	**type**\:   :py:class:`OutputLsaUpdatesLsa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: output_packets
                    
                    	Total number of packets sent
                    	**type**\:   :py:class:`OutputPackets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: sample_interval
                    
                    	Frequency of sampling in minutes
                    	**type**\:  int
                    
                    	**range:** 1..60
                    
                    	**units**\: minute
                    
                    

                    """

                    _prefix = 'manageability-perfmgmt-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.template_name = None
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
                        self.sample_interval = None


                    class InputLsaAcksLsa(object):
                        """
                        Number of LSA received in LSA Acknowledgements
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-acks-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcksLsa']['meta_info']


                    class OutputDbDsLsa(object):
                        """
                        Number of LSA sent in DBD packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-db-ds-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDsLsa']['meta_info']


                    class InputDbDsLsa(object):
                        """
                        Number of LSA received in DBD packets
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-db-ds-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDsLsa']['meta_info']


                    class InputLsaUpdates(object):
                        """
                        Number of LSA Updates received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-updates'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdates']['meta_info']


                    class OutputDbDs(object):
                        """
                        Number of DBD packets sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-db-ds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputDbDs']['meta_info']


                    class OutputLsaUpdatesLsa(object):
                        """
                        Number of LSA sent in LSA Updates
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-updates-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdatesLsa']['meta_info']


                    class InputDbDs(object):
                        """
                        Number of DBD packets received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-db-ds'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputDbDs']['meta_info']


                    class InputLsaUpdatesLsa(object):
                        """
                        Number of LSA received in LSA Updates
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-updates-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaUpdatesLsa']['meta_info']


                    class OutputPackets(object):
                        """
                        Total number of packets sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputPackets']['meta_info']


                    class InputPackets(object):
                        """
                        Total number of packets received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputPackets']['meta_info']


                    class OutputHelloPackets(object):
                        """
                        Total number of packets sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-hello-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputHelloPackets']['meta_info']


                    class InputHelloPackets(object):
                        """
                        Number of Hello packets received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-hello-packets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputHelloPackets']['meta_info']


                    class OutputLsRequests(object):
                        """
                        Number of LS Requests sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-ls-requests'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequests']['meta_info']


                    class OutputLsaAcksLsa(object):
                        """
                        Number of LSA sent in LSA Acknowledgements
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-acks-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcksLsa']['meta_info']


                    class OutputLsaAcks(object):
                        """
                        Number of LSA Acknowledgements sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-acks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaAcks']['meta_info']


                    class InputLsaAcks(object):
                        """
                        Number of LSA Acknowledgements received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-lsa-acks'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsaAcks']['meta_info']


                    class OutputLsaUpdates(object):
                        """
                        Number of LSA Updates sent
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-lsa-updates'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsaUpdates']['meta_info']


                    class OutputLsRequestsLsa(object):
                        """
                        Number of LSA sent in LS Requests
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:output-ls-requests-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.OutputLsRequestsLsa']['meta_info']


                    class InputLsRequestsLsa(object):
                        """
                        Number of LSA received in LS Requests
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-ls-requests-lsa'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequestsLsa']['meta_info']


                    class InputLsRequests(object):
                        """
                        Number of LS Requests received
                        
                        .. attribute:: end_range_value
                        
                        	Threshold end range value (for operator RG, set to 0 otherwise)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: operator
                        
                        	Operator
                        	**type**\:   :py:class:`PmThresholdOpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdOpEnum>`
                        
                        .. attribute:: percent
                        
                        	Set to TRUE if Specified threshold values are in percent
                        	**type**\:  bool
                        
                        .. attribute:: rearm_type
                        
                        	Configure the Rearm type
                        	**type**\:   :py:class:`PmThresholdRearmEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_perfmgmt_cfg.PmThresholdRearmEnum>`
                        
                        .. attribute:: rearm_window
                        
                        	Configure the rearm window size (for rearm type Window)
                        	**type**\:  int
                        
                        	**range:** 1..100
                        
                        .. attribute:: value
                        
                        	Threshold value (or start range value for operator RG)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'manageability-perfmgmt-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.end_range_value = None
                            self.operator = None
                            self.percent = None
                            self.rearm_type = None
                            self.rearm_window = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-manageability-perfmgmt-cfg:input-ls-requests'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.end_range_value is not None:
                                return True

                            if self.operator is not None:
                                return True

                            if self.percent is not None:
                                return True

                            if self.rearm_type is not None:
                                return True

                            if self.rearm_window is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                            return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate.InputLsRequests']['meta_info']

                    @property
                    def _common_path(self):
                        if self.template_name is None:
                            raise YPYModelError('Key property template_name is None')

                        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol-templates/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol-template[Cisco-IOS-XR-manageability-perfmgmt-cfg:template-name = ' + str(self.template_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.template_name is not None:
                            return True

                        if self.input_db_ds is not None and self.input_db_ds._has_data():
                            return True

                        if self.input_db_ds_lsa is not None and self.input_db_ds_lsa._has_data():
                            return True

                        if self.input_hello_packets is not None and self.input_hello_packets._has_data():
                            return True

                        if self.input_ls_requests is not None and self.input_ls_requests._has_data():
                            return True

                        if self.input_ls_requests_lsa is not None and self.input_ls_requests_lsa._has_data():
                            return True

                        if self.input_lsa_acks is not None and self.input_lsa_acks._has_data():
                            return True

                        if self.input_lsa_acks_lsa is not None and self.input_lsa_acks_lsa._has_data():
                            return True

                        if self.input_lsa_updates is not None and self.input_lsa_updates._has_data():
                            return True

                        if self.input_lsa_updates_lsa is not None and self.input_lsa_updates_lsa._has_data():
                            return True

                        if self.input_packets is not None and self.input_packets._has_data():
                            return True

                        if self.output_db_ds is not None and self.output_db_ds._has_data():
                            return True

                        if self.output_db_ds_lsa is not None and self.output_db_ds_lsa._has_data():
                            return True

                        if self.output_hello_packets is not None and self.output_hello_packets._has_data():
                            return True

                        if self.output_ls_requests is not None and self.output_ls_requests._has_data():
                            return True

                        if self.output_ls_requests_lsa is not None and self.output_ls_requests_lsa._has_data():
                            return True

                        if self.output_lsa_acks is not None and self.output_lsa_acks._has_data():
                            return True

                        if self.output_lsa_acks_lsa is not None and self.output_lsa_acks_lsa._has_data():
                            return True

                        if self.output_lsa_updates is not None and self.output_lsa_updates._has_data():
                            return True

                        if self.output_lsa_updates_lsa is not None and self.output_lsa_updates_lsa._has_data():
                            return True

                        if self.output_packets is not None and self.output_packets._has_data():
                            return True

                        if self.sample_interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                        return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates.Ospfv3ProtocolTemplate']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol-templates'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ospfv3_protocol_template is not None:
                        for child_ref in self.ospfv3_protocol_template:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                    return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol.Ospfv3ProtocolTemplates']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold/Cisco-IOS-XR-manageability-perfmgmt-cfg:ospfv3-protocol'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ospfv3_protocol_templates is not None and self.ospfv3_protocol_templates._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
                return meta._meta_table['PerfMgmt.Threshold.Ospfv3Protocol']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt/Cisco-IOS-XR-manageability-perfmgmt-cfg:threshold'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.basic_counter_interface is not None and self.basic_counter_interface._has_data():
                return True

            if self.bgp is not None and self.bgp._has_data():
                return True

            if self.cpu_node is not None and self.cpu_node._has_data():
                return True

            if self.data_rate_interface is not None and self.data_rate_interface._has_data():
                return True

            if self.generic_counter_interface is not None and self.generic_counter_interface._has_data():
                return True

            if self.ldp_mpls is not None and self.ldp_mpls._has_data():
                return True

            if self.memory_node is not None and self.memory_node._has_data():
                return True

            if self.ospfv2_protocol is not None and self.ospfv2_protocol._has_data():
                return True

            if self.ospfv3_protocol is not None and self.ospfv3_protocol._has_data():
                return True

            if self.process_node is not None and self.process_node._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
            return meta._meta_table['PerfMgmt.Threshold']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-manageability-perfmgmt-cfg:perf-mgmt'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.enable is not None and self.enable._has_data():
            return True

        if self.reg_exp_groups is not None and self.reg_exp_groups._has_data():
            return True

        if self.resources is not None and self.resources._has_data():
            return True

        if self.statistics is not None and self.statistics._has_data():
            return True

        if self.threshold is not None and self.threshold._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_manageability_perfmgmt_cfg as meta
        return meta._meta_table['PerfMgmt']['meta_info']


